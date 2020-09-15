# Program

## Redistributable (재배포)
 프로그램을 재배포 해도 된다는 뜻이다. 예로 상업적인 마이크로소프트의 오피스 2019, 365는 재배포가 불가하다.
 
## Online Install
설치 시 인터넷에 연결해서 필요한 파일을 다운받아서 설치한다.

## Office Install
설치 파일에 필요한 모든 파일이 같이 있어서 오프라인으로 설치한다.

# Profiling | [Wiki](https://en.wikipedia.org/wiki/Profiling_(computer_programming))
Profiling in computer science is a form of dynamic program analysis that measures, for example, the space(memory) or time complexity of a program, the usage of particular instructions, or frequency and duration of function calls. The most common use of profiling information is to aid program optimization.

Profiling is achieved by instrumenting either the program source code or its binary executable form using a tool called a profiler (or code profiler). Profilers may use a number of different techniques, such as event-based, statistical, instrumented, and simulation methods.

-   문제, 디자인, 코드, 컴파일, 어셈블리로 나눴을 때 문제, 디자인에서 가장 많은 효율을 볼 수 있다. (디자인 최적화, 코드 최적화)
-   레벨은 문제가 가장 어렵고, 여지가 가장 크며, 익숙도는 가장 크고, 툴 여부는 적다.
-   코드 레벨의 CPU 프로파일러는 Visual Studio Profiler, Very Sleepy, Glow Code가 있다.

### Hot spot | [Wiki](https://en.wikipedia.org/wiki/Hot_spot_(computer_programming))
A Hot spot in computer science is most usually defined as a region of a program where a high proportion of executed instructions occur or where most time is spent during the program's execution (not necessarily the same thing since some instructions are faster than others).

### Bottleneck | [Wiki](https://en.wikipedia.org/wiki/Bottleneck_(software))
A bottleneck in computer science occurs when the capacity of an application or a computer system is limited by a single component, like the neck of a bottle slowing down the overall water flow. The bottleneck has lowest throughput of all parts of the transaction path.

## Profiler
### AMD μProf (AMD CodeAnalyst) | [Homepage](https://developer.amd.com/amd-uprof/) | [Wiki](https://en.wikipedia.org/wiki/AMD_CodeAnalyst)
AMD uProf is a performance analysis tool for applications running on Windows and Linux operating systems. It allows developers to better understand the runtime performance of their application and to identify ways to improve its performance.

#### Specifications
- Processors: AMD CPU & APU Processors, Discrete GPUs: Graphics IP 7 GPUs, AMD Radeon 500 Series, FirePro models (Power Profiling Only) 
- Operating Systems: AMD uProf supports the 64-bit version of the following Operating Systems: Microsoft Windows 7, Windows 10 (up to May 2020 Update 20H1), Windows Server 2016, Windows Server 2019 and Linux Ubuntu 16.04 & later, RHEL 7.0 & later, openSUSE Leap 15.0, SLES 12 & 15, CentOS 7.0 & later.
- Compilers and Application Environment: Languages with C, C++, Fortran, Assembly, Java, .NET and Programs compiled with Microsoft compilers, GNU compilers, LLVM, AMD’s AOCC, Intel compilers and Parallelism with OpenMP, MPI and Applications compiled with and without optimization and/or debug information.

#### Reference
- 사례를 통해 살펴보는 프로파일링과 최적화, https://www.slideshare.net/veblush/ss-19957544?from_action=save, 2020-09-11-Fri.
- Instruction, https://kwonsye.github.io/computer%20science/2019/04/14/ca-4.html, 2020-09-14-Mon.
- CI/CD, https://deveric.tistory.com/106, 2020-09-14-Mon.
- Profiling Wiki, https://en.wikipedia.org/wiki/Profiling_(computer_programming), 2020-09-14-Mon.
- Hot spot Wiki, https://en.wikipedia.org/wiki/Hot_spot_(computer_programming), 2020-09-14-Mon.
- AMD μProf, https://developer.amd.com/amd-uprof/, 2020-09-15-Tue.
- AMD CodeAnalyst Wiki, https://en.wikipedia.org/wiki/AMD_CodeAnalyst, 2020-09-15-Tue.
- Bottleneck, https://en.wikipedia.org/wiki/Bottleneck_(software), 2020-09-15-Tue.
