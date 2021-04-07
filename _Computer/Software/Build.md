# *Build* | [Wiki (KR)](https://ko.wikipedia.org/wiki/%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4_%EB%B9%8C%EB%93%9C)
Build는 소스 코드 파일을 컴퓨터나 휴대폰에서 실행할 수 있는 독립(standalone) 소프트웨어 가공물로 변환하는 과정을 말하거나 그에 대한 결과물을 일컫는다. 빌드에 있어 가장 중요한 단계들 가운데 하나는 소스 코드 파일이 실행 코드로 변환되는 컴파일 과정이다. 컴퓨터 프로그램을 빌드하는 과정은 보통 다른 프로그램을 제어하는 프로그램인 빌드 도구에 의해 관리된다.

## *Build Process (ex. GCC)*
1. Preprocessing
- foo.c -> foo.i
- Preprocessor(전처리기, cpp0)가 `#`에 대한 처리를 한다. `#include`의 라이브러리를 불러오는 역할도 한다.

2. Compile
- foo.i -> foo.s
- Compiler(컴파일러, cc1)가 불러온 라이브러리를 참조하여 소스코드를 어셈블리 코드로 변환한다.

3. Assemble
- foo.s -> foo.o
- Assembler(어셈블러, as, collect2)가 어셈블리 코드에서 기계어 코드(오브젝트 파일)로 변환한다.

4. Link
- foo.o -> foo (elf, exe)
- Linker(링커, ld)가 a, so 라이브러리와 연결시켜 실행(executable) 파일을 만든다.

## *Build Tool/System*
:bulb: Make는 UNIX에서 주로 사용되는 프로그램 빌드 도구이다. 파일들끼리의 의존성과 각 파일에 필요한 명령을 정의하여 프로그램을 컴파일할 수 있으며 프로그램을 만들 수 있다. Makefile을 해석해서 빌드한다. CMake는 멀티 플랫폼에서 사용할 수 있는 Make로 오픈소스 프로젝트로 키트웨어와 인사이트 콘솔티엄에서 만들었다. Meta Make로 Make를 수행하지 않고 지정한 운영체제에 맞는 Make/Solution 파일을 생성한다. Ninja는 속도에 중점을 둔 소형 빌드 시스템이다. GYP는 빌드 자동화 도구이며 python으로 작성된 메타 빌드 시스템이다. Google이 Chromium 브라우저를 빌드할 때 OS에 의존하는 IDE의 프로젝트 파일을 생성하기 위해 만들어진 오픈 소스 소프트웨어다. GN은 Ninja로 응용프로그램 프로젝트를 구축할 수 있도록 Ninja 빌드 파일을 생성하는 메타 빌드 시스템이다. Chromium 빌드가 GYP에서 GN으로 전환되었다.

:bulb: TensorFlow는 third party 빌드로 bazel와 starlark를 사용한다. OpenCV는 3rdparty 빌드로 CMake와  cpp, h를 사용한다. PyTorch는 third party 빌드로 bazel과 submodule을 사용한다. Caffe는 빌드로 CMake와 docker를 사용한다. Keras는 python으로 `PyPI(pip)`, 또는 직접 소스에서 `(sudo) python setup.py install`한다. 

### *Make* | [GNU Make](https://www.gnu.org/software/make/) | [Wiki (KR)](https://ko.wikipedia.org/wiki/Make_(%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4)) | [Git Repositories](http://savannah.gnu.org/git/?group=make)
GNU Make is a tool which controls the generation of executables and other non-source files of a program from the program's source files.

Make gets its knowledge of how to build your program from a file called the makefile, which lists each of the non-source files and how to compute it from other files. When you write a program, you should write a makefile for it, so that it is possible to use Make to build and install the program.

### *CMake (Cross Platform Make)* | [Homeapge](https://cmake.org/) | [Wiki (KR)](https://ko.wikipedia.org/wiki/CMake) | [GitLab](https://gitlab.kitware.com/cmake/cmake)
CMake is an open-source, cross-platform family of tools designed to build, test and package software. CMake is used to control the software compilation process using simple platform and compiler independent configuration files, and generate native makefiles and workspaces that can be used in the compiler environment of your choice. The suite of CMake tools were created by Kitware in response to the need for a powerful, cross-platform build environment for open-source projects such as ITK and VTK.

#### How to use CMake
Command는 upper, lower case 모두 사용 가능하다. set()으로 설정된 내용은 현재와 하위 디렉토리의 CMakeLists.txt에만 적용된다. 상위, 동일 레벨 CMakeLists.txt에는 적용되지 않는다. Boolean type은 if()로 구분할 수 있고, 다른 비교는 STREQUAL (string equal)을 사용한다. `if(foo is true)` or `if(foo)` (Python) is same as `if(${FOO} STREQUAL "ture")` or `if(${FOO})` in CMake.

- Conditional statements: `if()`, `elseif()`, `else()`, `endif()`
- Variable declarartion/definition: `SET()`
  - `SET(var_name "value")`
  - `SET(var_list "value_1" "value_2")`
- Using variable: `$var_name` or `${var_name}`
- Make binary output: `ADD_EXECUTABLE()`
  - `ADD_EXECUTABLE(program.output main.cc foo.cc bar.cc)`
- Add an executable to the project using the specified source files | [CMake Document](https://cmake.org/cmake/help/v3.20/command/add_executable.html)
  - `add_executable(<name> [WIN32] [MACOSX_BUNDLE] [EXCLUDE_FROM_ALL] [source1] [source2 ...])`
- Minimum version: `CMAKE_MINIMUM_REQUIRED()`
  - `CMAKE_MINIMUM_REQUIRED(VERSION "version_number")`
  - `CMAKE_MINIMUM_REQUIRED(VERSION 3.0)`
- Project name: `PROJECT()`
  - `PROJECT(project_name)`
  - use with `${CMAKE_PROJECT_NAME}`
- Message output: `MESSAGE()`
  - `MESSAGE("Hello World!")`
  - `MESSAGE([Type] "message")`
  - [Type]
    - STATUS: plus '--'
    - WARNING: warning message and keep going
    - AUTHOR_WARNING: warning for develop and keep going
    - SEND_ERROR: error message and keep going without Makefile
    - FATAL_ERROR: error message and stop
- Specify libraries or flags to use when linking a given target and/or its dependents | [CMake Document](https://cmake.org/cmake/help/v3.20/command/target_link_libraries.html)
  - `target_link_libraries(<target> ... <item> ... ...)`
- Add a library to the project using the specified sources files | [CMake Document](https://cmake.org/cmake/help/v3.20/command/add_library.html)
  - `add_library(<name> [STATIC | SHARED | MODULE] [EXCLUDE_FROM_ALL] [<source>...]`
    - out: `lib<name>.a` or `<name>.lib`
    - `STATIC` libraries are archives of object files for use when linking other targets.
    - `SHARED` libraries are linked dynamically and loaded at runtime.
    - `MODULE` libraries are plugins that are not linked into other targets but may be loaded dynamically at runtime using dlopen-like functionality.
    - An `INTERFACE` library target does not compile sources and does not produce a library artifact on disk. However, it may have properties set on it and it may be installed and exported
- Add a subdirectory to the build | [CMake Document](https://cmake.org/cmake/help/v3.20/command/add_subdirectory.html)
  - `add_subdirectory(source_dir [binary_dir] [EXCLUDE_FROM_ALL])`

#### Options
- Explicitly specify a source directory: `-S <path-to-source>`
- Explicitly specify a build directory: `-B <path-to-build>`
- Create or update a cmake cache entry: `-D <var>[:<type>]=<value>`
- Specify a build system generator: `-G <generator-name>`
- Specify platform name if supported by generator: `-A <platform-name>`

#### CMake Public | Private | Interface
CMake uses somewhat similar inferitance concepts to C++, especially for the C++ public, and private access specifiers and inheritance types.

### *Ninja* | [Homepage](https://ninja-build.org/) | [Wiki (KR)](https://ko.wikipedia.org/wiki/%EB%8B%8C%EC%9E%90_(%EB%B9%8C%EB%93%9C_%EC%8B%9C%EC%8A%A4%ED%85%9C)) | [GitHub](https://github.com/ninja-build/ninja) | [Manual](https://ninja-build.org/manual.html)
Ninja is a small build system with a focus on speed. It differs from other build systems in two major respects: it is designed to have its input files generated by a higher-level build system, and it is designed to run builds as fast as possible.

### *GYP (Generate Your Projects)* | [Homepage](https://gyp.gsrc.io/) | [Wiki (KR)](https://ko.wikipedia.org/wiki/GYP_(%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4)) | [Google Source](https://chromium.googlesource.com/external/gyp)
GYP is a Meta-Build system: a build system that generates other build systems.

GYP is intended to support large projects that need to be built on multiple platforms (e.g., Mac, Windows, Linux), and where it is important that the project can be built using the IDEs that are popular on each platform as if the project is a “native” one.

### *GN (Generates Ninja build files)* | [Homepage](https://www.chromium.org/developers/gn-build-configuration) | [Wiki (KR)](https://ko.wikipedia.org/wiki/GN_(%EB%B9%8C%EB%93%9C_%EC%8B%9C%EC%8A%A4%ED%85%9C)) | [Google Source](https://gn.googlesource.com/gn/)
GN is a meta-build system that generates build files for Ninja.

### *Bazel* | [Homepage](https://www.bazel.build/) | [Wiki (KR)](https://ko.wikipedia.org/wiki/%EB%B0%94%EC%A0%A4_(%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4)) | [GitHub](https://github.com/bazelbuild/bazel)
Bazel is an open source tool that enables software build and test automation. Google used and built Blaze, a build tool internally, and released and released part of the Blaze tool with Bazel, named Blaze's anagram. Bazel was first released in March 2015 and was beta tested until September 2015.

Similar to build tools like Make, Apache Ant, or Apache Maven, Bazel uses a set of rules to build application software from source code. Rules and macros are written in the Skylark language, a subset of Python. There are basic rules for writing software written in Java, C, C++, Python, Objective-C and Bourne shell script programming languages. Bazel can create application software packages suitable for distribution for Android and iOS operating systems.

When designing Bazel, we focused on build speed, accuracy and reproducibility. This tool uses parallelism to accelerate parts of the build process. Includes Bazel Query language that can be used to analyze build dependencies in complex build graphs.

### *Starlark Language* | [Homepage](https://docs.bazel.build/versions/2.0.0/skylark/language.html) | [GitHub](https://github.com/bazelbuild/starlark)
Starlark (formerly known as Skylark) is a language intended for use as a configuration language. It was designed for the Bazel build system, but may be useful for other projects as well. This repository is where Starlark features are proposed, discussed, and specified. It contains information about the language, including the specification. There are multiple implementations of Starlark.

Starlark is a dialect of Python. Like Python, it is a dynamically typed language with high-level data types, first-class functions with lexical scope, and garbage collection. Independent Starlark threads execute in parallel, so Starlark workloads scale well on parallel machines. Starlark is a small and simple language with a familiar and highly readable syntax. You can use it as an expressive notation for structured data, defining functions to eliminate repetition, or you can use it to add scripting capabilities to an existing application.

A Starlark interpreter is typically embedded within a larger application, and the application may define additional domain-specific functions and data types beyond those provided by the core language. For example, Starlark was originally developed for the Bazel build tool. Bazel uses Starlark as the notation both for its BUILD files (like Makefiles, these declare the executables, libraries, and tests in a directory) and for its macro language, through which Bazel is extended with custom logic to support new languages and compilers.

### *Microsoft Visual C++ (MSVC)* | [MS Docs](https://docs.microsoft.com/en-us/cpp/?view=msvc-160) | [Wiki](https://en.wikipedia.org/wiki/Microsoft_Visual_C%2B%2B)
Microsoft Visual C++ (MSVC) is a compiler for the C, C++, and C++/CLI programming languages by Microsoft. MSVC is proprietary software; it was originally a standalone product but later become a part of Visual Studio and made available in both trialware and freeware forms. It features tools for developing and debugging C++ code, expecially code written for the Windows API, DirectX and .NET.

#### C/C++ Build in Windows | [MS Docs](https://docs.microsoft.com/en-us/cpp/build/reference/c-cpp-building-reference?view=msvc-160)
#### C/C++ Compile in Windows | [MS Docs](https://docs.microsoft.com/en-us/cpp/build/reference/compiling-a-c-cpp-program?view=msvc-160)
#### C/C++ Link in Windows | [MS Docs](https://docs.microsoft.com/en-us/cpp/build/reference/linking?view=msvc-160)

## Compiler
### *GCC (GNU C Compiler/GNU Compiler Collection)* | [Homepage](https://gcc.gnu.org/) | [Wiki (KR)](https://ko.wikipedia.org/wiki/GNU_%EC%BB%B4%ED%8C%8C%EC%9D%BC%EB%9F%AC_%EB%AA%A8%EC%9D%8C)
The GNU Compiler Collection includes front ends for C, C++, Objective-C, Fortran, Ada, Go, and D, as well as libraries for these languages (libstdc++,...). GCC was originally written as the compiler for the GNU operating system. The GNU system was developed to be 100% free software, free in the sense that it respects the user's freedom.[Ref]

GNU 컴파일러 모음(GNU Compiler Collection, 줄여서 GCC)는 GNU 프로젝트의 일환으로 개발되어 널리 쓰이고 있는 컴파일러이다.

자유 소프트웨어 중에 가장 잘 알려진 것들 중 하나인 GCC는 원래 C만을 지원했던 컴파일러로 이름도 "GNU C 컴파일러"였다. 이러한 까닭에 현재에도 GCC는 GNU 컴파일러 모음의 일부인 GNU C 컴파일러(GNU C Compiler)의 줄임말로 쓰이기도 한다. 그러나 나중에 C++, 자바, 포트란, 에이다 등 여러 언어를 컴파일할 수 있게 되면서, 현재의 이름으로 바뀌게 되었다.

#### How to use GCC
- `gcc`: compile C source code
  -`gcc foo.c`
- `g++`: compile C++ source code
  -`g++ foo.cpp`
- `-l` option: library linking
  - without prefix `lib` and suffix `.a`(Linux static link library) or `.so`(Linux dynamic link library) or `.lib`(Windows static link library) or `.dll`(Windows dynamic link library)
  - `-l library` or `-llibrary`
- `-L` option: optional library directory
  - defualt library directory: `/lib`, `/usr/lib`, and `/usr/local/lib`
  - `-L /home/directory` or `-L/home/directory`
  
### *LLVM (Low Level Virtual Machine)* | [Homepage](https://llvm.org/) | [Wiki (KR)](https://ko.wikipedia.org/wiki/LLVM)
The LLVM Project is a collection of modular and reusable compiler and toolchain technologies. Despite its name, LLVM has little to do with traditional virtual machines. The name "LLVM" itself is not an acronym; it is the full name of the project.

LLVM(이전 이름: Low Level Virtual Machine)은 컴파일러의 기반구조이다. 프로그램을 컴파일 타임, 링크 타임, 런타임 상황에서 프로그램의 작성 언어에 상관없이 최적화를 쉽게 구현할 수 있도록 구성되어 있다.

LLVM은 원래는 저급 가상 기계(low-level virtual machine)의 약자를 가리켰지만, LLVM이 성장하고 다양한 목적을 가지게 되면서 현재는 그 이름을 약자로서 사용하는 것이 아니라 그냥 프로젝트의 이름으로서 사용하고 있다.

LLVM의 핵심 코드는 'LLVM 라이선스'로 배포되며, 이것은 BSD 라이선스와 비슷한 속성을 가진다. 즉, LLVM을 사용한 프로그램을 배포하였을 때 해당 소스 코드를 공개/배포해야 하는 의무가 없다. 단 LLVM의 프론트엔드를 GNU 컴파일러 모음(GCC) 기반으로 사용할 경우 프론트엔드는 GPL로 배포한다. LLVM 프로젝트에서는 LLVM 라이선스를 가지는 프론트엔드를 위해, Clang이라는 프로젝트를 진행하고 있다.

### *Clang (a C language family frontend for LLVM)* | [Homepage](https://clang.llvm.org/) | [Wiki (KR)](https://ko.wikipedia.org/wiki/%ED%81%B4%EB%9E%AD)
The Clang project provides a language front-end and tooling infrastructure for languages in the C language family (C, C++, Objective C/C++, OpenCL, CUDA, and RenderScript) for the LLVM project. Both a GCC-compatible compiler driver (clang) and an MSVC-compatible compiler driver (clang-cl.exe) are provided.

클랭은 C, C++, 오브젝티브-C, 오브젝티브-C++ 프로그래밍 언어를 위한 컴파일러 프론트엔드이다. LLVM을 백엔드로 사용하며 LLVM 2.6 이후로 릴리즈의 일부로 자리잡았다.

목표는 GNU 컴파일러 모음 (GCC)를 대체하는 것이다. 개발은 완전히 오픈 소스이며 구글, 애플 등 대형 소프트웨어 기업의 지원을 받고 있다. 소스는 일리노이 대학교/NCSA 오픈 소스 라이선스로 이용할 수 있다.

클랭 프로젝트는 클랭 프론트엔드와 클랭 정적 분석기를 포함한다.

### *Clang-cl* | [Clang 12 Document](https://clang.llvm.org/docs/MSVCCompatibility.html)
When Clang compiles C++ code for Windows, it attempts to be compatible with MSVC. Clang-cl is a driver program for clang that attempts to be compatible with MSVC's cl.exe.

### Object file `.o`
- Executable object file
  - 링크까지 끝나 실행이 가능한 파일이다.
- Shared object file
  - 동적 링크가 가능한 파일이다.
- Relocatable object file
  - 링크를 하지 않은 파일, 링커를 통해 재배치가 가능하다는 뜻이다.

### Executable and Linking Format `.elf`
UNIX, Linux 환경에서 실행하는 프로그램의 바이너리 파일, 오브젝트 파일을 나타낸다.

### Symbolic Link | [Wiki](https://en.wikipedia.org/wiki/Symbolic_link)
A symbolic link (also symlink or soft link) is a term for any file that contains a reference to another file or directory in the form of an absolute or relative path and that affects pathname resolution. Symbolicn links were already present by 1978 in minicomputer operating systems from DEC and Data General's RDOS. Today they are supported by the POSIX operating system standard, most Unix-like operating systems such as FreeBSD, Linux, and macOS. Limited support also exists in Windows operating systems such as Windows Vista, Windows 7 and to some degree in Windows 2000 and Windows XP in the form of shortcut files.

### Using `extern "C"` Keyword in C++
C++ compiler는 funciton을 compile할 때 function의 이름을 임의로 수정하기 때문에 function의 이름이 그대로 유지되게 하려면 해당 function을 C 언어 방식으로 compile해야 한다. 따라서 선언된 해당 function 앞에 `extern "C"` keyword를 적어서 해당 function가 C 방식으로 compile 되게 한다. 이 방식은 C++로 DLL을 만들어 C#과 같은 다른 언어에 제공할 때도 동일하게 사용한다.

#### Reference
- Bazel, https://www.bazel.build/, 2020-07-16-Thu.
- Bazel wiki, https://ko.wikipedia.org/wiki/%EB%B0%94%EC%A0%A4_(%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4), 2020-07-16-Thu.
- Bazel GitHub, https://github.com/bazelbuild/bazel, 2020-07-16-Thu.
- Starlark GitHub, https://github.com/bazelbuild/starlark, 2020-07-16-Thu.
- GNU Make, https://www.gnu.org/software/make/, 2020-07-16-Thu.
- Make Wiki KR, https://ko.wikipedia.org/wiki/Make_(%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4), 2020-07-16-Thu.
- Make Git Repositories, http://savannah.gnu.org/git/?group=make, 2020-07-16-Thu.
- CMake, https://cmake.org/, 2020-07-16-Thu.
- CMake Wiki, https://ko.wikipedia.org/wiki/CMake, 2020-07-16-Thu.
- CMake GitLab, https://gitlab.kitware.com/cmake/cmake, 2020-07-16-Thu.
- Ninja, https://ninja-build.org/, 2020-07-16-Thu.
- Ninja Wiki, https://ko.wikipedia.org/wiki/%EB%8B%8C%EC%9E%90_(%EB%B9%8C%EB%93%9C_%EC%8B%9C%EC%8A%A4%ED%85%9C), 2020-07-16-Thu.
- Ninja GitHub, https://github.com/ninja-build/ninja, 2020-07-16-Thu.
- Ninja Manual, https://ninja-build.org/manual.html, 2020-07-16-Thu.
- GYP, https://gyp.gsrc.io/, 2020-07-16-Thu.
- GYP Wiki, https://ko.wikipedia.org/wiki/GYP_(%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4), 2020-07-16-Thu.
- GYP Google Source, https://chromium.googlesource.com/external/gyp, 2020-07-16-Thu.
- GN, https://www.chromium.org/developers/gn-build-configuration, 2020-07-16-Thu.
- GN Wiki, https://ko.wikipedia.org/wiki/GN_(%EB%B9%8C%EB%93%9C_%EC%8B%9C%EC%8A%A4%ED%85%9C), 2020-07-16-Thu.
- GN Google Source, https://gn.googlesource.com/gn/, 2020-07-16-Thu.
- CMake functions, https://www.tuwlab.com/ece/27260, 2020-08-06-Thu.
- Limit visibiliy using gnu/gcc version script, https://stackoverflow.com/questions/435352/limiting-visibility-of-symbols-when-linking-shared-libraries, 2020-08-06-Thu.
- Build Wiki KR, https://ko.wikipedia.org/wiki/%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4_%EB%B9%8C%EB%93%9C, 2020-11-12-Thu.
- gcc library option, https://nicewoong.github.io/development/2018/02/24/c-library-gcc-compile/, 2020-08-07-Fri.
- Compile process, https://m.blog.naver.com/s2kiess/220058401829, 2020-08-07-Fri.
- Object file, https://m.blog.naver.com/s2kiess/220058707917, 2020-08-07-Fri.
- ELF, https://m.blog.naver.com/s2kiess/220064366133, 2020-08-07-Fri.
- LLVM, https://llvm.org/, 2020-08-07-Fri.
- LLVM Wiki KR, https://ko.wikipedia.org/wiki/LLVM, 2020-08-07-Fri.
- Clang, https://clang.llvm.org/, 2020-08-07-Fri.
- Clang Wiki KR, https://ko.wikipedia.org/wiki/%ED%81%B4%EB%9E%AD, 2020-08-07-Fri.
- GCC, https://gcc.gnu.org/, 2020-08-07-Fri.
- GCC Wiki KR, https://ko.wikipedia.org/wiki/GNU_%EC%BB%B4%ED%8C%8C%EC%9D%BC%EB%9F%AC_%EB%AA%A8%EC%9D%8C, 2020-08-07-Fri.
- CMake Public vs. Private vs. Interface Blog, https://leimao.github.io/blog/CMake-Public-Private-Interface/, 2021-03-31-Wed.
- Symbolic Link Wiki, https://en.wikipedia.org/wiki/Symbolic_link, 2021-03-31-Wed.
- CMake Blog KR, https://tttsss77.tistory.com/194, 2021-04-01-Thu.
- C/C++ Build in Windows MS Docs, https://docs.microsoft.com/en-us/cpp/build/reference/c-cpp-building-reference?view=msvc-160, 2021-04-01-Thu.
- C/C++ Compile in Windows MS Docs, https://docs.microsoft.com/en-us/cpp/build/reference/compiling-a-c-cpp-program?view=msvc-160, 2021-04-01-Thu.
- C/C++ Link in Windows MS Docs, https://docs.microsoft.com/en-us/cpp/build/reference/linking?view=msvc-160, 2021-04-01-Thu.
- Microsoft Visual C++ Wiki, https://en.wikipedia.org/wiki/Microsoft_Visual_C%2B%2B, 2021-04-01-Thu.
- Microsoft Visual C++, https://docs.microsoft.com/en-us/cpp/?view=msvc-160, 2021-04-01-Thu.
- Clang 12 Document, https://clang.llvm.org/docs/MSVCCompatibility.html, 2021-04-01-Thu.
