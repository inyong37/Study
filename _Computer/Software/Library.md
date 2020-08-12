## Library | [Wiki](https://en.wikipedia.org/wiki/Library_(computing))
In computer science, a library is a collection of non-volatile resources used by computer programs, often for software development. These may include configuration data, documentation, help data, message templates, pre-written code and subroutines, classes, values or type specifications. In IBM's OS/360 and its successors they are referred to as partitioned data sets.

A library is also a collection of implementations of behavior, written in terms of a language, that has a well-defined interface by which the behavior is invoked. For instance, people who want to write a higher level program can use a library to make system calls instead of implementing those system calls over and over again. In addition, the behavior is provided for reuse by multiple independent programs. A program invokes the library-provided behavior via a mechanism of the language. For example, in a simple imperative language such as C, the behavior in a library is invoked by using C's normal function-call. What distinguishes the call as being to a library function, versus being to another function in the same program, is the way that the code is organized in the system.

Library code is organized in such a way that it can be used by multiple programs that have no connection to each other, while code that is part of a program is organized to be used only within that one program. This distinction can gain a hierarchical notion when a program grows large, such as a multi-million-line program. In that case, there may be internal libraries that are reused by independent sub-portions of the large program. The distinguishing feature is that a library is organized for the purposes of being reused by independent programs or sub-programs, and the user only needs to know the interface and not the internal details of the library.

The value of a library lies in the reuse of the behavior. When a program invokes a library, it gains the behavior implemented inside that library without having to implement that behavior itself. Libraries encourage the sharing of code in a modular fashion, and ease the distribution of the code.

The behavior implemented by a library can be connected to the invoking program at different program lifecycle phases. If the code of the library is accessed during the build of the invoking program, then the library is called a static library.[1] An alternative is to build the executable of the invoking program and distribute that, independently of the library implementation. The library behavior is connected after the executable has been invoked to be executed, either as part of the process of starting the execution, or in the middle of execution. In this case the library is called a dynamic library (loaded at runtime). A dynamic library can be loaded and linked when preparing a program for execution, by the linker. Alternatively, in the middle of execution, an application may explicitly request that a module be loaded.

Most compiled languages have a standard library although programmers can also create their own custom libraries. Most modern software systems provide libraries that implement the majority of the system services. Such libraries have commoditized the services which a modern application requires. As such, most code used by modern applications is provided in these system libraries.

## Plug-in | [Wiki](https://en.wikipedia.org/wiki/Plug-in_(computing))
In computing, a plug-in (or plugin, add-in, addin, add-on, or addon) is a software component that adds a specific feature to an existing computer program. When a program supports plug-ins, it enables customization.

A theme or skin is a preset package containing additional or changed graphical appearance details, achieved by the use of a graphical user interface (GUI) that can be applied to specific software and websites to suit the purpose, topic, or tastes of different users to customize the look and feel of a piece of computer software or an operating system front-end GUI (and window managers).[Ref]

## Third Party | [Wiki](https://en.wikipedia.org/wiki/Third-party_software_component) | [Term](https://techterms.com/definition/thirdparty)
In computer programming, a third-party software component is a reusable software component developed to be either freely distributed or sold by an entity other than the original vendor of the development platform. The third-party software component market thrives because many programmers believe that component-oriented development improves the efficiency and the quality of developing custom applications. Common third-party software includes macros, bots, and software/scripts to be run as add-ons for popular developing software.[Ref]

In the computer world, a third party may refer to either a hardware manufacturer or a software developer. It is a label given to companies that produce hardware or software for another company's product.

Third party hardware refers to components that are developed by companies besides the original computer manufacturer. For example, a person may buy a Dell computer and then upgrade it using third party components, such as an Nvidia video card and a Seagate hard drive. Since the components are not included with the computer and are purchased from companies other than Dell, they are considered third party hardware. These components would typically not supported by Dell, but instead would be supported by the original equipment manufacturer, or OEM.

Third party software refers to programs that are developed by companies other than the company that developed the computer's operating system. Therefore, any Macintosh applications that are not developed by Apple are considered third party applications. Likewise, any Windows programs developed by companies other than Microsoft are called third party programs. Since most programs are developed by companies other than Apple and Microsoft, third party applications make up the majority of software programs.

Some programs also support third party plug-ins, which add functionality to the software. For example, Adobe Photoshop supports plug-ins that add features like extra filters and selection tools to the program. These plug-ins may be created and distributed by other companies, but are designed to work with Adobe Photoshop. Therefore, they are called third party plug-ins.[Ref]

## ELF
### ELF Symbol Visibility
Dynamic linker의 symbol resolution을 도와주는 역할을 한다. readelf로 읽는 표에서 Vis 항목은 4가지 default, hidden, protected, internal 4종류가 있다.

- default는 visibilty를고려하지 않고 해당 symbol binding이 global인지 local(static)인지를 이용한다.
- hidden은 주로 사용되는 속성으로 해당 symbol을 외부로 공개하지 않게 만든다.
- protected는 잘 사용되지 않는 속성으로 공개하지만 다른 모듈에 의해 대체되지 않는다.
- internal은 잘 사용되지 않는 속성으로 해당 symbol을 공개하지 않으며 각 architecture 별로 약간씩 다른 효과를 가질 수 있다.

default는 외부로 공개할 symbol은 전역 변수, 함수, 내부에서만 사용할 symbol은 static으로 선언하면 된다. static으로 선언한 symbol은 항상 해당 파일 내의 symbol을 접근하는 것이므로 간접 접근이 필요없이 직접 접근이 가능하므로 컴파일러가 더 빠른 코드를 만들어 낼 수 있다. 또한 symbol이 외부로 공개되지 않으므로 relocation 및 symbol resolution 시에도 고려해야할 요소가 적어지므로 추가적인 성능 향상이 있다.

## Reference
- Third Party Wiki, https://en.wikipedia.org/wiki/Third-party_software_component, 2020-07-21-Tue.
- Third Party Term, https://techterms.com/definition/thirdparty, 2020-07-21-Tue.
- Plug-in Wiki, https://en.wikipedia.org/wiki/Plug-in_(computing), 2020-07-21-Tue.
- Library Wiki, https://en.wikipedia.org/wiki/Library_(computing), 2020-07-21-Tue.
- Third Party Kor, https://tuhbm.github.io/2018/01/26/thirdParty/, 2020-07-21-Tue.
- Third Party Kor, https://vivabin.tistory.com/2, 2020-07-21-Tue.
- ELF Symbol Visibility, http://egloos.zum.com/studyfoss/v/5257309, 2020-08-12-Wed.
- readelf, https://m.blog.naver.com/PostView.nhn?blogId=yon7961&logNo=50097076949&proxyReferer=https:%2F%2Fwww.google.com%2F, 2020-08-12-Wed.
- readelf Option, https://devanix.tistory.com/186, 2020-08-12-Wed.
