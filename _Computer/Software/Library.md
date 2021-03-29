# *Library* | [Wiki](https://en.wikipedia.org/wiki/Library_(computing))
In computer science, a library is a collection of non-volatile resources used by computer programs, often for software development. These may include configuration data, documentation, help data, message templates, pre-written code and subroutines, classes, values or type specifications. In IBM's OS/360 and its successors they are referred to as partitioned data sets.

A library is also a collection of implementations of behavior, written in terms of a language, that has a well-defined interface by which the behavior is invoked. For instance, people who want to write a higher level program can use a library to make system calls instead of implementing those system calls over and over again. In addition, the behavior is provided for reuse by multiple independent programs. A program invokes the library-provided behavior via a mechanism of the language. For example, in a simple imperative language such as C, the behavior in a library is invoked by using C's normal function-call. What distinguishes the call as being to a library function, versus being to another function in the same program, is the way that the code is organized in the system.

Library code is organized in such a way that it can be used by multiple programs that have no connection to each other, while code that is part of a program is organized to be used only within that one program. This distinction can gain a hierarchical notion when a program grows large, such as a multi-million-line program. In that case, there may be internal libraries that are reused by independent sub-portions of the large program. The distinguishing feature is that a library is organized for the purposes of being reused by independent programs or sub-programs, and the user only needs to know the interface and not the internal details of the library.

The value of a library lies in the reuse of the behavior. When a program invokes a library, it gains the behavior implemented inside that library without having to implement that behavior itself. Libraries encourage the sharing of code in a modular fashion, and ease the distribution of the code.

The behavior implemented by a library can be connected to the invoking program at different program lifecycle phases. If the code of the library is accessed during the build of the invoking program, then the library is called a static library.[1] An alternative is to build the executable of the invoking program and distribute that, independently of the library implementation. The library behavior is connected after the executable has been invoked to be executed, either as part of the process of starting the execution, or in the middle of execution. In this case the library is called a dynamic library (loaded at runtime). A dynamic library can be loaded and linked when preparing a program for execution, by the linker. Alternatively, in the middle of execution, an application may explicitly request that a module be loaded.

Most compiled languages have a standard library although programmers can also create their own custom libraries. Most modern software systems provide libraries that implement the majority of the system services. Such libraries have commoditized the services which a modern application requires. As such, most code used by modern applications is provided in these system libraries.

# *Plug-in* | [Wiki](https://en.wikipedia.org/wiki/Plug-in_(computing))
In computing, a plug-in (or plugin, add-in, addin, add-on, or addon) is a software component that adds a specific feature to an existing computer program. When a program supports plug-ins, it enables customization.

A theme or skin is a preset package containing additional or changed graphical appearance details, achieved by the use of a graphical user interface (GUI) that can be applied to specific software and websites to suit the purpose, topic, or tastes of different users to customize the look and feel of a piece of computer software or an operating system front-end GUI (and window managers).

# *Third Party* | [Wiki](https://en.wikipedia.org/wiki/Third-party_software_component) | [Term](https://techterms.com/definition/thirdparty)
In computer programming, a third-party software component is a reusable software component developed to be either freely distributed or sold by an entity other than the original vendor of the development platform. The third-party software component market thrives because many programmers believe that component-oriented development improves the efficiency and the quality of developing custom applications. Common third-party software includes macros, bots, and software/scripts to be run as add-ons for popular developing software.

In the computer world, a third party may refer to either a hardware manufacturer or a software developer. It is a label given to companies that produce hardware or software for another company's product.

Third party hardware refers to components that are developed by companies besides the original computer manufacturer. For example, a person may buy a Dell computer and then upgrade it using third party components, such as an Nvidia video card and a Seagate hard drive. Since the components are not included with the computer and are purchased from companies other than Dell, they are considered third party hardware. These components would typically not supported by Dell, but instead would be supported by the original equipment manufacturer, or OEM.

Third party software refers to programs that are developed by companies other than the company that developed the computer's operating system. Therefore, any Macintosh applications that are not developed by Apple are considered third party applications. Likewise, any Windows programs developed by companies other than Microsoft are called third party programs. Since most programs are developed by companies other than Apple and Microsoft, third party applications make up the majority of software programs.

Some programs also support third party plug-ins, which add functionality to the software. For example, Adobe Photoshop supports plug-ins that add features like extra filters and selection tools to the program. These plug-ins may be created and distributed by other companies, but are designed to work with Adobe Photoshop. Therefore, they are called third party plug-ins.

## *Circular Dependency* | [Wiki](https://en.wikipedia.org/wiki/Circular_dependency)
In software engineering, a circular dependency is a relation between two or more modules which either directly or indirectly depend on each other to function properly. Such modules are also known as mutually recursive.

Circular dependencies are natural in many domain models where certain objects of the same domain depend on each other. However, in software design, circular dependencies between larger software modules are considered an anti-pattern because of their negative effects. Despite this such circular (or cyclic) dependencies have been found to be widespread among the source files of real-world software. Mutually recursive modules are, however, somewhat common in functional programming, where inductive and recursive definitions are often encouraged.

## *Static Library* | [Wiki](https://en.wikipedia.org/wiki/Static_library)
A static library or statically-linked library is a set of routines, external functions and varialbes which are resolved in a caller at compile-time and copied into a target application by a compiler, linker, or binder, producing and object file and a stand-alone executable. This executable and the process of compiling it are both known as a static build of the program. Historically, libraries could only be static libraries are either merged with other static libraries and object files during building/linking to form a single executable or loaded at run-time into the address space of their corresponding executable at a static memory offset determined at compile-time/link-time.

#### Reference
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
