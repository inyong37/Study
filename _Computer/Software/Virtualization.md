# :bento: *Virtual Machine (VM)* | [WiKi (KR)](https://ko.wikipedia.org/wiki/%EA%B0%80%EC%83%81_%EB%A8%B8%EC%8B%A0)
가상 머신은 컴퓨팅 환경을 소프트웨어로 구현한 것, 즉 컴퓨터를 에뮬레이션하는 소프트웨어이다. 가상 머신상에서 운영 체제나 응용 프로그램을 설치 및 실행할 수 있다. 다른 기능들이 있는 여러 종류의 가상 머신들이 있다. 시스템 가상 머신들은, 또한 완전한 가상화 가상 머신들로 알려진 실제 기계의 대체제를 제공하고 완전한 운영 체계의 실행을 위해 요구되는 기능성의 수준을 제공한다. 하이퍼바이저는 하드웨어를 공유하고 관리하기 위해 네이티브 실행을 이용한다. 그리고 하이퍼바이저는 독립된 다른 환경들을 같은 물리적인 기계에서 실행하기 위해서 허용한다. 현대의 하이퍼바이저들은 하드웨어의 도움을 받는 가상화를 이용하는데, 그것들은 주로 주 CPU의 특정 하드웨어 기능을 사용하여 효과적이고 완전한 가상화를 제공한다. 프로세스 가상머신들은 플랫폼에 독립적인 프로그램 실행 환경과 추상화를 제공하여 하나의 프로그램을 실행하도록 설계되었다.

가상 머신은 원래 Popek와 Goldberg가 "실제 컴퓨터의 효율적이고 고립된 복제물"로 정의했다. 현재는 "실제 하드웨어와 직접적인 통신이 없는 가상 컴퓨터"를 가리킨다. 가상 머신은 실제 컴퓨터와 어느 정도의 통신과 사용을 기반으로 두 가지로 나뉜다. 시스템 가상 머신은 완전한 시스템 플랫폼을 제공하며, 다시 말해 완전한 운영 체제의 실행을 지원한다. 반대로, 프로세스 가상 머신은 하나의 단일 프로그램을 실행하기 위해 만들어져 있는데, 다시 말해 단일 프로세스를 지원한다. 가상 머신의 중요한 특징은 안에서 돌아가는 소프트웨어가 가상 머신이 제공하는 환경과 자원에 제한을 받으며 가상 세계를 벗어날 수 없다는 것이다.

## _Hypervisor_ | [vmware](https://www.vmware.com/topics/glossary/content/hypervisor.html)

A hypervisor, also known as a virtual machine monitor or VMM, is software that creates and runs virtual machines (VMs). A hypervisor allows one host computer to support multiple guest VMs by virtually sharing its resources, such as memory and processing.

Benefits of hypervisors:
- Speed
- Efficiency
- Flexibility
- Portability

Why use a hypervisor?:
- Space
- Energy
- Maintenance requirements

Types of hypervisors: There are two main hypervisor types, referred to as "Type 1" (or "bare metal") and "Type 2" (or "hosted"). A type 1 hypervisor acts like a lightweight operating system and runs directly on the host's hardware, while a type 2 hypervisor runs as a software layer on an operating system, like other computer programs.

What is a cloud hypervisor?: As cloud computing becomes pervasive, the hypervisor has emerged as an invaluable tool for running virtual machines and driving innovation in a cloud environment. Since a hypervisor is a software layer that enables one host computer to simultaneously support multiple VMs, hypervisors are a key element of the technology that makes cloud computing possible. Hypervisors make cloud-based applications available to users across a virtual environment while still enabling IT to maintain control over a cloud environment's infrastructure, applications and sensitive data.

How does a hypervisor work?: Hypervisors support the creation and management of virtual machines (VMs) by abstracting a computer’s software from its hardware. Hypervisors make virtualization possible by translating requests between the physical and virtual resources. Bare-metal hypervisors are sometimes embedded into the firmware at the same level as the motherboard basic input/output system (BIOS) to enable the operating system on a computer to access and use virtualization software.

Container vs hypervisor:

Hypervisors:
- Allow an operating system to run independently from the underlying hardware through the use of virtual machines.
- Share virtual computing, storage and memory resources.
- Can run multiple operating systems on top of one server (bare-metal hypervisor) or installed on top of one standard operating system and isolated from it (hosted hypervisor)

Containers:
- Allow applications to run independently of an operating system.
- Can run on any operating system-all they need is a container engine to run.
- Are extremely portable since in a container, an application has everything it needs to run.

Hypervisors and containers are used for different purposes. Hypervisors are used to create and run virtual machines (VMs), which each have their own complete operating systems, securely isolated from the others. In contrast to VMs, containers package up just an app and its related services. This makes them more lightweight and portable than VMs, so they are often used for fast and flexible application development and movement.

### :package: *[VMware](https://www.vmware.com/)*

### _[VMware Fusion](https://www.vmware.com/products/fusion.html)_

Harness the full power of your Mac when you use VMware Fusion to run Windows, Linux, containers, Kubernetes and more in virtual machines (VMs) without rebooting.

### _[VMware Workstation Player](https://www.vmware.com/products/workstation-player.html)_ | [Docs](https://docs.vmware.com/en/VMware-Workstation-Player/index.html) | [Windows Docs](https://docs.vmware.com/en/VMware-Workstation-Player-for-Windows/index.html) | [Linux Docs](https://docs.vmware.com/en/VMware-Workstation-Player-for-Linux/index.html)

Easily run multiple operating systems as virtual machines on your Windows or Linux PC with VMware Workstation Player.

### _[VMware Workstation Pro](https://www.vmware.com/products/workstation-pro.html)_ | [Docs](https://docs.vmware.com/en/VMware-Workstation-Pro/index.html)

Run Windows, Linux and BSD virtual machines on a Windows or Linux desktop with VMware Workstation Pro, the industry standard desktop hypervisor.

### :package: *[VirtualBox](https://www.virtualbox.org/)*

VirtualBox is a x86 and AMD64/Intel64 virtuallization product for enterprise as well as home use. Not only is VirtualBox an extremely feature rich, high performance product for enterprise customers, it is also the only professional solution that is freely available as Open Source Software under the terms of the GNU General Public License(GPL) version 2.

VirtualBox는 InnoTek에서 개발을 시작했고, Sun Microsystems에서 InnoTeck을 인수한 뒤, Oracle이 Sun Microsystems를 인수하여, 현재 Oracle에서 배포하고 있다.

Network | [Blog (KR)](https://technote.kr/213) | [Blog (KR)](https://velog.io/@xeomina/VirtualBox-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%EC%84%A4%EC%A0%95):
- NAT
- NAT Network
- Bridged Adapter
- Internal Network
- Host-only Adapter
- Generic Driver

### Hyper-V | [MS Docs (KR)](https://docs.microsoft.com/ko-kr/virtualization/hyper-v-on-windows/about/)

Hyper-V는 하드웨어 가상화를 제공합니다. 즉, 각 가상 컴퓨터가 가상 하드웨어에서 실행됩니다. Hyper-V를 통해 가상 하드 드라이브, 가상 스위치 및 가상 컴퓨터에 추가할 수 있는 각종 가상 디바이스를 만들 수 있습니다.

Hyper-V는 Windows 10 Pro, Enterprise 및 Education 64비트 버전에서 사용할 수 있으며 Home 버전에서는 사용할 수 없다.

Windows에서 Hyper-V를 실행할 때 몇 가지 기능은 Windows Server에서 Hyper-V를 실행할 때와는 다르게 작동한다. Windows Server에서만 사용할 수 있는 Hyper-V 기능은 다음과 같이 5가지이다. 1. 가상 컴퓨터를 실시간으로 한 호스트에서 다른 호스트로 마이그레이션, 2. Hyper-V 복제본, 3. 가상 파이버 채널, 4. SR-IOV 네트워킹, 5. 공유 .VHDX이다. Windows 10에서만 사용할 수 있는 Hyper-V 기능은 다음과 같이 2가지이다. 1. 빨리 만들기 및 VM 갤러리, 2. 기본 네트워크(NAT 스위치)이다. 메모리 관리 모델이 Windows의 Hyper-V에서 다르다. 서버에서 Hyper-V 메모리는 해당 서버에서 관리 컴퓨터만 실행된다는 가정 하에 관리된다. Windows의 Hyper-V에서 메모리는 대부분 클라이언트 컴퓨터가 가상 컴퓨터 실행 외에도 호스트의 소프트웨어를 실행한다는 예상에 따라 관리된다.

### _Virtualization_ | [Blog (KR)](https://blog.naver.com/PostView.naver?blogId=ilikebigmac&logNo=222009981745&parentCategoryNo=&categoryNo=&viewDate=&isShowPopularPosts=false&from=postView)

Performance:
- Bare metal/type 1 hypervisor: 80%
- Hosted/type 2 hypervisor: 60%

Hardware CPU Support:
- Intel: VT-x
- AMD: AMD-V

Types:
- VMware ESX (type 1)
- Linux KVM - CPU & RAM
  - Thin Hypervisor (type 1)
  - Thick Hypervisor (type 2)
- Linux VirtIO
- QEMU - Devices/Emulator
- Microwoft Windows Hyper-V
- VMware Workstation (type 2)
- VirtualBox (type 2)

### _[Vagrant](https://www.vagrantup.com/)_ | [Docs](https://developer.hashicorp.com/vagrant/docs)

Vagrant is the command line utility for managing the lifecycle of virtual machines.

### _[Ansible](https://www.ansible.com/)_ | [Docs](https://docs.ansible.com/ansible/latest/index.html)

Ansible is an IT automation tool. It can configure systems, deploy software, and orchestrate more advanced IT tasks such as continuous deployments or zero downtime rolling updates.

### VM on M1 macOS | [Blog (KR)](https://elsainmac.tistory.com/869?category=665146)

### Setup CentOS 7 Cluster on VirtualBox Ubuntu Desktop 20

[enable network (Blog KR)](https://evir.tistory.com/entry/CentOSVIrtualbox%EC%97%90-%EC%84%A4%EC%B9%98%ED%95%9C-CentOS-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%EC%84%A4%EC%A0%951):
1. `sudo su`
2. `vi /etc/sysconfig/network-scripts/ifcfg-eth*`
3. ONBOOT=yes
4. `service network restart`

[setup network on VirtualBox and GuestOS (Blog KR)](https://jinhokwon.github.io/devops/devops-virtualbox-network/):
1. Tools>Network>Host-only Networks Create
2. GuestOS (Powered Off)>Settings>Network>Adapter 1>NAT
3. GuestOS (Powered Off)>Settings>Network>Adapter 2>Host-only Adapter

- [enable ssh](https://lemonandgrapefruit.tistory.com/m/250):
1. GuestOS (Powered Off)>Settings>Network>Adapter 1>NAT>Advanced-Port Forwarding

---

### Reference
- Virtual Machine Wiki KR-KO, https://ko.wikipedia.org/wiki/%EA%B0%80%EC%83%81_%EB%A8%B8%EC%8B%A0, 2020-11-04-Wed.
- Windows 10 Hyper-V Introduction, https://docs.microsoft.com/ko-kr/virtualization/hyper-v-on-windows/about/, 2020-11-04-Wed.
- VirtualBox, https://www.virtualbox.org/, 2020-11-04-Wed.
- VMware, https://www.vmware.com/, 2020-11-04-Wed.
- VMware Fusion, https://www.vmware.com/products/fusion.html, 2023-01-04-Wed.
- VMware Workstation Player, https://www.vmware.com/products/workstation-player.html, 2023-01-04-Wed.
- VMware Workstation Pro, https://www.vmware.com/products/workstation-pro.html, 2023-01-04-Wed.
- VMware Workstation Player, https://docs.vmware.com/en/VMware-Workstation-Player/index.html, 2022-10-17-Mon.
- VMware Workstation Player Documentation, https://docs.vmware.com/en/VMware-Workstation-Player/index.html, 2022-10-17-Mon.
- VMware Workstation Player for Linux Documentation, https://docs.vmware.com/en/VMware-Workstation-Player-for-Linux/index.html, 2022-10-17-Mon.
- VMware Workstation Player for Windows Documentation, https://docs.vmware.com/en/VMware-Workstation-Player-for-Windows/index.html, 2022-10-17-Mon.
- VMware Workstation Pro Documentation, https://docs.vmware.com/en/VMware-Workstation-Pro/index.html, 2022-10-17-Mon.
- VirtualBox Network Blog KR, https://technote.kr/213, 2022-12-15-Thu.
- VirtualBox Network Blog KR, https://velog.io/@xeomina/VirtualBox-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%EC%84%A4%EC%A0%95, 2022-12-15-Thu.
- Virtualization Blog KR, https://blog.naver.com/PostView.naver?blogId=ilikebigmac&logNo=222009981745&parentCategoryNo=&categoryNo=&viewDate=&isShowPopularPosts=false&from=postView, 2023-01-04-Wed.
- Hypervisor vmware, https://www.vmware.com/topics/glossary/content/hypervisor.html, 2023-01-04-Wed.
- Vagrant, https://www.vagrantup.com/, 2023-01-04-Wed.
- Vagrant Docs, https://developer.hashicorp.com/vagrant/docs, 2023-01-04-Wed.
- Ansible, https://www.ansible.com/, 2023-01-04-Wed.
- Ansible Docs, https://docs.ansible.com/ansible/latest/index.html, 2023-01-04-Wed.
- VMware Fusion Kali Linux on M1 macOS Blog KR, https://elsainmac.tistory.com/869?category=665146, 2023-01-04-Wed.
- enable network Blog KR, https://evir.tistory.com/entry/CentOSVIrtualbox%EC%97%90-%EC%84%A4%EC%B9%98%ED%95%9C-CentOS-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%EC%84%A4%EC%A0%951, 2023-01-04-Wed.
- setup network on VirtualBox and GuestOS Blog KR, https://jinhokwon.github.io/devops/devops-virtualbox-network/, 2023-01-04-Wed.
- 
- enable ssh Blog KR, https://lemonandgrapefruit.tistory.com/m/250, 2023-01-04-Wed.
