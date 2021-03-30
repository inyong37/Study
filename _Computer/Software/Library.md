# *Library* | [Wiki](https://en.wikipedia.org/wiki/Library_(computing))
In computer science, a library is a collection of non-volatile resources used by computer programs, often for software development. These may include configuration data, documentation, help data, message templates, pre-written code and subroutines, classes, values or type specifications. In IBM's OS/360 and its successors they are referred to as partitioned data sets.

A library is also a collection of implementations of behavior, written in terms of a language, that has a well-defined interface by which the behavior is invoked. For instance, people who want to write a higher level program can use a library to make system calls instead of implementing those system calls over and over again. In addition, the behavior is provided for reuse by multiple independent programs. A program invokes the library-provided behavior via a mechanism of the language. For example, in a simple imperative language such as C, the behavior in a library is invoked by using C's normal function-call. What distinguishes the call as being to a library function, versus being to another function in the same program, is the way that the code is organized in the system.

Library code is organized in such a way that it can be used by multiple programs that have no connection to each other, while code that is part of a program is organized to be used only within that one program. This distinction can gain a hierarchical notion when a program grows large, such as a multi-million-line program. In that case, there may be internal libraries that are reused by independent sub-portions of the large program. The distinguishing feature is that a library is organized for the purposes of being reused by independent programs or sub-programs, and the user only needs to know the interface and not the internal details of the library.

The value of a library lies in the reuse of the behavior. When a program invokes a library, it gains the behavior implemented inside that library without having to implement that behavior itself. Libraries encourage the sharing of code in a modular fashion, and ease the distribution of the code.

The behavior implemented by a library can be connected to the invoking program at different program lifecycle phases. If the code of the library is accessed during the build of the invoking program, then the library is called a static library.[1] An alternative is to build the executable of the invoking program and distribute that, independently of the library implementation. The library behavior is connected after the executable has been invoked to be executed, either as part of the process of starting the execution, or in the middle of execution. In this case the library is called a dynamic library (loaded at runtime). A dynamic library can be loaded and linked when preparing a program for execution, by the linker. Alternatively, in the middle of execution, an application may explicitly request that a module be loaded.

Most compiled languages have a standard library although programmers can also create their own custom libraries. Most modern software systems provide libraries that implement the majority of the system services. Such libraries have commoditized the services which a modern application requires. As such, most code used by modern applications is provided in these system libraries.

## *Library vs. Header*
라이브러리는 기계어로 번역된 라이브러리이며, 헤더는 컴파일 하기 전의 프로그래머가 이해할 수 있고 문법에 맞게 작성되어 있는 선언들의 집합이다. 컴파일된 산물인 .o(object) 파일을 여러개 모아놓은 것이 라이브러리이다. 라이브러리를 사용하기 위해서는 해당 라이브러리의 헤더가 필요하다. 링커가 이해할 수 있는 symbol name을 가지고 library를 찾아 link하게 된다. compilier가 이런 header를 가지고 symbol name을 만들어서 object 파일을 넣어주면 linker가 해당 symbol name을 가지고 library를 검색해서 link하게 된다.

# *Plug-in* | [Wiki](https://en.wikipedia.org/wiki/Plug-in_(computing))
In computing, a plug-in (or plugin, add-in, addin, add-on, or addon) is a software component that adds a specific feature to an existing computer program. When a program supports plug-ins, it enables customization.

A theme or skin is a preset package containing additional or changed graphical appearance details, achieved by the use of a graphical user interface (GUI) that can be applied to specific software and websites to suit the purpose, topic, or tastes of different users to customize the look and feel of a piece of computer software or an operating system front-end GUI (and window managers).

# *Third Party* | [Wiki](https://en.wikipedia.org/wiki/Third-party_software_component) | [Term](https://techterms.com/definition/thirdparty)
In computer programming, a third-party software component is a reusable software component developed to be either freely distributed or sold by an entity other than the original vendor of the development platform. The third-party software component market thrives because many programmers believe that component-oriented development improves the efficiency and the quality of developing custom applications. Common third-party software includes macros, bots, and software/scripts to be run as add-ons for popular developing software.

In the computer world, a third party may refer to either a hardware manufacturer or a software developer. It is a label given to companies that produce hardware or software for another company's product.

Third party hardware refers to components that are developed by companies besides the original computer manufacturer. For example, a person may buy a Dell computer and then upgrade it using third party components, such as an Nvidia video card and a Seagate hard drive. Since the components are not included with the computer and are purchased from companies other than Dell, they are considered third party hardware. These components would typically not supported by Dell, but instead would be supported by the original equipment manufacturer, or OEM.

Third party software refers to programs that are developed by companies other than the company that developed the computer's operating system. Therefore, any Macintosh applications that are not developed by Apple are considered third party applications. Likewise, any Windows programs developed by companies other than Microsoft are called third party programs. Since most programs are developed by companies other than Apple and Microsoft, third party applications make up the majority of software programs.

Some programs also support third party plug-ins, which add functionality to the software. For example, Adobe Photoshop supports plug-ins that add features like extra filters and selection tools to the program. These plug-ins may be created and distributed by other companies, but are designed to work with Adobe Photoshop. Therefore, they are called third party plug-ins.

## *Library Types*
- Linux Library
  - Static
  
  Static Library(정적 라이브러리)로 컴파일 타임에 symbol reference resolve(프로그램에 라이브러리 적재)되며 컴파일 시 라이브러리를 적재한 그 프로그램만 라이브러리 코드를 사용한다.
  
  - Shared
    - Dynamic Linking
    
    Dynamic Linking(공유 라이브러리)로 프로그램 메모리에 적재 런타임에 symbol reference resolve되며 메모리에 라이브러리 적재되어 있으면 해당 라이브러리를 사용하는 프로그램끼리 공유한다.
    
    - Dynamic Loading
    
    Dynamic Loading(동적 라이브러리)로 프로그램 실행 중 필요할 때, 즉 사용하는 응용 프로그램이 결정하는 런타임에 symbol reference resolve되며 프로그램끼리 공유한다.

### *Static Library* | [Wiki](https://en.wikipedia.org/wiki/Static_library)
`"Static Library"는 compile-time에 실행 가능한 파일 또는 오브젝트 파일에 복사되는 라이브러리이다.`

A static library or statically-linked library is a set of routines, external functions and variables which are resolved in a caller at compile-time and copied into a target application by a compiler, linker, or binder, producing and object file and a stand-alone executable. This executable and the process of compiling it are both known as a static build of the program. Historically, libraries could only be static libraries are either merged with other static libraries and object files during building/linking to form a single executable or loaded at run-time into the address space of their corresponding executable at a static memory offset determined at compile-time/link-time.

### *Static Library: `.a` archive*
컴파일 시 라이브러리를 사용해 relocatable symbol들을 reference resolving (linking)한다. 즉 컴파일 시 필요한 코드(라이브러리)를 프로그램에 적재하고 하나의 프로그램을 만들어낸다. 실행 파일은 외부 라이브러리에 대한 의존성이 없어지기 때문에 이식성이 좋고, 런타임에 외부를 참조할 필요가 없기 때문에 속도에서 장점이 있다. 하지만 코드를 프로그램에 다 적재하므로(text) 프로그램 크기가 커진다. 또한 라이브러리 변경이 필요할 시(패치) 라이브러리만 재배포하면 되는 것이 아니라 변경된 라이브러리로 컴파일하여 프로그램을 재배포 해야한다.

### *Shared Library*
`"Shared Library"는 실행 가능한 파일 또는 오브젝트 파일이 공유해서 사용할 수 있는 라이브러리이다. 모듈은 실행 파일을 생성할 때 복사되지 않고 load/run-time에 메모리에 로드된다.`

A shared library or shared object is a file that is intended to be shared by executable files and further shared object files. Modules used by a program are loaded from individual shared objects into memory at load time or runtime, rather than being copied by a linker when it creates a single monolithic executable file for the program. Shared libraries can be statically linked during compile-time, meaning that references to the library modules are resolved and the modules are allocated memory when the executable file is created. But often linking of shared libraries is postponed until they are loaded.

### *Shared Library: Dynamic Linking `.so`*
공유 라이브러리는 응용 프로그램이 시작되는 순간, 즉 커널이 사용자 주소 공간(VM)을 만들고 응용 프로그램(ELF)을 적재하는 순간 같이 메모리에 적재된다. 해당 라이브러리를 사용하는 다른 프로그램이 이미 실행되어 해당 라이브러리가 메모리에 있으면 그것을 참조하여 링킹한다. 없으면 라이브러리를 메모라 상에 올리고 링킹한다. 링킹 시 일어나는 reference resolving은 relocatable symbol을 실제 주소로 대체한다. 실제 정적 라이브러리를 사용할 때는 실제 주소로 대체한다. 하지만 공유 라이브러리에서는 말 그대로 공유이므로 라이브러리를 메모리에 한번만 올려두고 프로세스는 그 라이브러리의 원하는 symbol이 있는 주소를 참조만 한다. 이때 참조는 run time link editor에 의해 결정된다. 프로세스에서 이 참조를 위한 정보들을 올리는 곳은 힙과 스택 중간이다. 공유 라이브러리는 프로그램 변경 시 변경된 부분의 공유 라이브러리만 재배포하면 되므로 유지 보수가 쉽고, 유연하다. 또한 코드를 프로그램에 완전히 붙이는 것이 아니고 여러 프로그램이 한번 메모리에 올려진 것을 고유하므로 디스크, 메모리 사용 공간이 정적 라이브러리보다 적다. 하지만 외부 의존성이 생기기에 이식하기 어려우며 메모리에 올리고 찾는데 시간이 걸리므로 속도 상의 성능 저하가 있다.

### *Shared Library: Dynamic Loading `.so`*
동적 라이브러리(동적 적재)는 프로그램 도중 응용 프로그램에서 특정 라이브러리를 사용할지 말지를 정한다. 즉, 정적은 컴파일 타임이고 공유는 프로그램 실행 시 refernce resolving을 하는 반면에, 동적 라이브러리는 relocatable symbol을 사용할때 reference resolving을 하는 것이다. 공유 라이브러리와 같이 유연하고 확장성 높은 프로그램을 만들 수 있다. 하지만 이식성은 떨어진다.

#### *How to use dynamic loading*
- `void *dlopen(const char *library_name, int flag)`
  - `library_name`: 라이브러리를 flag에 맞추어 열고 그 핸들을 return한다.
  - `flag`
    - `RTLD_NOW`: dlopen 실행이 끝나기 전(return 전) reference resolving 함
    - `RTLD_LAZY`: run time에 특정 symbol을 사용할 때 그 symbol에 대한 reference resolving 함
- `int dlclose(void *dl_handle)`: 라이브러리 핸들을 닫는다.
- `void *dlsym(void *dl_handle, char *symbol_name)`: 라이브러리 핸들에서 특정 심볼을 가져온다.
- `const char *dlerror(void)`: 에러를 반환한다.

### *Terminology*
- Static Library, `.a`, `.lib`, Static Link Library
- Dynamic Library, `.so`, `.dll`, Shared Library, Dynamic Shared Object, Dynamic Loading, Dynamic Link Library

### *Circular Dependency* | [Wiki](https://en.wikipedia.org/wiki/Circular_dependency)
In software engineering, a circular dependency is a relation between two or more modules which either directly or indirectly depend on each other to function properly. Such modules are also known as mutually recursive.

Circular dependencies are natural in many domain models where certain objects of the same domain depend on each other. However, in software design, circular dependencies between larger software modules are considered an anti-pattern because of their negative effects. Despite this such circular (or cyclic) dependencies have been found to be widespread among the source files of real-world software. Mutually recursive modules are, however, somewhat common in functional programming, where inductive and recursive definitions are often encouraged.

Windows shared library 사용에는 Unix보다 엄격한 기준을 가지고 있다. Unix에서는 unresolved symbol을 포함한 shared library를 링크할 수 있다. 대신 다른 shard library에서 해당 symbol을 제공해줘야 한다. 그렇지 않으면 program 로드가 실패한다. Windows에서는 해당 경우를 허용하지 않는다.

많은 시스템에서는 이것은 문제가 되지 않는다. 실행 파일은 high-level 라이브러리들을 의존하고, high-level 라이브러리들은 low-level 라이브러리들에 의존하고, 링크는 반대 순서이다. low-level 라이브러리들, high-level 라이브러리들, 마지막으로 실행 파일을 링크한다.

하지만 바이너리끼리 circular dependencies가 존재하면, 문제가 달라진다. 만약 X.DLL이 Y.DLL의 심볼을 필요로 하지만, Y.DLL 또한 X.DLL 심볼을 필요로 하면 chicken-and-egg 문제가 발생한다. 어떤 라이브버리를 먼저 링크해도 필요한 모든 심볼들을 찾을 수 없다.

Windows에서는 다른 방법을 제공한다. 먼저 라이브러리 X에 대해서 가짜로 링크를 한다. LIB.EXE를 사용해서 X.LIB을 만든다. 이는 LINK.EXE를 사용해서 만드는 파일과 같아 보이지만 X.EXP 파일은 생략되어 있다. 그리고 일반적인 방법과 같이 라이브러리 Y를 링크한다. X.LIB를 pull하고 Y.DLL, Y.LIB 파일이 생성된다. 마지막으로 X를 일반적인 방법으로 링크한다. 하지만 첫 단계와 다른 점은 추가로 X.EXP 파일을 포함한다. 이 링크를 통해 Y.LIB을 pull하고 X.DLL을 만들게 된다. 이 때 일반적일 때와 달리 이미 생성되어 있는 X.LIB 파일 생성을 생략하게 된다.

#### Reference
- Linux library, http://blog.naver.com/PostView.nhn?blogId=xogml_blog&logNo=130138049704, 2020-08-07-Fri.
- Static Linking, Dynamic Linking, https://jhnyang.tistory.com/42, 2020-08-08-Sat.
- Library Wiki, https://en.wikipedia.org/wiki/Library_(computing), 2020-07-21-Tue.
- Plug-in Wiki, https://en.wikipedia.org/wiki/Plug-in_(computing), 2020-07-21-Tue.
- Third Party Wiki, https://en.wikipedia.org/wiki/Third-party_software_component, 2020-07-21-Tue.
- Third Party Term, https://techterms.com/definition/thirdparty, 2020-07-21-Tue.
- Third Party Blog KR, https://tuhbm.github.io/2018/01/26/thirdParty/, 2020-07-21-Tue.
- Third Party Blog KR, https://vivabin.tistory.com/2, 2020-07-21-Tue.
- Circular Dependency Wiki, https://en.wikipedia.org/wiki/Circular_dependency, 2020-08-13-Thu.
- How to solve circular dependecy, https://brunch.co.kr/@fishz/143, 2020-08-13-Thu.
- Does circular dependecy really need?, http://hyper-cube.io/2018/03/30/circular_dependency/, 2020-08-13-Thu.
- Dependency Analyzer Blog KR, https://m.blog.naver.com/PostView.nhn?blogId=suresofttech&logNo=220729875733&proxyReferer=https:%2F%2Fwww.google.com%2F, 2020-08-13-Thu.
- Static Library Wiki, https://en.wikipedia.org/wiki/Static_library, 2021-03-29-Mon.
- Beginner's Guide to Linkers, https://www.lurklurk.org/linkers/linkers.html#wincircular, 2021-03-30-Tue.
- CMake Cyclic Dependencies of Static Libraries, https://cmake.org/cmake/help/latest/command/target_link_libraries.html#cyclic-dependencies-of-static-libraries, 2021-03-30-Tue.
