# Compile

## Process

### 1. Preprocessing
- foo.c -> foo.i
- Preprocessor(전처리기, cpp0)가 `#`에 대한 처리를 한다. `#include`의 라이브러리를 불러오는 역할도 한다.

### 2. Compile
- foo.i -> foo.s
- Compiler(컴파일러, cc1)가 불러온 라이브러리를 참조하여 소스코드를 어셈블리 코드로 변환한다.

### 3. Assemble
- foo.s -> foo.o
- Assembler(어셈블러, as, collect2)가 어셈블리 코드에서 기계어 코드(오브젝트 파일)로 변환한다.

### 4. Link
- foo.o -> foo (elf, exe)
- Linker(링커, ld)가 a, so 라이브러리와 연결시켜 실행 파일을 만든다.

## Compiler

### GCC (GNU C Compiler/GNU Compiler Collection) | [Homepage](https://gcc.gnu.org/) | [Wiki (Kor)](https://ko.wikipedia.org/wiki/GNU_%EC%BB%B4%ED%8C%8C%EC%9D%BC%EB%9F%AC_%EB%AA%A8%EC%9D%8C)
The GNU Compiler Collection includes front ends for C, C++, Objective-C, Fortran, Ada, Go, and D, as well as libraries for these languages (libstdc++,...). GCC was originally written as the compiler for the GNU operating system. The GNU system was developed to be 100% free software, free in the sense that it respects the user's freedom.[Ref]

GNU 컴파일러 모음(GNU Compiler Collection, 줄여서 GCC)는 GNU 프로젝트의 일환으로 개발되어 널리 쓰이고 있는 컴파일러이다.

자유 소프트웨어 중에 가장 잘 알려진 것들 중 하나인 GCC는 원래 C만을 지원했던 컴파일러로 이름도 "GNU C 컴파일러"였다. 이러한 까닭에 현재에도 GCC는 GNU 컴파일러 모음의 일부인 GNU C 컴파일러(GNU C Compiler)의 줄임말로 쓰이기도 한다. 그러나 나중에 C++, 자바, 포트란, 에이다 등 여러 언어를 컴파일할 수 있게 되면서, 현재의 이름으로 바뀌게 되었다.[Ref]

#### How to use
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
  
### LLVM (Low Level Virtual Machine) | [Homepage](https://llvm.org/) | [Wiki (Kor)](https://ko.wikipedia.org/wiki/LLVM)
The LLVM Project is a collection of modular and reusable compiler and toolchain technologies. Despite its name, LLVM has little to do with traditional virtual machines. The name "LLVM" itself is not an acronym; it is the full name of the project.[Ref]

LLVM(이전 이름: Low Level Virtual Machine)은 컴파일러의 기반구조이다. 프로그램을 컴파일 타임, 링크 타임, 런타임 상황에서 프로그램의 작성 언어에 상관없이 최적화를 쉽게 구현할 수 있도록 구성되어 있다.

LLVM은 원래는 저급 가상 기계(low-level virtual machine)의 약자를 가리켰지만, LLVM이 성장하고 다양한 목적을 가지게 되면서 현재는 그 이름을 약자로서 사용하는 것이 아니라 그냥 프로젝트의 이름으로서 사용하고 있다.

LLVM의 핵심 코드는 'LLVM 라이선스'로 배포되며, 이것은 BSD 라이선스와 비슷한 속성을 가진다. 즉, LLVM을 사용한 프로그램을 배포하였을 때 해당 소스 코드를 공개/배포해야 하는 의무가 없다. 단 LLVM의 프론트엔드를 GNU 컴파일러 모음(GCC) 기반으로 사용할 경우 프론트엔드는 GPL로 배포한다. LLVM 프로젝트에서는 LLVM 라이선스를 가지는 프론트엔드를 위해, Clang이라는 프로젝트를 진행하고 있다.[Ref]

### Clang: a C language family frontend for LLVM | [Homepage](https://clang.llvm.org/) | [Wiki (Kor)](https://ko.wikipedia.org/wiki/%ED%81%B4%EB%9E%AD)
The Clang project provides a language front-end and tooling infrastructure for languages in the C language family (C, C++, Objective C/C++, OpenCL, CUDA, and RenderScript) for the LLVM project. Both a GCC-compatible compiler driver (clang) and an MSVC-compatible compiler driver (clang-cl.exe) are provided. You can get and build the source today.[Ref]

클랭은 C, C++, 오브젝티브-C, 오브젝티브-C++ 프로그래밍 언어를 위한 컴파일러 프론트엔드이다. LLVM을 백엔드로 사용하며 LLVM 2.6 이후로 릴리즈의 일부로 자리잡았다.

목표는 GNU 컴파일러 모음 (GCC)를 대체하는 것이다. 개발은 완전히 오픈 소스이며 구글, 애플 등 대형 소프트웨어 기업의 지원을 받고 있다. 소스는 일리노이 대학교/NCSA 오픈 소스 라이선스로 이용할 수 있다.

클랭 프로젝트는 클랭 프론트엔드와 클랭 정적 분석기를 포함한다.[Ref]

## File

### Object file `.o`
- Executable object file
  - 링크까지 끝나 실행이 가능한 파일이다.
- Shared object file
  - 동적 링크가 가능한 파일이다.
- Relocatable object file
  - 링크를 하지 않은 파일, 링커를 통해 재배치가 가능하다는 뜻이다.

### Executable and Linking Format `.elf`
UNIX, Linux 환경에서 실행하는 프로그램의 바이너리 파일, 오브젝트 파일을 나타낸다.

### Library
- Linux Library
  - Static
  
  Static Library(정적 라이브러리)로 컴파일 타임에 symbol reference resolve(프로그램에 라이브러리 적재)되며 컴파일 시 라이브러리를 적재한 그 프로그램만 라이브러리 코드를 사용한다.
  
  - Shared
    - Dynamic Linking
    
    Dynamic Linking(공유 라이브러리)로 프로그램 메모리에 적재 런타임에 symbol reference resolve되며 메모리에 라이브러리 적재되어 있으면 해당 라이브러리를 사용하는 프로그램끼리 공유한다.
    
    - Dynamic Loading
    
    Dynamic Loading(동적 라이브러리)로 프로그램 실행 중 필요할 때, 즉 사용하는 응용 프로그램이 결정하는 런타임에 symbol reference resolve되며 프로그램끼리 공유한다.

### Static Library `.a` archive
컴파일 시 라이브러리를 사용해 relocatable symbol들을 reference resolving (linking)한다. 즉 컴파일 시 필요한 코드(라이브러리)를 프로그램에 적재하고 하나의 프로그램을 만들어낸다. 실행 파일은 외부 라이브러리에 대한 의존성이 없어지기 때문에 이식성이 좋고, 런타임에 외부를 참조할 필요가 없기 때문에 속도에서 장점이 있다. 하지만 코드를 프로그램에 다 적재하므로(text) 프로그램 크기가 커진다. 또한 라이브러리 변경이 필요할 시(패치) 라이브러리만 재배포하면 되는 것이 아니라 변경된 라이브러리로 컴파일하여 프로그램을 재배포 해야한다.

### Shared Library: Dynamic Linking `.so`
공유 라이브러리는 응용 프로그램이 시작되는 순간, 즉 커널이 사용자 주소 공간(VM)을 만들고 응용 프로그램(ELF)을 적재하는 순간 같이 메모리에 적재된다. 해당 라이브러리를 사용하는 다른 프로그램이 이미 실행되어 해당 라이브러리가 메모리에 있으면 그것을 참조하여 링킹한다. 없으면 라이브러리를 메모라 상에 올리고 링킹한다. 링킹 시 일어나는 reference resolving은 relocatable symbol을 실제 주소로 대체한다. 실제 정적 라이브러리를 사용할 때는 실제 주소로 대체한다. 하지만 공유 라이브러리에서는 말 그대로 공유이므로 라이브러리를 메모리에 한번만 올려두고 프로세스는 그 라이브러리의 원하는 symbol이 있는 주소를 참조만 한다. 이때 참조는 run time link editor에 의해 결정된다. 프로세스에서 이 참조를 위한 정보들을 올리는 곳은 힙과 스택 중간이다. 공유 라이브러리는 프로그램 변경 시 변경된 부분의 공유 라이브러리만 재배포하면 되므로 유지 보수가 쉽고, 유연하다. 또한 코드를 프로그램에 완전히 붙이는 것이 아니고 여러 프로그램이 한번 메모리에 올려진 것을 고유하므로 디스크, 메모리 사용 공간이 정적 라이브러리보다 적다. 하지만 외부 의존성이 생기기에 이식하기 어려우며 메모리에 올리고 찾는데 시간이 걸리므로 속도 상의 성능 저하가 있다.

### Shared Library: Dynamic Loading `.so`
동적 라이브러리(동적 적재)는 프로그램 도중 응용 프로그램에서 특정 라이브러리를 사용할지 말지를 정한다. 즉, 정적은 컴파일 타임이고 공유는 프로그램 실행 시 refernce resolving을 하는 반면에, 동적 라이브러리는 relocatable symbol을 사용할때 reference resolving을 하는 것이다. 공유 라이브러리와 같이 유연하고 확장성 높은 프로그램을 만들 수 있다. 하지만 이식성은 떨어진다.

#### How to use
- `void *dlopen(const char *library_name, int flag)`
  - `library_name`: 라이브러리를 flag에 맞추어 열고 그 핸들을 return한다.
  - `flag`
    - `RTLD_NOW`: dlopen 실행이 끝나기 전(return 전) reference resolving 함
    - `RTLD_LAZY`: run time에 특정 symbol을 사용할 때 그 symbol에 대한 reference resolving 함
- `int dlclose(void *dl_handle)`: 라이브러리 핸들을 닫는다.
- `void *dlsym(void *dl_handle, char *symbol_name)`: 라이브러리 핸들에서 특정 심볼을 가져온다.
- `const char *dlerror(void)`: 에러를 반환한다.

### Terminology
- Static Library, `.a`, `.lib`, Static Link Library
- Dynamic Library, `.so`, `.dll`, Shared Library, Dynamic Shared Object, Dynamic Loading, Dynamic Link Library

#### Reference
- gcc library option, https://nicewoong.github.io/development/2018/02/24/c-library-gcc-compile/, 2020-08-07-Fri.
- Compile process, https://m.blog.naver.com/s2kiess/220058401829, 2020-08-07-Fri.
- Object file, https://m.blog.naver.com/s2kiess/220058707917, 2020-08-07-Fri.
- ELF, https://m.blog.naver.com/s2kiess/220064366133, 2020-08-07-Fri.
- Linux library, http://blog.naver.com/PostView.nhn?blogId=xogml_blog&logNo=130138049704, 2020-08-07-Fri.
- LLVM, https://llvm.org/, 2020-08-07-Fri.
- LLVM Wiki Kor, https://ko.wikipedia.org/wiki/LLVM, 2020-08-07-Fri.
- Clang, https://clang.llvm.org/, 2020-08-07-Fri.
- Clang Wiki Kor, https://ko.wikipedia.org/wiki/%ED%81%B4%EB%9E%AD, 2020-08-07-Fri.
- GCC, https://gcc.gnu.org/, 2020-08-07-Fri.
- GCC Wiki Kor, https://ko.wikipedia.org/wiki/GNU_%EC%BB%B4%ED%8C%8C%EC%9D%BC%EB%9F%AC_%EB%AA%A8%EC%9D%8C, 2020-08-07-Fri.
- Static Linking, Dynamic Linking, https://jhnyang.tistory.com/42, 2020-08-08-Sat.
