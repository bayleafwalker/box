# Data Architecture

## Purpose

Define how data is owned, persisted, propagated, and queried across the kernel.

The governing rule is simple: service boundaries are also data boundaries.

## Data rules

1. Every service owns its own write model.
2. Cross-service foreign keys stop at public identifiers; there are no operational cross-database joins.
3. Downstream services keep local reference views of upstream facts they need.
4. Events are immutable integration facts, not permission to read another service's tables.
5. Scenario packs are repo configuration, not operational source-of-truth data stores.
6. If the simulator needs persistence, it gets its own store. It does not borrow kernel service tables.

## Service-owned write models

### `party-service`

Authoritative records:

```text
parties(
  party_id text primary key,
  display_name text not null,
  party_type text not null,
  contact_email text null,
  external_reference text null,
  created_at timestamptz not null
)

party_outbox(
  outbox_id bigint primary key,
  event_id text unique not null,
  subject text not null,
  payload jsonb not null,
  occurred_at timestamptz not null,
  published_at timestamptz null
)
```

Key rule:

- `party-service` owns party identity and normalization only. It does not carry order history or catalog references.

### `catalog-service`

Authoritative records:

```text
catalog_items(
  item_id text primary key,
  name text not null,
  item_type text not null,
  base_price_amount numeric not null,
  base_price_currency char(3) not null,
  active boolean not null,
  created_at timestamptz not null
)

catalog_outbox(
  outbox_id bigint primary key,
  event_id text unique not null,
  subject text not null,
  payload jsonb not null,
  occurred_at timestamptz not null,
  published_at timestamptz null
)
```

Key rule:

- `catalog-service` owns the public price reference for an item. Downstream services may copy that fact, but they do not write back to it.

### `transaction-service`

Authoritative records:

```text
orders(
  order_id text primary key,
  customer_id text not null,
  scenario text not null,
  status text not null,
  payment_method text null,
  total_amount numeric not null,
  total_currency char(3) not null,
  created_at timestamptz not null
)

order_lines(
  order_id text not null,
  line_number integer not null,
  item_id text not null,
  quantity integer not null,
  unit_price_amount numeric not null,
  unit_price_currency char(3) not null,
  primary key (order_id, line_number)
)

party_refs(
  party_id text primary key,
  display_name text not null,
  party_type text not null,
  contact_email text null,
  source_event_id text not null,
  updated_at timestamptz not null
)

catalog_item_refs(
  item_id text primary key,
  name text not null,
  item_type text not null,
  base_price_amount numeric not null,
  base_price_currency char(3) not null,
  active boolean not null,
  source_event_id text not null,
  updated_at timestamptz not null
)

transaction_inbox(
  event_id text primary key,
  subject text not null,
  received_at timestamptz not null,
  processed_at timestamptz null,
  payload_hash text not null
)

transaction_outbox(
  outbox_id bigint primary key,
  event_id text unique not null,
  subject text not null,
  payload jsonb not null,
  occurred_at timestamptz not null,
  published_at timestamptz null
)
```

Key rules:

- `orders` and `order_lines` are the write model.
- `party_refs` and `catalog_item_refs` are local reference views populated from consumed events.
- `transaction-service` uses those local reference views to enforce invariants; it does not depend on live cross-service SQL reads.

## Outbox and inbox patterns

### Outbox

Every event-producing service should write domain state and an outbox row in the same database transaction.

Why:

- prevents "row committed but event lost" failures
- makes retries explicit
- keeps event publication outside the request transaction

Expected outbox worker behavior:

1. read unpublished rows in order
2. publish to NATS JetStream
3. mark `published_at`
4. retry safely on transient failure

### Inbox

Every event-consuming service should persist processed event identity before or during projection updates.

Why:

- NATS delivery can be retried
- downstream consumers must be idempotent
- projection updates should be replay-safe

Expected consumer behavior:

1. receive event
2. check `transaction_inbox` for `event_id`
3. if unseen, upsert local projection and record the inbox row
4. acknowledge only after durable success

## Consistency model

The kernel uses eventual consistency across service boundaries.

Practical implications:

- a newly created party may not be visible to `transaction-service` until `party.created` is consumed
- a simulator or operator workflow may need to wait for reference propagation before creating dependent transactions
- error handling should distinguish "unknown reference because not yet propagated" from "unknown reference because invalid"

Do not hide this with shared storage or ad hoc cross-service table reads.

## Money and identifiers

### Money

Keep money explicit as `amount + currency` throughout contracts and storage.

Rules:

- store currency alongside every money amount
- use a fixed-precision numeric type in Postgres
- treat currency mismatch as a validation failure, not a display concern

### Identifiers

Use opaque service-owned identifiers.

Rules:

- callers may store IDs, but they must not infer semantics from them
- service replacement must preserve contract-level identifier semantics, not internal sequence layout
- foreign keys across service boundaries are logical references, not DB-enforced constraints

## Query and reporting model

Service APIs return service-owned views only.

If operators need a cross-service read model later, add one of these explicitly:

- a thin gateway composition for demo-friendly reads
- a reporting store or projection service fed by events
- simulator audit tables owned by the simulator

Do not turn operational service databases into an informal reporting lake.

## Simulator state

Scenario packs and seeds live in Git under `scenario-packs/`.

Runtime simulator state, if persisted, should live in a separate simulator-owned store with records such as:

```text
simulation_runs(
  run_id text primary key,
  scenario text not null,
  seed integer not null,
  started_at timestamptz not null,
  finished_at timestamptz null,
  status text not null
)

simulation_rejections(
  rejection_id bigint primary key,
  run_id text not null,
  contract_target text not null,
  reason text not null,
  payload jsonb not null,
  occurred_at timestamptz not null
)
```

This keeps simulation observability separate from business truth.

## Contract and schema evolution

Preferred policy:

- additive contract changes first
- backfill or dual-write where needed
- deprecate old shapes before removal
- use versioned manifests and schemas for breaking changes

Private database migrations are allowed to differ by implementation. Compatibility is measured at the API and event boundary, not at the table layout.
