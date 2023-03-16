# *Network* | [WiKi](https://en.wikipedia.org/wiki/Computer_network)

A computer network is a group of computers that use a set of common communication protocols over digital interconnections for the purpose of sharing resources located on or provided by the network nodes. THe interconnections between nodes are formed from a broad spectrum of telecommunication network technologies, based on physically wired, optical, and wireless radio-frequency methods that may be arranged in a variety of network topologies.

## _Telecommunications Network_ | [WiKi](https://en.wikipedia.org/wiki/Telecommunications_network)

A telecommunications network is a group of nodes interconnected by links that are used to exchange messages between the nodes. The links my use a variety of technologies based on the methodologies of circuit switching, message switching, or packet switching, to pass messages and signals.

## _Data Networks_

Data networks are used extensively throughout the world for communication between individuals and organizations. Data networks can be connected to allow users seamless access to resources that are hosted outside of the particular provider they are connected to. The Internet is the best example of many data networks from different organizations all operating under a single address space.

### _Wide Area Networks (WAN)_ | [WiKi](https://en.wikipedia.org/wiki/Wide_area_network) | [Cisco](https://www.cisco.com/c/en/us/products/switches/what-is-a-wan-wide-area-network.html)

In its simplest form, a wide-area network (WAN) is a collection of local-area networks (LANs) or other networks that communicate with one another. A WAN is essentially a network of networks, with the Internet of world's largest WAN.

Metropolitan Area Networks (MAN) | [WiKi](https://en.wikipedia.org/wiki/Metropolitan_area_network)

### _Local Area Networks (LAN)_ | [WiKi](https://en.wikipedia.org/wiki/Local_area_network) | [Cisco](https://www.cisco.com/c/en/us/products/switches/what-is-a-lan-local-area-network.html)

A local area network (LAN) is a collection of devices connected together in one physical location, such as a building, office, or home. A LAN can be small or large, ranging from a home network with one user to an enterprise network with thousands of users and devices in an office or school.

Regardless of size, a LAN's single defining characteristic is that it connects devices that are in a single, limited area. In contrast, a wide area network (WAN) or metropolitan area network (MAN) covers larger geographic areas. Some WANs and MANs connect many LANs together.

Internet Area Networks (IAN) | [WiKi](https://en.wikipedia.org/wiki/Internet_area_network)

Campus Area Networks (CAN) | [WiKi](https://en.wikipedia.org/wiki/Campus_network)

### _Wireless Personal Area Network (WPAN)_ | [CSRC](https://csrc.nist.gov/glossary/term/wireless_personal_area_network)

A small-scale wireless network that requires little or no infrastructure and operates within a short range. A WPAN is typically used by a few devices in a single room instead of connecting the devices with cables.

Personal Area Network (PAN) | [CSRC](https://csrc.nist.gov/glossary/term/personal_area_network)

Virual Private Networks (VPN) | [WiKi](https://en.wikipedia.org/wiki/Virtual_private_network)

## _Open Systems Interconnection (OSI) Model_ | [Cloudflare](https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/)

The open systems interconnection (OSI) model is a conceptual model created by the International Organization for Standardization which enables diverse communication systems to communicate using standard protocols. In plain English, the OSI provides a standard for different computer systems to be able to communicate with each other.

The OSI Model can be seen as a universal language for computing networking. It's based on the concept of splitting up a communication system into seven abstract layers, each one stacked upon the last.

- Application Layer 7
  - Human-computer interaction layer, where applications can access the network services.
  - Request content <-> Return content in required format

- Presentation Layer 6
  - Ensures that data is in a usable format and is where data encryption occurs.
  - Encryption -> Compression -> Translation

- Session Layer 5
  - Maintains connections and is responsible for controlling ports and sessions. 
  - Session of communication

- Transport Layer 4
  - Transmits data using transmission protocols including TCP and UDP.
  - Segmentation -> Transport -> Reassembly

- Network Layer 3
  - Decides which physical path the data will take.
  - Packets Creations -> Transport -> Packets Assembly

- Datalink Layer 2
  - Defines the format of data on the network.
  - Frame Creation -> Transport -> Transfer frames betweennet

- Physical Layer 1
  - Transmits raw bit stream over the physical medium.
  - Sending cable -> Bitstream -> Receiving cable

---

## _Node_ | [WiKi](https://en.wikipedia.org/wiki/Node_(networking))

In telecommunications networks, a node is either a redistribution point or a communication endpoint. The definition of a node depends on the network and protocol layer referred to. A physical network node is an electronic device that is attached to a network, and is capable of creating, receiving, or transmitting information over a communication channel. A passive distribution point such as a distribution frame or patch panel is consequently not a node.

## _Networking Hardware_ | [WiKi](https://en.wikipedia.org/wiki/Networking_hardware)

Networking hardware, also known as network equipment or computer networking devices, are electronic devices which are required for communication and interaction between devices on a computer network. Specially, they mediate data transmission in a computer network. Units which are the last receiver or generate data are called hosts, end systems or data termianl equipment.

## _Core_

Core network components interconnect other network components.

### _Gateway_ | [WiKi](https://en.wikipedia.org/wiki/Gateway_(telecommunications))

An interface providing a compatibliliy between networks by converting transmission speeds, protocols, codes, or security measures.

### _Router_ | [WiKi](https://en.wikipedia.org/wiki/Router_(computing)) | [WiKi (KR)](https://ko.wikipedia.org/wiki/%EB%9D%BC%EC%9A%B0%ED%84%B0)

A networking device that forwards data packets between computer networks. Routers perform the "traffic directing" functions on the Internet. A data packet is typically forwarded from one router to another through the networks that constitute the internetwork until it reaches its destination node. It works on OSI layer 3.

### _Switch_ | [WiKi](https://en.wikipedia.org/wiki/Network_switch)

A device that connects devices together on a computer network, by using packet switching to receive, process and forward data to the destination device. Unlike less advanced network hubs, a network switch forwards data only to one or multiple devices that need to receive it, rather than broadcasting the same data out of each of its ports. It works on OSI layer 2.

### Bridge | [WiKi](https://en.wikipedia.org/wiki/Bridging_(networking))

A device that connects multiple network segments. It works on OSI layers 1 and 2.

### _Repeater_ | [WiKi](https://en.wikipedia.org/wiki/Repeater)

An electronic device that receives a signal and retransmits it at a higher level or higher power, or onto the other side of an obstruction, so that the signal can cover longer distances.

### _Repeater Hub_ | [WiKi](https://en.wikipedia.org/wiki/Ethernet_hub)

For connecting multiple Ethernet devices together and making them act as a single network segment. It has multiple input/output (I/O) ports, in which a signal introduced at the input of any port appears at the output of every port except the original incoming. A hub works at the physical layer (layer 1) of the OSI model. Repeater hubs also participate in collision detection, forwarding a jam signal to all ports if it detects a collision. Hubs are now largely obsolete, having been replaced by network switches except in very old installations or specialized applications.

### _Wireless Access Point (WAP)_ | [WiKi](https://en.wikipedia.org/wiki/Wireless_access_point) | [WiKi (KR)](https://ko.wikipedia.org/wiki/%EB%AC%B4%EC%84%A0_%EC%95%A1%EC%84%B8%EC%8A%A4_%ED%8F%AC%EC%9D%B8%ED%8A%B8)

WAP는 컴퓨터 네트워크에서 와이파이를 이용한 관련 표준을 이용하여 무선 장치들을 유선 장치에 연결할 수 있게 하는 장치이다.

### :bulb: __Setup AP__ | __공유기 초기 설정하기__ :star:

1. __EFM ipTIME__ (A2004MU, A2004NS-MU, N104T):
- `http://192.168.0.1/`

2. __SKT__:
- `http://192.168.35.1/`

3. __KT__:
- `http://172.30.1.254/`

4. __LGU+__:
- `http://192.168.219.1/`

### Structured Calbing | [WiKi](https://en.wikipedia.org/wiki/Structured_cabling)

## Hybrid

Hybrid components can be found in the core or border of a network.

### Multilayer Switch (MLS) | [WiKi](https://en.wikipedia.org/wiki/Multilayer_switch)

A switch that, in addition to switching on OSI layer 2, provides functionality at higher protocol layers.

### Protocol Converter | [WiKi](https://en.wikipedia.org/wiki/Protocol_converter)

A hardware device that converts between two differenct types of transmission, for interoperation.

### Bridge Router (Brouter) | [WiKi](https://en.wikipedia.org/wiki/Bridge_router)

A device that works as a bridge and as a router. The brouter routes packets for known protocols and simply forwards all other packets as a bridge would.

## Border

Hardware or software components which typically sit on the connection point of different networks (for example, between an internal network and en external network) include:

### Proxy Server | [WiKi](https://en.wikipedia.org/wiki/Proxy_server)

Computer network service which allows client to make indirect network connections to other network services.

### Firewall | [WiKi](https://en.wikipedia.org/wiki/Firewall_(computing))

A piece of hardware or software put on the network to prevent some communications forbidden by the network policy. A firewall typically establishes a barrier between a trusted, secure internal network and another outside network, such as the Internet, that is assumed to not be secure or trusted.

### Network Address Translater (NAT) | [WiKi](https://en.wikipedia.org/wiki/Network_address_translation)

Network service (provided as hardware or as software) that converts internal to external network addresses and vice versa.

### Residential Gateway | [WiKi](https://en.wikipedia.org/wiki/Residential_gateway)

Interface between a WAN connection to an internet service provider and the home network.

## End Stations

Other hardware devices used for establishing networks or dial-up connections include:

### Network Interface Controller (NIC) | [WiKi](https://en.wikipedia.org/wiki/Network_interface_controller)

A device connecting a computer to a wire-based computer network.

### Wireless Network Interface Controller | [WiKi](https://en.wikipedia.org/wiki/Wireless_network_interface_controller)

A device connecting the attached computer to a radio-biased computer network.

### _MODEM_ | [WiKi](https://en.wikipedia.org/wiki/Modem)

Device that modulates an analog "carrier" signal (such as sound) to encode digital information, and that also demodulates such a carrier signal to decode the transmitted information. Used (for example) when a computer communicates with another computer over a telephone network.

### _ISDN Terminal Adapter (TA)_ | [WiKi](https://en.wikipedia.org/wiki/Terminal_adapter)

A specialized gateway for ISDN.

### _Line Driver_ | [WiKi](https://en.wikipedia.org/wiki/Line_driver)

A device to increase transmission distance by amplifying the signal; used in base-band networks only.

---

## *Server* | [WiKi](https://en.wikipedia.org/wiki/Server_(computing)) | [WiKi (KR)](https://ko.wikipedia.org/wiki/%EC%84%9C%EB%B2%84)

In computing, a server is a piece of computer hardware of software (computer program) that provides functionality for other programs of devices, called "clients". This architecture is called the client-server model. Servers can provide various functionalities, often called "services", such as sharing data or resources among multiple clients, or performing computation for a client. A single server can serve multiple clients, and a single client can use multiple servers. A client process may run on the same device or may connect over a network to a server on a different device. Typical servers are database servers, file servers, mail servers, print servers, web servers, game servers, and application servers.

Client-server systems are usually most frequently implemented by (and often identified with) the request-response model: a client sends a request to the server, which performs some action and sends a response back to the client, typically with a result for acknowledgment. Designating a computer as "server-class hardware" implies that is is specialized for running servers on it. This often implies that it is more powerful and relialbe than standard personal computers, but alternatively, large computing clusters may be composed of many relatively simple, replaceable server components.

### *File Server* | [WiKi](https://en.wikipedia.org/wiki/File_server)

In computing, a file server (or fileserver) is a computer attached to a network that provides a location for shared disk access, i.e. storage of computer files (such as text, image, sound, video) that can be accessed by the workstations that are able to reach the computer that shares the access through a computer network. The term server highlights the role of the machine in the tranditional client-server scheme, where the clients are the workstations using the storage. A file server does not normally perform computational tasks or run programs on behalf of its client workstations.

### _Database Server_ | [WiKi](https://en.wikipedia.org/wiki/Database_server)

A database server is a server which uses a database application that provides database services to other computer programs or to computers, as defined by the client-server model. Database management systems (DBMSs) frequently provide database-server functionality, and some database management systems (such as MySQL) rely exclusively on the client-server model for database access (while others, like SQLite, are meant for use as an ebmedded database).

## *Server Hosting* | [IBM](https://www.ibm.com/cloud/learn/server-hosting)

Server hosting is an IT service, typically offered by a cloud service provider, that provides remote access to off-premises virtual or physical servers and associated resources for a monthly subscription or usage-based price. Server hosting lets IT teams provision and start using application and data servers without the up-front cost, delays, and labor of purchasing, setting up, managing, and maintaining physical server hardware themselves, on-site.

### Types of Server Hosting

While smaller variations exist, server hosting offerings fall into three general categories:

### Shared server hosting

In shared hosting-the most basic and cost-effective form of server hosting-the resources of one physical server are virtualized and made available to multiple tenants (users or company accounts) in equal proportions. Shared hosting is ideal for basic, personal websites and web apps that have little traffic, few technical requirements, and limited performance or security requirments. But, because all tenants are allocated a finite amount of an individual server's capacity, providers do not allow websites to scale beyond a certain limit. And shared hosting is the server hosting model most susceptible to "noisy nieghbors"-tenants whose applications unexpectedly consume more than their share of resources, causing performance problems for other tenants. FOr more information about shared hosting, see "What is Cloud Hosting?" and "Web Hosting: An Introduction."

### VPS hosting

VPS (virtual private server) hosting offers a kind of next-level multi-tenant hosting-each tenant shares some, but not all, of the resources of a single hardware server and gets a little more control over the hosting environment. Each VPS runs its own operating system (OS) and applications, and it reserves its own portion of the machine's resources (memory, compute, etc.).

VPS provides more control over system specifications, guest operating systems, and the overall software stack. It's also the most easily and affordably scalable form of server hosting, making it an excellent choice for eCommerce systems, email servers, CRM, and other applications that typically bear moderate or spiky traffic.

### Dedicated server hosting

Dedicated server hosting is single-tenant hosting-the server has exclusive access ALL the resources of a single hardware server. Compared to the other forms of hosting listed above, dedicated hosting provides the greatest level of isolation from other servers and customers hosted by the cloud or IT service provider.

- A dedicated host provides sustained single-tenant access to an entire hardware server and all the software installed on it. This model provides the maximum amount of harware flexibility, transparency, and control over workload placement, and it also offers some advantages for hosting bring-your-own licnese software.

- A dedicated instance offers the same isolation and workload placement control but is not coupled with a specific machine. So, for example, if a dedicated instance is re-booted, it could wind up on a new physical machine-a machine dedicated to the same customer account, but nonetheless a new machine, potentially in a different physical location.

- The term bare metal server hosting is often used interchangeably with dedicated servers, but bare metal hosting offerings typically include more clould-like characterisitcs, such as provisioning in minutes (vs. hours), billing in hourly increments (vs. monthly), and providing higher-end hardware, including graphic processing units (GPUs).

### *Web Hosting* | [WiKi](https://en.wikipedia.org/wiki/Web_hosting_service)

A web hosting service (often shorted to web host) is a type of Internet hosting service that allows individuals and organizations to make their website accessible via the World Wide Web. Web hosts are companies that provide space on a server owned or leased for use by client, as well as providing Internet connectivity, typically in a data center. Web hosts can also provide data center space and connectivity to the Internet for other servers located in their data center, called colocation, also known as housing in Latin America or France.

### _Content Delivery Network (CDN)_ | [Cloudflare](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)

A content delivery network (CDN) refers to a geographically distributed group of servers which work together to provide fast delivery of Internet content.

### _Scaling Up vs. Scaling Out_ | [Azure](https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/scaling-out-vs-scaling-up/#overview) | [Blog (KR)](https://tecoble.techcourse.co.kr/post/2021-10-12-scale-up-scale-out/)

### _Scale Up_

Vertical scaling, or scaling up or down, where you increase or decrease computing power or databases as needed-either by changing performance levels or by using elastic database pools to automatically adjust to your workload demands.

When:
- Workloads are hitting some performance limit such as CPU or I/O limits.
- Need to quickly react to fix performance issues that can't be solved with classic database optimization.
- Need a solution that allows you to change service tiers to adapt to changing latency requirements.

### _Scale Out_

Horizontal scaling, or scaling out or in, where you add more databases or divide your large database into smaller nodes, using a data partitioning approach called sharding, which can be managed faster and more easily across servers.

When:
- Geo-distributed applications where every app should access part of the data in the region.
- Each app will access only the shard associated to that region without affecting other shards.
- A global sharding scenario-such as load balancing-where you have a large number of geo-distributed clients that insert data in their own dedicated shards.
- Maxed out your performance requirements, even in the highest performance tiers of your service, or if your data cannot fit into a single database.

### Health Check | [Blog (KR)](https://aroundck.tistory.com/6800)

1. ICMP - Layer 3
2. Port - Layer 4
3. Service - Layer 7

---

## *Distributed Computing* | [WiKi](https://en.wikipedia.org/wiki/Distributed_computing)

Distributed computing is a field of computer science that studies distributed systems. A distributed system is a system whose components are located on different networked computers, which communicate and coordinate their actions by passing messages to one another from any system. The components interact with one another in order to achieve a common goal. Three significant challenges of distributed systems are: maintaining concurrency of components, overcoming the lack of a global clock, and managing the independent failure of components. When a component of one system fails, the entire system does not fail. Examples of distributed systems vary from SOA-based systems to massively multiplayer online games to peer-to-peer applications.

## *Parallel Computing* | [WiKi](https://en.wikipedia.org/wiki/Parallel_computing)

Parallel computing is a type of computation in which many calculations or processes are carried out simultaneously. Large problems can often be divided into smaller ones, which can then be solved at the same time. There are several different forms of parallel computing: bit-level, instruction-level, data, and task parallelism. Parallelism has long been employed in high-performance computing, but has gained broader interest due to the physical constraints preventing frequency scaling. As power consumption (and consequently heat generation) by computers has become a concern in recent years, parallel computing has become the dominant paradigm in computer architecture, mainly in the form of multi-core processors.

### *Grid Computing* | [WiKi](https://en.wikipedia.org/wiki/Grid_computing)

Grid computing is the use of widely distributed computer resources to reach a common goal. A computing grid can be thought of as a distributed system with non-interactive workloads that involve many files. Grid computing is distinguished from conventional high-performance computing systems such as cluster computing in that grid computers have each node set to perform a different task/application. Grid computers also tend to be more heterogeneous and geographically dispersed (thus not physically coupled) than cluster computers. Although a single grid can be dedicated to a particular application, commonly a grid is used for a variety of purpose. Grids are often constructed with general-purpose grid middleware software libraries. Grid sizes can be quite large,

### *Cluster* | [WiKi](https://en.wikipedia.org/wiki/Computer_cluster)

A computer cluster is a set of computers that work together so that they can be viewed as a single system. Unlike grid computers, computer clusters have each node set to perform the same task, controlled and scheduled by software.

The components of a cluster are usually connected to each other through fast local area networks, with each node (computer used as a server) running its own instance of an operating system. In most circumstances, all of the nodes use the same hardware and the same operating system, although in some setups, different operating systems can be used on each computer, or different hardware.

### *Cloud Computing* | [WiKi](https://en.wikipedia.org/wiki/Cloud_computing)

Cloud computing is the on-demand availability of computer system resources, especially data storage (cloud storage) and computing power, without direct active management by the user. Large clouds often have functions distributed over multiple locations, each location being a data center. Cloud computing relies on sharing of resources to achieve coherence and typically uses a "pay-as-you-go" model, which can help in reducing capital expenses but may also lead to unexpected operating expenses for users.

---

### Multiplexing | [Blog (KR)](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=ljh0326s&logNo=220860314191)

멀티플렉싱(다중화)은 단일 링크를 통해 여러 개의 신호를 동시에 전송할 수 있도록 해주는 기술이다. 핵심은 주어진 자원을 얼마나 효율적으로 쓰는가이다. 멀티플렉싱 방법은 크게 analog 주파수 분할 다중화(FDM), analog 파장 분할 다중화(WDM), digital 시분할 다중화(TDM) 3가지로 나뉘며, TDM 방식은 동기식 TDM, 비동기식 TDM으로 나뉜다.

FDM(Frequency Division Multiplexing)은 주파수를 이용한 방식으로 주파수마다 채널을 할당해줘서 그것을 합쳐서 한 라인으로 보내는 것이다. 주파수들 사이에는 신호가 서로 겹치지 않게 하기 위해 보호 대역(guard band)이 있어서 보호 대역만큼 서로 떨어져 있다.

WDM(Wavelength Division Multiplexing)은 광섬유 안에서 멀티플렉싱을 하는 것으로, 기본적으로 FDM과 개념이 같다. 빛의 경우, 주파수란 개념이 없고 대신 파장이 있는데, 여러 파장을 합쳐서 한 라인으로 보내는 것을 말한다.

TDM(Time Division Multiplexing)은 시간에 따라 채널을 나눠주는 방법으로 디지털 네트워크에서 사용하는 방법이다. 실제 네트워크에서 FDM과 TDM을 섞어 쓴다.

동기식 TDM은 송수신이 사이클 시간이 정해져 있어 동기화하기는 쉬우나 항상 데이터를 보내지 않기 때문에 자원의 낭비가 일어난다.

비동기식 TDM은 통계적으로 peek 타임에 쓰는 사용량를 고려해서 비용을 절약할 수 있다. 통계적 TDM이라 하기도 한다.

### _[Multi Processing- vs. Multi Threading- vs. Multi Plexing- Server](https://engineering.linecorp.com/ko/blog/do-not-block-the-event-loop-part1/)_

Multi Processing Server:
1. 부모 프로세스는 리스닝 소켓으로 accept 함수를 호출해서 연결 요청을 수락한다.
2. 이때 얻는 소켓의 파일 디스크립터(클라이언트와 연결된 연결 소켓)를 자식 프로세스를 생성해 넘겨준다.
3. 자식 프로세스는 전달받은 파일 디스크립터를 바탕으로 서비스를 제공한다.

- Pros
  - 프로그램 흐름이 단순하기 때문에 이해하기 쉽다.
  - 안정적인 동작이 가능하다.
    - 운영 체제에서 프로세스는 독립된 실행 객체로 존재한다.
    - 서로 독립된 메모리 공간을 갖고 각 프로세스는 서로 영향을 미치지 않기 때문에 독립적으로 수행이 가능하다.
- Cons:
  - 프로세스 복사가 필요하기 떄문에 리소스를 많이 사용한다.
  - 병렬로 처리해야 하는 수만큼 프로세스를 생성해야 한다.
  - 서로 다른 독립적인 메모리 공간을 갖기 때문에 프로세스 간 정보 교환이 어렵다.

Multi Threading Server:
1. 메인 스레드는 리스닝 소켓으로 accept 함수를 호출해서 연결 요청을 수락한다.
2. 이 때 얻는 소켓의 파일 디스크립터(클라이언트와 연결된 연결 소켓)를 별도 워커 스레드를 생성해 넘겨준다.
3. 워커 스레드는 전달받은 파일 디스크립터를 바탕으로 서비스를 제공한다.

- Pros
  - 프로세스 복사 비용보다 스레드 생성 비용이 적다.
  - 서로 공유하는 메모리가 있기 때문에 스레드간 정보 교환이 쉽다.
- Cons
  - 하나의 프로세스 내에 다수의 스레드가 존재하기 때문에 하나의 스레드에서 발생한 문제가 프로세스 전체에 영향을 미쳐 나머지 다수의 스레드에 영향을 끼칠 수 있다.
  - 멀티프로세싱 방식보다는 비용이 적게 들지만 스레드 관리에 여전히 많은 리소스가 필요하다.
  - 일정 크기의 스레드를 생성해 풀로 관리하며 운영할 수 있지만 요청마다 스레드를 무한정 생성할 수 없기 때문에 많은 수의 요청을 동시에 처리할 수 없다(C10k problem을 해결하지 못한다).

Multi Plexing Server: 블로킹 I/O 모델 -> I/O 멀티플렉싱 모델
1. 애플리케이션에서 I/O 작업을 할 때, 스레드는 데이터가 사용할 수 있는 상태로 준비될 때까지 대기합니다.
2. 커널 내 버퍼에 복사된 데이터를 애플리케이션에서 사용하기 위해서는 커널 공간에서 사용자 공간으로 복사해야 합니다. 애플리케이션은 사용자 모드에서 사용자 공간에만 접근할 수 있기 떄문입니다.

- Pros
  - 단일 프로세스/스레드에서 여러 파일의 입출력 처리가 가능한 덕분에 동시에 수만 개의 커넥션도 처리할 수 있다. 이를 바탕으로 C10k problem을 해결할 수 있다.
  - POSIX 표준을 따르기 때문에 지원하는 운영 체제가 많아 이식성이 좋다.
  - 클라이언트 요청마다 처리하기 위한 별도 스레드를 만들지 않기 때문에 컨텍스트 전환(context switching) 오버헤드가 발생하지 않는다.
- Cons
  - select 함수를 호출해서 전달된 정보는 커널에 등록되지 않은 것이기 때문에 select 함수를 호출할 때마다 매번 관련 정보를 전달해야 한다.
  - select 함수의 호출 결과가 이벤트가 발생한 파일 디스크립터의 개수이기 때문에 어떤 파일 디스크립터에서 이벤트가 발생했는지 확인하기 위해서는 매번 fd_set 테이블 전체를 검사해야 한다.
  - 검사할 수 있는 파일 디스크립터 개수에 제한이 있다(최대 1024개).
  - select 함수를 호출할 때마다 데이터를 복사해야 한다(select 함수를 호출한 후 이벤트를 처리할 때 fd_set 테이블 변경이 필요하기 때문에 미리 복사가 필요하다).

---

## Load Balancing | [AWS](https://aws.amazon.com/what-is/load-balancing/?nc1=h_ls) | [Blog (KR)](https://m.post.naver.com/viewer/postView.naver?volumeNo=27046347&memberNo=2521903)

Load balancing is the method of distributing network traffic equally across a pool of resources that support an application. Modern applications must process millions of users simultaneously and return the correct text, videos, images, and other data to each user in a fast and reliable manner. To handle such high volumes of traffic, most applications have many resources servers with dupliate data between them. A load balancer is a device that sits between the user and the server group and acts as an invisible facilitator, ensuring that all resource servers are used equally.

## Load Balancing Algorithm

A load balancing algorithm is the set of of rules that a load balancer follows to determine the best server for each of the different client requests. Load balancing algorithms fall into two main categories; static load balancing and dynamic load balancing.

### Static Load Balancing

Static load balancing algorithms follow fixed rules and are independent of the current server state.

### Round-robin Method

Allocates requests sequentially. Suitable for use when multiple servers have the same specifications and sessions do not last long.

Servers have IP addresses that tell the client where to send requests. The IP address is a long number that is difficult to remember. To make it easy, a Domain Name System maps website names to servers. In the round-robin method, an authoritative name server does the load balancing instead of specialized hardware or software. The name server returns the IP addresses of different servers in the server farm turn by turn or in a round-robin fashion.

### Weighted Round Robin Method

Each server is weighted and client requests are prioritized among the servers with higher weights.

In weighted round-robin load balancing, you can assign different weights to each server based on their priorty or capacity. Servers with higher weights will recieve more incoming application traffic from the name server.

### IP Hash Method

Handles requests by mapping the client's IP address to a specific server.

In the IP hash method, the load balancer performs a mathematical computation, called hashing, on the client IP address. It converts the client IP address to a number, which is then mapped to individual servers.

### Dynamic Load Balancing

Dynamic load balancing algorithms examine the current state of the servers before distributing traffic. The following are some examples of dynamic load balancing algorithms.

### Least Connection Method

Priority distribution of traffic to the server with the fewest connectinos at the time the request is received. Suitable for long sessions or inconsistent traffic distributed to the server.

A connection is an open communication channel between a client and a server. When the client sends the first request to the server, they authenticate and establish an active connection between each other. In the least connection method, the load balancer checks which servers have the fewest active connections and sends traffic to those servers. This method assumes that all connections require equal processing power for all servers.

### Weighted least connection method

Weighted least connection algorithms assume that some servers can handle more active connections than others. Therefore, you can assign different weights or capacities to each server, and the load balancer sends the new client requests to the server with the least connections by capacity.

### Least Response Time Method

Distributes traffic considering both the server's current connection state and response time. Prioritize load distribution to servers with the fewest connections and the shortest response times.

The response time is the total time that the server takes to process the incoming requests and send a response. The least response time method combines the server response time and the active connections to determine the best server. Load balancers use this algorithm to ensure faster service for all users.

### Resource-based method

In the resource-based method, load balancers distribute traffic by analyzing the current server load. Specialized software called an agent runs on each server and calculates usage of server resources, such as its computing capacity and memory. Then, the load balancer checks the agent for sufficient free resources before distributing traffic to that server.

## Types of Load Balancing

### Application Load 

Complex modern applications have several server farms with multiple servers dedicated to a single application function. Application load balancers look at the request content, such as HTTP headers or SSL session IDs, to redirect traffic. 

### Network Load Balancing

Network load balancers examine IP addresses and other network information to redirect traffic optimally. They track the source of the application traffic and can assign a static IP address to several servers. Network load balancers use the static and dynamic load balancing algorithms described earlier to balance server load.

### Global Server Load Balancing

Global server load balancing occurs across several geographically distributed servers. For example, companies can have servers in multiple data centers, in different countries, and in third-party cloud providers around the globe. In this case, local load balancers manage the application load within a region or zone. They attempt to redirect traffic to a server destination that is geographically closer to the client. They might redirect traffic to servers outside the client’s geographic zone only in case of server failure.

### DNS Load Balancing

In DNS load balancing, you configure your domain to route network requests across a pool of resources on your domain. A domain can correspond to a website, a mail system, a print server, or another service that is made accessible through the internet. DNS load balancing is helpful for maintaining application availability and balancing network traffic across a globally distributed pool of resources. 

## *Load Balancer* | [Blog (KR)](https://m.post.naver.com/viewer/postView.naver?volumeNo=27046347&memberNo=2521903)

The equipment used in the upper layer has all the functions of the equipment in the lower layer. Higher tiers enable more sophisticated load balancing.

### *L4 Load Balancer*

L4 load balancer distributes the load based on information from the network layer (IP, IPX) or transport layer (TCP, UDP). It is possible to divide traffic according to IP address, port number, MAC address, and transport protocol.

### *L7 Load Balancer*

L7 load balancer distributes the load at the application layer (HTTP, FTP, SMTP). It is possible to distribute traffic ti specific servers based on user requests such as HTTP headers, cookies, etc. It is possible to check the contents of a packet and distribute the load to a specific server according to the contents. In addition, it can detect viruses or filter out anomalous traffic such as DoS/DDoS.

---

### *Failover* | [WiKi](https://en.wikipedia.org/wiki/Failover) | [Create a failover cluster](https://learn.microsoft.com/en-us/windows-server/failover-clustering/create-failover-cluster)

Failover is switching to a redundatnt or standby computer server, system, hardware component or network upon the failure or abnormal termination of the previously active application, server, system, hardware component, or network in a computer network. Failover and switchover are essentially the same operation, except that failover is automatic and usually operates without warning, while switchover requires human intervention.

### *Switchover* | [WiKi](https://en.wikipedia.org/wiki/Switchover)

Switchover is the manual switch from one system to a redundant or standby computer server, system, or network upon the failure or abnormal termination of the previously active server, system, or network, or to perform system maintenance, such as installing patches, and upgrading software or hardware.

### Failover vs. Failback | [Blog (KR)](https://velog.io/@zxcvbnm5288/%ED%8E%98%EC%9D%BC%EC%98%A4%EB%B2%84Failover%EC%99%80-%ED%8E%98%EC%9D%BC%EB%B0%B1Failback)

---

### M2M (Machine to Machine) |  [Blog (KR)](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=bonanet1661&logNo=40209624952)

### IoT vs. M2M | [Article (KR)](https://www.digikey.kr/ko/articles/the-difference-between-iot-and-m2m-communication-and-design)

IoT는 인터넷에 연결되는 장치의 네트워크인 반면, M2M은 두 개 이상의 전자 장치 지원 시스템, 기계, 또는 장치 간에 자동화된 방법으로 통신하는 방법이다. M2M는 지점 간 또는 다중 지점 간 연결을 한다. M2M은 IoT라는 용어가 생겨나기 이전에 있었고, 1990년 인터넷이 등장하기 이전에도 있었으며, 20세기 초 양방향 무선 통신이 발명된 이후에 등장했다.

---

### _Gateway_ | [WiKi](https://en.wikipedia.org/wiki/Gateway_(telecommunications))
A gateway is a piece of networking hardware or software used in telecommunications networks that allows data to flow from one discrete network to another. Gateways are distinct from routers or switches in that they communicate using more than one protocol to connect multiple networks and can operate at any of the seven layers of the open systems interconnection model (OSI).

The term gateway can also loosely refer to a computer or computer program configured to perform the tasks of a gateway, such as a default gateway or router, and in the case of HTTP, gateway is also often used as a synonym for reverse proxy.

### _IoT Gateway_

An Internet of things (IoT) gateway provides the bridge (protocol converter) between IoT devices in the field, the cloud, and user equipment such as smartphones. The IoT gateway provides a communication link between the field and the cloud, and may provide offline services and real-time control of devices in the field.

To achieve sustainable interoperability in the Internet of things ecosystem, two dominant architectures for data exchange protocols are used: bus-based (DDS, REST, XMPP) and broker-based (AMQP, CoAP, MQTT, JMI). Protocols that support information exchange between interoperable domains are classified as message centric (AMQP, MQTT, JMS, REST) or data-centric (DDS, CoAP, XMPP). Interconnected devices communicate using lightweight protocols that don't require extensive CPU resources. C, Java, Python and some scripting languages are the preferred choices of IoT application developers. IoT nodes use separate IoT gateways to handle protocol conversion, database storage or decision making (e.g. collision handling), in order to supplement the low intelligence of devices.

### _Mesh Networking_ | [WiKi](https://en.wikipedia.org/wiki/Mesh_networking)

A mesh networking (or simply meshnet) is a local area network topology in which the infrastructure nodes (i.e. bridges, swithces, and other infrastructure devices) connect directly, dynamically and non-hierarchially to as many other nodes as possible and cooperate with one another to efficiently route data to and from clients.

This lack of dependency on one node allows for every node to participate in the relay of information. Mesh networks dynamically self-organize and self-configure, which can reduce installation overhead. The ability to self-configure enables dynamic distribution of workloads, particularly in the event a few nodes should fail. This in turn contributes to fault-tolerance and reduced maintenance costs.

Mesh topology may be contrasted with conventional star/tree local network topologies in which the bridges/switches are directly linked to only a small subset of other bridges/switches, and the links between these infrastructure neighbours are hierarchical. While star-and-tree topologies are very well established, highly standardized and vendor-neutral, vendors of mesh network devices have not yet all agreed on common standards, and interoperability between devices from different vendors is not yet assured.

### _Mesh Wi-Fi_ | [TP-Link](https://www.tp-link.com/kr/mesh-wifi/)

안정적인 네트워크가 중요한 비즈니스 상황에서만 사용되었다. 최근 소비자 시장에도 진출해 빠른 속도와 넓은 범위의 Wi-Fi 네트워크를 제공한다.

Mesh Wi-Fi는 사각지대를 제거하고 가정 전체에서 중단없는 WiFi를 제공하기 위해 설계된 가정용 WiFi시스템이다. Mesh 시스템은 네트워크에 연결된 디바이스가 더 빠른 속도, 더 넓은 커버리즈 그리고 신뢰할 수 있는 연결성을 갖도록 도와줍니다. 기존의 공유기가 단일 포인트 지점에서 WiFi를 전송했다면 Mesh WiFi 시스템은 여러 개의 액세스 포인트에 신호를 전달합니다. 하나의 디바이스가 모뎀에 연결되면 해당 디바이스는 메인 허브가 됩니다. 다른 디바이스(노드)는 공유기의 신호를 잡고 다시 신호를 보냅니다. 그 결과 사용자가 어디에 있든 강한 신호의 무선 네트워크를 이용할 수 있습니다.

---

## _Wireless_ | [WiKi](https://en.wikipedia.org/wiki/Wireless) | [Bluetooth, WiFi, Zigbee, and Z-Wave in IoT Blog](https://itigic.com/wifi-bluetooth-zigbee-z-wave-differences/)

### _Wireless Fidelity (Wi-Fi, WiFi)_ | [WiFi Alliance](https://www.wi-fi.org/) | [Papers](https://www.wi-fi.org/discover-wi-fi/papers)

A wireless data transmission technology used for Internet based on radio waves such as the radio, television, mobile telehony. The frequencies used are different, specifically the WiFi uses 2.4GHz and 5GHz.

- It operates in the 2.4GHz and 5GHz frequency band.
- Its range depends on many factors but is much greater than Bluetooth.
- It allows the Internet connection of different devices and can also be used to connect devices to each other within a network.
- Maximum data transmission rate 9.6Gbps for WiFi 6.
- Difficulty crossing certain obstacles and may find interference with other waves emitting at the same frequencies.
- It use is perhaps the most widespread and hence we can find a lot of connected devices today.

### _[Wi-Fi Protected Setup (WPS) (KR)](https://www.wi-fi.org/ko/discover-wi-fi/wi-fi-protected-setup)_

Wi-Fi Protected Setup은 가정 및 소규모 사무실 환경에서 보안 적용된 Wi-Fi 네트워크를 간편하게 설정할 수 있도록 해주는 기술에 대한 인증 프로그램입니다. Wi-Fi Protected Setup은 소비자들이 익숙한 방법(버튼 누르기, PIN 입력)을 통해 네트워크를 구성하고 보안을 적용할 수 있도록 지원합니다.

### _Zigbee_ | [TI](https://www.ti.com/wireless-connectivity/zigbee/overview.html)

Zigbee is a standards-based wireless mesh network used widely in building automation, lighting, smart city, medical and asset tracking. Scalabe Zigbee offers the low power mesh solutions enabling multi-year coin cell use or battery-less operation across industrial temperatures. 

- Requires the use of a bridge or hub device.
- Mesh network system.
- The devices do not connect individually to the Internet.
- It offers low energy consumption.
- Reduced range, between 10 and 20 meters.
- Very low data transfer speeds, defined speed of 250Kbps.
- Mainly for home use, sensors, data collections that do not require high speeds, toys, etc.
- It is an open protocol.

### _Z-Wave_ | [TechTarget](https://www.techtarget.com/iotagenda/definition/Z-Wave)

- Requires the use of a bridge or hub device.
- Mesh network system.
- The devices do not connect individually to the Internet.
- It offers low energy consumption.
- Maximum reach 100m.
- Very low data transfer speeds, maximum speed of 100Kbps.
- Mainly for home use, control of household items, sensors, electronic security elements, start-up of electronic devices or entertainment.
- It is a closed protocol.

### *[NFC](http://nearfieldcommunication.org/)* | [NordVPN](https://nordvpn.com/ko/blog/nfc-ran/) | [Doorlock NEWS (KR)](https://www.mk.co.kr/news/it/view/2021/02/133597/) | [Mobile Blog (KR)](https://m.blog.naver.com/shin6752/222129724466)

Near field communication, abbreviated NFC, is a form of contactless communication between devices like smartphones or tablets. Contactless communication allows a user to wave the smartphone onver a NFC compatible device to send information without needing to touch the devices together or go throught multiple steps setting up a connection.

NFC는 Wi-Fi, 3G, LTE, 전원 또는 수동 페어링이 필요 없는 기술인 RFID에서 발전했습니다. NFC 칩은 보안 카드 또는 각종 결제 및 여행 카드에서 찾을 수 있습니다. 오늘날 대부분의 스마트폰에도 NFC가 있으며 주로 비접촉 모바일 결제에 사용됩니다.

- 카드 모드(Card Mode): NFC 단말이 스마트 카드처럼 동작합니다. 예를 들어, 안드로이드 폰을 교통 카드로 사용하는 경우입니다.
- 태그 읽기/쓰기(R/W Mode): NFC 단말이 NFC 태그로부터 데이터를 읽거나, NFC 태그에 데이터를 씁니다. 예를 들어 태그 읽어서 특정 웹 사이트로 연결하는 경우입니다.
- P2P 모드(P2P Mode): NFC 단말이 다른 NFC 단말로부터 데이터를 읽어옵니다. 예를 들어, NFC 단말 사이에 연락처를 전달하는 경우입니다.

주의할 점은 NFC를 활용한 도어록 해제방식은 피해야합니다. NFC의 경우, 한 개의 일련 번호를 대량으로 생산하기 때문에 내 휴대전화가 아닌 다른 사람의 휴대전화로도 열릴 수 있는 개연성이 충분합니다. 한국소비자원은 "교통카드, 신용카드, 휴대전화에 내장된 NFC 카드 등을 등록해 사용하지 말아햐 한다"고 강조했습니다.

### NFC 태그란?

NFC 태그는 NFC 칩이라고 생각하면 쉽게 이해할 수 있습니다. NFC 태그는 전자 유도의 원리에 따라 작동하므로 충전을 할 필요는 없습니다. 칩 자체는 아주 작으므로 명함, 펜, 열쇠 고리, 손목 밴드 등 많은 곳에 쉽게 손쉽게 설치할 수 있습니다. 또한 마이크로 칩과 여러 겹의 구리선으로 연결되어 있으며 이를 통해 주파수를 발생합니다. 마이크로 칩은 NFC를 지원하는 장치에서 읽을 수 있는 정보를 포함합니다.

또한 NFC 태그에 접촉하면 휴대폰이 매너 모드로 전환하거나, Wi-Fi를 켜기, 혹은 취침 모드로 들어가는 등의 지정한 동작을 수행하도록 할 수도 있습니다.

태그의 복잡성은 다양할 수 있습니다. 단순한 태그는 읽기 및 쓰기 의미 체계만 제공하며 때로는 일회성 프로그래밍 가능한 영역을 사용하여 카드를 읽기 전용으로 설정합니다. 더 복잡한 태그는 수학 연산을 제공하며 섹터에 대한 접속을 인증하기 위해 암호화 하드웨어를 사용합니다. 가장 정교한 태그는 태그에서 실행되는 코드와 복잡한 상호작용이 가능하도록 하는 운영 환경을 포함합니다. 태그에 저장되는 데이터를 다양한 형식으로 작성할 수도 있지만, 다수의 안드로이드 프레임워크 API는 NDEF(NFC Data Exchange Format)라는 NFC Forum 표준을 기반으로 합니다.

### NFC와 RFID의 차이점

- 수신 범위

NFC는 고작 10cm 정도인 것에 비해 일반적으로 RFID가 NFC보다 수신 범위가 긴데다 RFID는 단방향 통신이고, NFC는 양방향 통신입니다.

- 태그 및 리더 역할의 유동성

RFID는 태그와 리더 역할이 고정되어 있습니다. 예를 들어 결제를 하는 상황에서 RFID는 태그의 역할로서 정보를 내주는 역할만 수행하고 카드 리더기는 RFID에서 정보를 읽는 역할을 수행합니다. 반면 NFC는 상황에 따라 태그와 리더 역할을 유동적으로 변경할 수 있습니다.

### NFC와 블루투스 차이점

NFC와 Bluetooth는 모두 휴대폰에서 사용할 수 있는 비교적 단거리 통신 기술입니다.

- NFC는 블루투스보다 느린 속도로 작동하고 범위가 훨씬 짧지만 전력을 훨씬 적게 소비하고 페어링이 필요하지 않는다. NFC는 일반적으로 블루투스보다 빠르게 설정되지만 블루투스의 저에너지보다 전송 속도가 낮습니다. 하지만 NFC를 사용하면 수동 구성을 수행하여 장치를 식별하는 대신 두 NFC 장치 간의 연결이 0.1초 이내에 자동으로 설정됩니다. NFC의 최대 데이터 전송 속도 또한 블루투스보다 느립니다.

- 위에 서술되어 있듯이, NFC의 최대 수신 거리가 짧으므로 수신 거리 미만이면 연결이 자동으로 끊기기 때문에, 원치 않는 끼어들기의 가능성이 줄어듭니다. 신호를 전송하는 물리적 장치와의 상관 관계를 복잡하게 만드는 사람이 많고 혼잡한 지역에 특히 적합합니다.

### _[Bluetooth](https://www.bluetooth.com/)_ | [IEEE](https://ieeexplore.ieee.org/document/1368913)

Bluetooth is a standard for short range, low power, and low cost wireless communication that uses radio technology. Over 2100 compaines around the world already support Bluetooth technology. The wireless personal area network (WPAN) technology, based on the Bluetooth specification, is now an IEEE standard under the denomination of 802.15 WPANs. This work presents an overview about the Bluetooth communication. Bluetooth wireless technology encompasses several key points that facilitate its widespread adoption: 1) it is an open specification that is publicly available and royalty free; 2) its short-range wireless capability allows peripheral devices to communicate over a single air-interface, replacing the cables that use connectors with a multitude of shapes, sizes and numbers of pins; 3) Bluetooth supports both voice and data, making it an ideal technology to enable many types of devices to communicate; and 4) Bluetooth uses an unregulated frequency band available anywhere in the world.. To fully realize the Bluetooth vision, full networking of multiple Bluetooth devices is required. This leads to the investigation of Bluetooth scatternets, which must address ascatternet formation and reconfiguration, scheduling, and routing issues.

### Bluetooth Classic

The Bluetooth Classic radio, also referred to as Bluetooth Basic Rate/Enhanced Data Rate (BR/EDR), is a low power radio that streams data over 79 channels in the 2.4GHz unlicensed industrial, scientific, and medical (ISM) frequency band. Supporting point-to-point device communication, Bluetooth Classic is mainly used to enable wireless audio streaming and has become the standard radio protocol behind wireless speakers, headphones, and in-car entertainment systems. The Bluetooth Classic radio also enables data transfer applications, including mobile printing.

### Bluetooth Low Energy (LE)

The Bluetooth Low Energy (LE) radio is designed for very low power operation. Transmitting data over 40 channels in the 2.4GHz unlicensed ISM frequency band, the Bluetooth LE radio provides developers a tremendous amount of flexibility to build products that meet the unique connectivity requirements of their market. Bluetooth LE supports multiple communication topologies, expanding from point-to-point to broadcast and, most recently, mesh, enabling Bluetooth technology to support the creation of reliable, large-scale device networks. While initially known for its device communications capabilities, Bluetooth LE is now also widely used as a device positioning technology to address the increasing demand for high accuracy indoor location services. Bluetooth LE now includes features that enable one device to determine the presence, distance, and direction of another device.

- It operates in the free ISM band between 2.402 and 2.480GHz, so it does not require a license.
- Its range depends on the emission power available to the transmitting equipment and whether we are indoors or outdoors.
- It is oriented to the point-to-point connection or mesh network of few nodes.
- Maximum data transmission speed 2Mbps.
- Difficulty crossing certain obstacles such as walls.
- It use is mainly focused on desktop computers, laptops, mobile or audio output devices, hands-free, sports or home automation devices and even toys, medical technology or industry.

---

### _[Matter](https://csa-iot.org/all-solutions/matter/)_ | [GitHub](https://github.com/project-chip/connectedhomeip)

Matter (formerly Project Connected Home over IP, or Project CHIP) is a new Working Group within the Connectivity Standards Alliance (CSA, formerly Zigbee Alliance). This Working Group plans to develop and promote the adoption of a new, royalty-free connectivity standard to increase compatibility among smart home products, with security as a fundamental design tenet.

The goal of the Matter project is to simplify development for manufacturers and increase compatibility for consumers. The project is built around a shared belief that smart home devices should be secure, reliable, and seamless to use. By building upon Internet Protocol (IP), the project aims to enable communication across smart home devices, mobile apps, and cloud services and to define a specific set of IP-based networking technologies for device certification.

The CSA officially opened the Matter Working Group on January 17, 2020 and is in the process of drafting the specification.

---

### _Host-based card emulation overview_ | [Android](https://developer.android.com/guide/topics/connectivity/nfc/hce)

Many Android-powered devices that offer NFC functionality already support NFC card emulation. In most cases, the card is emulated by a separate chip in the device, called a secure element. Many SIM cards provided by wireless carriers also contain a secure element.

Android 4.4 and higher provide an additional method of card emulation that doesn't involve a secure element, called host-based card emulation. This allows any Android application to emulate a card and talk directly to the NFC reader. This topic describes how host-based card emulation (HCE) works on Android and how you can develop an app that emulates an NFC card using this technique.

### Card emulation with a secure element

When NFC card emulation is provided using a secure element, the card to be emulated is provisioned into the secure elemtn on the device through an Android application. Then, when the user holds the device over an NFC terminal, the NFC controller in the device routes all data from the reader directly to the secure element. 

The secure element itself performs the communication with the NFC terminal, and no Android application is involved in the transaction. After the transaction is complete, an Android application can query the secure element directly for the transaction status and notify the user.

### Host-based card emulation

When an NFC card is emulated using host-based card emulation, the data is routed directly to the host CPU instead of being routed to a secure element.

### Supported NFC cards and protocols

The NFC standards offer support for many different protocols, and there are different types of cards that you can emulate.

Android 4.4 and higher supports several protocols that are common in the market today. Many existing contactless cards are already based on these protocols, such as contactless payment cards. These protocols are also supported by many NFC readers in the market today, including Android NFC devices functioning as readers themselves (`IsoDep` class). This allows you to build and deploy an end-to-end NFC solution around the HCE using only Android-powered devices.

Specifically, Android 4.4 and higher supports emulating cards that are based on the NFC-Forum ISO-DEP specification (based on ISO/IEC 14443-4) and process Application Protocol Data Units (APDUs) as defined in the ISO/IEC 7816-4 specification. Android mandates emulating ISO-DEP only on top of the Nfc-A (ISO/IEC 14443-3 Type A) technology. Support for Nfc-B (ISO/IEC 14443-4 Type B) technology is optional.

### HCE services

The HCE architecture in Android is based around Android `Service` components (known as HCE services). One of the key advantages of a service is that it can run in the background without any user interface. This is a natural fit for many HCE applications, like loyality or transit cards, which the user shouldn't need to launch an app to use. Instead, tapping the device against the NFC reader starts the correct service if it is not already running and executes the transaction in the background. Of course, you are free to launch additional UI (such as user notifications) from your service when appropriate.

### _Core NFC_ | [Apple](https://developer.apple.com/documentation/corenfc)

Detect NFC tags, read messages that contiain NDEF data, and save data to writable tags.

Your app can read tags to give users more information about their physical environment and the real-world objects in it. Using Core NFC, you can read Near Field Communication (NFC) tags of types 1 through 5 that contain data in the NFC data Exchange Format (NDEF). For example, your app might give users information about products they find in a store or exhibits they visit in a museum.

Your app can also write data to tags, and interact with protocol specific tag such as ISO 7816, ISO 15693, FeliCa, and MIFARE tags.

Core NFC is not available for use in app extensions, and it requires a device that supports Near Field Communication. To determine if support is available, check the `readingAvailable` class property before starting a reader session.

Core NFC doesn't support payment-realted Application IDs.

### Tap to Pay on iPhone | [Apple](https://developer.apple.com/tap-to-pay/)

Payment apps can now accpet contactless payments from contactless credit or debit cards, Apple Pay, Apple Watch, and smartphones with other digital wallets - right on iPhone and without any extra terminals or hardware.

With over two thirds of all credit and debit cards in the U.S. issued as contactless - enabled cards, and rapidly increasing adoption of contactless payments, merchants will be able to seamlessly accept payments through a simple tap on their iPhone from most customers.

### ProximityReader | [Apple](https://developer.apple.com/documentation/ProximityReader)

Read contactless physical and digital wallet cards using your iPhone.

The ProximityReader framework supports Tap to Pay on iPhone, which allows a person's iPhone to act as a point-to-sale device without additional hardware. ProximityReader also supports the reading or loyalty cards from the Wallet app. Use this framework to initiate the payment process from your app.

The use of this framework requires you to coordinate with a participating payment service provider that is Level 3 certified. Contact your payment provider and work with them to set up a workflow for handling payments. When you're ready, contact Apple and request the entitlement you need to integrate Tap to Pay on iPhone support into your app.

Tap to Pay on iPhone follows the PCI CPoC Standard, which uses Level 2 certified payment kernels and a user interface for eading contactless payment cards.

---

### Reference
- Access Point, https://m.blog.naver.com/PostView.nhn?blogId=twers&logNo=50118628879&proxyReferer=https:%2F%2Fwww.google.com%2F, 2020-07-17-Fri.
- Wireless Access Point Wiki KR, https://ko.wikipedia.org/wiki/%EB%AC%B4%EC%84%A0_%EC%95%A1%EC%84%B8%EC%8A%A4_%ED%8F%AC%EC%9D%B8%ED%8A%B8, 2020-07-17-Fri.
- Access Point, http://www.ktword.co.kr/abbr_view.php?m_temp1=2237, 2020-07-17-Fri.
- Router Wiki KR, https://ko.wikipedia.org/wiki/%EB%9D%BC%EC%9A%B0%ED%84%B0, 2020-11-08-Sun.
- Server Wiki KR, https://ko.wikipedia.org/wiki/%EC%84%9C%EB%B2%84, 2020-11-08-Sun.
- Computer Network Wiki, https://en.wikipedia.org/wiki/Computer_network, 2021-03-30-Tue.
- Telecommunications Network Wiki, https://en.wikipedia.org/wiki/Telecommunications_network, 2021-04-29-Thu.
- Internet Wiki, https://en.wikipedia.org/wiki/Internet, 2021-04-29-Thu.
- WAN Wiki, https://en.wikipedia.org/wiki/Wide_area_network, 2021-04-29-Thu.
- MAN Wiki, https://en.wikipedia.org/wiki/Metropolitan_area_network, 2021-04-29-Thu.
- LAN Wiki, https://en.wikipedia.org/wiki/Local_area_network, 2021-04-29-Thu.
- IAN Wiki, https://en.wikipedia.org/wiki/Internet_area_network, 2021-04-29-Thu.
- CAN Wiki, https://en.wikipedia.org/wiki/Campus_network, 2021-04-29-Thu.
- VPN Wiki, https://en.wikipedia.org/wiki/Virtual_private_network, 2021-04-29-Thu.
- Node Wiki, https://en.wikipedia.org/wiki/Node_(networking), 2021-04-29-Thu.
- Networking Hardware Wiki, https://en.wikipedia.org/wiki/Networking_hardware, 2021-04-29-Thu.
- Gateway Wiki, https://en.wikipedia.org/wiki/Gateway_(telecommunications), 2021-04-29-Thu.
- Network Swiitch Wiki, https://en.wikipedia.org/wiki/Network_switch, 2021-04-29-Thu.
- Bridging Wiki, https://en.wikipedia.org/wiki/Bridging_(networking), 2021-04-29-Thu.
- Repeater Wiki, https://en.wikipedia.org/wiki/Repeater, 2021-04-29-Thu.
- Ethernet Hub Wiki, https://en.wikipedia.org/wiki/Ethernet_hub, 2021-04-29-Thu.
- WAP Wiki, https://en.wikipedia.org/wiki/Wireless_access_point, 2021-04-29-Thu.
- Structured Cabling Wiki, https://en.wikipedia.org/wiki/Structured_cabling, 2021-04-29-Thu.
- MLS Wiki, https://en.wikipedia.org/wiki/Multilayer_switch, 2021-04-29-Thu.
- Protocol Converter Wiki, https://en.wikipedia.org/wiki/Protocol_converter, 2021-04-29-Thu.
- Bridge Router Wiki, https://en.wikipedia.org/wiki/Bridge_router, 2021-04-29-Thu.
- Proxy Server Wiki, https://en.wikipedia.org/wiki/Proxy_server, 2021-04-29-Thu.
- Firewall Wiki, https://en.wikipedia.org/wiki/Firewall_(computing), 2021-04-29-Thu.
- NAT Wiki, https://en.wikipedia.org/wiki/Network_address_translation, 2021-04-29-Thu.
- Residential Gateway Wiki, https://en.wikipedia.org/wiki/Residential_gateway, 2021-04-29-Thu.
- NIC Wiki, https://en.wikipedia.org/wiki/Network_interface_controller, 2021-04-29-Thu.
- Wireless Network Interface Controller Wiki, https://en.wikipedia.org/wiki/Wireless_network_interface_controller, 2021-04-29-Thu.
- Modem Wiki, https://en.wikipedia.org/wiki/Modem, 2021-04-29-Thu.
- TA Wiki, https://en.wikipedia.org/wiki/Terminal_adapter, 2021-04-29-Thu.
- Line Driver Wiki, https://en.wikipedia.org/wiki/Line_driver, 2021-04-29-Thu.
- Mesh Wi-Fi TP-Link KR, https://www.tp-link.com/kr/mesh-wifi/, 2022-07-13-Wed.
- Gateway Wiki, https://en.wikipedia.org/wiki/Gateway_(telecommunications), 2022-07-13-Wed.
- Mesh Networking Wiki, https://en.wikipedia.org/wiki/Mesh_networking, 2022-07-13-Wed.
- Bluetooth IEEE, https://ieeexplore.ieee.org/document/1368913, 2022-07-13-Wed.
- Samsung Electronics SmartThings Blog KR, https://wildchild.tistory.com/entry/%EC%8A%A4%EB%A7%88%ED%8A%B8%EC%8B%B1%EC%8A%A4-%ED%97%88%EB%B8%8C-%EC%99%9C-%ED%95%84%EC%9A%94%ED%95%A0%EA%B9%8C-%EC%82%BC%EC%84%B1-%EC%8A%A4%EB%A7%88%ED%8A%B8%EC%8B%B1%EC%8A%A4-%ED%97%88%EB%B8%8C-%EC%8A%A4%EB%A7%88%ED%8A%B8%ED%99%88, 2022-07-13-Wed.
- Zigbee TI, https://www.ti.com/wireless-connectivity/zigbee/overview.html, 2022-07-13-Wed.
- Z-Wave TechTarget, https://www.techtarget.com/iotagenda/definition/Z-Wave, 2022-07-13-Wed.
- Bluetooth, WiFi, Zigbee, and Z-Wave in IoT Blog, https://itigic.com/wifi-bluetooth-zigbee-z-wave-differences/, 2022-07-13-Wed.
- NFC, http://nearfieldcommunication.org/, 2022-07-15-Fri.
- Bluetooth, https://www.bluetooth.com/, 2022-07-15-Fri.
- Wireless Wiki, https://en.wikipedia.org/wiki/Wireless, 2022-07-15-Fri.
- NFC NordVPN, https://nordvpn.com/ko/blog/nfc-ran/, 2022-07-15-Fri.
- Doorlock NEWS KR, https://www.mk.co.kr/news/it/view/2021/02/133597/, 2022-07-15-Fri.
- Mobile NFC Blog KR, https://m.blog.naver.com/shin6752/222129724466, 2022-07-15-Fri.
- Wireless Personal Area Network (WPAN) CSRC, https://csrc.nist.gov/glossary/term/wireless_personal_area_network, 2022-07-18-Mon.
- Personal Area Network (PAN) CSRC, https://csrc.nist.gov/glossary/term/personal_area_network, 2022-07-18-Mon.
- Wi-Fi Alliance, https://www.wi-fi.org/, 2022-07-18-Mon.
- Matter, https://csa-iot.org/all-solutions/matter/, 2022-07-18-Mon.
- Matter GitHub, https://github.com/project-chip/connectedhomeip, 2022-07-18-Mon.
- Host-based card emulation overview Anroid, https://developer.android.com/guide/topics/connectivity/nfc/hce, 2022-07-21-Thu.
- Core NFC Apple, https://developer.apple.com/documentation/corenfc, 2022-07-25-Mon.
- Tap to Pay on iPhone Apple, https://developer.apple.com/tap-to-pay/, 2022-07-25-Mon.
- ProximityReader Apple, https://developer.apple.com/documentation/ProximityReader, 2022-07-25-Mon.
- WPS KR, https://www.wi-fi.org/ko/discover-wi-fi/wi-fi-protected-setup, 2022-07-26-Tue.
- M2M Blog KR, https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=bonanet1661&logNo=40209624952, 2022-08-29-Mon.
- M2M vs. IoT Article KR, https://www.digikey.kr/ko/articles/the-difference-between-iot-and-m2m-communication-and-design, 2022-08-29-Mon.
- Network Multiplexing Blog KR, https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=ljh0326s&logNo=220860314191, 2022-09-01-Thu.
- Server Wiki, https://en.wikipedia.org/wiki/Server_(computing), 2022-09-29-Thu.
- Server Hosting IBM, https://www.ibm.com/cloud/learn/server-hosting, 2022-09-30-Fri.
- Web Hosting Wiki, https://en.wikipedia.org/wiki/Web_hosting_service, 2021-06-10-Thu.
- Failover Wiki, https://en.wikipedia.org/wiki/Failover, 2022-10-16-Sun.
- Create a failover cluster, https://learn.microsoft.com/en-us/windows-server/failover-clustering/create-failover-cluster, 2022-10-16-Sun.
- Switchover Wiki, https://en.wikipedia.org/wiki/Switchover, 2022-10-16-Sun.
- Distributed Computing WiKi, https://en.wikipedia.org/wiki/Distributed_computing, 2022-10-17-Mon.
- Parallel Computing WiKi, https://en.wikipedia.org/wiki/Parallel_computing, 2022-10-17-Mon.
- Grid Computing WiKi, https://en.wikipedia.org/wiki/Grid_computing, 2022-10-17-Mon.
- Cluster WiKi, https://en.wikipedia.org/wiki/Computer_cluster, 2022-10-17-Mon.
- Cloud Computing WiKi, https://en.wikipedia.org/wiki/Cloud_computing, 2022-10-17-Mon.
- Load Balancing Blog KR, https://m.post.naver.com/viewer/postView.naver?volumeNo=27046347&memberNo=2521903, 2022-10-18-Tue.
- Failover vs. Failback Blog KR, https://velog.io/@zxcvbnm5288/%ED%8E%98%EC%9D%BC%EC%98%A4%EB%B2%84Failover%EC%99%80-%ED%8E%98%EC%9D%BC%EB%B0%B1Failback, 2022-10-21-Fri.
- File Server WiKi, https://en.wikipedia.org/wiki/File_server, 2022-11-07-Mon.
- Database Server WiKi, https://en.wikipedia.org/wiki/Database_server, 2022-11-07-Mon.
- Content Delivery Network Clourflare, https://www.cloudflare.com/learning/cdn/what-is-a-cdn/, 2022-11-08-Tue.
- Modem WiKi KR, https://ko.wikipedia.org/wiki/%EB%AA%A8%EB%8E%80#:~:text=%EB%AA%A8%EB%8E%80(MODEM%2C%20MOdulator%20and%20DEModulator,%EC%A3%BC%EB%B3%80%EA%B8%B0%EA%B8%B0%EB%A1%9C%20%EB%A7%8E%EC%9D%B4%20%EC%82%AC%EC%9A%A9%ED%95%9C%EB%8B%A4., 2022-11-08-Tue.
- OSI Model Cloudflare, https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/, 2022-11-09-Wed.
- LAN Cisco, https://www.cisco.com/c/en/us/products/switches/what-is-a-lan-local-area-network.html, 2022-11-09-Wed.
- WAN Cisco, https://www.cisco.com/c/en/us/products/switches/what-is-a-wan-wide-area-network.html, 2022-11-09-Wed.
- Scaling Up vs. Scaling Out Azure, https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/scaling-out-vs-scaling-up/#overview, 2022-11-18-Fri.
- Scaling Up vs. Scaling Out Blog KR, https://tecoble.techcourse.co.kr/post/2021-10-12-scale-up-scale-out/, 2022-11-18-Fri.
- Server Event Loop Line KR, https://engineering.linecorp.com/ko/blog/do-not-block-the-event-loop-part1/, 2022-11-25-Fri.
- Health Check Blog KR, https://aroundck.tistory.com/6800, 2022-12-20-Tue.
- Load Balancing AWS, https://aws.amazon.com/what-is/load-balancing/, 2023-03-16-Thu.
