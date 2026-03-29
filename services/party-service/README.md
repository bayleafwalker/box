# party-service

Owns party identities such as customers, organizations, and contacts.

Boundary rules:

- source of truth for party identifiers
- emits `party.created`
- no other service reads its private storage directly
