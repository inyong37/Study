# VM: Virtual Machine | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/%EA%B0%80%EC%83%81_%EB%A8%B8%EC%8B%A0)
가상 머신은 컴퓨팅 환경을 소프트웨어로 구현한 것, 즉 컴퓨터를 에뮬레이션하는 소프트웨어이다. 가상 머신상에서 운영 체제나 응용 프로그램을 설치 및 실행할 수 있다. 다른 기능들이 있는 여러 종류의 가상 머신들이 있다. 시스템 가상 머신들은, 또한 완전한 가상화 가상 머신들로 알려진 실제 기계의 대체제를 제공하고 완전한 운영 체계의 실행을 위해 요구되는 기능성의 수준을 제공한다. 하이퍼바이저는 하드웨어를 공유하고 관리하기 위해 네이티브 실행을 이용한다. 그리고 하이퍼바이저는 독립된 다른 환경들을 같은 물리적인 기계에서 실행하기 위해서 허용한다. 현대의 하이퍼바이저들은 하드웨어의 도움을 받는 가상화를 이용하는데, 그것들은 주로 주 CPU의 특정 하드웨어 기능을 사용하여 효과적이고 완전한 가상화를 제공한다. 프로세스 가상머신들은 플랫폼에 독립적인 프로그램 실행 환경과 추상화를 제공하여 하나의 프로그램을 실행하도록 설계되었다.

가상 머신은 원래 Popek와 Goldberg가 "실제 컴퓨터의 효율적이고 고립된 복제물"로 정의했다. 현재는 "실제 하드웨어와 직접적인 통신이 없는 가상 컴퓨터"를 가리킨다. 가상 머신은 실제 컴퓨터와 어느 정도의 통신과 사용을 기반으로 두 가지로 나뉜다. 시스템 가상 머신은 완전한 시스템 플랫폼을 제공하며, 다시 말해 완전한 운영 체제의 실행을 지원한다. 반대로, 프로세스 가상 머신은 하나의 단일 프로그램을 실행하기 위해 만들어져 있는데, 다시 말해 단일 프로세스를 지원한다. 가상 머신의 중요한 특징은 안에서 돌아가는 소프트웨어가 가상 머신이 제공하는 환경과 자원에 제한을 받으며 가상 세계를 벗어날 수 없다는 것이다.

## VMware | [Homepage](https://www.vmware.com/)

## VirtualBox | [Homepage](https://www.virtualbox.org/)
VirtualBox is a x86 and AMD64/Intel64 virtuallization product for enterprise as well as home use. Not only is VirtualBox an extremely feature rich, high performance product for enterprise customers, it is also the only professional solution that is freely available as Open Source Software under the terms of the GNU General Public License(GPL) version 2.

VirtualBox는 InnoTek에서 개발을 시작했고, Sun Microsystems에서 InnoTeck을 인수한 뒤, Oracle이 Sun Microsystems를 인수하여, 현재 Oracle에서 배포하고 있다.

## Hyper-V | [Introduction](https://docs.microsoft.com/ko-kr/virtualization/hyper-v-on-windows/about/)
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

### Reference
- Virtual Machine Wiki KR-KO, https://ko.wikipedia.org/wiki/%EA%B0%80%EC%83%81_%EB%A8%B8%EC%8B%A0, 2020-11-04-Wed.
- Windows 10 Hyper-V Introduction, https://docs.microsoft.com/ko-kr/virtualization/hyper-v-on-windows/about/, 2020-11-04-Wed.
- VirtualBox, https://www.virtualbox.org/, 2020-11-04-Wed.
- VMware, https://www.vmware.com/, 2020-11-04-Wed.
- Open Container Initiative, https://opencontainers.org/, 2022-07-26-Tue.
- Container Runtime Interface Kubernetes, https://kubernetes.io/docs/concepts/architecture/cri/, 2022-07-26-Tue.
