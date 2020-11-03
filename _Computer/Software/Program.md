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
동작을 바꾸지 않으면서 구조를 개선하는 방법이다. 코드가 작성된 이후 디자인을 개선하는 작업이다. 값이 수정되지 않는 변수는 parameter로 넘길 수 있다. 값이 수정되는 변수는 함수로 추출하여 리턴 값으로 돌려줄 수 있따.

```
Other parts of the "Windows" have been moved to "Windows" page.
Other parts of the "Unix" and "Linux" have been moved to "Linux" page.
```

# Profiling | [Wiki](https://en.wikipedia.org/wiki/Profiling_(computer_programming))
Profiling in computer science is a form of dynamic program analysis that measures, for example, the space(memory) or time complexity of a program, the usage of particular instructions, or frequency and duration of function calls. The most common use of profiling information is to aid program optimization.

Profiling is achieved by instrumenting either the program source code or its binary executable form using a tool called a profiler (or code profiler). Profilers may use a number of different techniques, such as event-based, statistical, instrumented, and simulation methods.

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

## Profiler
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
### Visual Studio Profiler [perftips](https://github.com/inyong37/Study/blob/master/_Computer/Software/Program.md#perftips--examine-performance-using-perftips) | Code level

### Valgrind | [Homepage](https://valgrind.org/) | CPU/Memory & Instruction Level & Free Version & UNIX | [Tools](https://valgrind.org/info/tools.html)
Valgrind is an instrumentation framework for building dynamic analysis tools. There are Valgrind tools that can automatically detect many memory management and threading bugs, and profile programs in detail. 

The Valgrind distribution currently includes seven production-quality tools: a memory error detector, two thread error detectors, a cache and branch-prediction profiler, a call-graph generating cache and branch-prediction profiler, and two different heap profilers. It also includes an experimental SimPoint basic block vector generator. It runs on the following platforms: X86/Linux, AMD64/Linux, ARM/Linux, ARM64/Linux, PPC32/Linux, PPC64/Linux, PPC64LE/Linux, S390X/Linux, MIPS32/Linux, MIPS64/Linux, X86/Solaris, AMD64/Solaris, ARM/Android (2.3.x and later), ARM64/Android, X86/Android (4.0 and later), MIPS32/Android, X86/Darwin and AMD64/Darwin (Mac OS X 10.12).

Valgrind is Open Source / Free Software, and is freely available under the GNU General Public License, version 2.

The Valgrind distribution includes the following debugging and profiling tools: Memcheck, Cachegrind, Callgrind, Massif, Helgrind, DRD, DHAT, Experimental Tools, Other Tools.

#### [Memcheck](https://valgrind.org/info/tools.html#memcheck)

Memcheck detects memory-management problems, and is aimed primarily at C and C++ programs.

#### [Cachegrind](https://valgrind.org/info/tools.html#cachegrind)

Cachegrind is a cache profiler. It performs detailed simulation of the I1, D1 and L2 caches in your CPU and so can accurately pinpoint the sources of cache misses in your code. It identifies the number of cache misses, memory references and instructions executed for each line of source code, with per-function, per-module and whole-program summaries. It is useful with programs written in any language. Cachegrind runs programs about 20--100x slower than normal.

#### [Callgrind](https://valgrind.org/info/tools.html#callgrind)

Callgrind, by Josef Weidendorfer, is an extension to [Cachegrind](https://valgrind.org/info/tools.html#cachegrind). It provides all the information that Cachegrind does, plus extra information about callgraphs. It was folded into the main Valgrind distribution in version 3.2.0. Available separately is an amazing visualisation tool, [KCachegrind](http://kcachegrind.sourceforge.net/cgi-bin/show.cgi/KcacheGrindIndex), which gives a much better overview of the data that Callgrind collects; it can also be used to visualise Cachegrind's output.

#### How to use
- `$ valgrind --tool=callgrind program_name program_argument`
- `$ callgrind_annotatie --auto=yes callgrind.out.pid_number`

#### [Massif](https://valgrind.org/info/tools.html#massif)

Massif is a heap profiler. It performs detailed heap profiling by taking regular snapshots of a program's heap. It produces a graph showing heap usage over time, including information about which parts of the program are responsible for the most memory allocations. The graph is supplemented by a text or HTML file that includes more information for determining where the most memory is being allocated. Massif runs programs about 20x slower than normal.

#### [Helgrind](https://valgrind.org/info/tools.html#helgrind)

Helgrind is a thread debugger which finds data races in multithreaded programs. It looks for memory locations which are accessed by more than one (POSIX p-)thread, but for which no consistently used (pthread_mutex_) lock can be found. Such locations are indicative of missing synchronisation between threads, and could cause hard-to-find timing-dependent problems. It is useful for any program that uses pthreads. It is a somewhat experimental tool, so your feedback is especially welcome here.

#### [DRD](https://valgrind.org/info/tools.html#drd)

DRD is a tool for detecting errors in multithreaded C and C++ programs. The tool works for any program that uses the POSIX threading primitives or that uses threading concepts built on top of the POSIX threading primitives. While Helgrind can detect locking order violations, for most programs DRD needs less memory to perform its analysis.

#### [DHAT](https://valgrind.org/info/tools.html#dhat)

DHAT is a tool for examining how programs use their heap allocations. It tracks the allocated blocks, and inspects every memory access to find which block, if any, it is to. It comes with a GUI to facilitate exploring the profile results.

#### [Valgrind doesn't support measuring time.](https://stackoverflow.com/questions/6663614/use-valgrind-to-know-timein-seconds-spent-in-each-function)

### GNU gprof | [Homepage](https://sourceware.org/binutils/docs/gprof/) | [Wiki](https://en.wikipedia.org/wiki/Gprof) | CPU/Memory & Instruction Level & Free Version & UNIX
Gprof is a performance analysis tool for Unix applications. It used a hybrid of instrumentation and sampling and was created as an extended version of the older "prof" tool. Unlike prof, gprof is capable of limited call graph collecting and printing.

### Google gperftools (originally Google Performance Tools) | [Homepage](https://gperftools.github.io/gperftools/) | [GitHub](https://github.com/gperftools/gperftools)

gperftools is a collection of a high-performance multi-threaded malloc() implementation, plus some pretty nifty performance analysis tools. gperftools is distributed under the terms of the BSD License. gperftools was original home for pprof program. But do note that original pprof (which is still included with gperftools) os now deprecated in favor of golang version at https://github.com/google/pprof.

#### [thread-caching malloc](https://gperftools.github.io/gperftools/tcmalloc.html)

TCMalloc is faster than the glibc 2.3 malloc (available as a separate library called ptmalloc2) and other mallocs that I have tested. ptmalloc2 takes approximately 300 nanoseconds to execute a malloc/free pair on a 2.8 GHz P4 (for small objects). The TCMalloc implementation takes approximately 50 nanoseconds for the same operation pair. Speed is important for a malloc implementation because if malloc is not fast enough, application writers are inclined to write their own custom free lists on top of malloc. This can lead to extra complexity, and more memory usage unless the application writer is very careful to appropriately size the free lists and scavenge idle objects out of the free list.

TCMalloc also reduces lock contention for multi-threaded programs. For small objects, there is virtually zero contention. For large objects, TCMalloc tries to use fine grained and efficient spinlocks. ptmalloc2 also reduces lock contention by using per-thread arenas but there is a big problem with ptmalloc2's use of per-thread arenas. In ptmalloc2 memory can never move from one arena to another. This can lead to huge amounts of wasted space. For example, in one Google application, the first phase would allocate approximately 300MB of memory for its URL canonicalization data structures. When the first phase finished, a second phase would be started in the same address space. If this second phase was assigned a different arena than the one used by the first phase, this phase would not reuse any of the memory left after the first phase and would add another 300MB to the address space. Similar memory blowup problems were also noticed in other applications.

Another benefit of TCMalloc is space-efficient representation of small objects. For example, N 8-byte objects can be allocated while using space approximately `8N * 1.01` bytes. I.e., a one-percent space overhead. ptmalloc2 uses a four-byte header for each object and (I think) rounds up the size to a multiple of 8 bytes and ends up using `16N` bytes.

#### [heap-checking using tcmalloc](https://gperftools.github.io/gperftools/heap_checker.html)

This is the heap checker that used at Google to detect memory leaks in C++ programs. There are three parts to using it: linking the library into an application, running the code, and analyzing the output.

#### [heap-profiling using tcmalloc](https://gperftools.github.io/gperftools/heapprofile.html)

This is the heap profiler that used at Google, to explore how C++ programs manage memory. This facility can be useful for

- Figuring out what is in the program heap at any given time
- Locating memory leaks
- Finding places that do a lot of allocation

The profiling system instruments all allocations and frees. It keeps track of various pieces of information per allocation site. An allocation site is defined as the active stack trace at the call to `malloc`, `calloc`, `realloc`, or, `new`.

There are three parts to using it: linking the library into an application, running the code, and analyzing the output.

#### [CPU profiler](https://gperftools.github.io/gperftools/cpuprofile.html)

This is the CPU profiler that used at Google. There are three parts to using it: linking the library into an application, running the code, and analyzing the output.

### Google pprof | [GitHub](https://github.com/google/pprof)

pprof is a tool for visualization and analysis of profiling data.

pprof reads a collection of profiling samples in profile.proto format and generates reports to visualize and help analyze the data. It can generate both text and graphical reports (through the use of the dot visualization package).

profile.proto is a protocol buffer that describes a set of callstacks and symbolization information. A common usage is to represent a set of sampled callstacks from statistical profiling. The format is described on the [proto/profile.proto](https://github.com/google/pprof/blob/master/proto/profile.proto) file. For details on protocol buffers, see https://developers.google.com/protocol-buffers

Profiles can be read from a local file, or over http. Multiple profiles of the same type can be aggregated or compared.

If the profile samples contain machine addresses, pprof can symbolize them through the use of the native binutils tools (addr2line and nm).

**This is not an official Google product.**

### Very Sleepy | [Homepage](http://www.codersnotes.com/sleepy/) | [Wiki](https://github.com/VerySleepy/verysleepy/wiki) | [GitHub](https://github.com/VerySleepy/verysleepy) | CPU & Instruction Level & Free Version
Very Sleepy is a free C/C++ CPU profiler for Windows systems. Originally started as a fork of Nick Chapman's sleepy, many people have since contributed to add considerable improvements. It supports any native Windows app, if it has standard PDB or DWARF2 debugging information. No recompilation is necessary – it can just attach to any app as it's running. Both 32-bit x86 and 64-bit x64 systems are fully supported, and Very Sleepy will work with both Visual Studio or gcc/mingw compilers. Profiling results are displayed in full call-graph format, and can additionally be saved and exported to CSV format. Very Sleepy is released under the GNU Public License, so you're guaranteed the right to the source code and to change it how you wish.

Very Sleepy is a polling CPU profiler. Very Sleepy profiles CPU usage, i.e. it tries to find which parts of a program spend the most CPU time executing. CPU profilers can be roughly divided in two categories, according to their modus operandi:

Instrumenting profilers work by modifying the program before it is executed. This can be done at the source level, or after compilation (e.g. Valgrind). The advantages of instrumenting profilers is that they can gather exact information on how many times any function was called, or which functions call which functions exactly.

Polling profilers work by periodically inspecting the profiled program's state. This is usually done by attaching to the program as a debugger would, and periodically recording each thread's stack traces. The advantages of polling profilers is that they do not require modifying the program code before it is executed, and the results better statistically reflect which portions the program spends time in (due to not adding inconsistent overhead to small functions). Very Sleepy is a polling profiler.

### Glow Code | [Homepage](https://www.glowcode.com/) | CPU/Memory & Instruction Level & Paid Version & Windows
GlowCode is a complete real-time performance and memory profiler for Windows and .NET programmers who develop applications with C++, C#, or any .NET Framework-compliant language. GlowCode helps programmers optimize application performance, with tools to detect memory leaks and resource flaws, isolate performance bottlenecks, profile and tune code, trace real-time program execution, ensure code coverage, isolate boxing errors, identify excessive memory usage, and find hyperactive and loitering objects. For native, managed, and mixed code.

### Visual Studio Profiler | [MS Docs (Kor)](https://docs.microsoft.com/ko-kr/visualstudio/profiling/?view=vs-2019) | [Tools](https://docs.microsoft.com/en-us/visualstudio/profiling/profiling-feature-tour?view=vs-2019) | CPU/Memory/GPU & Code/Instruction Level & Partial Paid Version & Windows
#### [PerfTips](https://docs.microsoft.com/en-us/visualstudio/profiling/perftips?view=vs-2019) | [Examine performance using PerfTips](https://docs.microsoft.com/en-us/visualstudio/profiling/profiling-feature-tour?view=vs-2019#examine-performance-using-perftips)
Visual Studio debugger PerfTips and the debugger-integrated Diagnostic Tools help you to monitor and analyze the performance of your app while you are debugging.

Although the debugger-integrated diagnostic tools are a great way of becoming aware of performance issues while you are developing, the debugger can have a significant impact on the performance of your app. To collect more accurate performance data, consider using the tools in the Performance Profiler as an additional part of your performance investigations. See Run profiling tools with or without the debugger.
#### CPU Usage | [Measure application performance by analyzing CPU usage](https://docs.microsoft.com/en-us/visualstudio/profiling/beginners-guide-to-performance-profiling?view=vs-2019) | [Analyze CPU usage](https://docs.microsoft.com/en-us/visualstudio/profiling/profiling-feature-tour?view=vs-2019#analyze-cpu-usage)
Find performance issues while you're debugging with the debugger-integrated CPU Usage diagnostic tool. You can also analyze CPU usage without a debugger attached or by targeting a running app. For more information, see Run profiling tools with or without the debugger.

When the debugger pauses, the CPU Usage tool in the Diagnostic Tools window collects information about the functions that are executing in your application. The tool lists the functions that were performing work, and provides a timeline graph you can use to focus on specific segments of the sampling session.
#### Memory Usage | [Measure memory usage in Visual Studio](https://docs.microsoft.com/en-us/visualstudio/profiling/memory-usage?view=vs-2019) | [Analyze memory usage](https://docs.microsoft.com/en-us/visualstudio/profiling/profiling-feature-tour?view=vs-2019#analyze-memory-usage)
Find memory leaks and inefficient memory while you're debugging with the debugger-integrated Memory Usage diagnostic tool. The Memory Usage tool lets you take one or more snapshots of the managed and native memory heap to help understand the memory usage impact of object types. You can also analyze memory usage without a debugger attached or by targeting a running app. For more information, see Run profiling tools with or without the debugger.

Although you can collect memory snapshots at any time in the Memory Usage tool, you can use the Visual Studio debugger to control how your application executes while investigating performance issues. Setting breakpoints, stepping, Break All, and other debugger actions can help you focus your performance investigations on the code paths that are most relevant. Performing those actions while your app is running can eliminate the noise from the code that doesn't interest you and can significantly reduce the amount of time it takes you to diagnose an issue.
#### .Net Object Allocation | [Analyze memory usage by using the .NET Object Allocation tool](https://docs.microsoft.com/en-us/visualstudio/profiling/dotnet-alloc-tool?view=vs-2019)
#### [GPU Usage](https://docs.microsoft.com/en-us/visualstudio/profiling/gpu-usage?view=vs-2019) | [Analyze GPU Usage (Direct3D)](https://docs.microsoft.com/en-us/visualstudio/profiling/profiling-feature-tour?view=vs-2019#analyze-gpu-usage-direct3d)
#### Application Timeline | [Analyze resource consumption and UI thread activity (XAML)](https://docs.microsoft.com/en-us/visualstudio/profiling/application-timeline?view=vs-2019) | [Analyze resource consumption (XAML)](https://docs.microsoft.com/en-us/visualstudio/profiling/profiling-feature-tour?view=vs-2019#analyze-resource-consumption-xaml)
Use the Application Timeline profiler to find and fix application-interaction related performance issues in XAML applications. This tool helps improve the XAML application performance by showing a detailed view of the applications' resource consumption. You can analyze the time spent by your application preparing UI frames (layout and render), servicing network and disk requests, and in scenarios like Application Startup, Page Load, and Windows resize.
#### [Events viewer](https://docs.microsoft.com/en-us/visualstudio/profiling/events-viewer?view=vs-2019) | [Examine application events](https://docs.microsoft.com/en-us/visualstudio/profiling/profiling-feature-tour?view=vs-2019#examine-application-events)
The generic events viewer shows app activity through a list of events like module load, thread start, and system configuration. This view helps you better diagnose how your app is doing within the Visual Studio profiler.
#### .Net Async | [Analyze performance of .NET asynchronous code](https://docs.microsoft.com/en-us/visualstudio/profiling/analyze-async?view=vs-2019)| [Analyze asynchronous code (.NET)](https://docs.microsoft.com/en-us/visualstudio/profiling/profiling-feature-tour?view=vs-2019#analyze-asynchronous-code-net)
#### Database | [Analyze database performance using the Database tool](https://docs.microsoft.com/en-us/visualstudio/profiling/analyze-database?view=vs-2019) | [Analyze database performance (.NET Core)](https://docs.microsoft.com/en-us/visualstudio/profiling/profiling-feature-tour?view=vs-2019#analyze-database-performance-net-core)
#### Performance Explorer | [Analyze performance (legacy tools)](https://docs.microsoft.com/en-us/visualstudio/profiling/profiling-feature-tour?view=vs-2019#analyze-performance-legacy-tools)
In Visual Studio 2019, the legacy Performance Explorer and related profiling tools such as the Performance Wizard were folded into the Performance Profiler, which you can open using Debug > Performance Profiler. In the Performance Profiler, the available diagnostics tools depend on the target chosen and the current, open startup project. The CPU Usage tool provides the sampling capability previously supported in the Performance Wizard. The Instrumentation tool provides the instrumented profiling capability (for precise call counts and durations) that was in the Performance Wizard. Additional memory tools also appear in the Performance Profiler.
#### IntelliTrace | [IntelliTrace for Visual Studio Enterprise (C#, Visual Basic, C++)](https://docs.microsoft.com/en-us/visualstudio/debugger/intellitrace?view=vs-2019)

### Intel® VTune™ Profiler | [Homepage](https://software.intel.com/content/www/us/en/develop/tools/vtune-profiler.html) | CPU/Memory/GPU & Instruction Level & Partial Paid Version & Almost all OSs
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

### AMD μProf (AMD CodeAnalyst) | [Homepage](https://developer.amd.com/amd-uprof/) | [Wiki](https://en.wikipedia.org/wiki/AMD_CodeAnalyst) | CPU/Memory/GPU & Instruction Level & Free Version & Almost all OSs
AMD uProf is a performance analysis tool for applications running on Windows and Linux operating systems. It allows developers to better understand the runtime performance of their application and to identify ways to improve its performance.

### Specifications
#### Processors
- AMD CPU & APU Processors
- Discrete GPUs: Graphics IP 7 GPUs, AMD Radeon 500 Series, FirePro models (Power Profiling Only) 
#### Operating Systems
AMD uProf supports the 64-bit version of the following Operating Systems:
- Microsoft: Windows 7, Windows 10 (up to May 2020 Update 20H1), Windows Server 2016, Windows Server 2019
- Linux: Ubuntu 16.04 & later, RHEL 7.0 & later, openSUSE Leap 15.0, SLES 12 & 15, CentOS 7.0 & later.
#### Compilers and Application Environment
- Languages: C, C++, Fortran, Assembly, Java, .NET
- Programs compiled with Microsoft compilers, GNU compilers, LLVM, AMD’s AOCC, Intel compilers
- Parallelism: OpenMP, MPI
- Applications compiled with and without optimization and/or debug information.

### Nvidia PerfKit (PerfHud) | [Homepage](https://developer.nvidia.com/nvidia-perfkit) | GPU & Free Version & Almost all OSs
NVIDIA PerfKit is a comprehensive suite of performance tools to help debug and profile OpenGL and Direct3D applications. It gives you access to low-level performance counters inside the driver and hardware counters inside the GPU itself. The counters can be used to determine exactly how your application is using the GPU, identify performance issues, and confirm that performance problems have been resolved. NVIDIA PerfKit is available separately for 3 target platforms. PC packages includes support for 32-bit and 64-bit Windows 10, Windows 8, Windows 7, and Vista platforms. Android packages includes support for NVIDIA Tegra TK1 and TX1 devices running Android OS. Linux for Tegra support is available under NVIDIA PerfKit (L4T) targeting the NVIDIA Jetson Embedded Platform.

### Radeon GPU Profiler (AMD GPU Open) | [Homepage](https://gpuopen.com/rgp/) | [GitHub](https://github.com/GPUOpen-Tools/radeon_gpu_profiler) | GPU & Free Version & Almost all OSs
The Radeon GPU Profiler (RGP) is a ground-breaking low-level optimization tool from AMD. It provides detailed timing information on Radeon Graphics using custom, built-in, hardware thread-tracing, allowing the developer deep inspection of GPU workloads.

This unique tool generates easy to understand visualizations of how your DirectX®12 and Vulkan® games interact with the GPU at the hardware level. Profiling a game is both a quick, and simple process using the Radeon Developer Panel and the public display driver.

### Microsoft PIX | [Homepage](https://devblogs.microsoft.com/pix/) | Windows
Performance tuning and debugging for DirectX 12 games on Windows

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
#### Korean
- 문제, 디자인, 코드, 컴파일, 어셈블리로 나눴을 때 문제, 디자인에서 가장 많은 효율을 볼 수 있다. (디자인 최적화, 코드 최적화)
- 레벨은 문제가 가장 어렵고, 여지가 가장 크며, 익숙도는 가장 크고, 툴 여부는 적다.
- 코드 레벨의 CPU 프로파일러는 Visual Studio Profiler, Very Sleepy, Glow Code가 있다.
