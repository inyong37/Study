# System (Operating System) | [Wiki (KR)](https://ko.wikipedia.org/wiki/%EC%9A%B4%EC%98%81_%EC%B2%B4%EC%A0%9C)

Operating System(OS, 운영 체제는/조작 체계)는 시스템 하드웨어를 관리할 뿐 아니라 application을 실행하기 위하여 하드웨어 추상화 플팻폼과 공통 시스템 서비스를 제공하는 시스템 소프트웨어이다. 최근에는 가상화 기술의 발전에 힘입어 실제 하드웨어가 아닌 하이퍼바이저 위에서 실행되기도 한다. 또한 입출력과 메모리 할당과 같은 하드웨어 기능의 경우 운영 체제는 application과 컴퓨터 하드웨어 사이의 중재 역할을 한다. 그러나 application 코드는 일반적으로 하드웨어에서 직접 실행된다. OS는 휴대 전화, 게임기에서부터 슈퍼컴퓨터, 웹 서버에 이르기까지 컴퓨터를 포함하는 거의 모든 장치에서 볼 수 있다. OS는 한 면으로는 소비자를, 다른 한 면으로는 프로그램 개발자를 함께 하나의 시장으로 데려다 놓을 수 있는 양면 플랫폼이다. 잘 알려진 현대의 PC OS에는 Microsoft Windows, Mac OS X, Linux가 있다. 이 밖에 BSD, Unix 등의 PC용 OS가 있다.

OS는 실행되는 application들이 메모리와 CPU, IO 등의 자원들을 사용할 수 있도록 만들어 주고, 이들을 추상화하여 파일 시스템 등의 서비스를 제공한다. 또한 멀티태스킹을 지원하는 경우, 여러 개의 applications를 실행하고 있는 동안, OS는 이런한 모든 porcessors를 스케쥴링하여 마치 그들이 동시에 수행되는 것처럼 보이는 효과를 낸다.

Related books (in Study Repository's main readme.md):
- Operating System Concepts (10th Ed.)
- Operating System Concepts Essential (2nd Ed.)
- Advanced Programming in the UNIX Environment (3rd Ed.)
- Unix: A History and a Memoir

### What is a Real-Time Operating System? | [MS Docs](https://docs.microsoft.com/en-us/windows/iot/iot-enterprise/soft-real-time/soft-real-time)

When running a program, a normal operating system gives deterministic results but allows for a nondeterministic time to complete a task. In a real-time operating system both the results of program execution and the time take to get those results are (at least partially) deterministic.

### Hard Real-Time vs. Soft Real-Time | [MS Docs](https://docs.microsoft.com/en-us/windows/iot/iot-enterprise/soft-real-time/soft-real-time) | [JavatPoint](https://www.javatpoint.com/hard-and-soft-real-time-operating-system) | [Blog (KR)](https://velog.io/@joosing/%EC%89%BD%EA%B2%8C-%EC%9D%B4%ED%95%B4%ED%95%98%EB%8A%94-%EC%8B%A4%EC%8B%9C%EA%B0%84-%EC%9A%B4%EC%98%81%EC%B2%B4%EC%A0%9CRealtime-OS%EC%9D%98-%EA%B0%9C%EB%85%90-vxWorks-realtime-Linux)

요약: deterministic

A hard real-time operating system is one where the time taken is deterministic to an exact moment. These operating systems are deployed in use cases where failure to get results on time represents a total system failure. Examples include microcontrollers within a car engine or airplane, printers, laser cutters, etc. Azure Real-Time OS is an example of such an OS.

A soft real-time operating system is one where there is a small window of time for program completion rather than a precise moment due to a bit of jitter from the operating system. Soft real-time systems, though less precise, can be run on multiple cores and impose fewer restrictions on applications. This is the type of real-time performance that you can expect from Windows 10 IoT Enterprise.

Hard Real-Time System must generate accurate responses to the evnets within the specified time. A hard real-time system is purely deterministic and time constraint system: Flight Control System, Missile Guidance System, Weapons Defense System, Medical System, Inkjet Printer System, Railway Signalling System, Air Traffic Control System, Nuclear Reactor Control System, Anti-missile System, Chemical plant control, Autopilot System in Plane, Pacemakers.

In a soft real-time system, the meeting of deadline is not compulsory for every task, but the process should get processed and give the result: personal computer, auido and video systems.

## Firmware | [Wiki (KR)](https://ko.wikipedia.org/wiki/%ED%8E%8C%EC%9B%A8%EC%96%B4)

Firmware(펌웨어)는 특정 하드웨어 장치에 포함된 소프트웨어로, 소프트웨어를 읽어 실행하거나, 수정하는 것도 가능한 장치를 뜻한다. 하드웨어의 제어(low level control)와 구동을 담당하는 일종의 OS이다. Firmware는 ROM이나 PROM에 저장되며, 하드웨어보다는 교환하기가 쉽지만, 소프트웨어보다는 어렵다. Ashcer Opler는 firmware라는 용어를 1967년 "데이터메이션" 기사에서 만들어냈다. 원래는 마이크로코드를 담고 있는 컴퓨터의 명령 집합을 구현한, 쓰기 가능한 컨트롤 스토어(크기가 작은 특수 고속 메모리)의 내용물을 의미했는데 CPU가 실행할 수 있는 명령을 수정하기 위해 다시 로드할 수 있었다. 1990년대 중순까지 firmware를 업데이트하는 일은 일반적으로 소켓 형태의 ROM IC였던, firmware를 포함하는 기억 매체를 교체하는 일이 수반되었다. Flasy memorysms 시스템으로부터 물리적으로 IC를 제거하지 않고 firmware를 업데이트할 수 있게 해준다.

### Bootloader

Micro processor가 리셋 상태에서 빠져 나오면 맨 먼저 리셋 벡터로 정해진 메모리 주소로 가서 저장된 명령어를 실행한다. 전원이 들어온 직후에 RAM에는 아무런 의미가 없는 쓰레기 값이 저장되어 있으므로 리셋 벡터 위치에는 반드시 실행 가능한 명령어를 저장하고 있는 ROM이나 flasy memory와 같은 비휘발성 메모리가 있어야 한다. 리셋 벡터 위치의 비휘발성 메모리에 저장된 프로그램은 전원이 들어온 후 필요한 최소한의 하드웨어의 초기화와 OS의 kernel을 RAM으로 읽어 들여 실행할 준비 작업을 하는데 이런 일을 하는 시스템 소프트웨어를 bootloader(부트로더)라고 한다. Bootloader는 반드시 비휘발성 메모리에 저장된다.

PC처럼 큰 시스템에서 OS는 메모리가 아닌 HDD 또는 SDD와 같은 보조 기억 장치에 저장되어 있는데 CPU는 이에 저장되어 있는 프로그램을 직접 실행할 수 없다. PC 전원이 들어오면 ROM에 저장되어 있는 bootloader가 제일 먼저 실행되어 저장되어 있는 kernel을 RAM으로 읽어 들여 CPU가 kernel을 실행시키는데 필요한 준비 작업을 한다. HDD, SDD가 없는 임베디드 시스템의 경우에도 flasy memory에 저장된 OS 실행 코드를 RAM으로 옮기는 일을 bootloader가 한다. 경우에 따라서는 flasy memory를 절약하기 위해 실행 코드를 압축해서 저장하기도 하는데 이 떄에는 bootloader가 압축을 푸는 일 또한 한다. 그러나 AVR이나 8051 같은 8bit micro controller들은 규모가 큰 OS를 구동할 수 없기도 하거니와 flasy memory에 저장되어 있는 실행 코드를 직접 실행하므로 앞에서 설명한 역할을 하는 bootloader는 필요로 하지 않다. 그러나 이런 간단한 processor에서도 bootloader를 사용할 수 있는데 이 때 bootloader의 주역할은 호스트 컴퓨터와의 직렬 통신을 통해 실행 코드를 받아서 내부 flasy memory에 기록하는 것이다.

## BIOS: Basic Input Output System | [Wiki (KR)](https://ko.wikipedia.org/wiki/%EB%B0%94%EC%9D%B4%EC%98%A4%EC%8A%A4)

BISO(바이오스)는 OS 중 가장 기본적인 컴퓨터의 입출력을 처리하는 소프트웨어이다. 사용자가 컴퓨터를 켜면 시작되는 프로그램의 주변 장치와 컴퓨터 OS 사이의 데이터의 흐름을 관리한다. Firmware의 한 종류로 IBM 호환 컴퓨터의 경우에 전원이 공급되면 시작되는 부팅 절차에서 하드웨어 초기화를 수행하고, OS나 application에게 run-time 서비스(컴퓨터 프로그램의 실행을 지원하는 서비스)를 제공한다. BISO firmware는 PC에 내장되어 있어서 전원이 인가되면 실행이 시작되는 최초의 프로그램이다. BIOS라는 이름은 1975년도에 사용된 CP/M OS의 Basic Input/Output System에서 유래했다. 원래는 IBM 소유였으나 많은 회사들이 원본 프로그램을 분석(reverse engineering)하여 호환 프로그램을 개발하였다. 현대 PC에서 BIOS는 하드웨어 부품을 초기화하고 검사하는 역할, 부트로더 또는 대용량 저장장치에 저장된 OS를 RAM으로 읽어오는 기능을 수행한다.

넓은 의미로 컴퓨터에 탑재된 프로그램 중에서 하드웨어와 가장 낮은 수준에서 입출력을 담당하는 프로그램을 가리킨다. 좁은 의미의 정의에선 IMB-PC 호환 기종에 탑재된 것을 말하며, 보통 이 뜻으로 쓰인다. BIOS는 컴퓨터에서 하드웨어와 소프트웨어의 중간 형태를 가지는 firmware의 일종으로 대부분 소프트웨어가 하드웨어를 제어하고 하드웨어에 의해 변경되거나 생성된 정보를 소프트웨어에서 처리할 수 있도록 전달하는 등 인간의 신경망과 같은 기능을 수행한다.

## UEFI: Unified Extensible Firmware Interface | [Wiki (KR)](https://ko.wikipedia.org/wiki/%ED%86%B5%EC%9D%BC_%ED%99%95%EC%9E%A5_%ED%8E%8C%EC%9B%A8%EC%96%B4_%EC%9D%B8%ED%84%B0%ED%8E%98%EC%9D%B4%EC%8A%A4)

UEFI(통일/통합 확장 펌웨어 인터페이스)는 OS와 platform firmware 사이의 소프트웨어 인터페이스를 정의하는 규격이다. IBM PC 호환기종에서 사용되는 BIOS interface를 대체할 목적으로 개발되었다. Intel이 개발한 EFI(Extensible Firmware Interface) 규격에서 출발하였다. EFI의 관행과 데이터 포맷 중 일부는 Microsoft Windows의 것과 동일하게 사용된다. 2005년 UEFI는 EFI 1.10의 사용을 권장치 않기로 했다. 통일 EFI 포럼은 UEFI 사양을 관리하는 산업체이다.

---

## Types :books:

- CP/M (by Digital Research, at 1974)
- DOS
  - 86-DOS (aka QDOS, by Seattle Computer Products)
  - MS-DOS (By Microsoft, at 1981)
  - PC-DOS (By IBM, at 1981)
- Windows (By Microsoft) | Server | IoT
- Multics (By MIT, from 1965)
- Unix (by Bell Laboratory, at 1970's)
  - AIX (by IBM)
  - HP-UX (by Hewlett Packard Enterprise, from Unix System V, at 1984)
  - SunOS (by Sun Microsystems)
  - BSD (by Computer Systems Research Group in University of California, Berkeley, at 1977 ~ 1995)
    - Solaris (by Oracle)
    - FreeBSD (focused on processing power)
    - OpenBSD (focused on security)
    - NeXTSTEP (by NeXT)
      - Darwin (by Apple, based on XNU: FreeBSD and Mach)
        - iOS (formerly OS X for iPhone, iPhone OS, by Apple)
        - iPadOS
      - OS X
      - macOS 
- Mac OS (formerly System Software, by Apple, from January 1984)
  - Classic Mac OS (formerly Macintosh System, by Apple, until December 2001 with version 9.2.2)
  - Mac OS X
- MINIX 3 (by Andrew S. Tanenbaum et al., from October 2005, until 2018 with version 3.4.0 rc6)
- Linux (by Linus Torvalds and community, from September 1991)
  - SUSE Linux (by SUSE, from 1992)
  - Debian (by Debian Project, from September 1993)
    - Ubuntu (by Canonical, from October 2004, based GNOME 3 in version 22) | Ubuntu Core
      - Linux Mint (by community, from August 2006)
      - Ubuntu MATE (by Ubuntu Mate Team, from October 2014, based on GNOME 2 in version 18)
    - Raspberry Pi OS (formely Raspbian, by Mike Thompson, Peter Green and foundation, from June 2012)
  - CRUX (by Per Lidén, from 2002, used for the x86-64 architecture)
  - Arch Linux (by Judd Vinet, from March 11 2002, used for the x86-64 architecture)
  - Fedora (formerly Red Hat Linux, by Red Hat of IBM, from November 2003) | Workstation | Server | IoT
    - CentOS Stream (by Red Hat of IBM, from November 2021 with version 8)
    - Red Hat Enterprise Linux (by Red Hat of IBM, from Febuary 2000)
    - CentOS Linux (by Red Hat of IBM and community, from May 2004, until December 2021 with version 8)
    - Rocky Linux (by Rocky Enterprise Software Foundation (RESF), from April 2021 with version 8)
  - OpenWrt (by Linksys, from 2007, used for most of Router Platform)
  - Android (by Android of Google, from September 2008, used for Mobile Platform)
    - Wear OS (formerly Android Wear, from March 2014 with Android 4.4W, used for Android Smart Watch)
    - Android TV (used for Smart TV)
    - Android for Cars
      - Android Auto (from March 2015, used for connected vehicle by Android Phone)
      - Android Automotive OS (used for infortainment system of vehicle)
    - Android Things
    - Chrome OS
  - Google TV (by Google, Intel, Sony, and Logitech, from October 2010)
  - webOS (by LG Electronics, from February 2013)
    - webOS Open Source Edition (OSE)
    - Open webOS (by Hewlett-Packard, from April 2010)
    - Palm OS (by Palm, from January 2009)
  - Tizen (by Samsung Electronics, from April 2012)

- z/OS (by IBM, from October 2000, used for Mainframe)
- OpenVMS (by VSI, from October 1977, used for Servers)
- TinyOS (by TinyOS Alliance, from 2000)
- FreeRTOS (by Real Time Engineers Ltd., from 2003)
- Contiki-NG (from 2006, used for IoT devices)
- Mbed OS (by	Collaborative project managed by Arm, from September 2009)
- RIOT (by Free University of Berlin & French Institute for Research in Computer Science and Automation & Hamburg University of Applied Sciences, from October 2009, used for embedded systems)
- MicroPython (by Damien P. George, from May 2014)

---

## [CP/M](https://web.archive.org/web/20080515232659/http://www.digitalresearch.biz/CPM.HTM) | [Wiki (KR)](https://ko.wikipedia.org/wiki/CP/M)

CP/M은 인텔 8080/85 마이크로프로세서를 기반으로 하는 처음 제작된 운영 체제이다. 디지털 리서치의 개리 킬달(Gary Kildall)이 만들었다. 게리 킬달은 커스텀 플로피 디스크 컨트롤러를 통해 접속되는 슈거트 어소시에이트(Shugart Associates) 8인치 플로피 디스크 드라이브가 장착된 인텔 인텔렉-8 개발 시스템에서 구동할 운영 체제로서 CP/M을 1974년에 처음 개발하였다. 최소 8비트의 CP/M 시스템은 다음 5개의 부품을 포함하고 있어야한다. 1. 아스키 문자열 집합을 사용하는 컴퓨터 터미널(매우 오래된 시스템은 텔레프린터를 사용하였다.), 2. 인텔 8080(나중에는 8085) 또는 자일로그 Z80 마이크로프로세서, 3. 최소 16킬로바이트인 램, 4. 디스켓 첫 섹터를 부트스트래핑할 수 있는 환경, 5. 최소 한 개의 플로피 디스크 드라이브. 8비트 버전에서 동작하는 동안 메모리에 로드된 CP/M 운영 체제에는 다음 3개의 구성요소가 있었다. 1. 기본 입출력 시스템, 곧 BIOS, 2. 기본 디스크 운영 체제, 곧 BDOS, 3. 콘솔 명령어 프로세서, 곧 CCP.

---

## DOS: Disk Operating System | [Wiki (KR) 디스크 운영 체제](https://ko.wikipedia.org/wiki/%EB%94%94%EC%8A%A4%ED%81%AC_%EC%9A%B4%EC%98%81_%EC%B2%B4%EC%A0%9C) | [Wiki (KR) 도스](https://ko.wikipedia.org/wiki/%EB%8F%84%EC%8A%A4)

DOS는 플로피 디스크, 하드 디스크 드라이브, 광 디스크와 같은 디스크 스토리지 장치를 사용할 수 있는 컴퓨터 운영 체제이다. 디스크 운영 체제는 스토리지 디스크의 파일 정리, 읽기, 쓰기를 위한 파일 시스템을 제공해야 한다. 이 정의는 현재 쓰이는 마이크로소프트 윈도우 버전 등 현 세대의 운영 체제에 적용되지는 않으며 더 오래된 세대의 운영 체제에 국한시키는 것이 더 적절하다. 디스크 운영 체제들은 메인프레임, 마이크로프로세서, 가정용 컴퓨터 용으로 이용이 가능했으며 부팅 과정의 일환으로 직접 디스크에서 로드되는 것이 보통이었다.

운영 체제의 확장 기능이었던 DOS로는 다음 8개 예시가 있다. 1. Apple DOS, 2. 코모도어 DOS, 3. 아타리 DOS, 4. MSX-DOS, 5. 디스크 파일링 시스템, 6. 어드밴스드 디스크 파일링 시스템(ADFS), 7. AMSDOS, 8. GDOS/G+DOS. 메인 운영 체제였던 DOS로는 다음 4개 예시가 있다. 1. IBM 시스템/360 계열의 메인프로엠 컴퓨터를 위한 DOS/360 초기/단순 운영 체제(나중에 DOS/VSE가 되었으며 그 뒤로 간단히 VSE로 불렸다.), 2. DEC PDP-11 미니 컴퓨터용 DOS-11 운영 체제, 3. TRSDOS는 탠디의 TRS-80 계열의 컴퓨터용 운영 체제였다. 4. 인텔 x86 CPU와 호환되는 IBM PC용 MS-DOS.

DOS는 디스크 운영 체제의 일종으로서 디스크에 읽고 쓰기 등의 명령을 수행하는 프로그램이다. 명령어를 직접치는 명령 줄 기반이다. 1981년부터 1995년까지, 또 부분적으로 MS-DOS 기반인 마이크로소프트 Windows(95, 98, ME)를 포함한 2000년까지는 MS-DOS가 IBM PC 호환 기종 시장을 장악하였다. DOS는 MS-DOS, PC-DOS, DR-DOR, Free-DOS, ROM-DOS, PTS-DOS를 포함한 비슷한 명령 줄 시스템의 계열이다. 이 시스템 중 어느 것도 간단히 DOS라고 불리진 않았다. (1960년대의 이와 관련이 없는 IBM 메인프레임 운영 체제에만 사용되었음) 이와 무관한 수많은 비x86 마이크로컴퓨터 디스크 운영 체제는 DOS라는 이름을 그대로 사용했으며 이들을 사용하는 컴퓨터에대해 논할 때 단순히 DOS라고 부르곤 했다. (아미가 도스, AMSDOS, Apple DOS, 아타리 DOS, 코모도어 DOS, CSI-DOS, 프로도스, TRSDOS)

### 86-DOS (aka QDOS) | [Wiki (KR)](https://ko.wikipedia.org/wiki/86-%EB%8F%84%EC%8A%A4)

86-DOS는 시애틀 컴퓨터 프로덕트(SCP)에서 팀 패터슨에 의하여 Intel 8086 기반 컴퓨터 키트 용으로 개발되어 판매된 운영 체제로 현재는 단종되었다. 초기에는 QDOS(Quick and Dirty Operating System)로 알려졌으나, 1980년에 SCP가 운영 체제를 라이센스하기 시작하면서 86-DOS로 이름이 변경되었다. 86-DOS에는 디지털 리서치의 CP/M 운영 체제를 모방한 명령 구조 및 응용 프로그래밍 인터페이스가 있어 프로그램을 후자로부터 쉽게 이식할 수 있었다. 마이크로소프트에게 라이센스 되었다가 그 후 판매되어 MS-DOS 및 PC-DOS로 개발되었다.

### MS-DOS | [GitHub](https://github.com/Microsoft/MS-DOS) | [Wiki (KR)](https://ko.wikipedia.org/wiki/MS-DOS)

MS-DOS(MicroSoft Disk Operating System)은 DOS의 일종으로 마이크로소프트가 IBM의 의뢰를 받아 시애틀 컴퓨터 프로덕트로부터 사들여 개발한 IBM PC용 운영 체제(CP/M-86 호환의 DOS)로 사상 최초로 대중화된 운영 체제이다. 1981년 8월 처음 PC에 올려져서 제공되었으며 1995년 개발이 중단될 때까지 몇 차례의 판올림이 있었다. MS-DOS라는 독립 제품으로서의 최종 버전은 6.22이며 Windows 95가 출시된 이후부터는 윈도 제품의 일부로 제공되었고 Windows ME에 기본 내장되어있는 8.0까지 나왔다. 이후에는 더 이상 개발되지 않는다. 마이크로소프트는 이 제품의 인기에 힘입어 조그마한 프로그래밍 언어 회사에서 다양한 소프트웨어를 제공하는 회사로 자리잡게 된다.

### PC-DOS | [Wiki (KR)](https://ko.wikipedia.org/wiki/PC-DOS)

PC-DOS는 IBM 개인용 컴퓨터를 위한 클로즈드 소스 형태의 도스 운영 체제이며 1980년대에서 1990년대까지 판매되었다. 1981년에 IBM과 마이크로소프트 사이에서, 마이크로소프트는 기본 제품을 생산하고 두 회사는 합성 코드를 공유하여 더 강력하고 튼튼한 시스템으로 들어가는 서로 다른 부분을 개발하려고 했다. 또 MS-DOS와 PC-DOS는 별도로 시장화될 예정이었다. 다시 말해 PC-DOS는 IBM PC용으로만 판매하고 마이크로소프트는 오픈 마켓에 판매하려고 했다. 그러나 IBM은 자사의 개인용 컴퓨터를 위한 운영 체제의 소스 코드 소유권을 획득하려고 하지는 않았다. ThinkPad 제품은 현재 복구 파티션에 PC-DOS의 최신 버전의 복사본을 소유하고 있다.

### Font

IBM 3270

---

## Windows | [Windows 10 Homepage](https://www.microsoft.com/en-us/windows/) | [Wiki](https://en.wikipedia.org/wiki/Microsoft_Windows) | [IoT](https://developer.microsoft.com/en-us/windows/iot/)

Microsoft Windows, commonly referred to as Windows, is a group of several proprietary graphical operating system families, all of which are developed and marketed by Microsoft. Each family caters to a certain sector of the computing industry. Active Microsoft Windows families include Windows NT and Windows IoT; these may encompass subfamilies, e.g. Windows Server or Windows Embedded Compact (Windows CE). Defunct Microsoft Windows families include Windows 9x, Windows Mobile and Windows Phone.

Microsoft introduced an operating environment named Windows on November 20, 1985, as a graphical operating system shell for MS-DOS in response to the growing interest in graphical user interfaces (GUIs). Microsoft Windows came to dominate the world's personal computer (PC) market with over 90% market share, overtaking Mac OS, which had been introduced in 1984. Apple came to see Windows as an unfair encroachment on their innovation in GUI development as implemented on products such as the Lisa and Macintosh (eventually settled in court in Microsoft's favor in 1993). On PCs, Windows is still the most popular operating system. However, in 2014, Microsoft admitted losing the majority of the overall operating system market to Android, because of the massive growth in sales of Android smartphones. In 2014, the number of Windows devices sold was less than 25% that of Android devices sold. This comparison, however, may not be fully relevant, as the two operating systems traditionally target different platforms. Still, numbers for server use of Windows (that are comparable to competitors) show one third market share, similar to that for end user use.

As of February 2020, the most recent version of Windows for PCs, tablets and embedded devices is Windows 10, version 2004. The most recent version for server computers is Windows Server, version 2004. A specialized version of Windows also runs on the Xbox One video game console.

Download | [Windows 10 Download](https://www.microsoft.com/en-us/software-download/windows10) | [Windows 8.1 Download](https://www.microsoft.com/en-us/software-download/windows8ISO) | [Windows 7 Download](https://www.microsoft.com/en-us/software-download/windows7)

### Font

Consolas

### [MSDN (Microsoft Developer Network)](https://social.msdn.microsoft.com/forums/en-us/home) | [Wiki](https://en.wikipedia.org/wiki/Microsoft_Developer_Network) | [Docs](https://docs.microsoft.com/en-us/) | [GitHub](https://github.com/MicrosoftDocs)

Microsoft Developer Network (MSDN) was the division of Microsoft responsible for managing the firm's relationship with developers and testers, such as hardware developers interested in the operating system (OS), and software developers developing on the various OS platforms or using the API or scripting languages of Microsoft's applications. The relationship management is situated in assorted media: web sites, newsletters, developer conferences, trade media, blogs and DVD distribution.

From January 2020, the website has been fully integrated with Microsoft Docs.

```Other parts of the "Windows" have been moved to the "Windows" page.```

---

## [Multics](https://multicians.org/multics.html)

Multics (Multiplexed Information and Computing Service) was a mainframe time-sharing operating system begun in 1965 and used until 2000. Multics began as a research project and was an important influence on operating system development. The system became a commercial product sold by Honeywell to education, government, and industry.

Multics was a prototype of a Computer Utility, providing secure computing to remote users at their terminals. Multicians still miss the elegant, consistent, and powerful programming environment; some Multics features are only now being added to contemporary systems.

---

## [Unix](https://www.opengroup.org/membership/forums/platform/unix) | [Wiki](https://en.wikipedia.org/wiki/Unix)

Unix is a family of multitasking, multiuser computer operating systems that derive from the original AT&T Unix, development starting in the 1970s at the Bell Labs research center by Ken Thompson, Dennis Ritchie, and others.

Initially intended for use inside the Bell System, AT&T licensed Unix to outside parties in the late 1970s, leading to a variety of both academic and commercial Unix variants from vendors including University of California, Berkeley (BSD), Microsoft (Xenix), Sun Microsystems (SunOS/Solaris), HP/HPE (HP-UX), and IBM (AIX). In the early 1990s, AT&T sold its rights in Unix to Novell, which then sold its Unix business to the Santa Cruz Operation (SCO) in 1995. The UNIX trademark passed to The Open Group, a neutral industry consortium founded in 1996, which allows the use of the mark for certified operating systems that comply with the Single UNIX Specification (SUS). However, Novell continues to own the Unix copyrights, which the SCO Group, Inc. v. Novell, Inc. court case (2010) confirmed.

Unix systems are characterized by a modular design that is sometimes called the "Unix philosophy". According to this philosophy, the operating system should provide a set of simple tools, each of which performs a limited, well-defined function. A unified filesystem (the Unix filesystem) and an inter-process communication mechanism known as "pipes" serve as the main means of communication, and a shell scripting and command language (the Unix shell) is used to combine the tools to perform complex workflows.

Unix distinguishes itself from its predecessors as the first portable operating system: almost the entire operating system is written in the C programming language, which allows Unix to operate on numerous platforms.

[A diagram showing the key Unix and Unix-like operating systems (Wiki)](https://en.wikipedia.org/wiki/Unix#/media/File:Unix_history-simple.svg)

~~```Other parts of the "Uinx" have been moved to the "Unix" page.```~~

### [AIX](https://www.ibm.com/it-infrastructure/power/os/aix)

### [Solaris](https://www.oracle.com/solaris/solaris11/)

### [HP-UX](https://www.hpe.com/us/en/servers/hp-ux.html)

### [FreeBSD](https://www.freebsd.org/)

---

### *Portable Operating System Interface (POSIX)* | [WiKi](https://en.wikipedia.org/wiki/POSIX) | [WiKi (KR)](https://ko.wikipedia.org/wiki/POSIX)

The Portable Operating System Interface (POSIX) is a family of standards specified by the IEEE Computer Society for maintaining compatibility between operating systems. POSIX defines the application programming interface (API), along with command line shells and utility interfaces, for software compatibility with variants of Unix and other operating systems.

POSIX는 이식 가능 운영 체제 인터페이스의 약자로, 서로 다른 Unix OS의 공통 API를 정리하여 이식성이 높은 Unix application program을 개발하기 위한 목적으로 IEEE가 책정한 application interface 규격이다. POSIX의 마지막 글자 X는 Unix compatible OS에 보통 X가 붙는 것에서 유래한다. Unix 계열 외에 Microsoft Windows NT는 POSIX 1.0에 준하는 POSIX 서브 시스템을 탑재하고 있으며, POSIX application program을 서브 시스템에서 실행할 수 있다. 이는 주로 미국 정부기관의 컴퓨터 시스템 도입조건 (FIPS)에서 POSIX 준거할 것을 요구하기 때문이다. Windows 2000까지 POSIX 서브 시스템을 탑재하고 있었지만 Windows XP에서 폐지되었다. 이후 Windows 2003 R2부터 POSIX 2.0에 준하는 Subsystem for Unix-based Application (SUA)를 통해 POSIX를 지원하고 있다.

---

## [MINIX 3](https://www.minix3.org/)

MINIX 3 is a free, open-source, operating system designed to be highly reliable, flexible, and secure. It is based on a tiny microkernel running in kernel mode with the rest of the operating system running as a number of isolated, protected, processes in user mode. It runs on x86 and ARM CPUs, is compatible with NetBSD, and runs thousands of NetBSD packages.

---

## [Linux](https://www.linux.org/) | [Wiki](https://en.wikipedia.org/wiki/Linux) | [Download](https://www.linux.org/pages/download/)

Linux is a family of open source Unix-like operating systems based on the Linux kernel, an operating system kernel first released on September 17, 1991, by Linus Torvalds. Linux is typically packaged in a Linux distribution.

Distributions include the Linux kernel and supporting system software and libraries, many of which are provided by the GNU Project. Many Linux distributions use the word "Linux" in their name, but the Free Software Foundation uses the name GNU/Linux to emphasize the importance of GNU software, causing some controversy.

Popular Linux distributions include Debian, Fedora, and Ubuntu. Commercial distributions include Red Hat Enterprise Linux and SUSE Linux Enterprise Server. Desktop Linux distributions include a windowing system such as X11 or Wayland, and a desktop environment such as GNOME or KDE Plasma. Distributions intended for servers may omit graphics altogether, or include a solution stack such as LAMP. Because Linux is freely redistributable, anyone may create a distribution for any purpose.

Linux was originally developed for personal computers based on the Intel x86 architecture, but has since been ported to more platforms than any other operating system. Because of the dominance of Android on smartphones, Linux also has the largest installed base of all general-purpose operating systems. Although it is used by only around 2.3 percent of desktop computers, the Chromebook, which runs the Linux kernel-based Chrome OS, dominates the US K–12 education market and represents nearly 20 percent of sub-$300 notebook sales in the US. Linux is the leading operating system on servers (over 96.4% of the top 1 million web servers' operating systems are Linux), leads other big iron systems such as mainframe computers, and is the only OS used on TOP500 supercomputers (since November 2017, having gradually eliminated all competitors).

Linux also runs on embedded systems, i.e. devices whose operating system is typically built into the firmware and is highly tailored to the system. This includes routers, automation controls, smart home technology (like Google Nest), televisions (Samsung and LG Smart TVs use Tizen and WebOS, respectively), automobiles (for example, Tesla, Audi, Mercedes-Benz, Hyundai, and Toyota all rely on Linux), digital video recorders, video game consoles, and smartwatches. The Falcon 9's and the Dragon 2's avionics use a customized version of Linux.

Linux is one of the most prominent examples of free and open-source software collaboration. The source code may be used, modified and distributed commercially or non-commercially by anyone under the terms of its respective licenses, such as the GNU General Public License.

[From Earth to orbit with Linux and SpaceX](https://www.zdnet.com/article/from-earth-to-orbit-with-linux-and-spacex/)

[SpaceX Used Linux To Send NASA Astronauts To International Space Station](https://fossbytes.com/spacex-used-linux-to-send-nasa-astronauts-to-international-space-station/)

### [SUSE Linux](https://www.suse.com/products/server/)

### [Debian](https://www.debian.org/)

Download:
- [11.5.0-amd64-netinst](https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-11.5.0-amd64-netinst.iso)

### [Ubuntu](https://ubuntu.com/) | [Ubuntu Core](https://ubuntu.com/core)

### [Ubuntu MATE](https://ubuntu-mate.org/)

### [Linux Mint](https://www.linuxmint.com/)

### [Raspbian](https://www.raspbian.org/) | [Raspberry Pi OS](https://www.raspberrypi.com/software/)

### [Fedora](https://getfedora.org/)

Fedora creates an innovative, free, and open source platform for hardware, clouds, and containers that enables software developers and community members to build tailored solutions for their users.

### [Fedora Workstation](https://getfedora.org/en/workstation/)

Fedora Workstation is a polished, easy to use operating system for laptop and desktop computers, with a complete set of tools for developers and makers of all kinds.

Download [Fedora 37 Workstation](https://download.fedoraproject.org/pub/fedora/linux/releases/37/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-37-1.7.iso)

### [Fedora Server](https://getfedora.org/en/server/)

Fedora Server is a powerful, flexible operating system that includes the best and latest datacenter technologies. It puts you in control of all your infrastructure and services.

Download [Fedora 37 Server](https://download.fedoraproject.org/pub/fedora/linux/releases/37/Server/x86_64/iso/Fedora-Server-dvd-x86_64-37-1.7.iso)

### [Fedora IoT](https://getfedora.org/en/iot/)

Fedora IoT provides a trusted open source platform as a strong foundation for IoT ecosystems.

### [Fedora Cloud](https://getfedora.org/en/cloud/)

Fedora Cloud eidtion is a powerful and minial base operating system image with tailored images available for both public and many private cloud uses.

### [Fedora CoreOS](https://getfedora.org/en/coreos/)

Fedora CoreOS is an automatically updating, minimal, container-focused operating system.

### [Red Hat Enterprise Linux (RHEL)](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux) | [Red Hat](https://access.redhat.com/)

### [CentOS Linux](https://www.centos.org/) | [What is CentOS Linux?](https://wiki.centos.org/FrontPage)

Download CentOS 7 - x86_64:
- [Minimal](http://mirror.navercorp.com/centos/7.9.2009/isos/x86_64/CentOS-7-x86_64-Minimal-2009.iso)
- [DVD](http://mirror.navercorp.com/centos/7.9.2009/isos/x86_64/CentOS-7-x86_64-DVD-2009.iso)

### [Rocky Linux](https://rockylinux.org/)

Rocky Linux is an open-source enterprise operating system designed to be 100% bug-for-bug compatible with Red Hat Enterprise Linux. It is under intensive development by the community.

Download Rocky 8 - x86_64:
- [Minimal](https://download.rockylinux.org/pub/rocky/8/isos/x86_64/Rocky-8.7-x86_64-minimal.iso)
- [DVD](https://download.rockylinux.org/pub/rocky/8/isos/x86_64/Rocky-8.7-x86_64-dvd1.iso)

[Migrate CentOS Linux to Rocky Linux](https://www.lesstif.com/lpt/centos-8-rocky-linux-migration-113346015.html)

### [OpenWrt](https://openwrt.org/) - Router Platform

### Ubuntu Server vs. Desktop | [Blog](https://www.makeuseof.com/tag/difference-ubuntu-desktop-ubuntu-server/) | [Blog](https://linuxhint.com/ubuntu-desktop-ubuntu-server-difference/) | [Blog (KR)](https://developer-kus.tistory.com/33#:~:text=ubuntu%20%EB%8D%B0%EC%8A%A4%ED%81%AC%ED%83%91%EA%B3%BC%20%EC%84%9C%EB%B2%84%20%EC%BB%A4%EB%84%90%EC%9D%98%20%EC%B0%A8%EC%9D%B4%EC%A0%90%EC%9D%80%3F&text=%EA%B2%B0%EB%A1%A0%EC%9D%80%20GUI%EA%B0%80%20%EC%9E%88%EB%83%90,%EC%84%A4%EC%B9%98%ED%95%B4%EB%8F%84%20%EC%A2%8B%EC%9D%84%20%EA%B2%83%20%EA%B0%99%EB%8B%A4.) | [Blog (KR)](https://www.morenice.kr/119)

- Desktop includes a graphical user interface (GUI), Server does not.
  - Most Servers run headless
- Server can run as an email server, file server, web server, and Samba server. While Desktop applications are geared towards use on the host machine. 
  - Server packages concentrate on establishing connectivity with clients and security

`Other parts of the "Linux" have been moved to the "Linux" page.`

### [CRUX](https://crux.nu/)

CRUX is a lightweight Linux distribution for the x86-64 architecture targeted at experienced Linux users. The primary focus of this distribution is keep it simple, which is reflected in a straightforward tar.gz-based package system, BSD-style initscripts, and a relatively small collection of trimmed packages. The secondary focus is utilization of new Linux features and recent tools and libraries. CRUX also has a ports system which makes it easy to install and upgrade applications.

### [Arch Linux](https://archlinux.org/) | [Wiki](https://wiki.archlinux.org/title/Arch_Linux)

Arch Linux is an independently developed, x86-64 general-purpose GNU/Linux distribution that strives to provide the latest stable versions of most software by following a rolling-release model. The default installation is a minimal base system, configured by the user to only add what is purposely required.

Principles: 1. Simplicity, 2. Modernity, 3. Pragmatism, 4. User centrality, 5. Versatility

### Ubuntu vs. CentOS | [Blog (KR)](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=changfen15&logNo=221414926213) | [Blog (KR)](https://coconuts.tistory.com/175) | [Blog (KR)](https://velog.io/@imok-_/CentOS%EC%99%80-Ubuntu-%EC%B0%A8%EC%9D%B4)

패키지 수:
- Ubuntu가 desktop 환경의 유틸, 오피스 및 게임이 많다.
  - 동일 하드웨어일 때 성능이 낮다.
- CentOS는 웹 호스팅 툴이 더 많다.

배포 및 지원:
- CentOS의 업데이트가 길어 안정적이다.
- Ubuntu의 업데이트가 잦아 불안정해 버그가 발생할 확률이 더 높다.
  - Out of date가 되기 쉽다.

보안:
- CentOS의 패키지가 적어 보안 취약점이 적다.

### Ubuntu vs. Rocky Linux | [Blog (KR)](https://tech.osci.kr/2022/07/05/centos%EC%9D%98-%ED%96%A5%ED%9B%84-%EB%8C%80%EC%95%88-rocky-linux%EC%99%80-ubuntu/)

### CentOS vs. Fedora | [Blog](https://www.openlogic.com/blog/centos-vs-fedora)

Since CentOS is a downstream recomplilation of RHEL, the relation to Fedora is the same as with RHEL. This changed with the introdution of CentOS Steam. CentOS major version releases can lag behind HREL by a couple of months, but security patches and bugfixes are generally released within a day or so of them being released for RHEL. CentOS Stream is ahead of RHEL, but behind Fedora. So new packages get introduced into Fedora, make their way to CentOS Stream, then to RHEL.

### CentOS Stream vs. Fedora | [Blog](https://www.openlogic.com/blog/centos-vs-fedora)

Red Hat released CentOS Stream, which is a rolling distribution. It gets updates continuously, rather than in batches like the point releases fo RHEL. Fedora is ahead of CentOS Stream though, so it will have newer packages with perhaps more bugs than CentOS Stream.

### [Usage statistics of Linux for websites](https://w3techs.com/technologies/details/os-linux)

Percentage of websites using Linux (W3Techs.com, 13 December 2022):
- Unix: 80.4%
- Linux: 38.1%

Subcategories of Linux (W3Techs.com, 13 December 2022):
- Ubuntu: 32.8%
- Debian 16.6%
- CentOS: 8.7%
- Red Hat: 0.8%

실제 enterprise server에서 사용하는 서버는 다를 수 있다. 상용, 비상용(개인용) 구분이 없는 경우, 안정성보다 사용성을 우선시한다.

---

## :computer: Macintosh | macOS

`This part has moved to the 'macOS' page`

---

## :tv: Main Frame | [z/OS](https://www.ibm.com/it-infrastructure/z/zos)

---

### OpenVMS | [WiKi](https://en.wikipedia.org/wiki/OpenVMS)

---

## :floppy_disk: Embedded System | Firmware | RTOS | OS

### [Yocto Project (YP)](https://www.yoctoproject.org/)

요약: 임베디드 시스템을 구성하는 툴, 지원하는 하드웨어/회사가 많고 커스터 마이징이 자유롭지만, 사용하기 상대적으로 까다롭다.

THE YOCTO PROJECT.  IT'S NOT AN EMBEDDED LINUX DISTRIBUTION, IT CREATES A CUSTOM ONE FOR YOU.

The Yocto Project (YP) is an open source collaboration project that helps developers create custom Linux-based systems regardless of the hardware architecture. 

The project provides a flexible set of tools and a space where embedded developers worldwide can share technologies, software stacks, configurations, and best practices that can be used to create tailored Linux images for embedded and IOT devices, or anywhere a customized Linux OS is needed.

### [Buildroot](https://buildroot.org/)

요약: 임베디드 리눅스 시스템을 구성하는 툴, 사용하기 쉽고 간단하지만, 커스터 마이징과 지원하는 하드웨어/회사가 상대적으로 적다.

Buildroot is a simple, efficient and easy-to-use tool to generate embedded Linux systems through cross-compilation.

---

## :iphone: Mobile | Internet of Things (IoT) | [ubidots](https://ubidots.com/blog/iot-operating-systems/)

### [Android](https://developer.android.com/)

`Other parts of 'Android' moved to 'Mobile' Page.`

### [Tizen](https://www.tizen.org/) | [Samsung Electronics Smart TV (KR)](https://news.samsung.com/kr/%EC%9D%B8%ED%8F%AC%EA%B7%B8%EB%9E%98%ED%94%BD-%EC%82%BC%EC%84%B1-%EC%8A%A4%EB%A7%88%ED%8A%B8tv%EC%9A%A9-%ED%83%80%EC%9D%B4%EC%A0%A0-os%EC%9D%98-%EC%97%AC%EC%84%AF-%EA%B0%80%EC%A7%80-%EC%9E%A5)

`Other parts of 'Tizen' moved to 'Mobile' Page.`

### [webOS Open Source Edition (OSE)](https://www.webosose.org/) | [LG Electronics Smart TV (KR)](https://live.lge.co.kr/life-style-webos/)

`Other parts of 'webOS' moved to 'Mobile' Page.`

|IoT OS|Features|Use cases|
|:-|:-:|-:|
|Contiki NG|Open-source, free|Networked memory-constrained systems|
|FreeRTOS|Open-source, free, uses AWS IoT Core|Devices with tiny amounts of memory|
|Mbed OS|ARM-based, high-grade security|For portable code|
|MicroPython|Uses standard Python, easy to learn, C++|Rapid deployment|
|Embedded Linux|Linux kernel, free|Versatile - can be used for various use cases|
|RIOT|Open-source, full multithreading|Can be run as MacOS process|
|TinyOS|C language, open-source|Portability across similar devices|
|Windows 10 IoT|Proprietary, high-grade security|Ideal for heavy-duty industrial use cases|
|OpenWrt|Open-source, Linux-based|Primarily used in routers|

### [Contiki-NG](https://www.contiki-ng.org/)

### [FreeRTOS](https://www.freertos.org/)

### [Mbed OS](https://os.mbed.com/mbed-os/)

### [MicroPython](https://micropython.org/)

MicroPython is a lean and efficient implementation of the Python 3 programming language that includes a small subset of the Python standard library and is optimised to run on microcontrollers and in constrained environments.

The MicroPython pyboard is a compact electronic circuit board that runs MicroPython on the bare metal, giving you a low-level Python operating system that can be used to control all kinds of electronic projects.

MicroPython is packed full of advanced features such as an interactive prompt, arbitrary precision integers, closures, list comprehension, generators, exception handling and more. Yet it is compact enough to fit and run within just 256k of code space and 16k of RAM.

MicroPython aims to be as compatible with normal Python as possible to allow you to transfer code with ease from the desktop to a microcontroller or embedded system.

### [TinyOS](http://www.tinyos.net/)

TinyOS is an open source, BSD-licensed operating system designed for low-power wireless devices, such as those used in sensor networks, ubiquitous computing, personal area networks, smart buildings, and smart meters. A worldwide community from academia and industry use, develop, and support the operating system as well as its associated tools, averaging 35,000 downloads a year.

### [RIOT](https://www.riot-os.org/)

RIOT powers the Internet of Things like Linux powers the Internet. RIOT is a free, open source operating system developed by a grassroots community gathering companies, academia, and hobbyists, distributed all around the world.

RIOT supports most low-power IoT devices, microcontroller architectures (32-bit, 16-bit, 8-bit), and external devices. RIOT aims to implement all relevant open standards supporting an Internet of Things that is connected, secure, durable & privacy-friendly.

### Ubuntu Core

- Characteristic
  - Boards: x86, ARM(Raspberry PI, NXP, Xilinx, Qualcomm, and more)
  - Apps: app embedding, strict application isolation for security, tamper-proof containerisation, automatic over-the-ar (OTA) updates
  - App store: private branded IoT app store, secured, hosted and managed, global CDN for software delivery, CI/CD pipeline integration
  - Software updates: Choose suitable update frequency, Automatic roll-backs on failure, Metered billing, Single secure source of updates
  - Service: knowledge transfer workshops, product trainings, engineering consulting
  - Support: 24/7 tech support - there when you need us! ticket resolution, Long term commercial partnership

- Features
  - Agile containerization: a clean separation between the kernel, OS image and applications.
    - Secure, immutable and strictly confined containerization
    - Consistent, independent, and reliable software updates
    - Architectural flexibility with both Arm and x86 architectures supported
  - OTA updates
    - Transactional updates for reliability
    - Diffs only to minimise network traffic
    - Digital signatures to guarantee integrity and provenance
  - Secure boot: authenticates the boot process by default based on verification of digital signatures
    - Each component in the boot sequence cryptographicaly validates the authenticity of the subsequent component in the boot sequence.
    - Every component is measured, before it is loaded in the runtime memory space
    - If an improper or unsigned component is detected, the boot process is stopped
    - Supports for both hardware and software Root of Trust
  - Full disk encryption: digital signatures to cryptographically ensure data integrity with:
    - Disks are locked with private key based cryptography
    - Private keys for hardware, TPM and other secure layers are securely stored
    - Symmetric key encryption enabled by use of specialised software-enabled stores
  - Recovery mode
    - A graphical user interface to manage recovery options
    - Snapshots of configuration settings and software bills of materials are backed up in the recovery system
  - Validation sets
  - Remodelling: brand, model. IoT App Store ID, or version
    - Enable resellers to rebrand devices
    - Easy migration path between UC20 and UC22

### Fedora IoT

- Characteristic
  - Containerized applications
  - Reliable operating system
    - OSTree technology to provide an immutable operating system with atomic updates
    - greenboot health check framework for systemd, administractors can ensure the system boots into the expected state.
  - Security in mind
    - TPM2, SecureBoot, and automated storage decryption with Clevis
  - Web-based provisioning 
  - Multiple architecture support
    - x86_64, aarch64, and armhfp processors

---

## :closed_lock_with_key: Immutable Operating System - high secure & easy to manage | [TheNewStack](https://thenewstack.io/3-immutable-operating-systems-bottlerocket-flatcar-and-talos-linux/) | [Blog](https://fadingeek.medium.com/immutable-operating-systems-a-new-trend-56edf3e162cf)

Immutable operating systems have a lot of advantages. They are inherently more secure, because many attacks and exploits depend on writing or changing files. Also, even if an exploit is found, bad actors cannot change the operating system on disk (which in itself will thwart attacks that depend on writing to the filesystem), so a reboot will clear any memory-resident malware and recover back to a non-exploited state.

Immutable systems are also easier to manage and update: the operating system images are not patched or updated but replaced atomically (in one operation that is guaranteed to fully complete or fully fail — no partial upgrades!

### Immutable Linux | [MakeUseOf](https://www.makeuseof.com/vanilla-os-immutable-linux-distro/)

Immutability in Linux distros is a concepth that is becoming increasingly popular in containerized systems. Immutable distros are standardized so that they're the same across every installation.

Immutability increases security; as the core parts of the system like the kernel can't be modified, it's theoretically impossible for a malicious program to mess with it. Additional packages are installed in a separate area from the main system.

Immutable systems are al

### Vanilla OS | [MakeUseOf](https://www.makeuseof.com/vanilla-os-immutable-linux-distro/)

Vanilla OS ia a Linux distribution that aims for higher security than other desktop Linux distros. It's built on Ubuntu but adds a twist: the core system files are immutable. This means that it's locked down from changes that third-party programs might make.

---

<img width="462" alt="Screenshot 2022-12-28 at 9 11 19 AM" src="https://user-images.githubusercontent.com/20737479/209738490-b2a08f52-5c1c-4dbf-afa1-083a13e85377.png">

---

### Shebang

[Is space allowed between `#!` and `/binbash` in shebang?](https://unix.stackexchange.com/questions/276751/is-space-allowed-between-and-bin-bash-in-shebang): Yes

---

### Reference
- Program Files, Program Files (x86), https://www.howtogeek.com/129178/why-does-64-bit-windows-need-a-separate-program-files-x86-folder/, 2019-03-21-Thu
- 20세기 맥 OS는 어떤 모습이었을까, https://blog.naver.com/PostView.nhn?blogId=tech-plus&logNo=222046025324, 2020-08-03-Mon.
- Symbolic Link, https://fruitdev.tistory.com/85, 2020-08-05-Wed.
- Unix, https://www.opengroup.org/membership/forums/platform/unix, 2020-08-05-Wed.
- Linux, https://www.linux.org/, 2020-08-05-Wed.
- macOS, https://www.apple.com/macos/catalina/, 2020-008-05-Wed.
- ELF Wiki (Kor), https://ko.wikipedia.org/wiki/ELF_%ED%8C%8C%EC%9D%BC_%ED%98%95%EC%8B%9D, 2020-08-06-Thu.
- EXE Wiki (Kor), https://ko.wikipedia.org/wiki/EXE, 2020-08-06-Thu.
- 실행 파일 Wiki (Kor), https://ko.wikipedia.org/wiki/%EC%8B%A4%ED%96%89_%ED%8C%8C%EC%9D%BC, 2020-08-06-Thu.
- DLL 이란?, https://support.microsoft.com/ko-kr/help/815065/what-is-a-dll, 2020-08-06-Thu.
- DLL, https://goddaehee.tistory.com/185, 2020-08-06-Thu.
- Library, https://jasonjason.tistory.com/15, 2020-08-06-Thu.
- Shortcut, https://ko.wikipedia.org/wiki/%EB%B0%94%EB%A1%9C_%EA%B0%80%EA%B8%B0, 2020-08-08-Sat.
- Alias, https://webdir.tistory.com/107, 2020-08-25-Tue.
- openssh, https://jimnong.tistory.com/713, 2020-09-08-Tue.
- MSDN, https://social.msdn.microsoft.com/forums/en-us/home, 2020-09-16-Wed.
- MSDN Wiki, https://en.wikipedia.org/wiki/Microsoft_Developer_Network, 2020-09-16-Wed.
- Microsoft Docs, https://docs.microsoft.com/en-us/, 2020-09-16-Wed.
- man page Wiki, https://en.wikipedia.org/wiki/Man_page, 2020-09-16-Wed.
- Unix Wiki, https://en.wikipedia.org/wiki/Unix, 2020-09-16-Wed.
- A diagram showing the key Unix and Unix-like operating systems, https://en.wikipedia.org/wiki/Unix#/media/File:Unix_history-simple.svg, 2020-09-16-Wed.
- Linux Wiki, https://en.wikipedia.org/wiki/Linux, 2020-09-16-Wed.
- Windows Wiki, https://en.wikipedia.org/wiki/Microsoft_Windows, 2020-09-16-Wed.
- Differences between Unix and Linux, https://m.blog.naver.com/PostView.nhn?blogId=limoremo&logNo=220533015236&proxyReferer=https:%2F%2Fwww.google.com%2F, 2020-09-16-Wed.
- Linux vs. Unix, https://www.diffen.com/difference/Linux_vs_Unix, 20202-09-16-Wed.
- fuzzy finder Blog Kor, https://black7375.tistory.com/15, 2020-10-12-Mon.
- Solaris Wiki KR-KO, https://ko.wikipedia.org/wiki/%EC%86%94%EB%9D%BC%EB%A6%AC%EC%8A%A4_(%EC%9A%B4%EC%98%81_%EC%B2%B4%EC%A0%9C), 2020-10-29-Thu.
- Solaris Homepage, https://www.oracle.com/solaris/solaris11/, 2020-10-29-Thu.
- Unix history image Wiki KR-KO, https://ko.wikipedia.org/wiki/%EC%9C%A0%EB%8B%89%EC%8A%A4#/media/%ED%8C%8C%EC%9D%BC:Unix_history-simple.svg, 2020-10-29-Thu.
- Linux download, https://www.linux.org/pages/download/, 2020-10-29-Thu.
- Ubuntu, https://ubuntu.com/, 2020-10-29-Thu.
- CentOS, https://wiki.centos.org/FrontPage, 2020-10-29-Thu.
- Debian, https://www.debian.org/, 2020-10-29-Thu.
- Fedora, https://getfedora.org/, 2020-10-29-Thu.
- Mint, https://www.linuxmint.com/, 2020-10-29-Thu.
- Red Hat, https://access.redhat.com/, 2020-10-29-Thu.
- MS-DOS GitHub, https://github.com/Microsoft/MS-DOS, 2020-10-29-Thu.
- BSD Wiki KR-KO, https://ko.wikipedia.org/wiki/BSD, 2020-10-29-Thu.
- 86-DOS Wiki KR-KO, https://ko.wikipedia.org/wiki/86-%EB%8F%84%EC%8A%A4, 2020-10-30-Fri.
- PC-DOS Wiki KR-KO, https://ko.wikipedia.org/wiki/PC-DOS, 2020-10-30-Fri.
- MS-DOS Wiki KR-KO, https://ko.wikipedia.org/wiki/MS-DOS, 2020-10-30-Fri.
- CP/M Wiki KR-KO, https://ko.wikipedia.org/wiki/CP/M, 2020-10-30-Fri.
- CP/M, https://web.archive.org/web/20080515232659/http://www.digitalresearch.biz/CPM.HTM, 2020-10-30-Fri.
- 디스크 운영 체제 Wiki KR-KO, https://ko.wikipedia.org/wiki/%EB%94%94%EC%8A%A4%ED%81%AC_%EC%9A%B4%EC%98%81_%EC%B2%B4%EC%A0%9C 2020-10-30-Fri.
- 도스 Wiki KR-KO, https://ko.wikipedia.org/wiki/%EB%8F%84%EC%8A%A4, 2020-10-30-Fri.
- BIOS Wiki KR-KO, https://ko.wikipedia.org/wiki/%EB%B0%94%EC%9D%B4%EC%98%A4%EC%8A%A4, 2020-11-12-Thu.
- OS Wiki KR-KO, https://ko.wikipedia.org/wiki/%EC%9A%B4%EC%98%81_%EC%B2%B4%EC%A0%9C, 2020-11-12-Thu.
- Firmware Wiki KR-KO, https://ko.wikipedia.org/wiki/%ED%8E%8C%EC%9B%A8%EC%96%B4, 2020-11-12-Thu.
- Bootloader Blog KR-KO, https://m.blog.naver.com/eslectures/80140013119, 2020-11-13-Fri.
- RTOS Blog KR, https://velog.io/@joosing/%EC%89%BD%EA%B2%8C-%EC%9D%B4%ED%95%B4%ED%95%98%EB%8A%94-%EC%8B%A4%EC%8B%9C%EA%B0%84-%EC%9A%B4%EC%98%81%EC%B2%B4%EC%A0%9CRealtime-OS%EC%9D%98-%EA%B0%9C%EB%85%90-vxWorks-realtime-Linux, 2022-07-25-Mon.
- UEFI Wiki KR-KO, https://ko.wikipedia.org/wiki/%ED%86%B5%EC%9D%BC_%ED%99%95%EC%9E%A5_%ED%8E%8C%EC%9B%A8%EC%96%B4_%EC%9D%B8%ED%84%B0%ED%8E%98%EC%9D%B4%EC%8A%A4, 2020-11-13-Fri.
- POSIX Wiki, https://en.wikipedia.org/wiki/POSIX, 2021-03-29-Mon.
- POSIX Wiki KR, https://ko.wikipedia.org/wiki/POSIX, 2021-03-29-Mon.
- Real-Time Operating System MS Docs, https://docs.microsoft.com/en-us/windows/iot/iot-enterprise/soft-real-time/soft-real-time, 2022-06-27-Mon.
- Hard and Soft Real-Time Operating System, https://www.javatpoint.com/hard-and-soft-real-time-operating-system, 2022-07-14-Thu.
- Operating Systems Market Reports, https://w3techs.com/technologies/reportlist/operating_system, 2022-07-21-Thu.
- From Earth to orbit with Linux and SpaceX, https://www.zdnet.com/article/from-earth-to-orbit-with-linux-and-spacex/, 2022-07-25-Mon.
- SpaceX Used Linux To Send NASA Astronauts To International Space Station, https://fossbytes.com/spacex-used-linux-to-send-nasa-astronauts-to-international-space-station/, 2022-07-25-Mon.
- IoT OS, https://ubidots.com/blog/iot-operating-systems/, 2022-07-26-Tue.
- Fedora Workstation, https://getfedora.org/en/workstation/, 2022-07-26-Tue.
- Fedora Server, https://getfedora.org/en/server/, 2022-07-26-Tue.
- Fedora IoT, https://getfedora.org/en/iot/, 2022-07-26-Tue.
- Contiki-NG, https://www.contiki-ng.org/, 2022-07-26-Tue.
- FreeRTOS, https://www.freertos.org/, 2022-07-26-Tue.
- Mbed OS, https://os.mbed.com/mbed-os/, 2022-07-26-Tue.
- MicroPython, https://micropython.org/, 2022-07-26-Tue.
- OpenWrt, https://openwrt.org/, 2022-07-26-Tue.
- TinyOS, http://www.tinyos.net/, 2022-07-26-Tue.
- RIOT, https://www.riot-os.org/, 2022-07-26-Tue.
- Windows IoT, https://developer.microsoft.com/en-us/windows/iot/, 2022-07-26-Tue.
- SmartTV TIZEN Samsung Electronics, https://news.samsung.com/kr/%EC%9D%B8%ED%8F%AC%EA%B7%B8%EB%9E%98%ED%94%BD-%EC%82%BC%EC%84%B1-%EC%8A%A4%EB%A7%88%ED%8A%B8tv%EC%9A%A9-%ED%83%80%EC%9D%B4%EC%A0%A0-os%EC%9D%98-%EC%97%AC%EC%84%AF-%EA%B0%80%EC%A7%80-%EC%9E%A5, 2022-07-26-Tue.
- SmartTV webOS LG Electronics, https://live.lge.co.kr/life-style-webos/, 2022-07-26-Tue.
- Multics, https://multicians.org/multics.html, 2022-07-28-Thu.
- Buildroot, https://buildroot.org/, 2022-08-03-Wed.
- Yocto Project, https://www.yoctoproject.org/, 20222-08-03-Wed.
- IoT Linux Distros, https://techgenix.com/iot-linux-distros/, 2022-08-03-Wed.
- Rocky Linux, https://rockylinux.org/, 2022-08-08-Mon.
- Raspbian, https://www.raspbian.org/, 2022-08-08-Mon.
- Raspberry Pi OS, https://www.raspberrypi.com/software/, 2022-08-08-Mon.
- Android, https://developer.android.com/, 2022-08-08-Mon.
- Ubuntu Server vs. Desktop Blog, https://www.makeuseof.com/tag/difference-ubuntu-desktop-ubuntu-server/, 2022-11-29-Tue.
- Ubuntu Server vs. Desktop Blog, https://linuxhint.com/ubuntu-desktop-ubuntu-server-difference/, 2022-11-29-Tue.
- Ubuntu Server vs. Desktop Blog KR, https://developer-kus.tistory.com/33#:~:text=ubuntu%20%EB%8D%B0%EC%8A%A4%ED%81%AC%ED%83%91%EA%B3%BC%20%EC%84%9C%EB%B2%84%20%EC%BB%A4%EB%84%90%EC%9D%98%20%EC%B0%A8%EC%9D%B4%EC%A0%90%EC%9D%80%3F&text=%EA%B2%B0%EB%A1%A0%EC%9D%80%20GUI%EA%B0%80%20%EC%9E%88%EB%83%90,%EC%84%A4%EC%B9%98%ED%95%B4%EB%8F%84%20%EC%A2%8B%EC%9D%84%20%EA%B2%83%20%EA%B0%99%EB%8B%A4., 2022-11-29-Tue.
- Ubuntu Server vs. Desktop Blog KR, https://www.morenice.kr/119, 2022-11-29-Tue.
- Ubuntu vs. CentOS Blog KR, https://velog.io/@imok-_/CentOS%EC%99%80-Ubuntu-%EC%B0%A8%EC%9D%B4, 2022-11-30-Wed.
- Ubuntu vs. CentOS Blog KR, https://coconuts.tistory.com/175, 2022-11-30-Wed.
- Ubuntu vs. CentOS Blog KR, https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=changfen15&logNo=221414926213, 2022-11-30-Wed.
- Ubuntu vs. Rocky Linux Blog KR, https://tech.osci.kr/2022/07/05/centos%EC%9D%98-%ED%96%A5%ED%9B%84-%EB%8C%80%EC%95%88-rocky-linux%EC%99%80-ubuntu/, 2022-11-30-Wed.
- Download Rocky 8 - x86_64 - Minimal, https://download.rockylinux.org/pub/rocky/8/isos/x86_64/Rocky-8.7-x86_64-minimal.iso, 2022-12-01-Thu.
- Download Rocky 8 - x86_64 - DVD, https://download.rockylinux.org/pub/rocky/8/isos/x86_64/Rocky-8.7-x86_64-dvd1.iso, 2022-12-01-Thu.
- Download CentOS 7 - x86_64 - Minimal, http://mirror.navercorp.com/centos/7.9.2009/isos/x86_64/CentOS-7-x86_64-Minimal-2009.iso, 2022-12-01-Thu.
- Download CentOS 7 - x86_64 - DVD, http://mirror.navercorp.com/centos/7.9.2009/isos/x86_64/CentOS-7-x86_64-DVD-2009.iso, 2022-12-01-Thu.
- Download Fedora 37 Workstation, https://download.fedoraproject.org/pub/fedora/linux/releases/37/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-37-1.7.iso, 2022-12-01-Thu.
- Download Fedora 37 Server, https://download.fedoraproject.org/pub/fedora/linux/releases/37/Server/x86_64/iso/Fedora-Server-dvd-x86_64-37-1.7.iso, 2022-12-01-Thu.
- Migrate CentOS Linux to Rocky Linux, https://www.lesstif.com/lpt/centos-8-rocky-linux-migration-113346015.html, 2022-12-06-Tue.
- Arch Linux, https://archlinux.org/, 2022-12-07-Wed.
- CRUX, https://crux.nu/, 2022-12-07-Wed.
- Fedora Cloud, https://getfedora.org/en/cloud/, 2022-12-07-Wed.
- Fedora CoreOS, https://getfedora.org/en/coreos/, 2022-12-07-Wed.
- CentOS vs. Fedora Blog, https://www.openlogic.com/blog/centos-vs-fedora, 2022-12-07-Wed.
- Usage statistics of Linux for websites, https://w3techs.com/technologies/details/os-linux, 2022-12-13-Tue.
- OpenVMS WiKi, https://en.wikipedia.org/wiki/OpenVMS, 2022-12-27-Tue.
- Immutable OS Blog, https://fadingeek.medium.com/immutable-operating-systems-a-new-trend-56edf3e162cf, 2023-03-24-Fri.
- Vanilla OS MakeUseOf, https://www.makeuseof.com/vanilla-os-immutable-linux-distro/, 2023-03-24-Fri.
- 3 Immutable OS TheNewStack, https://thenewstack.io/3-immutable-operating-systems-bottlerocket-flatcar-and-talos-linux/, 2023-03-24-Fri.
- Tizen, https://www.tizen.org/, 2023-04-25-Tue.
- webOS, https://www.webosose.org/, 2023-04-25-Tue.
- SUSE Linux Wiki, https://en.wikipedia.org/wiki/SUSE_Linux, 2023-05-12-Fri.
- SUSE Linux Enterprise Server, https://www.suse.com/products/server/, 2023-05-12-Fri.
- Arch Linux Wiki, https://wiki.archlinux.org/title/Arch_Linux, 2023-10-11-Wed.
- Allowing Space in Shebang, https://unix.stackexchange.com/questions/276751/is-space-allowed-between-and-bin-bash-in-shebang, 2023-10-18-Wed.
