# *Virtual Machine (VM)* | [WiKi (KR)](https://ko.wikipedia.org/wiki/%EA%B0%80%EC%83%81_%EB%A8%B8%EC%8B%A0)
가상 머신은 컴퓨팅 환경을 소프트웨어로 구현한 것, 즉 컴퓨터를 에뮬레이션하는 소프트웨어이다. 가상 머신상에서 운영 체제나 응용 프로그램을 설치 및 실행할 수 있다. 다른 기능들이 있는 여러 종류의 가상 머신들이 있다. 시스템 가상 머신들은, 또한 완전한 가상화 가상 머신들로 알려진 실제 기계의 대체제를 제공하고 완전한 운영 체계의 실행을 위해 요구되는 기능성의 수준을 제공한다. 하이퍼바이저는 하드웨어를 공유하고 관리하기 위해 네이티브 실행을 이용한다. 그리고 하이퍼바이저는 독립된 다른 환경들을 같은 물리적인 기계에서 실행하기 위해서 허용한다. 현대의 하이퍼바이저들은 하드웨어의 도움을 받는 가상화를 이용하는데, 그것들은 주로 주 CPU의 특정 하드웨어 기능을 사용하여 효과적이고 완전한 가상화를 제공한다. 프로세스 가상머신들은 플랫폼에 독립적인 프로그램 실행 환경과 추상화를 제공하여 하나의 프로그램을 실행하도록 설계되었다.

가상 머신은 원래 Popek와 Goldberg가 "실제 컴퓨터의 효율적이고 고립된 복제물"로 정의했다. 현재는 "실제 하드웨어와 직접적인 통신이 없는 가상 컴퓨터"를 가리킨다. 가상 머신은 실제 컴퓨터와 어느 정도의 통신과 사용을 기반으로 두 가지로 나뉜다. 시스템 가상 머신은 완전한 시스템 플랫폼을 제공하며, 다시 말해 완전한 운영 체제의 실행을 지원한다. 반대로, 프로세스 가상 머신은 하나의 단일 프로그램을 실행하기 위해 만들어져 있는데, 다시 말해 단일 프로세스를 지원한다. 가상 머신의 중요한 특징은 안에서 돌아가는 소프트웨어가 가상 머신이 제공하는 환경과 자원에 제한을 받으며 가상 세계를 벗어날 수 없다는 것이다.

## *[VMware](https://www.vmware.com/)*

[VMware Workstation Player](https://docs.vmware.com/en/VMware-Workstation-Player/index.html) | [Workstation Docs](https://docs.vmware.com/en/VMware-Workstation-Player/index.html) | [Linux Docs](https://docs.vmware.com/en/VMware-Workstation-Player-for-Linux/index.html) | [Windows Docs](https://docs.vmware.com/en/VMware-Workstation-Player-for-Windows/index.html) | [Workstation Pro Docs](https://docs.vmware.com/en/VMware-Workstation-Pro/index.html)

Local Virtual Machines. Easily run multiple operating systems as virtual machines on your Windows or Linux PC with VMware Workstation Player.

## *[VirtualBox](https://www.virtualbox.org/)*

VirtualBox is a x86 and AMD64/Intel64 virtuallization product for enterprise as well as home use. Not only is VirtualBox an extremely feature rich, high performance product for enterprise customers, it is also the only professional solution that is freely available as Open Source Software under the terms of the GNU General Public License(GPL) version 2.

VirtualBox는 InnoTek에서 개발을 시작했고, Sun Microsystems에서 InnoTeck을 인수한 뒤, Oracle이 Sun Microsystems를 인수하여, 현재 Oracle에서 배포하고 있다.

## Hyper-V | [MS Docs (KR)](https://docs.microsoft.com/ko-kr/virtualization/hyper-v-on-windows/about/)

Hyper-V는 하드웨어 가상화를 제공합니다. 즉, 각 가상 컴퓨터가 가상 하드웨어에서 실행됩니다. Hyper-V를 통해 가상 하드 드라이브, 가상 스위치 및 가상 컴퓨터에 추가할 수 있는 각종 가상 디바이스를 만들 수 있습니다.

Hyper-V는 Windows 10 Pro, Enterprise 및 Education 64비트 버전에서 사용할 수 있으며 Home 버전에서는 사용할 수 없다.

Windows에서 Hyper-V를 실행할 때 몇 가지 기능은 Windows Server에서 Hyper-V를 실행할 때와는 다르게 작동한다. Windows Server에서만 사용할 수 있는 Hyper-V 기능은 다음과 같이 5가지이다. 1. 가상 컴퓨터를 실시간으로 한 호스트에서 다른 호스트로 마이그레이션, 2. Hyper-V 복제본, 3. 가상 파이버 채널, 4. SR-IOV 네트워킹, 5. 공유 .VHDX이다. Windows 10에서만 사용할 수 있는 Hyper-V 기능은 다음과 같이 2가지이다. 1. 빨리 만들기 및 VM 갤러리, 2. 기본 네트워크(NAT 스위치)이다. 메모리 관리 모델이 Windows의 Hyper-V에서 다르다. 서버에서 Hyper-V 메모리는 해당 서버에서 관리 컴퓨터만 실행된다는 가정 하에 관리된다. Windows의 Hyper-V에서 메모리는 대부분 클라이언트 컴퓨터가 가상 컴퓨터 실행 외에도 호스트의 소프트웨어를 실행한다는 예상에 따라 관리된다.

---

### [Open Container Initiative (OCI)](https://opencontainers.org/)

The Open Container Initiative is an open governance structure for the express purpose of creating open industry standards around container formats and runtimes.

Established in June 2015 by Docker and other leaders in the container industry, the OCI currently contains two specifications: the Runtime Specification (runtime-spec) and the Image Specification (image-spec). The Runtime Specification outlines how to run a "filesystem bundle" that is unpacked on disk. At a high-level an OCI implementation would download an OCI Image then unpack that image into an OCI Runtime filesystem bundle. At this point the OCI Runtime Bundle would be run by an OCI Runtime.

### Container Runtime Interface (CRI) | [Kubernetes](https://kubernetes.io/docs/concepts/architecture/cri/)

The CRI is a plugin interface which enables the kubelet to use a wide variety of container runtimes, without having a need to recomplile the cluster components.

You need a working container runtime on each Node in your cluster, so that the kubelet can launch Pods and their containers.

The Container Runtime Interface (CRI) is the main protocol for the communication between the kubelet and Container Runtime.

The Kubernetes Container Runtime Interface (CRI) defines the main gRPC protocol for the communication between the cluster components kubelet and container runtime.

---

# *Container* | [What is a container (IBM)](https://www.ibm.com/cloud/learn/containers) | [What is a container (MS)](https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-a-container/#overview) | [What is a container (Google)](https://cloud.google.com/learn/what-are-containers) | [What is a container (Docker)](https://www.docker.com/resources/what-container/)

A container is a standard unit of software that packages up code and all its dependencies so that application runs quickly and reliably from one computing envrionment to another. A Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings.

## *[Docker](https://www.docker.com/)* | [Docs](https://docs.docker.com/get-started/overview/)

Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly. With Docker, you can manage your infrastructure in the same ways you manage your applications. By taking advantage of Docker's methodologies for shipping, testing, and deploying code quickly, you can significantly reduce the delay between writing code and running it in production.

## *[Kubernetes](https://kubernetes.io/)* | [What is Kubernetes (KR)](https://kubernetes.io/docs/concepts/overview/)

Kubernetes is a portable, extensible, open source platform for managing containerized workload and services, that facilitates both declarative configuration and automation. It has a large rapidly growing ecosystem. Kubernetes services, support, and tools are widely available.

The name Kubernetes originates from Greek, meaning helmsman or pilot. K8s as an abbreviation results from counting the eight letters between the "K" and the "s". Google open-sourced the Kubernetes project in 2014. Kubernetes combines ovver 15 years of Google's experience running production workloads at scale with best-of-breed ideas and practices from the community.

### Going back in time

- Tranditional deployment era

Early on, organizations ran applications on physical servers. There was no way to define resource boundaries for applications in a physical server, and this caused resource allocation issues. For example, if multiple applications run on a physical server, there can be instances where one application would take up most of the resources, and as a result, the other applications would underperform. A solution for this would be to run each application on a different physical server. But this did not scale as resources were underutilized, and it was expensive for organizations to maintain many physical servers.

- Virtualized deployment era

As a solution, virtualization was introduced. It allows you to run multiple Virtual Machines (VMs) on a single physical server's CPU. Virtualization allows applications to be isolated between VMs and provides a level of security as the information of one application cannot be freely accessed by another application.

Virtualization allows better utilization of resources in a physical server and allows better scalability because an application can be added or updated easily, reduces hardware costs, and much more. With virtualization you can present a set of physical resources as a cluster of disposable virtual machines.

Each VM is a full machine running all the components, including its own operating system, on top of the virtualized hardware.

- Container deployment era

Containers are similar to VMs, but they have relaxed isolation properties to share the Operating System (OS) among the applications. Therefore, containers are considered lightweight. Similar to a VM, a container has its own filesystem, share of CPU, memory, process space, and more. As they are decoupled from the underlying infrastructure, they are portable across clouds and OS distributions.

Containers have become popular because they provide extra benefits, such as:

- Agile application creation and deployment: increased ease and efficiency of container image creation compared to VM image use.
- Continuous development, integration, and deployment: provides for reliable and frequent container image build and deployment with quick and efficient rollbacks (due to image immutability).
- Dev and Ops separation of concerns: create application container images at build/release time rather than deployment time, thereby decoupling applications from infrastructure.
- Observability: not only surfaces OS-level information and metrics, but also application health and other signals.
- Environmental consistency across development, testing, and production: Runs the same on a laptop as it does in the cloud.
- Cloud and OS distribution portability: Runs on Ubuntu, RHEL, CoreOS, on-premises, on major public clouds, and anywhere else.
- Application-centric management: Raises the level of abstraction from running an OS on virtual hardware to running an application on an OS using logical resources.
- Loosely coupled, distributed, elastic, liberated micro-services: applications are broken into smaller, independent pieces and can be deployed and managed dynamically – not a monolithic stack running on one big single-purpose machine.
- Resource isolation: predictable application performance.
- Resource utilization: high efficiency and density.

---

### Reference
- Virtual Machine Wiki KR-KO, https://ko.wikipedia.org/wiki/%EA%B0%80%EC%83%81_%EB%A8%B8%EC%8B%A0, 2020-11-04-Wed.
- Windows 10 Hyper-V Introduction, https://docs.microsoft.com/ko-kr/virtualization/hyper-v-on-windows/about/, 2020-11-04-Wed.
- VirtualBox, https://www.virtualbox.org/, 2020-11-04-Wed.
- VMware, https://www.vmware.com/, 2020-11-04-Wed.
- Open Container Initiative, https://opencontainers.org/, 2022-07-26-Tue.
- Container Runtime Interface Kubernetes, https://kubernetes.io/docs/concepts/architecture/cri/, 2022-07-26-Tue.
- Kubernetes, https://kubernetes.io/, 2022-10-11-Tue.
- What is Kubernetes, https://kubernetes.io/docs/concepts/overview/, 2022-10-11-Tue.
- VMware Workstation Player, https://docs.vmware.com/en/VMware-Workstation-Player/index.html, 2022-10-17-Mon.
- VMware Workstation Player Documentation, https://docs.vmware.com/en/VMware-Workstation-Player/index.html, 2022-10-17-Mon.
- VMware Workstation Player for Linux Documentation, https://docs.vmware.com/en/VMware-Workstation-Player-for-Linux/index.html, 2022-10-17-Mon.
- VMware Workstation Player for Windows Documentation, https://docs.vmware.com/en/VMware-Workstation-Player-for-Windows/index.html, 2022-10-17-Mon.
- VMware Workstation Pro Documentation, https://docs.vmware.com/en/VMware-Workstation-Pro/index.html, 2022-10-17-Mon.
- Container IBM Cloud, https://www.ibm.com/cloud/learn/containers, 2022-10-17-Mon.
- Container MicroSoft Cloud, https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-a-container/#overview, 2022-10-17-Mon.
- Container Google Cloud, https://cloud.google.com/learn/what-are-containers, 2022-10-17-Mon.
- Container Docker, https://www.docker.com/resources/what-container/, 2022-10-17-Mon.
- Docker, https://www.docker.com/, 2022-10-17-Mon.
- What is a Docker, What is a container, https://docs.docker.com/get-started/overview/, 2022-10-17-Mon.
