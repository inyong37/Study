# _Network_

`Language and Framework of Web move to "Web" folder.`

# _Internet_ | [WiKi](https://en.wikipedia.org/wiki/Internet)

The Internet (or internet) is the global system of interconnected computer networks that uses the Internet protocol suite (TCP/IP) to communicate between networks and devices. It is a network of networks that consists of private, public, academic, business, and government networks of local to global scope, linked by a broad array of electronic, wireless, and optical networking technologies. The Internet carries a vast range of information resources and services, such as the inter-linked hypertext documents and applications of the World Wide Web (WWW), electronic mail, telephony, and file sharing.

The origins of the Internet date back to the development of packet switching and research commissioned by the United States Department of Defense in the 1960s to enable time-sharing of computers. The primary precursor network, the ARPANET, initially served as a backbone for interconnection of regional academic and military networks in the 1970s. The funding of the National Science Foundation Network as a new backbone in the 1980s, as well as private funding for other commercial extensions, led to worldwide participation in the development of new networking technologies, and the merger of many networks. The linking of commercial networks and enterprices by the early 1990s marked the beginning of the transiion to the modern Internet, and generated a sustained exponential growth as generations of institutional, personal, and mobile computers were connected to the network. Although the Internet was widely used by academia in the 1980s, commercialization incorporated its services and technologies into virtually every aspect of modern life.

Most traditional communication media, including telephony, radio, television, paper mail and newspapers are reshaped, redefined, or even bypassed by the Internet, giving birth to new services such as email, Internet telephony, Internet television, online music, digital newspapers, and video streaming websites. Newspaper, book, and other print publishing are adapting to website technology, or are reshaped into blogging, web feeds and online news aggregators. The Internet has enabled and accelerated new forms of personal interactions throught instant messaging, Internet forums, and social networking services. Online shopping has grown exponentially for major retailers, small businesses, and enttrepreneurs, as it enables firms to extend their "brick and mortar" presence to serve a larger market or even sell goods and services entirely online. Business-to-business and financial services on the Internet affect supply chains across entire industries.

The Internet has no single centralized governance in either technological implementation or policies for access and usage; each constituent network sets its own policies. The overreaching definitions of the two principal name spaces in the Interent, the Internet Protocol address (IP address) space and the Domain Name System (DNS), are directed by a maintainer organization, the Internet Corporation for Assigned Names and Numbers (ICANN). The technical underpinning and standardization of the core protocols is an activity of the Internet Engineering Task Force (IETF), a non-profit organization of loosely affiliated international participants that anyone may associate with by contributing technical expertise. In November 2006, the Internet was included on USA Today's list of New Seven Wonders.

### *Virtual Private Network (VPN)*

VPN(가상사설망)은 네트워크를 통해 그룹이 내부적으로 통신할 목적으로 사용하는 사설 통신망이다.

## *Proxy* | [Blog (KR)](https://brownbears.tistory.com/191)

프록시란 대리라는 의미로, 주로 보안상의 이유로 직접 통신할 수 없는 두 점 사이에서 통신을 할 경우 그 사이에 있어서 중계기로서 대리로 통신을 수행하는 기능을 가리켜 프록시, 그 중계 기능을 하는 것을 프록시 서버라 한다.

### Proxy Server

Proxy Server(프록시 서버)는 클라이언트가 다른 네트워크 서비스에 간접적으로 접속할 수 있게 해주는 시스템 또는 프로그램이다. 서버와 클라이언트 사이 중계기로서 대리로 통신하는 것을 "Proxy" 중계를 해주는 것을 "Proxy Server"라 한다.

### Ego Motion

Ego motion is a 3D motion of a system within an environment.

### visual odometry/odometry

Visual odometry is the estimation of ego-motion using computer vision techniques.

### ego-motion vs odometry

Both words can be used interchangeably in general.

### *Hyper Text Transfer Protocol (HTTP)*

### *HTTP Secure (HTTPS)*

### HTTP vs. HTTPS

HTTPS is also referred to as HTTP over TLS or http over SSL

### *File Transfer Protocol (FTP)*

### *Secure Shell (SSH)*

## *Domain Name System (DNS)* | [WiKi](https://en.wikipedia.org/wiki/Domain_Name_System) | [WiKi (KR)](https://ko.wikipedia.org/wiki/%EB%8F%84%EB%A9%94%EC%9D%B8_%EB%84%A4%EC%9E%84_%EC%8B%9C%EC%8A%A4%ED%85%9C)

The Domain Name System (DNS) is a hierarchical and decentralized naming system for computers, services, or other resources connected to the Internet or a private network. It associates various information with domain names assigned to each of the participating entities. Most prominently, it translates more readily memorized domain names to the numerical IP addresses needed for locating and identifying computer services and devices with the underlying network protocols. By providing a worldwide, distributed directory service, the Domain Name System has been an essential component of the functionality of the Internet since 1985.

The Domain Name System delegates the responsibility of assigning domain names and mapping those names to Internet resources by designating authoritative name servers for each domain. Network administrators may delegate authority over sub-domains of their allocated name space to other name servers. This mechanism provides distributed and fault-tolerant service and was designed to avoid a single large central database.

The Domain Name System also specifies the technical functionality of the database service that is at its core. It defines the DNS protocol, a detailed specification of the data structures and data communication exchanges used in the DNS, as part of the Internet Protocol Suite.

The Internet maintains two principal namespaces, the domain name hierarchy and the Internet Protocol (IP) address spaces. The Domain Name System maintains the domain name hierarchy and provides translation services between it and the address spaces. Internet name servers and a communication protocol implement the Domain Name System. A DNS name server is a server that stores the DNS records for a domain; a DNS name server responds with answers to queries against its database.

The most common types of records stored in the DNS database are for Start of Authority (SOA), IP addresses (A and AAAA), SMTP mail exchangers (MX), name servers (NS), pointers for reverse DNS lookups (PTR), and domain name aliases (CNAME). Although not intended to be a general purpose database, DNS has been expanded over time to store records for other types of data for either automatic lookups, such as DNSSEC records, or for human queries such as responsible person (RP) records. As a general purpose database, the DNS has also been used in combating unsolicited email (spam) by storing a real-time blackhole list (RBL). The DNS database is traditionally stored in a structured text file, the zone file, but other database systems are common.

### *Dynamic DNS (DDNS)* | [WiKi](https://en.wikipedia.org/wiki/Dynamic_DNS) | [WiKi (KR)](https://ko.wikipedia.org/wiki/DDNS)

Dynamic DNS (DDNS) is a method of automatically updating a name server in the Domain Name System (DNS), often in real time, with the active DDNS configuration of its configured hostnames, addresses or other information.

The term is used to describe two different concepts. The first is "dynamic DNS updating" which refers to systems that are used to update traditional DNS records without manual editing. These mechanisms are explained in RFC 2136, and use the TSIG mechanism to provide security. The second kind of dynamic DNS permits lightweight and immediate updates often using an update client, which do not use the RFC2136 standard for updating DNS records. These clients provide a persistent addressing method for devices that change their location, configuration or IP address frequently.

### *Multicast* | [Blog (KR)](https://softtone-someday.tistory.com/14)

멀티캐스트는 같은 데이터를 특정 그룹에게 보내주어야 할 때 사용하는 인터넷 protocol이다. 멀티캐스트는 송신자는 한 채널에 자신의 데이터를 보내고 수신자는 그 데이터 중 자신이 조인한 채널만 수신한다. 1:N 통신 기술이다. 멀티캐스트는 상대방이 데이터를 제대로 받았는지 확인하지 않는 UDP(User Datagram Protocol) 방식을 사용한다. 멀티캐스트 주소는 224.0.0.0 ~ 239.255.255.255 범위를 갖고, 이 대역은 멀티캐스트 신호만 보내도록 규정되어 있다.

멀티캐스트는 TTL(Time to Live)이라는 필드를 가진다. 이는 전송된 신호가 몇 번의 라우터를 거칠 동안 살아있게 할 거냐는 뜻이다. 멀티캐스트 신호가 라우터를 지날 때마다 TTL 값을 하나씩 감소시킨다. 만약, TTL=1이라면 라우터를 하나 지나면 TTL=0이 되면서 이후에 해당 신호는 더 이상 사용되지 않는다. 즉, 신호의 생존 주기이다.

멀티캐스트는 보통 그룹과 IP address, port number가 정해져 있다. 수신자는 해당하는 그룹에 join해야 해당 주소로 보내지고 있는 신호를 받을 수 있다. 또한, 그룹에 참여한 후 실제 사용할 포트와 해당 주소를 묶는 bind 작업이 필요하다. 즉, 이 멀티캐스트 그룹의 신호들은 이 인터넷 주소로 듣겠다고 선언해야한다.

브로드캐스트는 멀티캐스트에서 그룹을 뺀 개념이다. 모두에게 신호를 보내고, 모두가 모든 신호를 듣는다. 연결된 장치들 모두가 듣기 때문에 구현이 용이하지만, 원하지 않는 대상도 내 신호를 들을 수 있고 불필요한 트래픽이 발생한다.

### *multicast Domain Name Service (mDNS)* | [MOMOIOT (KR)](https://momoiot.co.kr/iot-tech/mdns/)

mDNS는 UDP 멀티캐스트를 기반으로, 로컬 네트워크 상에 있는 어떤 호스트 또는 호스트의 IP를 찾기 위해 만들어진 protocol이다. mDNS를 지원하는 호스트는 확장 기능으로 자신이 제공할 수 있는 서비스를 알림으로써 LAN 상의 다른 호스트가 이를 discovery하여 활용할 수 있는 방안으로 제공하기도 한다.

예로, 컴퓨터에서 LAN 상에 있는 프린터를 검색하여 이를 사용할 수 있도록 만든 기능도 mDNS를 활용한 것이다. IoT에서 mDNS 기능을 활용하여 LAN 상에 있는 companion 기기를 검색하여 검색된 기기가 있으면 서로 유기적으로 정보를 교환하면서 시스템적으로 동작할 수 있도록 구현할 수 있다.

### Device Discovery Protocol: SSDP vs. mDNS | [Blog (KR)](https://www.joinc.co.kr/w/Site/IOT/Discovery)

IoT에서 네트워크 자동 설정을 위한 DHCP는 필수다.

SSDP는 notify HTTP method를 announce하여 멀티캐스트 그룹 멤버에서 자신이 join했음을 알려줄 수 있다. SSDP는 두 가지 방식으로 찾을 수 있다. 첫 번째는 기기가 자신의 정보를 멀티캐스트 채널을 통해서 알리는 방식이다. Control point가 멀티캐스트 채널에 붙어 있다면, 연결할 수 있는 기기가 검색됐음을 알려줄 것이다. 두 번째는 control point에서 멀티캐스트 채널로 search 요청을 보내는 방식이다. 멀티캐스트 채널에 붙어 있는 기기가 있다면, search 요청에 응답할 것이다. 기기를 찾은 후에는 기기의 mac address와 IP address를 이용해서 유니캐스트 통신을 한다.

mDNS는 로컬 네트워크 영역에서 설정 없이(zero configuration) 호스트 이름을 찾기 위해 사용하는 서비스이다. Unicast Domain Name System (DNS)와 유사한 프로그래밍 인터페이스와 패킷 형식을 사용한다. 소형 네트워크 환경에서 별도의 네임 서버를 사용하지 않고 호스트를 찾을 수 있다. mDNS는 멀티캐스트 기술을 이용한다. mDNS client는 호스트 이름을 알아야 할 경우 IP 멀티캐스트 쿼리 메세지를 전송한다. 이때 자신의 호스트 이름과 IP 주소 등, 자신을 확인할 수 있는 정보들을 함께 전송한다. 멀티캐스트 채널에 있던 모든 호스트들은 이 정보를 수신해서 mDNS 캐쉬에 업데이트한다. 패킷 구조를 제외하면 SSDP와 작동 방식이 매우 유사하다.

## *Dynamic Host Configuration Protocol (DHCP)* | [Blog (KR)](https://jwprogramming.tistory.com/35)

DHCP란 호스트의 IP 주소와 각종 TCP/IP protocol의 기본 설정을 client에게 자동적으로 제공해주는 protocol이다. DHCP에 대한 표준은 RFC 문서에 정의되어 있으며, DHCP는 네트워크에 사용되는 IP 주소를 DHCP server가 중앙집중식으로 관리하는 client/server 모델을 사용한다. DHCP 지원 client는 네트워크 부팅 과정에서 DHCP server에 IP 주소를 요청하고 이를 얻을 수 있다. 즉, 네트워크 안에 컴퓨터에 자동으로 네임 서버 주소, IP 주소, 게이트웨이 주소를 할당해주고, 해당 client에게 일정 기간 임대하는 동적 주소 할당 프로토콜이다.

PC의 수가 많거나 PC 자체 변동사항이 많은 경우 IP 설정이 자동으로 되기 때문에 효율적으로 사용 가능하며 IP를 자동으로 할당해주기 때문에 IP 충돌을 막을 수 있다. 단, DHCP server에 의존되기 때문에 server가 다운되면 IP 할당이 제대로 이루어지지 않는다.

DHCP를 통한 IP 주소 할당은 임대라는 개념을 가지고 있는데, 이는 DHCP server가 IP 주소를 영구적으로 단말에 할당하는 것이 아니고 임대기간(IP Lease Time)을 명시하여 그 기간 동안만 단말이 IP 주소를 사용하도록 하는 것이다. 단말은 임대기간 이우헤도 계속 해당 IP 주소를 사용하고자 한다면 IP 주소 임대기간 연장(IP Address Renewal)을 DHCP server에 요청해야 하고 또한 단말은 임대 받은 IP 주소가 더 이상 필요치 않게 되면 IP 주소 반납 절차(IP Address Release)를 수행하게 된다. DHCP server와 client 사이에 메세지는 1. DHCP Discover (by client), 2. DHCP Offer (by server), 3. DHCP Request (by client), 4. DHCP Ack (by server)로 이루어진다.

### *Simple Service Discovery Protocol (SSDP)* | [Blog (KR)](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=koromoon&logNo=220201986853) | [Home Assistant Integration](https://www.home-assistant.io/integrations/ssdp/)

SSDP는 네트워크 서비스나 정보를 찾기 위해서 사용하는 네트워크 protocol이며, 이를 이용하면 DHCP나 DNS와 같은 네트워크 서버 혹은 정적인 host 설정 없이 이런 일들을 수행할 수 있다. 일반 거주와 소규모 사무 환경에서 UPnP(Universal Plug and Play)를 위한 기본적인 protocol로 널리 사용된다(SSDP는 UPnP 표준에 포함된다). HTTPU(UDP 기반의 HTTP)를 이용하며, 모든 데이터는 TEXT로 통신한다. UDP 1900 port를 사용하며 IP Multicast 주소를 이용한다. SSDP는 Advertisement, Search 두 개의 타입이 있다.

### UPnP (Universal Plug and Play) | [Blog (KR)](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=koromoon&logNo=220201986853)

홈 네트워크에 있는 네트워크 장치들이 서로 연동될 수 있도록 하는 범용 표준 protocol로 특정 운영체제나 프로그래밍 언어, 미디어와는 독립적으로 네트워크 상의 다바이스 간에 명령과 제어를 가능하게 한다. 사용자가 직접 네트워크 설정, 유지 관리를 하지 않고도 쉽게 디바이스와 서비스 연결을 제공한다. IP, TCP, UDP, HTTP, XML과 같은 기존의 protocol을 사용한다. Wire protocol에 기반을 두고 있으며, 디바이스 간의 교환하는 데이터는 XML로 표현되고 HTTP를 통해서 통신한다. IP 네트워킹을 채택한 이유는 다른 물리적 미디어로 확장이 용이하며 실제 여러 vendor 간의 상호 운용성을 가능케한다. UPnP를 통한 디바이스 간의 통신은 discovery, control, description, presentation, eventing 단계로 나누어지며, SSDP를 이용한 통신은 discovery 단계에서 이용된다.

---

### *Anonymous Pipe* | [WiKi](https://en.wikipedia.org/wiki/Anonymous_pipe) | [Blog (KR)](https://12bme.tistory.com/226)

An anonymous pipe is a simple FIFO communication chaneel that may be used for one-way IPC(InterProcess Communication). AN implementation is often integrated into the operating system's file IO subsystem. Typically a parent program opens anonymous pipes, and creates a new porcess that inherits the other ends of the pipes, or creates several new processes and arranges them in a pipeline. Ful-duplex(two-way) communication normally requires two anonymous pipes. Pipelines are supported in most popular operating systems, from Unix and DOS onwards, and are created using the "|" character in many shells.

### *Named Pipe* | [WiKi](https://en.wikipedia.org/wiki/Named_pipe) | [Blog (KR)](https://mug896.github.io/bash-shell/named_pipe.html)

A named pips(also known as a FIFO for its behavior) is an extension to the traditional pipe concept on Unix and Unix-like systems, and is one of the methods of IPC. The concepth is also found in OS/2 and Microsoft Windows, althought the semantics differ substantially. A tranditional pipe is unnamed and lasts only as long as the process. A named pipe, however, can last as long as the system is up, beyond the life of the process. It can be deleted if no longer used, Usually a named pipe appears as a file, and generally processes attach to it for IPC.

### *File Descriptor* | [Wiki (KR)](https://ko.wikipedia.org/wiki/%ED%8C%8C%EC%9D%BC_%EC%84%9C%EC%88%A0%EC%9E%90)

File descriptor(파일 서술자/기술자)는 특정한 파일에 접근하기 위한 추상적인 키이다. 이 용어는 일반적으로 POSIX 운영 체제에 쓰인다. Microsoft Windows와 C 표준 입출력 라이브러리 환경에서는 file handle(파일 핸들)이라는 말이 선호되지만 후자의 경우 기술적으로 다른 객체이다. POSIX에서 fd는 정수, 곧 C형 int를 말한다. 모든 프로세스가 갖추어야 하는 표준 POSIX fd는 다음과 같이 3개가 있다. 1. 정숫값 0인 경우 stdin(표준 입력), 2. 정숫값이 1인 경우 stdout(표준 출력), 3. 정숫값이 2인 경우 stderr(표준 오류)이다.

### URI vs. URL vs. URN

Uniform Resource Identifier(URI), Uniform Resource Locator(URL), and Uniform Resource Name(URN)는 각 네트워크 상에 존재하는 자원을 구분하는 ID(식별자), 네트워크 상에 존재하는 resource의 location, 중복되지 않는 유일한 resource name을 나타낸다. URN, URL은 URI에 포함된다. 따라서 URN, URL은 URI라 할 수 있다. URL은 where을 나타내는 것으로 자원에 접근하는 방법이나 네트워크 위치를 표현하고 있다. http://, https://, ftp:// 등이 포함되면 URL이다. URN은 what을 나타내는 것으로 해당 자원이 무엇인지 중복되지 않는 유일한 식별 가능한 이름이어야 한다.

### Cloud Computing

Cloud computing은 여러 deivces에서 나온 정보들을 cloud에서 전부 처리하는 computing environment이다.

### Edge Computing

Edge computing은 cloud에서 모든 연산을 처리하는 것이 아닌, mobile devices들이 직접 연산을 하거나 edge들에서 데이터 연산을 하여 cloud에 데이터를 뿌려주는 것이다.

---

### *WebSocket* | [Blog (KR)](https://duckdevelope.tistory.com/19)

Transport protocol의 일종으로 웹 버전의 TCP 또는 Socket이다. WebSocket은 server와 client 간에 socket connection을 유지해서 언제든 양방향 통신 또는 데이터 전송이 가능하도록 하는 기술이다. Real-time web application 구현을 위해 널리 사용된다(Social Network applications, multiplayer games, Google Docs, video call, stock exchange).

웹 어플리케이션에서 기존 server와 client 간의 통신은 대부분 Http를 통해 이루어졌으며 Http는 request/response 기반의 stateless protocol이다. Server와 client 간의 socket connection과 같은 영구적인 연결이 되어있지 않고 client 쪽에서 필요할 떄 request를 할 때만 server가 response를 하는 방식으로 통신이 진행되는 단방향 통신이다. 이럴 경우 server 쪽 데이터가 업데이트되더라도 client 쪽에는 화면은 refresh하지 않는 한 변경된 데이터가 업데이트되지 않는 문제가 발생한다. 이런 문제는 long polling, Ajax를 사용해 어느 정도 해결이 가능하지만, 데이터의 빠른 업데이트가 중요한 요소인 application에서는 실시간 업데이트가 아주 중요하기 때문에 Web Socket을 사용한다.

Web Socket은 stateful protocol이기 때문에 client와 한 번 연결이 되면 계속 같은 라인을 사용해서 통신하기 때문에 Http 사용 시 필요없이 발생되는 Http와 TCP 연결 traffic을 피할 수 있다. 마지막으로 Web Socket은 Http와 같은 port 80을 사용하기에 기업용 application에 적용할 때 방화벽은 재설정하지 않아도 되는 장점이 있다. Server와 client 간의 WebSocket 연결은 Http protocol을 통해 이루어진다. 만약 연결이 정상적으로 이루어진다면 server와 client 간에 WebSocket 연결이 이루어지고 일정 시간이 지나면 Http 연결은 자동으로 끊어진다.

HTTP 통신 방법과 WebSocket의 차이점은 protocoldㅣ다. WebSocket protocol은 접속 확립에 HTTP를 사용하지만, 그 후 통신은 WebSocket 독자의 protocol로 이루어진다. 또한 header가 상당히 작아 overhead가 적은 특성이 있다. 장시간 접속을 전제로 하기 때문에, 접속한 상태라면 client라 server로부터 data 송신이 가능하다. 더불어 데이터의 송신과 수신에 각각 connection을 맺을 필요가 없어 하나의 connection으로 데이터를 송수신할 수 있다.

### REST vs. WebSocket | [Blog (KR)](https://yoonucho.github.io/review/2019/04/01/restVSwebsocket.html)

둘의 차이점은 Connection 유지 여부이다.

WebSocket 이전의 양방향 통신 방법은 client가 server에게 HTTP request를 주기적으로 요청하는 Polling 방식, client가 server에게 HTTP request를 요청하면 server는 대기하다가 event 발생 시 client에게 reponse하는 Long Polling 방식, Long Polling 방식과 같이 client에서 server로 HTTP request를 보내고 server에서 event를 전달할 때 해당 request를 끊지 않고 필요한 메세지만 보내기(flush)를 반복하는 Streaming 방식이 있다. AJAX는 JavaScript의 XmlHttpRequest object를 기반으로, 비동기 JavaScript 및 XML의 축약된 양식으로 웹 페이지 일부만 송수신하는 반이중 통신 방식이다.

### [MQTT (Message Queuing Telemetry Transport)](https://mqtt.org/) | [Blog (KR)](https://medium.com/@jspark141515/mqtt%EB%9E%80-314472c246ee) | [Home Assistant Integration](https://www.home-assistant.io/integrations/mqtt/)

MQTT is an OASIS standard messaging protocol for the Internet of Things (IoT). It is designed as an extremely lightweight publish/subscribe messaging transport that is ideal for connecting remote devices with a small code footprint and minimal network bandwidth. MQTT today is used in a wide variety of industries, such as automotive, manufacturing, telecommunications, oil and gas, etc.

MQTT는 M2M, IoT를 위한 프로토콜로서, 최소한의 전력과 패킷량으로 통신하는 프로토콜이다. MQTT는 Http, TCP 등의 통신과 같이 client-server 구조로 이루어지지 않고 Broker, Publisher, Subscriber 구조로 이루어져있다.

Publish는 topic을 발행(publish)하고, Subscriber는 topic에 구독(subsribe)한다. Brokers는 이들을 중계하는 역할을 하며, 단일 topic에 여러 Subscriber가 구독할 수 있기 떄문에 1:N통신도 가능하다. 계층을 구성할 수 있기 때문에 IoT 센서와 같은 데이터를 관리하기에 용이하다.

MQTT는 QoS(Quality of Service)를 제공한다. 세 단계로 나누어져 있다. 메세지는 한번만 전달되며, 전달 이후 수신 과정을 확인하지 않는다. 메세지는 한번 이상 전달되고, hand shaking 과정을 추적하나 strict하게 추적하지 않기 때문에 중복 수신의 가능성이 있다. 메세지는 한번만 전달되고 hand shaking의 모든 과정을 확인한다. QoS의 단계가 높아질수록 통신의 품질은 향상되지만 성능 저하의 가능성이 있으므로 프로젝트 특성에 따라 결정되어야 한다.

Broker의 종류는 Mosquitto, HiveMQ, mosca, ActiveMQ, RabbitMQ 등이 있다. 사용 예시로는, Docker를 이용해 Mosquitto broker를 생성한다. MQTT Explorer와 같은 도구로 Broker의 IP 주소를 입력하여 broker에 접속한다. 이 도구를 이용해 Publsih가 가능하다. Subsribe는 Python과 paho 라이브러리를 이용하여 client에 IP 주소로 접속하고 "/test/1"를 subscribe한다. MQTT Explorer에서 "/test/1" topic에 데이터를 publish하면, python 코드를 실행해놓은 곳에서 topic의 데이터를 받아 읽을 수 있다.

---

# The Web | [Wiki](https://en.wikipedia.org/wiki/World_Wide_Web) | [Tutorial](https://opentutorials.org/course/3083)

The World Wide Web (WWW), commonly known as The Web, is an information system where documents and other web resources are identified by Uniform Resource Locators (URLs, such as https://example.com/), which may be interlinked by hyperlinks, and are accessible over the Internet. The resources of the Web are transferred via the Hypertext Transfer Protocol (HTTP), may be accessed by users by a software application called a web browswer, and are published by a software application called a web server. The World Wide Web is not synonymous with the Internet, which pre-dated the Web in some form by over two decades and upon which technologies the Web is built.

English scientist Sir Timothy Berners-Lee invented the World Wide Web in 1989. He wrote the first web brower in 1990 while employed at CERN near Geneva, Switzerland. The browser was released outside CERN to other research institutions starting in January 1991, and then to the general public in August 1991. The Web began to enter everyday use in 1993-4, when websites for general use started to become available. The World Wide Web has been central to the development of the Information Age, and is the primary tool bilions of people use to interact on the Internet.

Web resources may be any type of downloaded media, but web pages are hypertext documents formatted in Hypertext Markup Language (HTML). Special HTML syntax displays embedded hyperlinks with URLs which permits users to navigate to other web resources. In addition to text, web pages may contain references to images, video, audio, and software components which are either displayed or internally executed in the user's web browser to render pages or streams of multimedia content.

Multiple web resources with a common theme and usually a common domain name, make up a website. Websties are sotred in computers that are running a web server, which is a program that responds to requests made over the Internet from web browsers running on a user's coimputer. Website content can be provided by a publisher, or interactively from user-generated content. Websites are provided for a myraid of informative, entertainment, commercial, and governmental reasons.

### *Web Browser* | [Wiki](https://en.wikipedia.org/wiki/Web_browser)

A web browswer (commonly referred to as a browser) is application software for accessing the World Wide Web. When a user requests a web page from a particular website, the web browser retrieves the necessary content from a web server and then displays the page on the user's device.

A web browser is not the same thing as a search engine, though the two are often confused. A search engine is a website that provides links to other websites. However, to connect to a website's server and display its web pages, a user must have a web browser installed.

Web browsers are used on a range of devices, including desktops, laptops, and smartphones. In 2020, an estimated 4.9 billion people used a browser. The most used browser is Google Chrome, with a 64% global market share on all devices, followed by Safari with 19%.

### *Web Site* | [Wiki](https://en.wikipedia.org/wiki/Website) | [Home of the first website](http://info.cern.ch/)

A webste (also written as web site) is a collection of web pages and related content that is identified by a common domain name and published on at least on web server. Notable examples are wikipedia.org, google.com, and amazon.com.

All publicly accessible websites collectively constitute the World Wide Web. There are also private websites that can only be accessed on a private network, such as a company's internal website for its employees.

Websites are typically dedicated to a particular topic or purpose, such as news, education, commerce, entertainment, or social networking, Hyperlinking between web pages guides the navigation of the site, which often starts with a home page.

Users can access websites on a range of devices, including desktops, laptops, tablets, and smartphones. The app used on these devices is called a web browser.

### _Web Page_ | [Wiki](https://en.wikipedia.org/wiki/Web_page)

A web page(or webpage) is a hypertext document provided by a website and displayed to a user in a web browser. A website typically consists of many web pages linked together in a coherent fashion. The name "web page" is a metaphor of paper pages bound together into a book.

### _Web Server_ | [Wiki](https://en.wikipedia.org/wiki/Web_server)

A web server is computer software and underlying hardware that accepts requests via HTTP, the network protocol created to distribute web pages, or its secure variant HTTPS. A user agent, commonly a web browser or web crawler, initiates communication by making a request for a specific resource using HTTP, and the server responds with the content of that resource or an error message. The server can also accept and store resources sent from the user agent if configured to do so.

A server can be a single computer, or even an embedded system such as a router with a built-in configuration interface, but high-traffic websites typically run web servers on fleets of computers designed to handle large numbers of requests for documents, multimedia files and interactive scripts. A resource sent from a web server can be a preexisting file available to the server, or it can be generated at the time of the request by another program that communicates with the server program. The former is often faster and more easily cached for repeated requests, which the latter supports a broader range of applications. Websites that server generated content usually incorporate stored files whenever possible.

Technologies such as REST and SOAP, which use HTTP as a basic for general computer-to-computer communication, have extended the application of web servers well beyond their original purpose of serving human-readable pages.

### *[NGINX](https://nginx.org/en/)* | [HW Specification](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://www.nginx.com/wp-content/uploads/2019/11/Sizing-Guide-for-Deploying-NGINX-Plus-on-Bare-Metal-Servers-2019-11-09.pdf) | [HW Specification (KR)](https://nginxstore.com/docs/sizing-guide-for-deploying-nginx-plus/)

nginx is an HTTP and reverse proxy server, a mail proxy server, and a generic TCP/UCP proxy server, originally written by Igor Sysoev. For a long time, it has been running on many heavily loaded Russian sites including Yandex, Mail.Ru, VK, and Rambler. According to Netcraft, nginx served or proxied 21.48% busiest sites in September 2022. Here are some of the success stories: Dropbox, Netflix, Wordpress.com, FastMail.FM.

The sources and documentation are distributed under the 2-clause BSD-like license.

Commercial support is available from Nginx, Inc.

- $750: 2 CPU Cores (Intel Xeon CPU E5-2690 v3 @2.60GHz) & 4 GB RAM & 2x1 GbE NIC & 500 GB HDD: 90,000 RPS, 4,000 SSL TPS (RSA), 4,500 SSL TPS (ECC) 1Gbps throughput

Requests per second (RPS): Measures the ability of NGINX Plus to process HTTP requests. The client sends connections. NGINX Plus processes each request and forwards it to a web server over a separate keepalive connection.

SSL transactions per second (SSL TPS): Measures the ability of NGINX Plus to process new SSL/TLS connections. Clients send a series of HTTPS requests, each on a new connection. NGINX Plus parses the requests and forwards them to a web server over an established keepalive connection. The web server sends back a 0-byte response for each request.

Throughput: Measures the volume in gigabits per second (Gbps) of traffic that NGINX Plus can sustain when serving large files over HTTP.

### NGINX Tunning | [Blog (KR)]

### *[nip.io](https://nip.io/)*

Dead simple wildcard DNS for any IP Address. Stop editing your `etc/hosts` file with custom hostname and IP address mappings. nip.io allows you to do that by mapping any IP Address to a hostname using the following formats:

Without a name:

10.0.0.1.nip.io maps to 10.0.0.1

192-168-1-250.nip.io maps to 192.168.1.250

0a000803.nip.io maps to 10.0.8.3

With a name:

app.10.8.0.1.nip.io maps to 10.8.0.1

app-116-203-255-68.nip.io maps to 116.203.255.68

app-c0a801fc.nip.io maps to 192.168.1.252

customer1.app.10.0.0.1.nip.io maps to 10.0.0.1

customer2-app-127-0-0-1.nip.io maps to 127.0.0.1

customer3-app-7f000101.nip.io maps to 127.0.0.1

nip.io maps <anything>[.-]<IP Address>.nip.io in "dot", "dash" or "hexadecimal" notation to the corresponding <IP Address>:
  
dot notation: magic.127.0.0.1.nip.io
  
dash notation: magic-127-0-0-1.nip.io
  
hexadecimal notation: magic-7f000001.nip.io

The "dash" and "hexadecimal" notation is especially useful when using services like LetsEncrypt as it's just a regular sub-domain of nip.io

---

### Reference

- ego-motion vs odometry, https://answers.ros.org/question/296686/what-is-the-differences-between-ego-motion-and-odometry/, 2020-03-16-Mon.
- http vs https, https://www.keycdn.com/blog/difference-between-http-and-https, 2020-03-16-Mon.
- DNS Wiki, https://en.wikipedia.org/wiki/Domain_Name_System, 2020-10-06-Tue.
- DNS Wiki KR, https://ko.wikipedia.org/wiki/%EB%8F%84%EB%A9%94%EC%9D%B8_%EB%84%A4%EC%9E%84_%EC%8B%9C%EC%8A%A4%ED%85%9C, 2020-10-06-Tue.
- DDNS Wiki, https://en.wikipedia.org/wiki/Dynamic_DNS, 2020-10-06-Tue.
- DDNS Wiki KR, https://ko.wikipedia.org/wiki/DDNS, 2020-10-06-Tue.
- Internet Wiki, https://en.wikipedia.org/wiki/Internet, 2021-06-22-Tue.
- Anonymous Pipe Wiki, https://en.wikipedia.org/wiki/Anonymous_pipe, 2020-11-09-Mon.
- Pipe blog KR, https://12bme.tistory.com/226, 2020-11-09-Mon.
- Named Pipe Wiki, https://en.wikipedia.org/wiki/Named_pipe, 2020-11-09-Mon.
- Named Pipe blog KR, https://mug896.github.io/bash-shell/named_pipe.html, 2020-11-09-Mon.
- File Descriptor Wiki KR, https://ko.wikipedia.org/wiki/%ED%8C%8C%EC%9D%BC_%EC%84%9C%EC%88%A0%EC%9E%90, 2020-11-09-Mon.
- URI vs. URL vs. URN Blog KR, https://nsinc.tistory.com/192, 2021-03-08-Mon.
- Cloud Computing and Edge Computing, http://melonicedlatte.com/machinelearning/2019/11/01/212800.html, 2021-03-09-Tue.
- Roblox, https://www.roblox.com/, 2021-04-29-Thu.
- Opentutorials WEBn KR, https://opentutorials.org/course/3083, 2021-06-10-Thu.
- Web Wiki, https://en.wikipedia.org/wiki/World_Wide_Web, 2021-06-10-Thu.
- Web Browser Wiki, https://en.wikipedia.org/wiki/Web_browser, 2021-06-10-Thu.
- Web Site Wiki, https://en.wikipedia.org/wiki/Website, 2021-06-10-Thu.
- Web Page Wiki, https://en.wikipedia.org/wiki/Web_page, 2021-06-10-Thu.
- Web Server Wiki, https://en.wikipedia.org/wiki/Web_server, 2021-06-10-Thu.
- MQTT, https://mqtt.org/, 2022-08-18-Thu.
- MQTT Blog KR, https://medium.com/@jspark141515/mqtt%EB%9E%80-314472c246ee, 2022-08-29-Mon.
- Proxy Blog KR, https://brownbears.tistory.com/191, 2022-08-29-Mon.
- Home Assistant Integration MQTT, https://www.home-assistant.io/integrations/mqtt/, 2022-08-29-Mon.
- WebSocket Blog KR, https://duckdevelope.tistory.com/19, 2022-08-29-Mon.
- SSDP UPnP Blog KR, https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=koromoon&logNo=220201986853, 2022-08-29-Mon.
- mDNS MOMOIOT KR, https://momoiot.co.kr/iot-tech/mdns/, 2022-08-29-Mon.
- DHCP Blog KR, https://jwprogramming.tistory.com/35, 2022-08-29-Mon.
- REST vs. WebSocket Blog KR, https://yoonucho.github.io/review/2019/04/01/restVSwebsocket.html, 2022-08-29-Mon.
- Discovery Protocol SSDP vs. mDNS Blog KR, https://www.joinc.co.kr/w/Site/IOT/Discovery, 2022-08-29-Mon.
- Multicast Blog KR, https://softtone-someday.tistory.com/14, 2022-08-29-Mon.
- NGINX, https://nginx.org/en/, 2022-10-15-Sat.
- nip.io, https://nip.io/, 2022-10-15-Sat.
- NGINX Server Hardware Specification, chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://www.nginx.com/wp-content/uploads/2019/11/Sizing-Guide-for-Deploying-NGINX-Plus-on-Bare-Metal-Servers-2019-11-09.pdf, 2022-11-01-Tue.
- NGINX Server Hardware Specification KR, https://nginxstore.com/docs/sizing-guide-for-deploying-nginx-plus/, 2022-11-01-Tue.
- NGINX Tuning Blog KR, https://couplewith.tistory.com/entry/%EA%BF%80%ED%8C%81%EA%B3%A0%EC%84%B1%EB%8A%A5-Nginx%EB%A5%BC%EC%9C%84%ED%95%9C-%ED%8A%9C%EB%8B%9D4-%EB%A9%94%EB%AA%A8%EB%A6%AC-%EB%B0%8F-CPU-%ED%8A%9C%EB%8B%9D%ED%95%98%EA%B8%B0-Processor, 2022-11-04-Fri.
  
