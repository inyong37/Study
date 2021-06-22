# Network

## Internet | [Wiki](https://en.wikipedia.org/wiki/Internet)
The Internet (or internet) is the global system of interconnected computer networks that uses the Internet protocol suite (TCP/IP) to communicate between networks and devices. It is a network of networks that consists of private, public, academic, business, and government networks of local to global scope, linked by a broad array of electronic, wireless, and optical networking technologies. The Internet carries a vast range of information resources and services, such as the inter-linked hypertext documents and applications of the World Wide Web (WWW), electronic mail, telephony, and file sharing.

The origins of the Internet date back to the development of packet switching and research commissioned by the United States Department of Defense in the 1960s to enable time-sharing of computers. The primary precursor network, the ARPANET, initially served as a backbone for interconnection of regional academic and military networks in the 1970s. The funding of the National Science Foundation Network as a new backbone in the 1980s, as well as private funding for other commercial extensions, led to worldwide participation in the development of new networking technologies, and the merger of many networks. The linking of commercial networks and enterprices by the early 1990s marked the beginning of the transiion to the modern Internet, and generated a sustained exponential growth as generations of institutional, personal, and mobile computers were connected to the network. Although the Internet was widely used by academia in the 1980s, commercialization incorporated its services and technologies into virtually every aspect of modern life.

Most traditional communication media, including telephony, radio, television, paper mail and newspapers are reshaped, redefined, or even bypassed by the Internet, giving birth to new services such as email, Internet telephony, Internet television, online music, digital newspapers, and video streaming websites. Newspaper, book, and other print publishing are adapting to website technology, or are reshaped into blogging, web feeds and online news aggregators. The Internet has enabled and accelerated new forms of personal interactions throught instant messaging, Internet forums, and social networking services. Online shopping has grown exponentially for major retailers, small businesses, and enttrepreneurs, as it enables firms to extend their "brick and mortar" presence to serve a larger market or even sell goods and services entirely online. Business-to-business and financial services on the Internet affect supply chains across entire industries.

The Internet has no single centralized governance in either technological implementation or policies for access and usage; each constituent network sets its own policies. The overreaching definitions of the two principal name spaces in the Interent, the Internet Protocol address (IP address) space and the Domain Name System (DNS), are directed by a maintainer organization, the Internet Corporation for Assigned Names and Numbers (ICANN). The technical underpinning and standardization of the core protocols is an activity of the Internet Engineering Task Force (IETF), a non-profit organization of loosely affiliated international participants that anyone may associate with by contributing technical expertise. In November 2006, the Internet was included on USA Today's list of New Seven Wonders.

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

### File Descriptor | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/%ED%8C%8C%EC%9D%BC_%EC%84%9C%EC%88%A0%EC%9E%90)
File descriptor(파일 서술자/기술자)는 특정한 파일에 접근하기 위한 추상적인 키이다. 이 용어는 일반적으로 POSIX 운영 체제에 쓰인다. Microsoft Windows와 C 표준 입출력 라이브러리 환경에서는 file handle(파일 핸들)이라는 말이 선호되지만 후자의 경우 기술적으로 다른 객체이다. POSIX에서 fd는 정수, 곧 C형 int를 말한다. 모든 프로세스가 갖추어야 하는 표준 POSIX fd는 다음과 같이 3개가 있다. 1. 정숫값 0인 경우 stdin(표준 입력), 2. 정숫값이 1인 경우 stdout(표준 출력), 3. 정숫값이 2인 경우 stderr(표준 오류)이다.

### URI vs. URL vs. URN
Uniform Resource Identifier(URI), Uniform Resource Locator(URL), and Uniform Resource Name(URN)는 각 네트워크 상에 존재하는 자원을 구분하는 ID(식별자), 네트워크 상에 존재하는 resource의 location, 중복되지 않는 유일한 resource name을 나타낸다. URN, URL은 URI에 포함된다. 따라서 URN, URL은 URI라 할 수 있다. URL은 where을 나타내는 것으로 자원에 접근하는 방법이나 네트워크 위치를 표현하고 있다. http://, https://, ftp:// 등이 포함되면 URL이다. URN은 what을 나타내는 것으로 해당 자원이 무엇인지 중복되지 않는 유일한 식별 가능한 이름이어야 한다.

### Cloud Computing
Cloud computing은 여러 deivces에서 나온 정보들을 cloud에서 전부 처리하는 computing environment이다.

### Edge Computing
Edge computing은 cloud에서 모든 연산을 처리하는 것이 아닌, mobile devices들이 직접 연산을 하거나 edge들에서 데이터 연산을 하여 cloud에 데이터를 뿌려주는 것이다.

-----

## The Web | [Wiki](https://en.wikipedia.org/wiki/World_Wide_Web) | [Tutorial](https://opentutorials.org/course/3083)
The World Wide Web (WWW), commonly known as The Web, is an information system where documents and other web resources are identified by Uniform Resource Locators (URLs, such as https://example.com/), which may be interlinked by hyperlinks, and are accessible over the Internet. The resources of the Web are transferred via the Hypertext Transfer Protocol (HTTP), may be accessed by users by a software application called a web browswer, and are published by a software application called a web server. The World Wide Web is not synonymous with the Internet, which pre-dated the Web in some form by over two decades and upon which technologies the Web is built.

English scientist Sir Timothy Berners-Lee invented the World Wide Web in 1989. He wrote the first web brower in 1990 while employed at CERN near Geneva, Switzerland. The browser was released outside CERN to other research institutions starting in January 1991, and then to the general public in August 1991. The Web began to enter everyday use in 1993-4, when websites for general use started to become available. The World Wide Web has been central to the development of the Information Age, and is the primary tool bilions of people use to interact on the Internet.

Web resources may be any type of downloaded media, but web pages are hypertext documents formatted in Hypertext Markup Language (HTML). Special HTML syntax displays embedded hyperlinks with URLs which permits users to navigate to other web resources. In addition to text, web pages may contain references to images, video, audio, and software components which are either displayed or internally executed in the user's web browser to render pages or streams of multimedia content.

Multiple web resources with a common theme and usually a common domain name, make up a website. Websties are sotred in computers that are running a web server, which is a program that responds to requests made over the Internet from web browsers running on a user's coimputer. Website content can be provided by a publisher, or interactively from user-generated content. Websites are provided for a myraid of informative, entertainment, commercial, and governmental reasons.

### Web Browser | [Wiki](https://en.wikipedia.org/wiki/Web_browser)
A web browswer (commonly referred to as a browser) is application software for accessing the World Wide Web. When a user requests a web page from a particular website, the web browser retrieves the necessary content from a web server and then displays the page on the user's device.

A web browser is not the same thing as a search engine, though the two are often confused. A search engine is a website that provides links to other websites. However, to connect to a website's server and display its web pages, a user must have a web browser installed.

Web browsers are used on a range of devices, including desktops, laptops, and smartphones. In 2020, an estimated 4.9 billion people used a browser. The most used browser is Google Chrome, with a 64% global market share on all devices, followed by Safari with 19%.

### Web Site | [Wiki](https://en.wikipedia.org/wiki/Website) | [Home of the first website](http://info.cern.ch/)
A webste (also written as web site) is a collection of web pages and related content that is identified by a common domain name and published on at least on web server. Notable examples are wikipedia.org, google.com, and amazon.com.

All publicly accessible websites collectively constitute the World Wide Web. There are also private websites that can only be accessed on a private network, such as a company's internal website for its employees.

Websites are typically dedicated to a particular topic or purpose, such as news, education, commerce, entertainment, or social networking, Hyperlinking between web pages guides the navigation of the site, which often starts with a home page.

Users can access websites on a range of devices, including desktops, laptops, tablets, and smartphones. The app used on these devices is called a web browser.

### Web Page | [Wiki](https://en.wikipedia.org/wiki/Web_page)
A web page(or webpage) is a hypertext document provided by a website and displayed to a user in a web browser. A website typically consists of many web pages linked together in a coherent fashion. The name "web page" is a metaphor of paper pages bound together into a book.

### Web Server | [Wiki](https://en.wikipedia.org/wiki/Web_server)
A web server is computer software and underlying hardware that accepts requests via HTTP, the network protocol created to distribute web pages, or its secure variant HTTPS. A user agent, commonly a web browser or web crawler, initiates communication by making a request for a specific resource using HTTP, and the server responds with the content of that resource or an error message. The server can also accept and store resources sent from the user agent if configured to do so.

A server can be a single computer, or even an embedded system such as a router with a built-in configuration interface, but high-traffic websites typically run web servers on fleets of computers designed to handle large numbers of requests for documents, multimedia files and interactive scripts. A resource sent from a web server can be a preexisting file available to the server, or it can be generated at the time of the request by another program that communicates with the server program. The former is often faster and more easily cached for repeated requests, which the latter supports a broader range of applications. Websites that server generated content usually incorporate stored files whenever possible.

Technologies such as REST and SOAP, which use HTTP as a basic for general computer-to-computer communication, have extended the application of web servers well beyond their original purpose of serving human-readable pages.

### Web Hosting | [Wiki](https://en.wikipedia.org/wiki/Web_hosting_service)
A web hosting service (often shorted to web host) is a type of Internet hosting service that allows individuals and organizations to make their website accessible via the World Wide Web. Web hosts are companies that provide space on a server owned or leased for use by client, as well as providing Internet connectivity, typically in a data center. Web hosts can also provide data center space and connectivity to the Internet for other servers located in their data center, called colocation, also known as housing in Latin America or France.

-----

### *[React](https://reactjs.org/)*
A JavaScript library for building user interfaces.

### *[Spring](https://spring.io/)* | [Wiki](https://en.wikipedia.org/wiki/Spring_Framework)
The Spring Framework is an application framework and inversion of control container for the Java platform. The framework's core features can be used by any Java application, but there are extensions for building web applications on top of the Java EE (Enterprices Edition) platform. Although the framework does not impose any specific programming model, it has become popluar in the Java community as an addition to the Enterprice JavaBeans (EJB) model. The Spring Framework is open source.

### *[Node.js](https://nodejs.org/en/)* | [Wiki](https://en.wikipedia.org/wiki/Node.js)
Node.js is a JavaScript runtime built on Chrome's V8 JavaScript engine.

Node.js is an open-source, cross-platform, back-end JavaScript runtime environment that runs on the V8 engine and executes JavaScript code outside a web browser. Node.js lets developers use JavaScript to write command line tools and for server-side scripting-running scripts server-side to produce dynamic web page content before the page is sent the the user's web browswer. Consequently, Node.js represents a "JavaScript everywhere" paradigm, unifying web-application development around a single programming language, rather than different languages for server-side and client-side scripts.

Though .js is the standard filename extension for JavaScript code, the name "Node.js" doesn't refer to a particular file in this context and is merely the name of the product. Node.js has an event-driven architecture capable of asynchronous I/O. These design choices aim to optimize throughput and scalability in web applications with many input/output operations, as well as for real-time Web applications (e.g., real-time communication programs and browser games).

The Node.js distributed development project was previously governed by the Node.js Foundation, and has now merged with the JS Foundation to form the OpenJS Foundation, which is facilitated by the Linux Foundation's Collaborative Projects program.

Corporate users of Node.js software include GoDaddy, Groupon, IBM, LinkedIn, Microsoft, Netflix, PayPal, Rakuten, SAP, Voxer, Walmark, Yahoo!, and Amazon Web Services.

### *[Deno](https://deno.land/)* | [Wiki](https://en.wikipedia.org/wiki/Deno_(software))
Deno is a runtime for JavaScript and TypeScript that based on the V8 JavaScript engine and the Rust programming language. It was created by Ryan Dahl, original creator of Node.js, and is focuesd on productivity. It was announced by Dahl in 2018 during his talk "10 Things I Regret About Node.js". Deno explicitly takes on the role of both runtime and package manager within a single executable, rather than requiring a separate package-management program.

#### Reference
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
- React.js Blog KR, https://seokjun.kim/time-to-stop-react/ 2021-04-29-Thu.
- React, https://reactjs.org/, 2021-04-29-Thu.
- Spring, https://spring.io/ 2021-04-29-Thu.
- Node.js, https://nodejs.org/en/, 2021-04-29-Thu.
- Deno, https://deno.land/, 2021-04-29-Thu.
- Roblox, https://www.roblox.com/, 2021-04-29-Thu.
- Opentutorials WEBn KR, https://opentutorials.org/course/3083, 2021-06-10-Thu.
- Web Wiki, https://en.wikipedia.org/wiki/World_Wide_Web, 2021-06-10-Thu.
- Web Browser Wiki, https://en.wikipedia.org/wiki/Web_browser, 2021-06-10-Thu.
- Web Site Wiki, https://en.wikipedia.org/wiki/Website, 2021-06-10-Thu.
- Web Page Wiki, https://en.wikipedia.org/wiki/Web_page, 2021-06-10-Thu.
- Web Server Wiki, https://en.wikipedia.org/wiki/Web_server, 2021-06-10-Thu.
- Web Hosting Wiki, https://en.wikipedia.org/wiki/Web_hosting_service, 2021-06-10-Thu.
- Deno Wiki, https://en.wikipedia.org/wiki/Deno_(software), 2021-06-22-Tue.
- Node.js Wiki, https://en.wikipedia.org/wiki/Node.js, 2021-06-22-Tue.
- Spring Wiki, https://en.wikipedia.org/wiki/Spring_Framework, 2021-06-22-Tue.
