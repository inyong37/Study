# Embedded System | [Wiki](https://en.wikipedia.org/wiki/Embedded_system)

- Summary
  - Dedicated function system (contrast in general personal computer).
  - Constraint in time.
- 요약
  - 특정 기능을 위한 시스템이다(일반적인 용도의 PC와 차이가 있다). 
  - 시간 제약 조건을 포함한 시스템이 있다(i.e. 자동차 운전 시스템 등의 real-time deadline이 존재하는 시스템). 

An embedded system is a computer system-a combination of a computer processor, computer memory and input/output peripheral devices-that has a dedicated function within a larger mechanical or electronic system. It is embedded as part of a complete device often including eletrical or electronic hardware and mechanical parts. Because an embedded system typically controls physical operations of the machine that it is embedded within, it often has real-time computing constraints. Embedded systems control many devices in common use today. In 2009, it was estimated that ninety-eight percent of all micorprocessors manufactured were used in embedded systems.

Modern embedded systems are often based on microcontrollers (i.e. microprocessors with integrated memory and peripheral interfaces), but ordinary microprocessors (using external chips for memory and peripheral interface circuits) are also common, expecially in more complex systems. In either case, the processor(s) used may be types ranging from general purpose to those specialized in a certain class of computations, or even custom designed for the application at hand. A common standard class of dedicated processors is the digital signal processor (DSP).

Since the embedded system is dedicated to specific tasks, design engineers can optimize it to reduce the size and cost of the product and increase its reliability and performance. Some embedded systems are mass-produced, benefiting from economies of scale.

Embedded systems range in size from portable personal devices such as digital watches and MP3 players to bigger machines like home appliances, industrial assembly lines, robots, transport vehicles, traffic light controllers, and medical imaging systems. Often they constitute subsystems of other machines like avionics in aircraft and spacecraft. Large installations like factories, pipelines and electrical grids rely on multiple embedded systems networked together. Generalized through software customization, embedded systems such as programmable logic controllers frequently comprise their functional units.

Embedded systems range from those law in complexity, with a single microcontroller chip, to very high with multiple units, peripherals and networks, which may reside in equipment racks or across large geographical areas connected via long-distance communications lines.

### Embedded Platform | [Blog (KR)](https://jeongchul.tistory.com/98?category=519468)

임베디드 플랫폼이란 최적화된 하드웨어와 소프트웨어를 합친 것이다. CPU, OS, 개발 환경(Tool, IDE)를 일컫는다. 소프트웨어에는 운영체제 없이 동작하는 firmware, priority를 중요시하는 RTOS, Windows CE와 같은 non-RTOS가 있다. 같은 자원에 여러 개의 태스크가 동시에 접근해야 하는 경우 non-RTOS, 태스트 수는 그리 많지 않으나 태스트 간 우선 순위 보장이 반드시 필요한 경우 RTOS를 사용한다. 태스크 수가 많지 않으며, 동시 접근하거나 우선 순위 보장이 필요 없는 경우 firmware를 사용한다. 태스크란 독립적으로 실행 가능한 software의 단위로, process, thread가 이에 속한다.

## [Book: Programming Embedded Systems](https://books.google.co.kr/books?id=nPZaPJrw_L0C&pg=PA1&redir_esc=y&hl=ko#v=onepage&q&f=false)

### What Is an Embedded System?

An embedded system is a combination of computer hardware and software-and perhaps additional parts, either mechanical or electronic-designed to perform a dedicated function. A good example os the microwave oven, Almost every household has one, and tens of millions of them are used every day, but very few people realize that a computer processor and software are involved in the preparation of their lunch or dinner.

The design of an embedded system to perform a dedicated function is in direct contrast to that of the personal computer. It too is comprised of computer hardware and software and mechanical components (disk drives, for example). However, a personal computer is not designed to perform a specific function. Rather, it is able to do many different things. Many people use the term general-purpose computer to make this distinction clear. As shipped, a general-purpose computer is a blank slate; the manufacturer does not know what the customer will do with it. One customer may use if for a network file server, another may use it exclusively for playing games, and a third may use it to write the next great American novel.

Frequently, an embedded system is a component within some larger system. For example, modern cars and trucks contains many embedded systems. One embedded system controls the antilock brakes, another monitors and controls the vehicle’s emissions, and a third displays information on the dashboard. Some luxury car manufacturers have even touted the number of processors (often more than 60, including one in each headlight) in advertisements. In most cases, automotive embedded systems are connected by a communications network.

It is important to point out that a general-purpose computer interfaces to numerous embedded systems. For example, a typical computer has a keyboard and mouse, each of which is an embedded system. These peripherals each contains a processor and software and is designed to perform a specific function. Another example is a modem, which is designed to send and receive digital data over an analog telephone line; that’s all it does. And the specific function of other peripherals can each be summarized in a single sentence as well.

The existence of the processor and software in an embedded system may be unnoticed by a user of the device. Such is the case for a microwave oven, MP3 player, or alarm clock. In some cases, it would even be possible to build a functionally equivalent device that does not contain the processor and software. This could be done by replacing the processor-software combination with a custom integrated circuit (IC) that performs the same functions in hardware. However, the processor and software combination typically offers more flexibility than a hardwired design. It is generally much easier, cheaper, and less poser intensive to use a processor and software in an embedded system.

- History and Future

### Real-Time Systems
One subclass of embedded systems deserves an introduction at this point. A real-time system has timing constraints. The function of a real-time system is thus partly specified in terms of its ability to make certain calculations or decisions in a timely manner. These important calculations or activities have deadlines for completion.

The crucial distinction among real-time systems lies in what happens if a deadline is missed. For example, if the real-time system is part of an airplane’s flight control system, the lives of the passengers and crew may be endangered by a single missed deadline. However, if instead the system involved in satellite communication, the damage could be limited to a single corrupt data packet (which may or may not have catastrophic consequences depending on the application and error recovery scheme). The more severe the consequence, the more likely it will be said that the deadline is “hard” and thus, that the system is a hard real-time system. Real-time systems at the other end of this continuum are said to have “soft” deadlines-a soft real-time system.

- Non-real time ← soft real time → hard real time
    - Computer simulation, User interface, Internet video, Cruise control, Telecommunications, Flight control, Electronic engine

Real-time system design is not simply about speed. Deadlines for real-time systems vary; one deadline might be in a millisecond, while another is an hour away. The main concern for a real-time system is that there is a guarantee that the hard deadlines of the system are always met. In order to accomplish this the system must be predictable.

The architecture of the embedded software, and its interaction with the system hardware, play a key role in ensuring that real-time systems meet their deadlines. Key software design issues include whether polling is sufficient or interrupts should be used, and what priorities should be assigned to the various tasks and interrupts. Additional forethought must go into understanding the worst-case performance requirements of the specific system activities.

All of the topics and examples presented in this book are applicable to the designers of real-time systems. The designer of a real-time system must be more diligent in his work. He must guarantee reliable operation of the software and hardware under all possible conditions. And, to the degree that human lives depend upon the system’s proper execution, this guarantee must be backed by engineering calculations and descriptive paperwork.

## [Book: Embedded System Design](https://books.google.co.kr/books?id=BjNZXwH7HlkC&pg=PA2&redir_esc=y#v=onepage&q&f=false)
- What is an embedded system?

---

## Embedded Operating System | [TechTarget](https://www.techtarget.com/iotagenda/definition/embedded-operating-system)

An embedded operating system is a specialized operating system designated to perform a specific task for a device that is not a computer. The main job of an embedded OS is to run the code that allows the device to do its job. The embeded OS also makes the device's hardware accessible to software that is running on top of the OS.

An embedded OS often works within an embedded system. An embedded system is a computer that supports a machine. It performs one task in the bigger machine. Examples include computer systems in cars, traffic lights, digital televisions, ATMs, airplane controls, point of sale (POS) terminals, digital cameras, GPS navigation systems, elevators and Smart meters.

Networks of devices containing embedded systems make up the internet of things (IoT). THe embedded systems perform basic operations inside IoT devices, such as transferring data over a network without human interaction.

---

### [Bootlin](https://bootlin.com/)

Bootlin is an engineering company specialized in embedded Linux and more generally in Free and OPen Source software for embedded systems.

---

# Internet of Things (IoT) | [Wiki](https://en.wikipedia.org/wiki/Internet_of_things)
- 요약
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

#### [Smart Wallpad](https://smarthome.samsungsds.com/smarthome/product/view?prdId=100&locale=ko)

- 도어록 연동: Zigbee, 447MHz
- 기기간 통신 방식
  - 공용부 연동: RS-485
  - 플랫폼 연동: Wi-Fi
  - 무선기기 연동: Zigbee 

### [Home Assistant](https://www.home-assistant.io/) | [GitHub](https://github.com/home-assistant) | [KR](https://hakorea.github.io/)

#### Home Assistant Operating System | [GitHub](https://github.com/home-assistant/operating-system)

Home Assistant Operating System (formerly HassOS) is a Linux based operating system optimized to host Home Assistant and its Add-ons.

Home Assistant Operating System uses Docker as Container engine. It by default deploys the Home Assistant Supervisor as a container. Home Assistant Supervisor in turn uses the Docer container engine to control Home Assistant Core and Add-Ons in seperate containers. Home Assistant Operating System is not based on a regular Linux distribution like Ubuntu. It is build using Buildroot and it is optimized to run Home Assistant. It targets single board copmute (SBC) devices like the Raspberry Pi or ODROID but also supports x84-64 systems with UEFI.

##### Components

- Bootloader:
  - Barebox for devices that support UEFI
  - U-Boot for devices that don't support UEFI
- Operating System:
  - Buildroot LTS Linux
- File Systems:
  - SquashFS for read-only file systems (using LZ4 compression)
  - ZRAM for `/tmp`, `/var` and swap (using LZ4 compression)
- Container Platform:
  - Docker Engine for running Home Assistant components in containers
- Updates:
  - RAUC for Over The Air (OTA) and USB updates
- Security:
  - AppArmor Linux kernel security module

#### Home Assistant Core | [GitHub](https://github.com/home-assistant/core)

Open source home automation that puts local control and privacy first. Powered by a worldwide community of tinkerers and DIY enthusiasts. Perfect to run on a Raspberry Pi or a local server.

The system is built using a modular approach so support for other devices or actions can be implemented easily.

##### Feature integrations

- Amazon Alexa
- ecobee
- ESPHome
- Google Assistant
- Google Cast
- HomeKit
- IKEA TRÅDFRI
- Lutron Caséta
- MQTT
- Philips Hue
- Plex Media Server
- Shelly
- SmartThings
- Sonos
- Z-Wave JS
- Zigbee Home Automation

---

## [VxWorks](https://www.windriver.com/products/vxworks) | [PDF](https://www.windriver.com/sites/default/files/2022-02/605577969.pdf) | [Blog (KR)](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=ygszzang11&logNo=50178390478) [Differences](https://askanydifference.com/difference-between-vxworks-and-linux/)

It's the operating system behind nine different Mars missions, including the Mars Reconnaissance Orgiter as well as the Spirits and Opportunity Mars Exploration Rovers. It is also used in more than 2 billion other critical devices that are still on planet Earth. From automotive to manufacturing, if it's a deterministic, ultra-reliable, or multi-core embedded system, VxWorks is the operating system of choice.

VxWorks is designed for multicore computing on embedded systems running on Arm, Intel, and Power architectures.

Linux는 process끼리 pipe/message 방식으로 메모리를 동기화하지만, VxWorks는 memory를 함께 사용하여 동기화한다. 이 방식은 데이터 동기화 방식이 간편하지만, A task에서 데이터를 지우면 B task도 영향을 받는다.

Single Board Computer (SBC)에 주로 사용된다. Priority scheduling, multitasking, fast interrupt 등의 장점이 있다.

||VxWorks|Linux|
|:-|:-|:-|
|OS Family|Real-time operating system|Unix-like|
|Targets|Embedded systems only|Personal computers, supercomputers, mobile devices, embedded devices, etc|
|First Released|1987|1991|
|Uses|Mars Rover 2020, Mars Reconnaissance Orbiter, Mars Sciecne Laboratory known as Curiosity Rover|Space X, Jet Propulsion Laboratiry in the development of spacecraft, etc.|

## Board Support Package (BSP) | [Wind River](https://cdn.windriver.com/products/bsp_web/what_is_a_bsp.pdf) | [TechTarget](https://www.techtarget.com/whatis/definition/board-support-package) | [Blog (KR)](https://jeongchul.tistory.com/103)

A board support package (BSP) is essential code for a given computer hardware device that will make device work with the computer's OS. The BSP contains a small program called a bootloader or boot manager that places the OS and device drivers into memory. The contents of the BSP depend on the particular hardware and OS.

Specific tasks that the BPS performs include the following,in order:

- Initialize the processor.
- Initialize the bus.
- Initialize the interrupt controller.
- Initialize the clock.
- Initialize the RAM settings.
- Configure the segments (if applicable).
- Run the boot loader.

In addition to the foregoing, a BSP can contain directives, compilation parameters, and hardware parameters for configuring the OS.

VxWorks(Wind River)와 같은 일부 상용 RTOS를 제외한 대부분의 RTOS와 Firmware에는 non-RTOS에서와 같은 file system이 없다. 컴파일이 끝나면 최종적으로 CPU에 종속적인 binary 실행 코드 하나만 생성된다. 따라서 firmware와 RTOS의 BSP는 제품의 기능이라 할 수 있는 코드(user application)와 그러한 제품의 기능을 실제 구현하기 위해 하드웨어를 직접적으로 제어하는 코드(firmware)가 하나의 파일로 묶여 BSP를 구성한다.

그러나 Linux, Windows CE와 같은 non-RTOS들은 다음의 3가지 실행 코드들로 구성된다.

|파일 타입|BSP 종류|기능|
|:-:|:-:|:-|
|Firmware|Boot Loader|HDD 혹은 Flash 메모리에 있는 kernel image를 메모리에 loading 역할|
|OS Kernel|Kernel Image|OS 압축 이미지 파일|
|User Application|File System Image|User Application이 실행되는 환경, 압축 이미지 파일|

|Fireware/RTOS BSP|non-RTOS BSP|
|:-:|:-:|
|Firmware|Boot Loader 하드웨어 종속적인 kernel|
|User Application|User Application 하드웨어 독립적인 kernel|

ARM process 기반의 embedded Linuxdㅔ서 사용 가능한 boot loader는 크게 다음과 같다.

|Boot Loader|배경|선택 기준|
|:-:|:-|:-|
|BLOB|Intel에서 개발한 XScale Core 기반의 CPU에 적용하기 위해 개발된 부트로더|Intel의 XScale Core 기반으로 개발하는 경우라면 기본적으로 제공되는 BLOB 사용|
|ARMBOOT|XScale Core처럼 변형된 ARM Core 기반 CPU가 아니라, 변형되지 않은 ARM Core 기반 CPU에 적용하기 위해 개발된 부트로더|변형시키지 않은 순수 ARM 프로세서 기반으로 개발하는 경우 주로 선택되었으나, 최근엔 U-BOOT를 더 많이 사용하는 추세|
|U-BOOT|ARM Core, PPC Core, MIPS Core 등 다양한 프로세서에 범용적으로 적용하기 위해 개발된 대부분의 ARM 프로세서에 적용되고 있다.|ARM 프로세서 기반으로 개발하는 경우라면 특별한 일이 없는 한 U-BOOT를 사용하는게 좋다.|

Embedded Linux File System 비교

|File System|특징|주요 사용 분야|
|:-:|:-|:-|
|CramFS|가장 사이즈가 작은 파일 시스템으로 ROM File System이기 때문에 부팅된 이후에는 파일 시스템에 별도의 데이터를 기록할 수 없다.|실행될 때마다 기존에 했던 일을 똑같이 단순 반복하는 분야에 적용(e.g. 산업용 로봇)|
|RAMDISK|RAM의 일부를 파일 시스템으로 사용하는 방법으로 플래시 메모리부터 읽어오는 파일 시스템에 비해 실행 속도가 매우 빠르다는 장점이 있다. 그러나 RAM의 일부를 파일 시스템용으로 사용하다보니 RAM 사이즈가 줄어들어 실행시킬 수 있는 user application의 수가 많지 않다는 단점이 있다.|User application의 실행 속도는 빨라야 하나, 그 수가 비교적으로 적은 분야에 적용(e.g. 네트워크 장비)|
|JFFS, YAFFS|BSP들을 저장하는 용도로 사용되는 flash 메모리 일부를 파일 시스템으로 사용하는 방법으로, RAM 사이즈에 영향을 주지 않기 때문에 매우 많은 user application을 실행시킬 수 있다는 장점이 있다. 다만, 속도가 비교적으로 느린 flash memory부터 읽어와야 하기 때문에 실행 속도가 RAMDISK에 비해 비교적 느리다.|User application의 실행 속도는 비교적 느려도 되나, 그 수가 매우 많은 분야에 적용하면 좋다. (e.g. 모바일 단말기)|

---

### Reference
- Embedded System Wiki, https://en.wikipedia.org/wiki/Embedded_system, 2022-06-22-Wed.
- Programming Embedded Systems with C and GNU Development Tools 2nd Ed., O’REILLY, 2006, https://books.google.co.kr/books?id=nPZaPJrw_L0C&pg=PA1&redir_esc=y&hl=ko#v=onepage&q&f=false, 2022-06-21-Tue.
- Embedded Systems Design 2nd Ed., Newnes, 2003, https://books.google.co.kr/books?id=BjNZXwH7HlkC&pg=PA2&redir_esc=y#v=onepage&q&f=false, 2022-06-21-Tue.
- bootlin, https://bootlin.com/company/about-us/, 2022-07-21-Thu.
- bootlin, https://bootlin.com/, 2022-07-21-Thu.
- Embedded Linux Conference, https://events.linuxfoundation.org/open-source-summit-europe/about/embedded-linux-conference/, 2022-07-21-Thu.
- Embedded Operating System, https://www.techtarget.com/iotagenda/definition/embedded-operating-system, 2022-07-21-Thu.
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
- Home Assistant KR, https://hakorea.github.io/, 2022-07-20-Wed.
- Collection of Home Assistant Postings KR, https://www.clien.net/service/board/cm_iot/14621402, 2022-07-20-Wed.
- Home Assistant GitHub, https://github.com/home-assistant, 2022-07-20-Wed.
- Home Assistant, https://www.home-assistant.io/, 2022-07-20-Wed.
- Home Assistant Operating System GitHub, https://github.com/home-assistant/operating-system, 2022-07-20-Wed.
- Home Assistant Core GitHub, https://github.com/home-assistant/core, 2022-07-20-Wed.
- 월패드 IoT 스마트홈과 차이점 Samsung Electronics, https://r1.community.samsung.com/t5/smartthings/%EC%9B%94%EA%B0%84%EC%9D%B4%EB%B2%A4%ED%8A%B8-%EC%9B%94%ED%8C%A8%EB%93%9C-iot-%EC%8A%A4%EB%A7%88%ED%8A%B8%ED%99%88%EA%B3%BC-%EC%B0%A8%EC%9D%B4%EC%A0%90/td-p/3588879, 2022-07-20-Wed.
- 삼성 SmartThings로 IoT 기능 활용하기, https://blog.naver.com/PostView.nhn?blogId=onlygod831&logNo=222008735703&parentCategoryNo=&categoryNo=38&viewDate=&isShowPopularPosts=true&from=search, 2022-07-20-Wed.
- VxWorks Wind River, https://www.windriver.com/products/vxworks, 2022-07-25-Mon.
- Board Support Package Wind River, https://cdn.windriver.com/products/bsp_web/what_is_a_bsp.pdf, 2022-07-25-Mon.
- Board Support Package TechTarget, https://www.techtarget.com/whatis/definition/board-support-package, 2022-07-25-Mon.
- BSP Blog KR, https://jeongchul.tistory.com/103, 2022-07-25-Mon.
- Embedded Platform Blog KR, https://jeongchul.tistory.com/98?category=519468, 2022-07-25-Mon.
- VxWorks, https://www.windriver.com/sites/default/files/2022-02/605577969.pdf, 2022-07-25-Mon.
- VxWorks Blog KR, https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=ygszzang11&logNo=50178390478, 2022-07-25-Mon.
- Difference Between VxWorks and Linux, https://askanydifference.com/difference-between-vxworks-and-linux/, 2022-07-25-Mon.
- Smart Wallpad Samsung Electronics KR, https://smarthome.samsungsds.com/smarthome/product/view?prdId=100&locale=ko, 2022-07-26-Tue.
