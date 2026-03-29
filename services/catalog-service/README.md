# catalog-service

Owns offerings, goods, services, and price references.

Boundary rules:

- source of truth for item and price references
- emits `catalog.item.created`
- downstream services consume contracts rather than internal tables
