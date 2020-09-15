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
### Intel® VTune™ Profiler | [Homepage](https://software.intel.com/content/www/us/en/develop/tools/vtune-profiler.html) | Instruction Level & Partial Paid Version
Intel® VTune™ Profiler collects key profiling data and presents it with a powerful interface that simplifies its analysis and interpretation.

### Specifications
#### Processors
- Intel® and compatible processors and coprocessors
#### FPGAs
- Intel® Arria® 10 FPGA, Intel® Stratix® 10 FPGA
#### Host operating systems
- Windows*, Linux, macOS* (optional download)
#### Target operating systems
- Windows, Linux, FreeBSD*, Android*, Tizen*, Wind River Linux*, Yocto Project*
#### Programming languages
- C, C++, C#, Fortran, Java*, Python*, Google Go* Programming language, Assembly
#### Compilers
- Compilers from Intel, Microsoft* compilers, GNU Compiler Collection (GCC)*, Other Compilers that follow the same standards
#### Development environments
- Integration with Microsoft Visual Studio*, Stand-alone product
#### Threading analysis
- OpenMP*, Intel® Threading Building Blocks (Intel® TBB), Native threads
#### Extended threading performance analysius
- OpenMP, Intel TBB
#### Message passing interface (MPI) parallelism
- Integration with the Intel Trace Analyzer and Collector MPI profiler
#### GPU
- Media and OpenCL™ application tuning on newer Intel® processors

### AMD μProf (AMD CodeAnalyst) | [Homepage](https://developer.amd.com/amd-uprof/) | [Wiki](https://en.wikipedia.org/wiki/AMD_CodeAnalyst) | Instruction Level * Free Version
AMD uProf is a performance analysis tool for applications running on Windows and Linux operating systems. It allows developers to better understand the runtime performance of their application and to identify ways to improve its performance.

### Specifications
#### Processors
- AMD CPU & APU Processors
- Discrete GPUs: Graphics IP 7 GPUs, AMD Radeon 500 Series, FirePro models (Power Profiling Only) 
#### Operating Systems
AMD uProf supports the 64-bit version of the following Operating Systems:
- Microsoft
  - Windows 7, Windows 10 (up to May 2020 Update 20H1), Windows Server 2016, Windows Server 2019
- Linux
  - Ubuntu 16.04 & later, RHEL 7.0 & later, openSUSE Leap 15.0, SLES 12 & 15, CentOS 7.0 & later.
#### Compilers and Application Environment
- Languages
  - C, C++, Fortran, Assembly, Java, .NET
- Programs compiled with
  - Microsoft compilers, GNU compilers, LLVM, AMD’s AOCC, Intel compilers
- Parallelism
  - OpenMP, MPI
- Applications compiled with and without optimization and/or debug information.

### In-house Profiler | Code level
using chrono for c++
```
3# include <chrono>
int main(){
 std::chrono::system_clock::time_point start = std::chrono::system_clock::now();
 work();
 std::chrono::duration<double> sec = std::chrono::system_clock::now() - start;
 std::cout << sec.count() << " seconds" << std::endl;
 return 0;
}
```

### Glow Code | [Homepage](https://www.glowcode.com/) | Instruction Level & Paid Version
GlowCode is a complete real-time performance and memory profiler for Windows and .NET programmers who develop applications with C++, C#, or any .NET Framework-compliant language. GlowCode helps programmers optimize application performance, with tools to detect memory leaks and resource flaws, isolate performance bottlenecks, profile and tune code, trace real-time program execution, ensure code coverage, isolate boxing errors, identify excessive memory usage, and find hyperactive and loitering objects. For native, managed, and mixed code.

### Very Sleepy | [Home](https://github.com/VerySleepy/verysleepy/wiki) | [GitHub](https://github.com/VerySleepy/verysleepy) | Instruction Level & Free Version
Very Sleepy is a polling CPU profiler. Very Sleepy profiles CPU usage, i.e. it tries to find which parts of a program spend the most CPU time executing. CPU profilers can be roughly divided in two categories, according to their modus operandi:

Instrumenting profilers work by modifying the program before it is executed. This can be done at the source level, or after compilation (e.g. Valgrind). The advantages of instrumenting profilers is that they can gather exact information on how many times any function was called, or which functions call which functions exactly.

Polling profilers work by periodically inspecting the profiled program's state. This is usually done by attaching to the program as a debugger would, and periodically recording each thread's stack traces. The advantages of polling profilers is that they do not require modifying the program code before it is executed, and the results better statistically reflect which portions the program spends time in (due to not adding inconsistent overhead to small functions). Very Sleepy is a polling profiler.

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
- Very Sleepy Home, https://github.com/VerySleepy/verysleepy/wiki, 2020-09-15-Tue.
