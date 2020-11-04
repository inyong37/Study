# Program

### Redistributable (재배포)
프로그램을 재배포 해도 된다는 뜻이다. 예로 상업적인 마이크로소프트의 오피스 2019, 365는 재배포가 불가하다.

#### Online Install
설치 시 인터넷에 연결해서 필요한 파일을 다운받아서 설치한다.

#### Office Install
설치 파일에 필요한 모든 파일이 같이 있어서 오프라인으로 설치한다.

### Daemon | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/%EB%8D%B0%EB%AA%AC_(%EC%BB%B4%ED%93%A8%ED%8C%85))
데몬은 멀티태스킹 운영 체제에서 사용자가 직접적으로 제어하지 않고 백그라운드에서 돌면서 여러 작업을 하는 프로그램을 말한다. 시스템 로그를 남기는 `syslogd`처럼 데몬을 뜻하는 d를 이름 끝에 달고 있으며, 일반적으로 프로세스로 실행된다. 데몬은 대개 부모 프로세스를 갖지 않아 PPID가 1이며, 프로세스 트리에서 init 바로 아래에 위치한다. 데몬이 되는 방법은 일반적으로 자식 프로세스를 포크하여 생성하고 자식을 분기한 자신을 죽이면서 init이 고아가 된 자식 프로세스를 자기 밑으로 데려가도록 하는 방식이다. 이러한 방식을 "fork off and die"라 부르기도 한다. 시스템은 시동할 때 데몬을 시작하는 경우가 많으며, 이런 데몬들은 네트워크 요청, 하드웨어 동작, 여타 프로그램에 반응하는 기능을 담당하게 된다. 그 밖에도 몇몇 리눅스에 있는 devfsd처럼 하드웨어 설정이나, cron처럼 주기적인 작업을 실행하는 등 기타 다양한 목적으로 사용된다.

도깨비나 유령을 뜻하는 데몬이란 이름은 MIT의 MAC 프로젝트 프로그래머들이 만든 것이다. 처음 만들어질 때는 맥스웰의 도깨비 사고 실험에서 맥스웰이 언급한, 보이지 않는 곳에서 분자들을 골라주는 일을 하고 있는 유령에서 영감을 얻은 것이다. 이후 유닉스 시스템은 이 용어를 받아들여 사용했다. 그리스 신화에서도 신들이 관여하지 않는 일을 처리하는 데몬이 등장하는데, 이는 사용자가 직접 신경쓰지 않도록 하면서 백그라운드에서 일을 처리해주는 데몬의 역할과 맞아 떨어진다. BSD 계열의 운영 체제는 BSD 데몬을 마스코트 삼았으나, 실제로 BSD의 마스코트는 기독교적 세계에세 그리는 악마의 모습을 귀였게 만든 것이다. 또한 원래 DAEMON은 두문자어가 아니지만 "Disk And Execution MONitor"로 두문자어처럼 뜻을 맞추어 말하기도 한다.

### Refactoring
동작을 바꾸지 않으면서 구조를 개선하는 방법이다. 코드가 작성된 이후 디자인을 개선하는 작업이다. 값이 수정되지 않는 변수는 parameter로 넘길 수 있다. 값이 수정되는 변수는 함수로 추출하여 리턴 값으로 돌려줄 수 있다.

### D-Bus: Desktop Bus | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/D-Bus)
컴퓨터에서 D-Bus는 같은 머신에서 동시에 실행 중인 여러 컴퓨터 프로그램(프로세스) 간의 통신을 가능케하는 소프트웨어 버스, 프로세스 간 통신(IPC), 원격 프로시저 호출(RPC) 매커니즘이다. D-Bus는 레드햇의 하복 페닝튼이 그놈, KDE 등의 리눅스 데스크탑 환경이 제공하는 서비스들을 표준화하기 위해 발의된 Freedesktop.org 프로젝트의 일부로서 개발되었다. Freedesktop.org 프로젝트는 이 사양의 참조 구현체로서 libdbus라는 이름의 자유-오픈 소스 라이브러리를 개발하였다. 이 라이브러리는 D-Bus와는 구별된다. 실제로 다른 구현체의 D-Bus 클라이언트 라이브러리도 존재한다. GDBus(GNOME), QtDBUS(Qt/KDE), dbus-java, sd-bus(systemd의 일부) 등이 있다.

```
Other parts of the "Windows" have been moved to "Windows" page.
Other parts of the "Unix" and "Linux" have been moved to "Linux" page.
```

### Hot spot | [Wiki](https://en.wikipedia.org/wiki/Hot_spot_(computer_programming))
A Hot spot in computer science is most usually defined as a region of a program where a high proportion of executed instructions occur or where most time is spent during the program's execution (not necessarily the same thing since some instructions are faster than others).

### Bottleneck | [Wiki](https://en.wikipedia.org/wiki/Bottleneck_(software))
A bottleneck in computer science occurs when the capacity of an application or a computer system is limited by a single component, like the neck of a bottle slowing down the overall water flow. The bottleneck has lowest throughput of all parts of the transaction path.

### Call stack | [Wiki](https://en.wikipedia.org/wiki/Call_stack)
A call stack in computer science is a stack data structure that stores infomation about the active subroutines of a computer program. This kind of stack is also known as an execution stack, program stack, control stack, run-time stack, or machine stack, and is often shortened to just "the stack". Althought maintenance of the call stack is immportant for the porper functioning of most software, the details are normally hidden and automatic in high-level programming languages. Many computer instruction sets provide special instructions for manipulating stacks.

A call stack is used for several related purposes, but the main reason for having one is to keep track of the point to which each active subroutine should return control when it finishes executing. An active subroutine is one that has been called, but is yet to complete execution, after which control should be handed back to the point of call. Such activations of subroutines may be nested to any level (recursive as a special case), hence the stack structure. For example, if a subroutine DrawSquare calls a subroutine DrawLine from four different places, DrawLine must know where to return when its execution completes. To accomplish this, the address following the instruction that jumps to DrawLine, the return address, is pushed onto the top of the call stack with each call.

### Instruction | [Wiki](https://en.wikipedia.org/wiki/Instruction)
Instruction, one operation of a processor within a computer architecture instruction set

### Instruction Set Architecture (ISA) | [Wiki](https://en.wikipedia.org/wiki/Instruction_set_architecture) 
An instruction set architecture (ISA) in computer science is an abstract model of a computer. It is also referred to as architecture or computer architecture. A realization of an ISA, such as a central processing unit (CPU), is called an implementation.

In general, an ISA defines the supported data types, the registers, the hardware support for managing main memory, fundamental features (such as the memory consistency, addressing modes, virtual memory), and the input/output model of a family of implementations of the ISA.

An ISA specifies the behavior of machine code running on implementations of that ISA in a fashion that does not depend on the characteristics of that implementation, providing binary compatibility between implementations. This enables multiple implementations of an ISA that differ in performance, physical size, and monetary cost (among other things), but that are capable of running the same machine code, so that a lower-performance, lower-cost machine can be replaced with a higher-cost, higher-performance machine without having to replace software. It also enables the evolution of the microarchitectures of the implementations of that ISA, so that a newer, higher-performance implementation of an ISA can run software that runs on previous generations of implementations.

If an operating system maintains a standard and compatible application binary interface (ABI) for a particular ISA, machine code for that ISA and operating system will run on future implementations of that ISA and newer versions of that operating system. However, if an ISA supports running multiple operating systems, it does not guarantee that machine code for one operating system will run on another operating system, unless the first operating system supports running machine code built for the other operating system.

An ISA can be extended by adding instructions or other capabilities, or adding support for larger addresses and data values; an implementation of the extended ISA will still be able to execute machine code for versions of the ISA without those extensions. Machine code using those extensions will only run on implementations that support those extensions.

The binary compatibility that they provide make ISAs one of the most fundamental abstractions in computing.

### Computer Program | [Wiki](https://en.wikipedia.org/wiki/Computer_program)
A computer program is a collection of instructions that can be executed by a computer to perform a specific task.

A computer program is usually written by a computer programmer in a programming language. From the program in its human-readable form of source code, a compiler or assembler can derive machine code—a form consisting of instructions that the computer can directly execute. Alternatively, a computer program may be executed with the aid of an interpreter.

A collection of computer programs, libraries, and related data are referred to as software. Computer programs may be categorized along functional lines, such as application software and system software. The underlying method used for some calculation or manipulation is known as an algorithm.

## Profiling | [Wiki](https://en.wikipedia.org/wiki/Profiling_(computer_programming))
문제, 디자인, 코드, 컴파일, 어셈블리로 나눴을 때 문제, 디자인에서 가장 많은 효율을 볼 수 있다. 디자인 최적화, 코드 최적화가 중요하다. 레벨은 문제가 가장 어렵고, 여지가 가장 크며, 익숙도는 가장 크고, 툴 여부는 적다. 코드 레벨의 CPU 프로파일러는 Visual Studio Profiler, Very Sleepy, Glow Code가 있다.

Profiling in computer science is a form of dynamic program analysis that measures, for example, the space(memory) or time complexity of a program, the usage of particular instructions, or frequency and duration of function calls. The most common use of profiling information is to aid program optimization.

Profiling is achieved by instrumenting either the program source code or its binary executable form using a tool called a profiler (or code profiler). Profilers may use a number of different techniques, such as event-based, statistical, instrumented, and simulation methods.

```
Other parts of the "Profiling" and the "Profiler" have been moved to "Profiling" page.
```

### IPC: Inter-Process Communication | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4_%EA%B0%84_%ED%86%B5%EC%8B%A0)
프로세스 간 통신이란 프로세스들 사이에 서로 데이터를 주고받는 행위 또는 그에 대한 방법이나 경로를 뜻한다. IPC는 마이크로커널과 나노커널의 디자인 프로세스에 매우 중요하다. 마이크로커널은 커널이 제공하는 기능의 수를 줄였기 때문이다. 해당 기능들은 IPC를 통해 서버와 통신함으로써 얻으며 일반적인 모놀리딕 커널에 비해 IPC의 수가 극적으로 증가된다.

주요 IPC 방식으로는 파일(대부분), 신호(대부분. Windows와 같은 일부 시스템은 C 런타임 라이브러리에서만 신호를 제공하며 IPC 방식으로 사용하는 것을 지원하지는 않음), 소켓(대부분), 메시지 큐(대부분), 파이프(모든 POSIX, Windows), 지명 파이프(모든 POSIX, Windows), 세미포어(모든 POSIX, Windows), 공유 메모리(모든 POSIX, Windows), 메서지 전달(비공유(MPI 패러다임, 자바 RMI, CORBA, MSMQ, 메일슬롯, QNX 등)), 메모리 맵 파일(모든 POSIX, Windows)이 있다.

### RPC: Remote Procedure Call | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/%EC%9B%90%EA%B2%A9_%ED%94%84%EB%A1%9C%EC%8B%9C%EC%A0%80_%ED%98%B8%EC%B6%9C)
원격 프로시저 호출은 별도의 원격 제어를 위한 코딩 없이 다른 주소 공간에서 함수나 프로시저를 실행할 수 있게 하는 프로세스 간 통신 기술이다. RPC을 이용하면 프로그래머는 함수가 실행 프로그램에 로컬 위치에 있든 원격 위치에 있든 동일한 코드를 이용할 수 있다. 객체 지향의 원칙을 사용하는 소프트웨어의 경우 RPC를 원격 호출(remote invocation) 또는 원격 메소드 호출(remote method invocation)이라고 일컫는다. 가끔 ONC RPC와 DCE/RPC와 같은 비호환 대상을 수행하기 위해 쓰이는 다른 수많은 기술이 있다.

#### Reference
- 사례를 통해 살펴보는 프로파일링과 최적화, https://www.slideshare.net/veblush/ss-19957544?from_action=save, 2020-09-11-Fri.
- Instruction, https://kwonsye.github.io/computer%20science/2019/04/14/ca-4.html, 2020-09-14-Mon.
- CI/CD, https://deveric.tistory.com/106, 2020-09-14-Mon.
- Profiling Wiki, https://en.wikipedia.org/wiki/Profiling_(computer_programming), 2020-09-14-Mon.
- Hot spot Wiki, https://en.wikipedia.org/wiki/Hot_spot_(computer_programming), 2020-09-14-Mon.
- AMD μProf, https://developer.amd.com/amd-uprof/, 2020-09-15-Tue.
- AMD CodeAnalyst Wiki, https://en.wikipedia.org/wiki/AMD_CodeAnalyst, 2020-09-15-Tue.
- Bottleneck, https://en.wikipedia.org/wiki/Bottleneck_(software), 2020-09-15-Tue.
- C++ chrono, https://jacking.tistory.com/988, 2020-09-15-Tue.
- Intel VTune Profiler, https://software.intel.com/content/www/us/en/develop/tools/vtune-profiler.html, 2020-09-15-Tue.
- Glow Code, https://www.glowcode.com/, 2020-09-15-Tue.
- Very Sleepy GitHub, https://github.com/VerySleepy/verysleepy, 2020-09-15-Tue.
- Very Sleepy Wiki, https://github.com/VerySleepy/verysleepy/wiki, 2020-09-15-Tue.
- Very Sleepy, http://www.codersnotes.com/sleepy/, 2020-09-15-Tue.
- Nvidia PerfKit, https://developer.nvidia.com/nvidia-perfkit, 2020-09-15-Tue.
- PerfHud Korean blog, https://mgun.tistory.com/1169, 2020-09-15-Tue.
- Frame Profiler, https://docs.nvidia.com/gameworks/content/developertools/mobile/perfhud_frame_profiler.htm, 2020-09-15-Tue.
- AMD GPU Open (Radeon GPU Profiler), https://gpuopen.com/rgp/, 2020-09-15-Tue.
- Radeon GPU Profiler GitHub, https://github.com/GPUOpen-Tools/radeon_gpu_profiler, 2020-09-15-Tue.
- Microsoft PIX, https://devblogs.microsoft.com/pix/, 2020-09-15-Tue.
- Valgrind, https://valgrind.org/, 2020-09-15-Tue.
- Visual Studio Profiler docs Korean, https://docs.microsoft.com/ko-kr/visualstudio/profiling/?view=vs-2019, 2020-09-15-Tue.
- Call stack Wiki, https://en.wikipedia.org/wiki/Call_stack, 2020-09-18-Fri.
- Visual Studio Profilers, https://docs.microsoft.com/en-us/visualstudio/profiling/profiling-feature-tour?view=vs-2019, 2020-09-18-Fri.
- Instruction Wiki, https://en.wikipedia.org/wiki/Instruction, 2020-09-21-Mon.
- Instruction Set Architecture Wiki, https://en.wikipedia.org/wiki/Instruction_set_architecture, 2020-09-21-Mon.
- Computer Program Wiki, https://en.wikipedia.org/wiki/Computer_program, 2020-09-21-Mon.
- Callgrind Korean guide, https://m.blog.naver.com/PostView.nhn?blogId=kimyoseob&logNo=220639317811&proxyReferer=https:%2F%2Fwww.google.com%2F 2020-09-22-Tue.
- Valgrind Tools, https://valgrind.org/info/tools.html, 2020-09-23-Wed.
- Valgrind doesn't support to measure time, https://stackoverflow.com/questions/6663614/use-valgrind-to-know-timein-seconds-spent-in-each-function, 2020-09-23-Wed.
- Google gperftools GitHub, https://github.com/gperftools/gperftools, 2020-09-23-Wed.
- Google gperftools, https://gperftools.github.io/gperftools/, 2020-09-23-Wed.
- Google gperftools thread-caching malloc, https://gperftools.github.io/gperftools/tcmalloc.html, 2020-09-23-Wed.
- Google gperftools heap-checking using tcmalloc, https://gperftools.github.io/gperftools/heap_checker.html, 20202-09-23-Wed.
- Google gperftools heap-profiling using tcmalloc, https://gperftools.github.io/gperftools/heapprofile.html, 2020-09-23-Wed.
- Google gperftools CPU profiler, https://gperftools.github.io/gperftools/cpuprofile.html, 2020-09-23-Wed.
- Google pprof GitHub, https://github.com/google/pprof, 2020-09-23-Wed.
- Daemon Wiki KR-KO, https://ko.wikipedia.org/wiki/%EB%8D%B0%EB%AA%AC_(%EC%BB%B4%ED%93%A8%ED%8C%85) 2020-10-30-Fri.
- Refactoring Blog KR-KO, https://nesoy.github.io/articles/2018-05/Refactoring, 2020-11-03-Tue.
- DBus Wiki KR-KO, https://ko.wikipedia.org/wiki/D-Bus, 2020-11-04-Wed.
- IPC Wiki KR-KO, https://ko.wikipedia.org/wiki/%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4_%EA%B0%84_%ED%86%B5%EC%8B%A0, 2020-11-04-Wed.
- RPC Wiki KR-KO, https://ko.wikipedia.org/wiki/%EC%9B%90%EA%B2%A9_%ED%94%84%EB%A1%9C%EC%8B%9C%EC%A0%80_%ED%98%B8%EC%B6%9C, 2020-11-04-Wed.
