terraform {
  required_version = ">= 1.0"
  required_providers {
    hcloud = {
      source  = "hetznercloud/hcloud"
      version = "~> 1.57"
    }
  }
}

provider "hcloud" {
  token = var.hcloud_token
}

module "talos" {
  source  = "hcloud-talos/talos/hcloud"
  version = "2.20.7"

  hcloud_token    = var.hcloud_token
  cluster_name    = var.cluster_name
  datacenter_name = var.server_location

  talos_version      = var.talos_version
  kubernetes_version = var.kubernetes_version
  cilium_version     = var.cilium_version

  control_plane_count          = 1
  control_plane_server_type    = "cx23"
  control_plane_allow_schedule = true

  worker_nodes = [
    {
      type  = "cx33"
      count = 1
      labels = {
        "node.kubernetes.io/role" = "worker"
      }
      taints = []
    }
  ]

  network_ipv4_cidr = "10.40.0.0/16"
  node_ipv4_cidr    = "10.40.1.0/24"
  pod_ipv4_cidr     = "10.40.16.0/20"
  service_ipv4_cidr = "10.40.8.0/21"

  enable_ipv6 = false

  firewall_use_current_ip   = false
  firewall_kube_api_source  = ["0.0.0.0/0", "::/0"]
  firewall_talos_api_source = ["0.0.0.0/0", "::/0"]

  tailscale = {
    enabled  = true
    auth_key = var.tailscale_auth_key
  }
}
