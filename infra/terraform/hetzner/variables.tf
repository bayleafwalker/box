variable "hcloud_token" {
  type      = string
  sensitive = true
}

variable "tailscale_auth_key" {
  type      = string
  sensitive = true
}

variable "cluster_name" {
  type    = string
  default = "box-demo"
}

variable "server_location" {
  type    = string
  default = "hel1-dc2"
}

variable "talos_version" {
  type    = string
  default = "v1.11.5"
}

variable "kubernetes_version" {
  type    = string
  default = "v1.34.1"
}

variable "cilium_version" {
  type    = string
  default = "v1.18.3"
}
