# Program (Computer Program) | [Wiki](https://en.wikipedia.org/wiki/Computer_program)

```
Other parts of the "Windows" have been moved to "Windows" page.
Other parts of the "Unix" and "Linux" have been moved to "Linux" page.
Other parts of the "Profiling" and the "Profiler" have been moved to "Profiling" page.
Other parts of the "Test" have been moved to "Test" page.
```

A computer program is a collection of instructions that can be executed by a computer to perform a specific task.

A computer program is usually written by a computer programmer in a programming language. From the program in its human-readable form of source code, a compiler or assembler can derive machine code—a form consisting of instructions that the computer can directly execute. Alternatively, a computer program may be executed with the aid of an interpreter.

A collection of computer programs, libraries, and related data are referred to as software. Computer programs may be categorized along functional lines, such as application software and system software. The underlying method used for some calculation or manipulation is known as an algorithm.

Executable file for a task.

## Process | [Wiki (KR)](https://ko.wikipedia.org/wiki/%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4)

프로세스는 실행 중인 프로그램의 인스턴스, 독립적인 개체이다. 운영 체제로부터 하드웨어 자원인 CPU 시간, 주소, 독립된 메모리(code, data, bass, stack, heap)을 할당 받는다. 각 프로세스는 다른 프로세스의 변수, 자료 구조에 접근할 수 없으며, 하기 위해서는 IPC를 사용해야한다.

## Thread | [Wiki (KR)](https://ko.wikipedia.org/wiki/%EC%8A%A4%EB%A0%88%EB%93%9C_(%EC%BB%B4%ED%93%A8%ED%8C%85))

스레드는 프로세스 내에서 실행되는 흐름의 단위이다. 각 스레드는 프로세스 내에서 stack만 따로 할당받고 code, data, heap은 공유한다. 스레드들은 프로세스 내의 주소, 공간 자원들을 공유하면서 실행된다. 각각의 스레드는 별도의 레지스터와 스택을 갖고 있지만 힙 메모리는 공유되어 서로 읽고 쓸 수 있다. 한 스레드가 프로세스의 자원을 수정하면 다른 스레드(sibling thread)로 내용을 즉시 볼 수 있다.

### Multi Processing

멀티 프로세싱이란 하나의 응용 프로그램(application)을 여러 개의 프로세스로 구성하여 각 프로세스가 하나의 작업(task)을 처리하도록 하는 것이다. 여러 개의 자식 프로세스 중 하나에 문제가 발생하면 그 자식 프로세스만 죽는 것 이상으로 영향을 미치지 않는다. Context switching 과정에서 캐쉬 메모리 초기화 등 작업, 시간의 오버헤드가 발생한다. 프로세스는 각 독립된 메모리 영역을 사용하기에 공유하지 않아 context switching이 발생하면 캐쉬에 있는 모든 데이터를 리셋하고 다시 캐쉬 정보를 불러와야 한다. 멀티 프로세싱은 각 각의 프로세스이기에 IPC를 사용해야한다.

### Context Switching

Context switching은 CPU에서 여러 프로세스를 돌아가면서 작업을 처리하는 과정이다. Context switching은 동작 중인 프로세스가 대기를 하면서 해당 프로세스의 상태(context)를 보관하고 대기하고 있던 다음 순서의 프로세스가 동작하면서 이전에 보관했던 프로세스의 상태를 복구하는 작업이다.

### Multi Threading

멀티 스레딩이란 하나의 응용 프로그램을 여러 개의 스레드로 구성하고 각 스레드로 하여금 하나의 작업을 처리하도록 하는 것이다. Windows, Linux 등 많은 운영 체제들이 멀티 프로세싱을 지원하고 있지만 멀티 스레딩을 기본으로 하고 있다. 웹 서버는 대표적인 멀티 스레드 응용 프로그램이다. 장점으로는 시스템 자원 소모 감소(자원의 효율성 증대), 시스템 처리량 증가(처리 비용 감소)으로, 멀티 프로세싱과 비교하면 프로세스를 생성하여 자원을 할당하는 시스템 콜이 줄어들어 자원을 효율적으로 관리할 수 있으며, 프로세스 내의 stack 영역을 제외한 모든 메모리를 공유하기 때문에 스레드 간 데이터를 주고 받는 것이 간단하고 작업량이 작아 context switching이 빠르다. 단점으로는 주의 깊은 설계가 필요하고, 디버깅이 까다롭고, 단일 프로세스 시스템의 경우 효과를 기대하기 어렵고, 다른 프로세스에서 스레드를 각각 제어할 수 없고, 멀티 스레드의 경우 자원 공유의 문제가 발생하며(동기화), 하나의 스레드에 문제가 발생하면 전체 프로세스가 영향을 받는다.

### Multi Processing vs. Multi Threading

멀티 프로세스 대신 멀티 스레드를 사용하면, 즉 프로그램을 여러 개 키지 않고 하나의 프로그램 안에서 여러 작업을 수행하면 다음의 장점들이 있다. 자원을 사용하는 것이 효율적이며 처리 비용이 감소하고 응답 시간이 단축된다. 멀티 프로세스로 실행되는 작업을 멀티 스레드로 실행할 경우, 프로세스를 생성하여 자원을 할당하는 시스템 콜이 줄어들어 자원을 효율적으로 관리할 수 있다. 프로세스 간의 context switching 시 단순히 CPU 레지스터 교체뿐만 아니라 CPU와 RAM 사이의 캐쉬 메모리에 대한 데이터까지 초기화되므로 오버헤드가 크다. 즉, 프로세스 간의 전환 속도보다 스레드 간의 전환 속도가 빠르다. 스레드는 프로세스 내의 메모리를 공유하기 때문에 독립적인 프로세스와 달리 스레드 간 데이터를 주고 받는 것이 IPC에 비해 간단하며 시스템 자원 소모가 줄어든다. 단, 스레드 간의 자원 공유는 전역 변수(data segment)를 이용하므로 함께 사용할 때 충돌이 발생할 수 있다.

### Parent Process | [Wiki](https://en.wikipedia.org/wiki/Parent_process)

A parent process is a process that has created one or more child process. In Unix-like operating systems, every process except process 0 (the swapper) is crated when another process executes the fork() system call. The process that invoked fork is the parent process and the newly crated process is the child process. Every process (except process 0) has one parent process, but can have many child processes. The operating system kernel identifies each process by its process identifier. Process 0 is a special process that is created when the system boots; after forking a child process (process 1), process 0 becomes the swapper process (sometimes also known as the idle task). Process 1, known as init, is the ancestor of every other process in the system. In the Linux kernel, in which there is a very slim difference between processes and POSIX threads, there are two kinds of parent processes, namely real parent and parent. Parent is the process that receives the SIGCHLD signal on child's termination, whereas real parent is the thread that actually created this child process in a multithreaded environment. For a normal process, both these two values are same, but for a POSIX thread which acts as a process, these two values may be different.

### Zombie Processes

The operating system maintains a table that associates every process, by means of its process identifier (pid) to the data necessary for its functioning. During a process's lifetime, such data might include memory segments designated to the process, the arguements it's been invoked with, environment variables, counters about resource usage, user-id, group-id and group set, and maybe other types of information. When a process terminates its execution, either by calling exit or by receiving a signal that causes it to terminate abruptly, the operating system releases most of the resources and information related to that process, but still keeps the data about resource utilization and the termination status code, because a parent process might be interested in knowing if that child executed successfully and the amount of system resources it consumed during its execution. By default, the system assumes that the parent process is indeed interested insuch information at the time of the cihld's termination, and thus sends the parent the signal SIGCHLD to alert that there is some data about a child to be collected. Such collection is done by calling a function of the wait family )either wait itself or one of its relatives, such as waitpid, waitid or wait4). As soon as this collection is made, the system releases those last bits of information about the cihld process and removes its pid from the process table. However, if the parent process lingers in collecting the child's data (or fails to do it at all), the system has no option but keep the child's pid and termination data in the process table indefinitely. Such a terminated process whose data has not been collected is called a zombie process, or simply a zombie, in the UNIX parlance. Zombie processes might pose problems on systems with limited resources or that have limited-size process tables, as the creation of new, active processes might be prevented by the lack or resources still used by long lasting zombies.

### Orphan Processes | [Wiki](https://en.wikipedia.org/wiki/Orphan_process)

An Orphan Process is a computer process whose parent process has finished or terminated, thought it remains running itself.

### Redistributable (재배포)

프로그램을 재배포 해도 된다는 뜻이다. 예로 상업적인 마이크로소프트의 오피스 2019, 365는 재배포가 불가하다.

### Online Install

설치 시 인터넷에 연결해서 필요한 파일을 다운받아서 설치한다.

### Office Install

설치 파일에 필요한 모든 파일이 같이 있어서 오프라인으로 설치한다.

### Call stack | [WiKi](https://en.wikipedia.org/wiki/Call_stack)

A call stack in computer science is a stack data structure that stores infomation about the active subroutines of a computer program. This kind of stack is also known as an execution stack, program stack, control stack, run-time stack, or machine stack, and is often shortened to just "the stack". Althought maintenance of the call stack is immportant for the porper functioning of most software, the details are normally hidden and automatic in high-level programming languages. Many computer instruction sets provide special instructions for manipulating stacks.

A call stack is used for several related purposes, but the main reason for having one is to keep track of the point to which each active subroutine should return control when it finishes executing. An active subroutine is one that has been called, but is yet to complete execution, after which control should be handed back to the point of call. Such activations of subroutines may be nested to any level (recursive as a special case), hence the stack structure. For example, if a subroutine DrawSquare calls a subroutine DrawLine from four different places, DrawLine must know where to return when its execution completes. To accomplish this, the address following the instruction that jumps to DrawLine, the return address, is pushed onto the top of the call stack with each call.

### Instruction* | [Wiki](https://en.wikipedia.org/wiki/Instruction)

Instruction, one operation of a processor within a computer architecture instruction set

### Instruction Set Architecture (ISA) | [Wiki](https://en.wikipedia.org/wiki/Instruction_set_architecture) 

An instruction set architecture (ISA) in computer science is an abstract model of a computer. It is also referred to as architecture or computer architecture. A realization of an ISA, such as a central processing unit (CPU), is called an implementation.

In general, an ISA defines the supported data types, the registers, the hardware support for managing main memory, fundamental features (such as the memory consistency, addressing modes, virtual memory), and the input/output model of a family of implementations of the ISA.

An ISA specifies the behavior of machine code running on implementations of that ISA in a fashion that does not depend on the characteristics of that implementation, providing binary compatibility between implementations. This enables multiple implementations of an ISA that differ in performance, physical size, and monetary cost (among other things), but that are capable of running the same machine code, so that a lower-performance, lower-cost machine can be replaced with a higher-cost, higher-performance machine without having to replace software. It also enables the evolution of the microarchitectures of the implementations of that ISA, so that a newer, higher-performance implementation of an ISA can run software that runs on previous generations of implementations.

If an operating system maintains a standard and compatible application binary interface (ABI) for a particular ISA, machine code for that ISA and operating system will run on future implementations of that ISA and newer versions of that operating system. However, if an ISA supports running multiple operating systems, it does not guarantee that machine code for one operating system will run on another operating system, unless the first operating system supports running machine code built for the other operating system.

An ISA can be extended by adding instructions or other capabilities, or adding support for larger addresses and data values; an implementation of the extended ISA will still be able to execute machine code for versions of the ISA without those extensions. Machine code using those extensions will only run on implementations that support those extensions.

The binary compatibility that they provide make ISAs one of the most fundamental abstractions in computing.

### Inter-Process Communication (IPC) | [Wiki (KR)](https://ko.wikipedia.org/wiki/%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4_%EA%B0%84_%ED%86%B5%EC%8B%A0)

프로세스 간 통신이란 프로세스들 사이에 서로 데이터를 주고받는 행위 또는 그에 대한 방법이나 경로를 뜻한다. IPC는 마이크로커널과 나노커널의 디자인 프로세스에 매우 중요하다. 마이크로커널은 커널이 제공하는 기능의 수를 줄였기 때문이다. 해당 기능들은 IPC를 통해 서버와 통신함으로써 얻으며 일반적인 모놀리딕 커널에 비해 IPC의 수가 극적으로 증가된다.

주요 IPC 방식으로는 파일(대부분), 신호(대부분. Windows와 같은 일부 시스템은 C 런타임 라이브러리에서만 신호를 제공하며 IPC 방식으로 사용하는 것을 지원하지는 않음), 소켓(대부분), 메시지 큐(대부분), 파이프(모든 POSIX, Windows), 지명 파이프(모든 POSIX, Windows), 세미포어(모든 POSIX, Windows), 공유 메모리(모든 POSIX, Windows), 메서지 전달(비공유(MPI 패러다임, 자바 RMI, CORBA, MSMQ, 메일슬롯, QNX 등)), 메모리 맵 파일(모든 POSIX, Windows)이 있다.

### Remote Procedure Call (RPC) | [Wiki (KR)](https://ko.wikipedia.org/wiki/%EC%9B%90%EA%B2%A9_%ED%94%84%EB%A1%9C%EC%8B%9C%EC%A0%80_%ED%98%B8%EC%B6%9C)

원격 프로시저 호출은 별도의 원격 제어를 위한 코딩 없이 다른 주소 공간에서 함수나 프로시저를 실행할 수 있게 하는 프로세스 간 통신 기술이다. RPC을 이용하면 프로그래머는 함수가 실행 프로그램에 로컬 위치에 있든 원격 위치에 있든 동일한 코드를 이용할 수 있다. 객체 지향의 원칙을 사용하는 소프트웨어의 경우 RPC를 원격 호출(remote invocation) 또는 원격 메소드 호출(remote method invocation)이라고 일컫는다. 가끔 ONC RPC와 DCE/RPC와 같은 비호환 대상을 수행하기 위해 쓰이는 다른 수많은 기술이 있다.

### Daemon | [Wiki (KR)](https://ko.wikipedia.org/wiki/%EB%8D%B0%EB%AA%AC_(%EC%BB%B4%ED%93%A8%ED%8C%85))

데몬은 멀티태스킹 운영 체제에서 사용자가 직접적으로 제어하지 않고 백그라운드에서 돌면서 여러 작업을 하는 프로그램을 말한다. 시스템 로그를 남기는 `syslogd`처럼 데몬을 뜻하는 d를 이름 끝에 달고 있으며, 일반적으로 프로세스로 실행된다. 데몬은 대개 부모 프로세스를 갖지 않아 PPID가 1이며, 프로세스 트리에서 init 바로 아래에 위치한다. 데몬이 되는 방법은 일반적으로 자식 프로세스를 포크하여 생성하고 자식을 분기한 자신을 죽이면서 init이 고아가 된 자식 프로세스를 자기 밑으로 데려가도록 하는 방식이다. 이러한 방식을 "fork off and die"라 부르기도 한다. 시스템은 시동할 때 데몬을 시작하는 경우가 많으며, 이런 데몬들은 네트워크 요청, 하드웨어 동작, 여타 프로그램에 반응하는 기능을 담당하게 된다. 그 밖에도 몇몇 리눅스에 있는 devfsd처럼 하드웨어 설정이나, cron처럼 주기적인 작업을 실행하는 등 기타 다양한 목적으로 사용된다.

도깨비나 유령을 뜻하는 데몬이란 이름은 MIT의 MAC 프로젝트 프로그래머들이 만든 것이다. 처음 만들어질 때는 맥스웰의 도깨비 사고 실험에서 맥스웰이 언급한, 보이지 않는 곳에서 분자들을 골라주는 일을 하고 있는 유령에서 영감을 얻은 것이다. 이후 유닉스 시스템은 이 용어를 받아들여 사용했다. 그리스 신화에서도 신들이 관여하지 않는 일을 처리하는 데몬이 등장하는데, 이는 사용자가 직접 신경쓰지 않도록 하면서 백그라운드에서 일을 처리해주는 데몬의 역할과 맞아 떨어진다. BSD 계열의 운영 체제는 BSD 데몬을 마스코트 삼았으나, 실제로 BSD의 마스코트는 기독교적 세계에세 그리는 악마의 모습을 귀였게 만든 것이다. 또한 원래 DAEMON은 두문자어가 아니지만 "Disk And Execution MONitor"로 두문자어처럼 뜻을 맞추어 말하기도 한다.

### Refactoring

동작을 바꾸지 않으면서 구조를 개선하는 방법이다. 코드가 작성된 이후 디자인을 개선하는 작업이다. 값이 수정되지 않는 변수는 parameter로 넘길 수 있다. 값이 수정되는 변수는 함수로 추출하여 리턴 값으로 돌려줄 수 있다.

### Desktop Bus (D-BUS) | [Wiki (KR)](https://ko.wikipedia.org/wiki/D-Bus)

컴퓨터에서 D-Bus는 같은 머신에서 동시에 실행 중인 여러 컴퓨터 프로그램(프로세스) 간의 통신을 가능케하는 소프트웨어 버스, 프로세스 간 통신(IPC), 원격 프로시저 호출(RPC) 매커니즘이다. D-Bus는 레드햇의 하복 페닝튼이 그놈, KDE 등의 리눅스 데스크탑 환경이 제공하는 서비스들을 표준화하기 위해 발의된 Freedesktop.org 프로젝트의 일부로서 개발되었다. Freedesktop.org 프로젝트는 이 사양의 참조 구현체로서 libdbus라는 이름의 자유-오픈 소스 라이브러리를 개발하였다. 이 라이브러리는 D-Bus와는 구별된다. 실제로 다른 구현체의 D-Bus 클라이언트 라이브러리도 존재한다. GDBus(GNOME), QtDBUS(Qt/KDE), dbus-java, sd-bus(systemd의 일부) 등이 있다.

### Clipboard | [Wiki (KR)](https://ko.wikipedia.org/wiki/%ED%81%B4%EB%A6%BD%EB%B3%B4%EB%93%9C)

클립보드(종이 끼우개)는 잘라내서 붙여넣는 과정을 통해 문서나 응용 프로그램 사이에 자료가 전송될 때 짧은 시간 동안 해당 자료를 저장하는 데에 사용되는 소프트웨어 프로그램이다. 보통 그래픽 사용자 인터페이스 환경의 일부이며 환경 안에 있는 대부분의 프로그램으로부터 접근할 수 있는 임시 메모리 블록과 동의어이다.

Windows의 일부 버전은 클립보드 뷰어(XP/2000에서는 클립북 뷰어) 응용 프로그램(Clipbrd.exe)을 사용하여 클립보드의 내용을 언제든지 볼 수 있게 되어 있다. 더 오래된 윈도우 버전에서는 메모장이나 워드패드 편집기의 복사본을 열어서 붙여 넣으면서 알아 볼 수 있다. 이러한 기능은 "편집" 메뉴의 복사, 잘라내기, 붙여넣기 등의 하부 메뉴를 통해 사용할 수 있다. 데이터를 복사하여 클립보드에 저장: `Control` + `c` 또는 `Control` + `Insert`, 데이터를 잘라내어 클립보드에 저장: `Control` + `x` 또는 `Shift` + `Delete`, 클립보드에 저장된 데이터를 붙여넣기: `Control` + `v` 또는 `Shift` + `Insert`.

OS X - 맥 운영 체제에서 파인더의 편집 메뉴로부터 클립보드 보기 메뉴 항목을 선택함으로써 내용을 볼 수 있다. 데이터를 복사하여 클립보드에 저장: `Command` + `c`, 데이터를 잘라내어 클립보드에 저장: `Command` + `x`, 클립보드에 저장된 데이터를 붙여넣기: `Command` + `v`.

X Window System는 Unix, Linux 시스템에서 사용되며 selection을 통해 클립보드를 제공한다. selection은 비동기적이므로 데이터는 사용자가 원할 때에만 복사되고 원하는 형태로 변환된다.

### Patch | [Wiki (KR)](https://ko.wikipedia.org/wiki/%ED%8C%A8%EC%B9%98_(%EC%BB%B4%ED%93%A8%ED%8C%85))

패치는 수정 또는 개선을 위해 컴퓨터 프로그램이나 지원 데이터를 업데이트하도록 설계된 일종의 소프트웨어이다. 즉, 일반적으로 이미 발표된 소프트웨어 제품에서 발견된 사소한 기능 개선 또는 버그나 오류 등을 수정하기 위해 개발자/회사가 내놓는 업데이트 프로그램을 지칭한다. 설치 프로그램과 비슷한 형식으로 기존에 설치된 프로그램을 자동으로 검색하여 필요한 내용을 바꿔주는 형태가 일반적이다. 보안 취약점 및 기타 버그의 수정을 포함하는데 이러한 패치는 버그픽스라고 하며 사용성과 성능을 개선한다.

### [Application Programming Interface (API)](https://www.redhat.com/en/topics/api/what-are-application-programming-interfaces) | [Wiki (KR)](https://ko.wikipedia.org/wiki/API)

API는 application에서 사용할 수 있도록 OS나 programming language가 제공하는 기능을 제어할 수 있도록 만든 interface를 뜻한다. 주로 파일 제어, 창 제어, 화상 처리, 문자 제어 등을 위한 interface를 제공한다.

API stands for application programing interface, which is a set of definitions and protocols for building and integrating application software.

### Open Audio Library (OpenAL) | [Wiki (KR)](https://ko.wikipedia.org/wiki/OpenAL)

OpenAL은 2000년 로키 소프트웨어에서 Windows 게임을 Linux로 porting을 쉽게 하기 위해 만든 자유 소프트웨어 cross-platform audio API이다. 다중 채널 3차원 오디오 출력을 효율적으로 구현해내기 위해 설계되었다.

### Open Computing Language (OpenCL) | [Wiki (KR)](https://ko.wikipedia.org/wiki/OpenCL)

OpenCL은 애플이 최초로 개발한 개방형 범용 병렬 컴퓨팅 framework이다. AMD, Intel, Nvidia 등과 함께 문서를 다듬어 최초 제아서를 크로노스 그룹에 제출하여 2008년 6월 16일 Khronos Compute Working Group이 만들어졌다. CPU, GPU, DSP 등의 processor로 이루어진 이종 플랫폼에서 실행되는 프로그램을 작성할 수 있게 해준다. OpenCL은 kernel code를 작성하기 위한 C99 기반의 언어인 OpenCL C와 platform을 정희가ㅗ 제어하기 위한 API를 포함하고 있다. OpenCL은 task-based 및 data-based 병렬 컴퓨팅을 제공한다. 비영리 기술 컨소시엄인 크로노스 그룸에서 관리하고 있다.

### Open Graphics Library (OpenGL) | [Wiki (KR)](https://ko.wikipedia.org/wiki/OpenGL)

OpenGL은 1992년 실리콘 그래픽스에서 만든 2차원 및 3차원 그래픽스 표준 API 규격이다. Programming language, platform 간의 cross-platform programming을 지원한다. Microsoft의 Direct3D와 함께 컴퓨터 그래픽 세계를 양분하고 있다. Direct3D와는 달리, 표준안이 여러 관련 업체의 토론과 제안으로 이루어지기에 버전 업데이트는 느린 편이다. 현재 비영리 기술 컨소시엄인 크로노스 그룹에 의하여 관리되고 있다.

### Interface | [WiKi (KR)](https://ko.wikipedia.org/wiki/인터페이스_(컴퓨팅))

Interface는 서로 다른 2개의 system, device 사이에서 정보나 신호를 주고 받는 경우의 접점이나 경계면이다. 즉, 사용자가 기기를 쉽게 동작시키는데 도움을 주는 시스템을 의미한다. 컴퓨팅에서 컴퓨터 시스템끼리 정보를 교환하는 공유 경계이다. 이러한 교환은 software, hardware, 주변기기, user 간에 이루어질 수 있으며, 서로 복합적으로 이루어질 수도 있다. 터치스크린과 같은 일부 컴퓨터 하드웨어 장치들은 interface를 통해 데이터를 송수신할 수 있으며 마우스나 마이크로폰과 같은 장치들은 오직 시스템에 데이터를 전송만 하는 interface를 제공한다.

---

## Design Pattern

### Factory Pattern

### Observer Pattern

---

### Ad hoc | [Wiki (KR)](https://ko.wikipedia.org/wiki/%EC%95%A0%EB%93%9C%ED%98%B9)

Ad hoc(애드 혹)은 "이것을 위해" 즉 "특별한 목적을 위해서"라는 뜻의 라틴어로, 일반적으로 1. 특정한 문제나 일을 위해 만들어진 관습적인 해결책, 2. 일반화할 수 없는 해결책, 3. 어떤 다른 목적에 적응시킬 수 없는 해결책을 나타낸다.

### Distribution vs. Release | [Stackoverflow](https://stackoverflow.com/questions/8380570/whats-the-difference-between-distribution-and-release-build-configurations)

It depends on the programmer and the build settings they want to put into each target. For one programmer, Release is an ADHOC and Distribution is a store build. Also opposite case can be happened.

## Execution | [Wiki](https://en.wikipedia.org/wiki/Execution_(computing))

Keywords: code, translation, compiler, compile-time, optimizing compiler, intermediate representation (IR), execution, runtime system, runtime, executable, interpreter, virtual machine, source code, object code, bytecode, machine code, microcode, compilation strategies, just-in-time (JIT), tracing just-in-time, ahead-of-time (AOT), transcompilation, recompilation, notable runtimes, android runtime (ART), common language runtime (CLR) & Mono, crt0, HHVM, Java virtual machine (JVM), objective-c, v8, node.js, zend engine, notable compilers & toolchains, GNU compiler collection (GCC), LLVM, Clang

### Difference Between Packing and Packaging | [QnA](https://keydifferences.com/difference-between-packing-and-packaging.html)
While packing is more about protection, the packaging is focuses on the design and appearance of the product which makes it attractive. So, packing implies the act of covering up the item or product, to protect it from any damage, whereas packaging refers to a set of activities, which involves designing a proper cover for the product, which not only stores the product and protects it from any damage, but also attracts customers with its appearance and instigates them to buy it. 

### UI (User Interface) vs. UX (User Experience) | [Blog](https://maze.co/blog/ui-vs-ux/)
UI design is about using typography, images, and other visual design elements to turn a basi interface into something digestible and usable.

A UI designer focuses on how the colors, typography, and images of a design connect to the brand of a product.

UX design is about understanding the overall journey of your users and turning it into a product.

UX as a category is not necessarily tied to websites. Steve Jobs famously included the experience of going to an Apple store as part of UX. Even the location had to be perfect. So how you buy a product, how you first see it - this is all important to UX.

UX starts with a problem and ends with a wireframe or prototype.

The role of a user experience designer is to understand the customer journey. That means understanding the target audience, interviewing customers, defining user flows, and conducting user testing.

### CRUD | [Wiki](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)

Create, read, update and delete (CRUD) are the four basic operations of persistent storage. CRUD is also sometimes used to describe user interface conventions that facilitate viewing, searching, and changing information using computer-based forms and reports. The term was likely first popularized by James Martin in his 1983 book Managing the Data-base environment.

### [XZ Utils](https://tukaani.org/xz/)

XZ Utils is free general-purpose data compression software with a high compression ratio. XZ Utils were written for POSIX-like systems, but also work on some not-so-POSIX systems. XZ Utils are the successor to LZMA Utils.

The core of the XZ Utils compressions code is based on LZMA SDK, but it has been modified quite a lot to be suitable for XZ Utils. The primary compression algorithm is currently LZMA2, which is used inside the .xz container format. With typical files, XZ Utils create 30 % smaller output than gzip and 15 % smaller output than bzip2.

XZ Utils consist of several components:
- liblzma is a compression library with an API similar to that of zlib.
- xz is a command line tool with syntax similar to that of gzip.
- xzdec is a decompression-only tool smaller than the full-featured xz tool.
- A set of shell scripts (xzgrep, xzdiff, etc.) have been adapted from gzip to ease viewing, grepping, and comparing compressed files.
- Emulation of command line tools of LZMA Utils eases transition from LZMA Utils to XZ Utils.

While liblzma has a zlib-like API, liblzma doesn't include any file I/O functions. A separate I/O library is planned, which would abstract handling of .gz, .bz2, and .xz files with an esay to use API.

---

`Deployment, DevOps contents have moved to the 'Development' page.`

---

### Reference
- Instruction, https://kwonsye.github.io/computer%20science/2019/04/14/ca-4.html, 2020-09-14-Mon.
- Call stack Wiki, https://en.wikipedia.org/wiki/Call_stack, 2020-09-18-Fri.
- Instruction Wiki, https://en.wikipedia.org/wiki/Instruction, 2020-09-21-Mon.
- Instruction Set Architecture Wiki, https://en.wikipedia.org/wiki/Instruction_set_architecture, 2020-09-21-Mon.
- Computer Program Wiki, https://en.wikipedia.org/wiki/Computer_program, 2020-09-21-Mon.
- Daemon Wiki KR-KO, https://ko.wikipedia.org/wiki/%EB%8D%B0%EB%AA%AC_(%EC%BB%B4%ED%93%A8%ED%8C%85) 2020-10-30-Fri.
- Refactoring Blog KR-KO, https://nesoy.github.io/articles/2018-05/Refactoring, 2020-11-03-Tue.
- DBus Wiki KR-KO, https://ko.wikipedia.org/wiki/D-Bus, 2020-11-04-Wed.
- IPC Wiki KR-KO, https://ko.wikipedia.org/wiki/%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4_%EA%B0%84_%ED%86%B5%EC%8B%A0, 2020-11-04-Wed.
- RPC Wiki KR-KO, https://ko.wikipedia.org/wiki/%EC%9B%90%EA%B2%A9_%ED%94%84%EB%A1%9C%EC%8B%9C%EC%A0%80_%ED%98%B8%EC%B6%9C, 2020-11-04-Wed.
- Process vs. Thread Blog KR-KO, https://gmlwjd9405.github.io/2018/09/14/process-vs-thread.html, 2020-11-06-Fri.
- Thread Wiki KR-KO, https://ko.wikipedia.org/wiki/%EC%8A%A4%EB%A0%88%EB%93%9C_(%EC%BB%B4%ED%93%A8%ED%8C%85), 2020-11-06-Fri.
- Process Wiki KR-KO, https://ko.wikipedia.org/wiki/%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4, 2020-11-06-Fri.
- Clipboard Wiki KR, https://ko.wikipedia.org/wiki/%ED%81%B4%EB%A6%BD%EB%B3%B4%EB%93%9C, 2021-03-04-Thu.
- Patch Wiki KR, https://ko.wikipedia.org/wiki/%ED%8C%A8%EC%B9%98_(%EC%BB%B4%ED%93%A8%ED%8C%85), 2021-03-04-Thu.
- API Wiki KR, https://ko.wikipedia.org/wiki/API, 2021-03-25-Thu.
- Interface Wiki KR, https://ko.wikipedia.org/wiki/인터페이스_(컴퓨팅), 2021-03-25-Thu.
- OpenAL Wiki KR, https://ko.wikipedia.org/wiki/OpenAL, 2021-03-25-Thu.
- OpenCL Wiki KR, https://ko.wikipedia.org/wiki/OpenCL, 2021-03-25-Thu.
- OpenGL Wiki KR, https://ko.wikipedia.org/wiki/OpenGL, 2021-03-25-Thu.
- Parent Process Wiki, https://en.wikipedia.org/wiki/Parent_process, 2021-03-26-Fri.
- Orphan Process Wiki, https://en.wikipedia.org/wiki/Orphan_process, 2021-03-26-Fri.
- Ad hoc Wiki KR, https://ko.wikipedia.org/wiki/%EC%95%A0%EB%93%9C%ED%98%B9, 2021-04-09-Fri.
- Distribution vs. Release, https://stackoverflow.com/questions/8380570/whats-the-difference-between-distribution-and-release-build-configurations, 2021-04-09-Fri.
- Execution Wiki, https://en.wikipedia.org/wiki/Execution_(computing), 2021-04-29-Thu.
- Difference Between Packing and Packaging, https://keydifferences.com/difference-between-packing-and-packaging.html, 2021-07-01-Thu.
- UI vs. UX Blog, https://maze.co/blog/ui-vs-ux/, 2021-08-18-Wed.
- CRUD Wiki, https://en.wikipedia.org/wiki/Create,_read,_update_and_delete, 2021-08-31-Tue.
- XZ Utils, https://tukaani.org/xz/, 2022-07-20-Wed.
- Unix Daemon Blog KR, https://blogger.pe.kr/770, 2022-09-21-Wed.
- Unix Daemon vs. Windows Service Blog KR, https://hec-ker.tistory.com/323, 2022-09-21-Wed.
- Unix Daemon Python Blog KR, https://oddpoet.net/blog/2013/09/24/python-daemon/, 2022-09-21-Wed.
- Unix Daemon Python Blog KR, http://blog.cloudsys.co.kr/python-daemon-example-install/, 2022-09-21-Wed.
- Windows Service Python Blog KR, https://bitcoder.tistory.com/116, 2022-09-21-Wed.
- API Red Hat, https://www.redhat.com/en/topics/api/what-are-application-programming-interfaces, 2023-11-14-Tue.
