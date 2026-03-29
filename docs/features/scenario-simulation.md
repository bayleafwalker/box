# Scenario Simulation

## Objective

Turn the static kernel into a living business demo by driving contract-valid commands and events from scenario packs.

## User value

- a demo environment can look alive without manual scripting
- different businesses can reuse the same kernel without rewriting service internals
- anomalies and rate behavior become testable rather than hand-waved

## Scope

- scenario registry and loading model
- deterministic simulation engine
- seed management and replay
- rate and anomaly policies for `hotdog-stand` and `it-consultancy`
- observability for generated events and rejected payloads

## Out of scope

- direct DB seeding into service internals
- industry-general ontology work
- large-scale analytics pipelines

## First delivery bar

- one command loads a scenario and starts generation
- simulator outputs validate against the current service contracts
- operators can explain what was generated and why
