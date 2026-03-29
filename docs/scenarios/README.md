# Scenario Packs

Scenario packs provide business-specific overlays on top of a stable service kernel.

Each pack must define:

- enabled services
- contract versions it expects
- entity mappings for its business vocabulary
- seed data hints
- simulation policies and anomaly controls

Each pack must not:

- define private service persistence details
- introduce undocumented event payload fields
- bypass service contracts in order to "speed up" the demo

Initial packs:

- `hotdog-stand`
- `it-consultancy`
