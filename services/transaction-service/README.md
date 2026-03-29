# transaction-service

Owns order-like business transactions.

Boundary rules:

- creates and tracks orders and sales transactions
- consumes `party.created` and `catalog.item.created`
- emits `order.created`
