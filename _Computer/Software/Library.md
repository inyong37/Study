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

### ELF
### ELF Symbol Visibility
Dynamic linker의 symbol resolution을 도와주는 역할을 한다. readelf로 읽는 표에서 Vis 항목은 4가지 default, hidden, protected, internal 4종류가 있다.

- default는 visibilty를고려하지 않고 해당 symbol binding이 global인지 local(static)인지를 이용한다.
- hidden은 주로 사용되는 속성으로 해당 symbol을 외부로 공개하지 않게 만든다.
- protected는 잘 사용되지 않는 속성으로 공개하지만 다른 모듈에 의해 대체되지 않는다.
- internal은 잘 사용되지 않는 속성으로 해당 symbol을 공개하지 않으며 각 architecture 별로 약간씩 다른 효과를 가질 수 있다.

default는 외부로 공개할 symbol은 전역 변수, 함수, 내부에서만 사용할 symbol은 static으로 선언하면 된다. static으로 선언한 symbol은 항상 해당 파일 내의 symbol을 접근하는 것이므로 간접 접근이 필요없이 직접 접근이 가능하므로 컴파일러가 더 빠른 코드를 만들어 낼 수 있다. 또한 symbol이 외부로 공개되지 않으므로 relocation 및 symbol resolution 시에도 고려해야할 요소가 적어지므로 추가적인 성능 향상이 있다.

### Link `ln`
`ln`은 Link의 약어로 Linux 파일 시스템에서 링크 파일을 만드는 명령어이다. Linux에서는 symbolic link와 hard link 2가지 링크 파일이 존재한다.

### Symbolic Link
단순히 원본 파일을 가리키도록 링크만 시켜둔 것으로 Windows의 shortcut과 같은 것이며, 원본 파일을 가리키고만 있으므로 원본 파일의 크기와는 무관하다. 그리고 symbolic link에서는 원본 파일이 삭제되어 존재하지 않을 경우에 링크 파일은 깜박거리면서 링크 파일의 원본 파일이 없다는 것을 알려준다.

### Hard Link
원본 파일과 다른 이름으로 존재하는 동일한 파일이며 원본 파일과 동일한 내용의 다른 파일이다. 그리고 hard link에서는 원본 파일과 링크 파일 2개가 서로 다른 파일이기 때문에 둘 중 하나를 삭제하더라도 나머지 하나는 그대로 남아 있다. 또한 hard link에서는 원본 파일의 내용이 변경될 경우에는 링크 파일의 내용 또한 자동으로 변경된다.

#### Usage
- `ln -s /tmp /var/tmp`
- `ln hard_source hard_link`
- `--backup`: 대상 파일이 이미 존재할 경우에 백업 파일을 만든 후에 링크 파일 생성
- `-b`: 링크 파일 생성 시에 대상 파일이 이미 존재하면 백업 파일을 만든 후에 링크 파일을 생성
- `-d`: 디렉토리에 대한 하드 링크 파일 생성을 가능하게 함
- `-f`: 대상 파일이 존재할 경우에 대상 파일을 지우고 링크 파일을 생성
- `-i`: 대상 파일이 존재할 경우에 대상 파일을 지울 것인가를 확인 요청
- `-s`: Create Symbolic link file 생성
- `-S`: 백업 파일 생성 시에 원하는 suffix 지정
- `-t`: 링크 파일을 생성할 디렉토리를 지정

### Circular Dependency | [Wiki](https://en.wikipedia.org/wiki/Circular_dependency)
In software engineering, a circular dependency is a relation between two or more modules which either directly or indirectly depend on each other to function properly. Such modules are also known as mutually recursive.

Circular dependencies are natural in many domain models where certain objects of the same domain depend on each other. However, in software design, circular dependencies between larger software modules are considered an anti-pattern because of their negative effects. Despite this such circular (or cyclic) dependencies have been found to be widespread among the source files of real-world software. Mutually recursive modules are, however, somewhat common in functional programming, where inductive and recursive definitions are often encouraged.[Ref]

#### Reference
- Third Party Wiki, https://en.wikipedia.org/wiki/Third-party_software_component, 2020-07-21-Tue.
- Third Party Term, https://techterms.com/definition/thirdparty, 2020-07-21-Tue.
- Plug-in Wiki, https://en.wikipedia.org/wiki/Plug-in_(computing), 2020-07-21-Tue.
- Library Wiki, https://en.wikipedia.org/wiki/Library_(computing), 2020-07-21-Tue.
- Third Party KR, https://tuhbm.github.io/2018/01/26/thirdParty/, 2020-07-21-Tue.
- Third Party KR, https://vivabin.tistory.com/2, 2020-07-21-Tue.
- ELF Symbol Visibility, http://egloos.zum.com/studyfoss/v/5257309, 2020-08-12-Wed.
- readelf, https://m.blog.naver.com/PostView.nhn?blogId=yon7961&logNo=50097076949&proxyReferer=https:%2F%2Fwww.google.com%2F, 2020-08-12-Wed.
- readelf Option, https://devanix.tistory.com/186, 2020-08-12-Wed.
- ln, https://webdir.tistory.com/148, 2020-08-13-Thu.
- Circular Dependency Wiki, https://en.wikipedia.org/wiki/Circular_dependency, 2020-08-13-Thu.
- Dependency Management, https://architecture101.blog/2008/12/07/dependency_managment/, 2020-08-13-Thu.
- How to solve circular dependecy, https://brunch.co.kr/@fishz/143, 2020-08-13-Thu.
- Does circular dependecy really need?, http://hyper-cube.io/2018/03/30/circular_dependency/, 2020-08-13-Thu.
- Dependency Analyzer, https://m.blog.naver.com/PostView.nhn?blogId=suresofttech&logNo=220729875733&proxyReferer=https:%2F%2Fwww.google.com%2F, 2020-08-13-Thu.
- Library Visibility, https://cmake.org/cmake/help/latest/command/target_link_libraries.html, 2020-08-14-Fri.
