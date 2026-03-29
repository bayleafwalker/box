# Scenario and Simulation Requirements

## Scope

Scenario pack model and simulator behavior for Phase 0 and Phase 2.

## Requirements

1. A scenario pack must declare the enabled service set and the expected contract versions.
2. A scenario pack must map business-specific labels onto the shared service kernel rather than redefining core service ownership.
3. Simulation policies must be replayable from a deterministic seed.
4. Simulator-produced payloads must validate against the service contracts they target.
5. Simulator logic must use public API or event contracts and must not mutate private service storage directly.
6. The platform must support at least two initial scenarios: one simple and one moderately rich.
7. Initial anomalies should be configuration-driven rather than hardcoded into service implementations.
