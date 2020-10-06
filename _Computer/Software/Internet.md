# Internet

## VPN (Virtual Private Network, 가상사설망)
```
네트워크를 통해 그룹이 내부적으로 통신할 목적으로 사용하는 사설 통신망이다.
```

## Proxy Server (프록시 서버)
```
클라이언트가 다른 네트워크 서비스에 간접적으로 접속할 수 있게 해주는 시스템 또는 프로그램이다.
서버와 클라이언트 사이 중계기로서 대리로 통신하는 것을 '프록시' 중계를 해주는 것을 '프록시 서버'라 한다.
```

## ego-motion vs odometry
both can be used interchangeably in general

### ego-motion
3D motion of a system within an environment

### visual odometry/odometry
the estimation of ego-motion using computer vision techniques

## HTTPS
### HTTP(HyperTxet Trnasfer Protocol) vs HTTPS(HyperTxet Trnasfer Protocol Secure)
https is also referred to as http over TLS or http over SSL

## DNS(Domain Name System) | [Wiki](https://en.wikipedia.org/wiki/Domain_Name_System) |
The Domain Name System (DNS) is a hierarchical and decentralized naming system for computers, services, or other resources connected to the Internet or a private network. It associates various information with domain names assigned to each of the participating entities. Most prominently, it translates more readily memorized domain names to the numerical IP addresses needed for locating and identifying computer services and devices with the underlying network protocols. By providing a worldwide, distributed directory service, the Domain Name System has been an essential component of the functionality of the Internet since 1985.

The Domain Name System delegates the responsibility of assigning domain names and mapping those names to Internet resources by designating authoritative name servers for each domain. Network administrators may delegate authority over sub-domains of their allocated name space to other name servers. This mechanism provides distributed and fault-tolerant service and was designed to avoid a single large central database.

The Domain Name System also specifies the technical functionality of the database service that is at its core. It defines the DNS protocol, a detailed specification of the data structures and data communication exchanges used in the DNS, as part of the Internet Protocol Suite.

The Internet maintains two principal namespaces, the domain name hierarchy and the Internet Protocol (IP) address spaces. The Domain Name System maintains the domain name hierarchy and provides translation services between it and the address spaces. Internet name servers and a communication protocol implement the Domain Name System. A DNS name server is a server that stores the DNS records for a domain; a DNS name server responds with answers to queries against its database.

The most common types of records stored in the DNS database are for Start of Authority (SOA), IP addresses (A and AAAA), SMTP mail exchangers (MX), name servers (NS), pointers for reverse DNS lookups (PTR), and domain name aliases (CNAME). Although not intended to be a general purpose database, DNS has been expanded over time to store records for other types of data for either automatic lookups, such as DNSSEC records, or for human queries such as responsible person (RP) records. As a general purpose database, the DNS has also been used in combating unsolicited email (spam) by storing a real-time blackhole list (RBL). The DNS database is traditionally stored in a structured text file, the zone file, but other database systems are common.

## DDNS(Dynamic DNS) | [Wiki](https://en.wikipedia.org/wiki/Dynamic_DNS) | [Wiki (Kor)](https://ko.wikipedia.org/wiki/DDNS)
Dynamic DNS (DDNS) is a method of automatically updating a name server in the Domain Name System (DNS), often in real time, with the active DDNS configuration of its configured hostnames, addresses or other information.

The term is used to describe two different concepts. The first is "dynamic DNS updating" which refers to systems that are used to update traditional DNS records without manual editing. These mechanisms are explained in RFC 2136, and use the TSIG mechanism to provide security. The second kind of dynamic DNS permits lightweight and immediate updates often using an update client, which do not use the RFC2136 standard for updating DNS records. These clients provide a persistent addressing method for devices that change their location, configuration or IP address frequently.

#### Reference
- ego-motion vs odometry, https://answers.ros.org/question/296686/what-is-the-differences-between-ego-motion-and-odometry/
- http vs https, https://www.keycdn.com/blog/difference-between-http-and-https
- DNS Wiki, https://en.wikipedia.org/wiki/Domain_Name_System, 2020-10-06-Tue.
- DNS Wiki Kor, https://ko.wikipedia.org/wiki/%EB%8F%84%EB%A9%94%EC%9D%B8_%EB%84%A4%EC%9E%84_%EC%8B%9C%EC%8A%A4%ED%85%9C, 2020-10-06-Tue.
- DDNS Wiki, https://en.wikipedia.org/wiki/Dynamic_DNS, 2020-10-06-Tue.
- DDNS Wiki Kor, https://ko.wikipedia.org/wiki/DDNS, 2020-10-06-Tue.
