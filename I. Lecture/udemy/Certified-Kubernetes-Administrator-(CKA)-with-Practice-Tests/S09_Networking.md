# Section 9: Networking

## Date

2023-01-18-Wednesday

## Contents

### 196. Networking - Section Introduction

- Switching and Routing
  - Switching
  - Routing
  - Default Gateway
  - NAT
- Linux Interface for Virtual Networking
  - Bridge Network
  - VLAN
  - VXLAN
- IP Address Management & Name Resolution
  - DNS
  - IPAM
  - DHCP
- Firewalls
- Load-Balancers
- Tools:
  - Ping
  - NC - NetCat
  - TCPDUMP
  - IPTABLES

### 197. Download Presentation Deck

- Kubernetes+-CKA-+0800+-+Networking-v1.2.pdf
- Ingress.pdf

### 198. Prerequisite - Switching Routing

- ip link
- ip addr
- ip add add
- ip route
- route
- ip route add
- cat /proc/sys/net/ipv4/ip_forward

### 199. Prerequisite - DNS

- cat >> /etc/hosts
- cat /etc/nsswitch.conf
  - files(Local) -> DNS
- cat /etc/resolve.conf
- Domain Names
  - Root, Top Level Domain Name, Subdomain
- Record Types
  - CNAME: name to name
- nslookup
- dig

### 200. Prerequisite - CoreDNS

- https://github.com/kubernetes/dns/blob/master/docs/specification.md
- https://coredns.io/plugins/kubernetes/

### 201. Prerequisite - Network Namespaces

### 202. FAQ

### 203. Prerequisite - Docker Networking

### 204. Prerequisite - CNI

### 205. Cluster Networking

### 206. Important Note about CNI and CKA Exam

### 207. Practice Test - Explore Kubernetes Environment

### 208. Solution - Explore Environment (optional)

### 209

### 227. Article: Ingress

### 228. Practice Test - Ingress - 1

### 229. Solution - Ingress Networking 1 - (optional)

### 230. Ingress - Annotations and rewrite-target

### 231. Practice Test - Ingress - 2

### 232. Solution - Ingress Networking - 2 (optional
