# Network

### Internet

### VPN: Virtual Private Network
VPN(가상사설망)은 네트워크를 통해 그룹이 내부적으로 통신할 목적으로 사용하는 사설 통신망이다.

### Proxy Server
Proxy Server(프록시 서버)는 클라이언트가 다른 네트워크 서비스에 간접적으로 접속할 수 있게 해주는 시스템 또는 프로그램이다. 서버와 클라이언트 사이 중계기로서 대리로 통신하는 것을 "Proxy" 중계를 해주는 것을 "Proxy Server"라 한다.

### Ego Motion
Ego motion is a 3D motion of a system within an environment.

### visual odometry/odometry
Visual odometry is the estimation of ego-motion using computer vision techniques.

#### ego-motion vs odometry
Both words can be used interchangeably in general.

### HTTP: Hyper Text Transfer Protocol

### HTTPS: HTTP Secure

#### HTTP vs HTTPS
HTTPS is also referred to as HTTP over TLS or http over SSL

### FTP: File Transfer Protocol

### SSH: Secure SHell

### DNS: Domain Name System | [Wiki](https://en.wikipedia.org/wiki/Domain_Name_System) | [Wiki (Kor)](https://ko.wikipedia.org/wiki/%EB%8F%84%EB%A9%94%EC%9D%B8_%EB%84%A4%EC%9E%84_%EC%8B%9C%EC%8A%A4%ED%85%9C)
The Domain Name System (DNS) is a hierarchical and decentralized naming system for computers, services, or other resources connected to the Internet or a private network. It associates various information with domain names assigned to each of the participating entities. Most prominently, it translates more readily memorized domain names to the numerical IP addresses needed for locating and identifying computer services and devices with the underlying network protocols. By providing a worldwide, distributed directory service, the Domain Name System has been an essential component of the functionality of the Internet since 1985.

The Domain Name System delegates the responsibility of assigning domain names and mapping those names to Internet resources by designating authoritative name servers for each domain. Network administrators may delegate authority over sub-domains of their allocated name space to other name servers. This mechanism provides distributed and fault-tolerant service and was designed to avoid a single large central database.

The Domain Name System also specifies the technical functionality of the database service that is at its core. It defines the DNS protocol, a detailed specification of the data structures and data communication exchanges used in the DNS, as part of the Internet Protocol Suite.

The Internet maintains two principal namespaces, the domain name hierarchy and the Internet Protocol (IP) address spaces. The Domain Name System maintains the domain name hierarchy and provides translation services between it and the address spaces. Internet name servers and a communication protocol implement the Domain Name System. A DNS name server is a server that stores the DNS records for a domain; a DNS name server responds with answers to queries against its database.

The most common types of records stored in the DNS database are for Start of Authority (SOA), IP addresses (A and AAAA), SMTP mail exchangers (MX), name servers (NS), pointers for reverse DNS lookups (PTR), and domain name aliases (CNAME). Although not intended to be a general purpose database, DNS has been expanded over time to store records for other types of data for either automatic lookups, such as DNSSEC records, or for human queries such as responsible person (RP) records. As a general purpose database, the DNS has also been used in combating unsolicited email (spam) by storing a real-time blackhole list (RBL). The DNS database is traditionally stored in a structured text file, the zone file, but other database systems are common.

### DDNS: Dynamic DNS | [Wiki](https://en.wikipedia.org/wiki/Dynamic_DNS) | [Wiki (Kor)](https://ko.wikipedia.org/wiki/DDNS)
Dynamic DNS (DDNS) is a method of automatically updating a name server in the Domain Name System (DNS), often in real time, with the active DDNS configuration of its configured hostnames, addresses or other information.

The term is used to describe two different concepts. The first is "dynamic DNS updating" which refers to systems that are used to update traditional DNS records without manual editing. These mechanisms are explained in RFC 2136, and use the TSIG mechanism to provide security. The second kind of dynamic DNS permits lightweight and immediate updates often using an update client, which do not use the RFC2136 standard for updating DNS records. These clients provide a persistent addressing method for devices that change their location, configuration or IP address frequently.

### Anonymous Pipe | [Wiki](https://en.wikipedia.org/wiki/Anonymous_pipe) | [Blog (KR-KO)](https://12bme.tistory.com/226)
An anonymous pipe is a simple FIFO communication chaneel that may be used for one-way IPC(InterProcess Communication). AN implementation is often integrated into the operating system's file IO subsystem. Typically a parent program opens anonymous pipes, and creates a new porcess that inherits the other ends of the pipes, or creates several new processes and arranges them in a pipeline. Ful-duplex(two-way) communication normally requires two anonymous pipes. Pipelines are supported in most popular operating systems, from Unix and DOS onwards, and are created using the "|" character in many shells.

### Named Pipe | [Wiki](https://en.wikipedia.org/wiki/Named_pipe) | [Blog (KR-KO)](https://mug896.github.io/bash-shell/named_pipe.html)
A named pips(also known as a FIFO for its behavior) is an extension to the traditional pipe concept on Unix and Unix-like systems, and is one of the methods of IPC. The concepth is also found in OS/2 and Microsoft Windows, althought the semantics differ substantially. A tranditional pipe is unnamed and lasts only as long as the process. A named pipe, however, can last as long as the system is up, beyond the life of the process. It can be deleted if no longer used, Usually a named pipe appears as a file, and generally processes attach to it for IPC.

#### Reference
- ego-motion vs odometry, https://answers.ros.org/question/296686/what-is-the-differences-between-ego-motion-and-odometry/, 2020-03-16-Mon.
- http vs https, https://www.keycdn.com/blog/difference-between-http-and-https, 2020-03-16-Mon.
- DNS Wiki, https://en.wikipedia.org/wiki/Domain_Name_System, 2020-10-06-Tue.
- DNS Wiki Kor, https://ko.wikipedia.org/wiki/%EB%8F%84%EB%A9%94%EC%9D%B8_%EB%84%A4%EC%9E%84_%EC%8B%9C%EC%8A%A4%ED%85%9C, 2020-10-06-Tue.
- DDNS Wiki, https://en.wikipedia.org/wiki/Dynamic_DNS, 2020-10-06-Tue.
- DDNS Wiki Kor, https://ko.wikipedia.org/wiki/DDNS, 2020-10-06-Tue.
- Internet
- Anonymous Pipe Wiki, https://en.wikipedia.org/wiki/Anonymous_pipe, 2020-11-09-Mon.
- Pipe blog KR-KO, https://12bme.tistory.com/226, 2020-11-09-Mon.
- Named Pipe Wiki, https://en.wikipedia.org/wiki/Named_pipe, 2020-11-09-Mon.
- Named Pipe blog KR-KO, https://mug896.github.io/bash-shell/named_pipe.html, 2020-11-09-Mon.
