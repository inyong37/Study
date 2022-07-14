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

IoT 게이트웨이는 연결된 디바이스의 데이터를 수집하고, 인터넷 영역으로 전달하며, 외부에서 각각의 디바이스와 연결할 수 있는 인터페이스 역할을 하는 일종의 관문이라고 할 수 있습니다. 대부분의 IoT 사물들이 소형, 저전력의 특성을 갖고 있기 때문에 처리 능력(Processing Power)과 메모리 등에 한계가 있습니다. 하지만 IoT 게이트웨이를 두게 됨으로써 사물들이 최소한의 인터페이스 장치만으로도 인터넷에 접근할 수 있는 것이죠. 또한 각각즤 사물로부터 들어오는 주기적인 데이터를 분석하여 유의미한 데이터만을 전달함으로써 네트워크 대역폭의 부담을 낮추고 데이터의 실효성을 높이는 역할도 수행합니다.

#### 홈 IoT Gateway

국내의 경우 ISP 사업자를 중심으로 홈 오토메이션, 보안 등의 IoT 서비스가 주류를 이루고 있습니다. 집 안의 다양한 형태의 전자제품들과 연결되어 집 밖에서 원격 서비스를 제공하기 위해서는 게이트가 필수적입니다. 

#### 의료 IoT Gateway

의료용 IoT 게이트웨이는 높은 휴대성, 실시간 데이터 수집과 같은 다양한 형태의 센서 디바이스를 통합하여 관리할 수 있는 형태로 구현되고 있습니다. 프리스케일(Freescale)은 저전력 웨어러블 기술을 기반으로 환자 상태의 조기 알람과 질병 예방이 가능한 IoT 플랫폼을 개발했습니다. 게이트웨이는 센서 데이터를 수집하고 분석하여 유요한 데이터를 WAN으로 전달합니다. 또한 원격 모니터링을 위한 원격 접속 디바이스를 구성할 수 있습니다.

#### IoT Gateway Platform

인텔은 쿼크(Quark)와 아톰(Atom) SoC를 기반으로 Wind River 디바이스 플랫폼과 맥아피(McAfee)의 임베디드 보안 기술을 탑재한 토탈 솔루션 형태로 IoT 게이트웨이를 선보이고 있습니다. 인텔의 IoT 게이트웨이는 로컬 의사결정, 전달한 데이터에 대한 필터링 및 전처리, 기존의 임베디드 기기 또는 클라우드와의 연결을 지원합니다. 인텔 프로세서와 Wind River, McAfee Embedded Control과 같은 이미 검증되고 정합된 솔루션을 바탕으로 구성된 것 역시 장점으로 내세우고 있습니다.

FreeScale, ARM, Oracle 연합은 풍부한 SoC 경험과 Java라는 강력한 무기를 앞세워 'OneBox'라는 IoT 게이트웨이 플랫폼을 선보였습니다. OneBox 플랫폼은 Java 임베디드 기반의 IoT 기기와의 호환이 용이하고 손쉬운 디바이스 개발 환경을 제공하고 있습니다.

이러한 게이트웨이 플랫폼은 상호 호환성을 확장성을 높이기 위해 MQTT, REST와 같은 표준화된 메시징 프로토콜과 지그비, 블루투스, 와이파이 등의 표준화된 인터페이스를 중심으로 구성되어 있습니다. 

IoT 게이트웨이는 사물의 부족한 부분을 채워주며 서비스를 구성하는 다양한 사물 간의 정보 교환을 용이하게 함으로써 각각의 IoT 사물들을 더욱 똑똑하고 효율적으로 동작할 수 있도록 도와줍니다. 또한 어디서나 게이트웨이를 통해 IoT 사물들을 통합하여 제어할 수 있는 인터페이스를 제공함으로써 새로운 형태의 서비스를 가능하게 합니다.

#### Reference
- Internet of Things Wiki, https://en.wikipedia.org/wiki/Internet_of_things, 2022-06-22-Wed.
- What is IoT? AWS, https://aws.amazon.com/what-is/iot/?nc1=h_ls, 2022-06-21-Tue.
- Understanding the Internet of Things (IoT) RedHat, https://www.redhat.com/en/topics/internet-of-things, 2022-06-21-Tue.
- What is the Internet of Things (IoT)? RedHat, https://www.redhat.com/en/topics/internet-of-things/what-is-iot, 2022-06-21-Tue.
- 무선 통신 - 지그비 사용하기 Youtube, https://youtu.be/iquILj4CcaU, 2022-07-14-Thu.
- IoT를 위한 네트워크 기술 소개 Youtube, https://youtu.be/X8wMvr5hL5E, 2022-07-14-Thu.
- IoT Gateway LG CNS KR, https://blog.lgcns.com/1120, 2022-07-14-Thu.
- IoT Platform OneBox, https://www.design-reuse.com/news/33189/freescale-arm-oracle-one-box-iot-gateway.html, 2022-07-14-Thu.
