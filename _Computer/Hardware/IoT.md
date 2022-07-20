# Internet of Things (IoT) | [Wiki](https://en.wikipedia.org/wiki/Internet_of_things)
- Summary
  - IoT는 네트워크에 연결된 클라우드부터 센서 등을 비롯한 기기들이 정보를 수집, 가공, 처리하여 유의미한 결과를 내는 시스템이다.
  - 엣지 컴퓨팅, 클라우드 컴퓨팅, 머신러닝을 이용한 데이터 처리 방법이 있다.

The Internet of Things (IoT) describes physical objects (or groups of such as objects) with sensors, processing ability, software, and other technologies that connect and exchange data with other devices and systems over the Internet or other communications networks. Internet of things has been considered a misnoomer because devices do not need to be connected to the public internet, they only need to be connected to a network and be individually addressable.

The field has evolved due to the convergence of multiple technologies, including ubiquitous computing, commodity sensors, increasingly powerful embedded systems, and machine learning. Tranditional fields of embedded systems, wireless sensor networks, control systems, automation (including home and building automation), independently and collectively enable the Internet of things. In the consumer market, IoT technology is most synonymous with products pertaining to the concept of the "smart home", including devices and appliances (such as lighting fixtures, thermostats, home security systems, cameras, and other home appliances) that support one or more common ecosystems, and can be controlled via devices associated with that ecosystem, such as smartphones and smart speakers. IoT is also used in healthcare systems.

There are number of concerns about the risks in the growth of IoT technologies and products, especially in the areas of privacy and security, and consequently, industry and governmental moves to address these concerns have begun, including the development of international and local standards, guidelines, and regulatory frameworks.

## What is IoT? | [AWS](https://aws.amazon.com/what-is/iot/?nc1=h_ls)
The term IoT, or Internet of Things, refers to the collective netowrk of connected devices and the technology that facilitates communication between devices and the cloud, as well as between the devices themselves. Thanks to the advent of inexpensive computer chips and high bandwidth telecommunication, we now have billions of devices connected to the internet. This means everyday devices like toothbrushes, vacuums, cars, and machines can use sensors to collect data and respond intelligently to users.

The Internet of Things integrates everyday "things" with the internet. Computer Enginners have been adding sensors and processors to everyday objects since the 90s. However, progress was initially slow because the chips were big and bulky. Low power computer chips called RFID tags were first used to track expensive equipment. As computing devices shrank in size, these chips also became smaller, faster, and smarter over time.

The cost of integrating computing power into small objects has now dropped considerably. For example, you can add connectivity with Alexa voice services capabilities to MCUs with less than 1MB embedded RAM, such as for light switches. A whole industry has sprung up with a focus on filling our homes, businesses, and offices with IoT devices. These smart objects can automatically transmit data to and from the Internet. All these "invisible computing devices" and the technology associated with them are collectively referred to as the Internet of Things.

## How does IoT work?
A typical IoT system works through the real-time collection and exchange of data. An IoT system has three components:

### Smart devices
This is a device, like a television, security camera, or exercise equipment that has been give computing capabilities. It collects data from its environment, user inputs, or usage patterns and communicates data over the internet to and from its IoT application.

### IoT application
An Iot application is a collection of services and software that integrates data received from various IoT devices. It uses machine learning or artificial intelligence (AI) technology to analyze this data and make informed decisions. These decisions are communicated back to the IoT device and the IoT device then responds intelligently to inputs.

### A graphical user interface
The IoT device or fleet of devices can be managed through a graphical user interface. Common examples include a mobile application or website that can be used to register and control smart devices.

- What are examples of IoT devices? Connected cars, Connected homes, Smart cities, Smart buildings
- What is Industrial IoT? Manufacturing, Automobile, Logistics and transport, Retail
- How can IoT improve our lives?

- What are the benefits of IoT for business? Accelerate innovation, Turn data into insights and action with AI and ML, Increase security, Scale differentiated solutions

## What are IoT technologies?
### Edge computing
Edge computing refers to the technology used to make smart devices do more than just send or receive data to their IoT platform. It increases the computing power at the edges of an IoT network, reducing communication latency and improving response time.

### Cloud computing
Cloud technology is used for remote data storage and IoT device management - making the data accessible to multiple devices in the network.

### Machine learning
Machine learning regers to the software and algorithms used to process data and make real-time decisions based on that data. These machine learning algorithms can be deployed in the cloud or at the edge.

## Understanding the Internet of Things (IoT) | [RedHat](https://www.redhat.com/en/topics/internet-of-things)
The Internet of Things (IoT) is made up of smart devices connected to a network, sending and receiving data to and from other devices. IoT creates new opportunities to gather data from the world around us and manage large numbers of devices in different physical locations. IoT also introduces the challenges of collecting, storing, and analyzing enourmous volumes of data.

IoT is a related concept to edge computing, a strategy for computing on location where data is collected or used. Many edge computing use cases, such as manufacturing and utilities, involve the use of Industrial IoT (IIoT) devices.

## What is the Internet of Things (IoT)? | [RedHat](https://www.redhat.com/en/topics/internet-of-things/what-is-iot)
The Internet of Things (IoT) refers to the process of connecting everyday physical objects to the internet-from common household objects like lightbulbs; to healthcare assets like medical devices; to wearables, smart devices, and even smart cities.

The Iot devices placed within those physical objects primarily fall into 1 to 2 categories: they are either a switch (that sends a command to a thing), or a sensor (that collects data and sends it elsewhere).

### IoT Gateway | [LG CNS](https://blog.lgcns.com/1120)

IoT 게이트웨이는 연결된 디바이스의 데이터를 수집하고, 인터넷 영역으로 전달하며, 외부에서 각각의 디바이스와 연결할 수 있는 인터페이스 역할을 하는 일종의 관문이라고 할 수 있습니다. 대부분의 IoT 사물들이 소형, 저전력의 특성을 갖고 있기 때문에 처리 능력(Processing Power)과 메모리 등에 한계가 있습니다. 하지만 IoT 게이트웨이를 두게 됨으로써 사물들이 최소한의 인터페이스 장치만으로도 인터넷에 접근할 수 있는 것이죠. 또한 각각의 사물로부터 들어오는 주기적인 데이터를 분석하여 유의미한 데이터만을 전달함으로써 네트워크 대역폭의 부담을 낮추고 데이터의 실효성을 높이는 역할도 수행합니다.

#### 홈 IoT Gateway

국내의 경우 ISP 사업자를 중심으로 홈 오토메이션, 보안 등의 IoT 서비스가 주류를 이루고 있습니다. 집 안의 다양한 형태의 전자제품들과 연결되어 집 밖에서 원격 서비스를 제공하기 위해서는 게이트가 필수적입니다. 

#### 의료 IoT Gateway

의료용 IoT 게이트웨이는 높은 휴대성, 실시간 데이터 수집과 같은 다양한 형태의 센서 디바이스를 통합하여 관리할 수 있는 형태로 구현되고 있습니다. 프리스케일(Freescale)은 저전력 웨어러블 기술을 기반으로 환자 상태의 조기 알람과 질병 예방이 가능한 IoT 플랫폼을 개발했습니다. 게이트웨이는 센서 데이터를 수집하고 분석하여 유요한 데이터를 WAN으로 전달합니다. 또한 원격 모니터링을 위한 원격 접속 디바이스를 구성할 수 있습니다.

#### IoT Gateway Platform

인텔은 쿼크(Quark)와 아톰(Atom) SoC를 기반으로 Wind River 디바이스 플랫폼과 맥아피(McAfee)의 임베디드 보안 기술을 탑재한 토탈 솔루션 형태로 IoT 게이트웨이를 선보이고 있습니다. 인텔의 IoT 게이트웨이는 로컬 의사결정, 전달한 데이터에 대한 필터링 및 전처리, 기존의 임베디드 기기 또는 클라우드와의 연결을 지원합니다. 인텔 프로세서와 Wind River, McAfee Embedded Control과 같은 이미 검증되고 정합된 솔루션을 바탕으로 구성된 것 역시 장점으로 내세우고 있습니다.

FreeScale, ARM, Oracle 연합은 풍부한 SoC 경험과 Java라는 강력한 무기를 앞세워 'OneBox'라는 IoT 게이트웨이 플랫폼을 선보였습니다. OneBox 플랫폼은 Java 임베디드 기반의 IoT 기기와의 호환이 용이하고 손쉬운 디바이스 개발 환경을 제공하고 있습니다.

이러한 게이트웨이 플랫폼은 상호 호환성을 확장성을 높이기 위해 MQTT, REST와 같은 표준화된 메시징 프로토콜과 지그비, 블루투스, 와이파이 등의 표준화된 인터페이스를 중심으로 구성되어 있습니다. 

IoT 게이트웨이는 사물의 부족한 부분을 채워주며 서비스를 구성하는 다양한 사물 간의 정보 교환을 용이하게 함으로써 각각의 IoT 사물들을 더욱 똑똑하고 효율적으로 동작할 수 있도록 도와줍니다. 또한 어디서나 게이트웨이를 통해 IoT 사물들을 통합하여 제어할 수 있는 인터페이스를 제공함으로써 새로운 형태의 서비스를 가능하게 합니다.

### Smart Dust | [Blog (KR)](https://www.itfind.or.kr/WZIN/jugidong/1140/114004.htm)

스마트 더스크 기술이란 먼지 크기의 매우 작은 센서들을 건물, 도로, 의복, 인체 등 물리적 공간에 먼지처럼 뿌려 주위의 온도, 습도, 가속도, 압력 등의 정보를 무선 네트워크로 감지, 관리할 수 있는 기술을 말한다. 이러한 스마트 더스크 내에는 센서, 센서 제어 회로, 컴퓨터, 양방향 무선 통신 모듈, 전원 장치 등이 내장되며, 현재의 초고집적 반도체 기술과 MEMS 기술을 통해 작게 구현할 수 있다. 스마트 더스트(Smart Dust)라는 용어는 1997년부터 UC Berkely에서 소형 감지기 및 통신 패키지 개발 프로젝트를 이끌어 왔으며, 현재 미국 더스트 사의 CTO인 Kris Pister에 의해 처음으로 사용되었다. 기존의 컴퓨팅 기술의 개발은 작업 처리 시간의 단축에 많은 초점을 두어 온 반면, 스마트 더스트 기술은 주어진 작업의 에너지 소모를 최소화하고 최소화한 크기에 필요한 정보를 수집할 수 있는 센서를 탑재하는 데 주력하고 있다. 또한 스마트 더스트 상호 간의 통신을 위한 네트워크를 적용하여 각 스마트 더스트를 감지하고 서로 효율적으로 컴퓨팅 작용을 할 수 있도록 하고 있다. 

### Matter | [Blog](https://csa-iot.org/newsroom/testing-one-two-three/) | [src](https://github.com/project-chip/connectedhomeip/tree/master/src)

Matter is new, open, IP-based IoT protocol slated for release this fall and set to address one of IoT's biggest challenges - interoperability. 

- app: Application Layer -- Zigbee Cluster Library (ZCL)
- ble: BLE Layer -- Bluetooth Transport Protocol (BTP)
- darwin: Darwin Framework (iOS and macOS)
- qrcodetool: QR code tool
- setup_payload: QR code setup data encode / decode library
- NFC Tag Reading

---

## Smart Home | Home Automation | [Wiki](https://en.wikipedia.org/wiki/Home_automation)

Home automation or domotics is building automation for a home, called a smart home or smart house. A home automation system will monitor and/or control home attributes such as lighting, climate, entertainment systems, and applicances. It may also include home security such as access control and alarm systems. When connected with the Internet, home devices are an important constituent of the the Internet of Things (IoT).

A home automation system typically connects controlled devices to a central smart home hub (sometimes called a gateway). The user interface for control of the system uses either wall-mounted terminals, tablet or desktop computers, a mobile phone application, or a Web interface that may also be accessible off-site through the Internet.

While there are many competing vendeors, there are increasing efforts towards open source systems. However, there are issues with the current state of home automation including a lack of standardized security measures and deprecation of older devices without backwards compatibility.

Home automation has high potential for sharing data between family members or trusted individuals for personal security and could lead to energy saving measures with a positive environmental impact in the future.

The home automation market was worth US$5.77 billion in 2013, predicted to reach a market value of US$12.81 billion by 2020.

### Samsung Electronics SmartThings | [How to Connect](https://www.samsungsvc.co.kr/solution/22417)

1. SmartThings에 등록할 가전 제품의 전원을 켜세요.
2. 스마트폰에서 SmartThings 앱을 실행하세요.
3. SmartThings 홈 화면에서 + > 디바이스 추가를 탭하세요.
4. 디바이스 추가 화면에서 다음과 같이 가전제품을 선택하세요.
  - 직접 선택: 등록할 Samsung 가전제품 유형을 탭하세요.
  - 자동 검색: 자동 검색을 탭한 후 연결 가능한 디바이스 목록에서 등록할 가전제품을 탭하세요.
  - 스마트 홈 어댑터 선택: 외장형 동글을 사용하는 공기청정기, 냉장고, 에어컨의 경우 제품 종류 대신 스마트 홈 어댑터(동글)를 선택하세요.
    - 참고: 일부 가전제품을 SmartThings에 연결하려면 외장형 동글을 별도로 설치해야 합니다. 가전제품과 함께 제공된 사용설명서를 참조하여 동글 설치 지원 여부 및 정확한 설치 위치를 확인하세요.  
5. 디바이스 시작하기 화면에서 다음을 탭하세요.
6. 가전제품이 설치된 장소와 방을 선택한 후 다음을 탭하세요.
7. 가전제품의 종류(공기청정기, 냉장고, 에어컨, 세탁기, 에어드레서)에 따라 AP 모드로 설정하세요. 가전제품의 디스플레이에 AP가 표시되고 연결이 진행됩니다.
8. 스마트폰과 가전제품의 연결이 완료되었습니다. 앱에서 연결 완료 메세지를 확인한 후 완료를 탭하세요.

#### Reference
- Internet of Things Wiki, https://en.wikipedia.org/wiki/Internet_of_things, 2022-06-22-Wed.
- What is IoT? AWS, https://aws.amazon.com/what-is/iot/?nc1=h_ls, 2022-06-21-Tue.
- Understanding the Internet of Things (IoT) RedHat, https://www.redhat.com/en/topics/internet-of-things, 2022-06-21-Tue.
- What is the Internet of Things (IoT)? RedHat, https://www.redhat.com/en/topics/internet-of-things/what-is-iot, 2022-06-21-Tue.
- 무선 통신 - 지그비 사용하기 Youtube, https://youtu.be/iquILj4CcaU, 2022-07-14-Thu.
- IoT를 위한 네트워크 기술 소개 Youtube, https://youtu.be/X8wMvr5hL5E, 2022-07-14-Thu.
- IoT Gateway LG CNS KR, https://blog.lgcns.com/1120, 2022-07-14-Thu.
- IoT Platform OneBox, https://www.design-reuse.com/news/33189/freescale-arm-oracle-one-box-iot-gateway.html, 2022-07-14-Thu.
- Smart Dust Blog KR, https://www.itfind.or.kr/WZIN/jugidong/1140/114004.htm, 2022-07-14-Thu.
- Matter Blog, https://csa-iot.org/newsroom/testing-one-two-three/, 2022-07-19-Tue.
- Matter src, https://github.com/project-chip/connectedhomeip/tree/master/src, 2022-07-19-Tue.
- Samsung Electroncis SmartThings How to Connect, https://www.samsungsvc.co.kr/solution/22417, 2022-07-20-Wed.
- Home Automation Wiki, https://en.wikipedia.org/wiki/Home_automation, 2022-07-20-Wed.
