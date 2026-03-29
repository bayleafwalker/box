# Hetzner Terraform Bootstrap

This directory follows the same general layout used in the local Talos/Hetzner projects:

- Terraform provisions the base cluster chassis
- Talos supplies the Kubernetes layer
- Flux takes over desired-state reconciliation after bootstrap

The files here are a starting point, not a finished production deployment.
