# Product Vision

Business-in-a-Box is a contract-first demo platform that provisions infrastructure, deploys modular business services, and generates realistic synthetic business activity through scenario packs and simulation policies.

## Phase framing

### Phase 0

- establish contracts, scenario model, and local validation
- pin the initial repository and infra structure
- prove that mocked payloads validate against the service boundaries

### Phase 1

- implement the three-service kernel
- add independent persistence per service
- expose gateway and health surfaces

### Phase 2

- build the simulation engine
- support deterministic seeds and replayable policies
- surface generated activity in an operator-facing dashboard

### Phase 3

- turn the local skeleton into a real Hetzner/Talos/Flux deployment path
- document recovery, rollback, and replacement workflows

## Design stance

This project is a platform, contract, and simulation exercise. It is not an attempt to model every business correctly.
