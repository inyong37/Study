# [Java](https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-java-programming-language)

```
This page is from the "Language" page.
```

Java is a multiplatform, object-oriented programming language that runs on billions of devices worldwide. It powers applications, smartphone operating systems, enterprise software, and many well-known programs. Despite having been invented over 20 years ago, Java is currently the most popular programming language for app developers. 

Java was invented by James Gosling in 1995 while he was working at Sun Microsystems. Though it quickly gained popularity after its release, Java didn't start out as the powerhouse programming language it is today.

---

### :computer: [Eclipse](https://www.eclipse.org/)

- Key
  - `Control` `l`: go to # line
  - `Control` `f`: find 'word' in this code
  - `Control` `h`: search 'word' in a whole directory

### :computer: [IntelliJ](https://www.jetbrains.com/idea/)

---

### JDK (Java Development Kit) | [Wiki](https://en.wikipedia.org/wiki/Java_Development_Kit)

The Java Development Kit (JDK) is an implementation of either one of the Java Platform, Standard Edition, Java Platform, Enterprise Edition, or Java Platform, Micro Edition platforms released by Oracle Corporation in the form of a binary product aimed at Java developers on Solaris, Linux, macOS or Windows. The JDK includes a private JVM and a few other resources to finish the development of a Java application.[2] Since the introduction of the Java platform, it has been by far the most widely used Software Development Kit (SDK).

### [OpenJDK](https://openjdk.java.net/) | [Wiki](https://en.wikipedia.org/wiki/OpenJDK) | [OpenJDK 15 Download](https://jdk.java.net/15/)

The place to collaborate on an open-source implementation of the Java Platform, Standard Edition, and related projects.

OpenJDK (Open Java Development Kit) is a free and open-source implementation of the Java Platform, Standard Edition (Java SE). It is the result of an effort Sun Microsystems began in 2006. The implementation is licensed under the GNU General Public License (GNU GPL) version 2 with a linking exception. Were it not for the GPL linking exception, components that linked to the Java class library would be subject to the terms of the GPL license. OpenJDK is the official reference implementation of Java SE since version 7.

### JRE (Java Runtime Environment) | [Wiki in JDK](https://en.wikipedia.org/wiki/Java_Development_Kit)

The Java Runtime Environment (JRE) released by Oracle is a freely available software distribution containing a stand-alone JVM (HotSpot), the Java standard library (Java Class Library), a configuration tool, and—until its discontinuation in JDK 9—a browser plug-in. It is the most common Java environment installed on personal computers in the laptop and desktop form factor. Mobile phones including feature phones and early smartphones that ship with a JVM are most likely to include a JVM meant to run applications targeting Micro Edition of the Java platform. Meanwhile, most modern smartphones, tablet computers, and other handheld PCs that run Java apps are most likely to do so through support of the Android operating system, which includes an open source virtual machine incompatible with the JVM specification. (Instead, Google's Android development tools take Java programs as input and output Dalvik bytecode, which is the native input format for the virtual machine on Android devices.)

JDK 11 버전 이후로는 JRE가 포함되지 않는다.

### JVM (Java Virtual Machine) | [Wiki](https://en.wikipedia.org/wiki/Java_virtual_machine)

A Java virtual machine (JVM) is a virtual machine that enables a computer to run Java programs as well as programs written in other languages that are also compiled to Java bytecode. The JVM is detailed by a specification that formally describes what is required in a JVM implementation. Having a specification ensures interoperability of Java programs across different implementations so that program authors using the Java Development Kit (JDK) need not worry about idiosyncrasies of the underlying hardware platform.

The JVM reference implementation is developed by the OpenJDK project as open source code and includes a JIT compiler called HotSpot. The commercially supported Java releases available from Oracle Corporation are based on the OpenJDK runtime. Eclipse OpenJ9 is another open source JVM for OpenJDK.

### Paid? Oracle JDK vs OpenJDK
Commercial version JDK is Oracle JDK and open source based JDK is OpenJDK. Oracle JDK has some pulgin used to pay, from Sun Microsystems

---

## [Spring](https://spring.io/)

Spring can do microservices, reactive, cloud, web apps, serverless, event driven, and batch.

### [Spring Boot](https://spring.io/projects/spring-boot)

Spring Boot makes it easy to create stand-alone, production-grade Spring based Applications that you can just run.

### [Spring Framework](https://spring.io/projects/spring-boot) | [Blog (KR)](https://devscb.tistory.com/119) | [Blog (KR)](https://zinisang.tistory.com/62)

The Spring Framework provides a comprehensive programming and configuration model for modern Java-based enterprise applications - on any kind of deployment platform.

Components:
* ServletContainer: client(browser)로부터 http 요청을 받아 servlet 로직을 처리할 수 있는 componenta
  * Servlet: servlet이란 javax.servlet 패키지에 정의된 인터페이스로, 자바 클래스 파일로 된 서버 로직임 
* Spring: spring framework 영역
* DispatcherServlet: spring framework에서 front controller로, 실제 동작하기 위한 로직 요청에 대해 처리할 수 있도록 함
  * Dispatch: 요청이 오면 실제로 로직을 수행할 component로 요청을 보내주고 반환을 받는 역할을 함
* HandlerMapping: spring framework에 작성된 여러 컨트롤러들 중에서 로직을 수행할 컨트롤러를 확인하는 component임
* Controller: http request를 처리할 수 있도록 개발자가 작성한 component
* Service: 비지니스 로직을 수행하는 개발자가 작성한 component
* DAO: Database에 직접 접근하는 개발자가 작성한 객체
* ViewResolver: ViewName을 기반으로 어떤 View 파일을 사용할 것인지 확인하는 component
* View: 개발자가 작성한 UI 화면

Sequence:
* `Client` - `Servlet Container` - `DispatcherServlet` - `HandlerMapping` - `Controller` - `Service` - `DAO` - `DB`
* `ViewResolver` - `View`
1. `Client` -> `ServletContainer`: http 요청
2. `ServletContainer` -> `DispatcherServlet`: http request 객체 전달
3. `DispatcherServlet` -> `HandlerMapping`: 어떤 controller를 호출할지 확인
4. `DispatcherServlet` <- `HandlerMapping`: http 요청을 실행할 Controller 반환
5. `DispatcherServlet` --> `Controller`: http request 객체 전달
6. `Controller` -> `Service`: 서비스 호출
7. `Service` -> `DAO`: Data 접근 호출
8. `DAO` -> `DB`: DB 접근
9. `DAO` <- `DB`: DTO/VO 반환
10. `Service` <- `DAO`: DTO/VO 반환
11. `Controller` <- `Service`: 호출 결과 반환
12. `DispatcherServlet` <-- `Controller`: 로직 수행 후 처리할 ViewName과 Model 반환
13. `DispatcherServlet` ------> `ViewResolver`: ViewName 전달
14. `DispatcherServlet` <------ `ViewResolver`: ViewName에 매핑된 View 파일 전달
15. `DispatcherServlet` -------> `View`: Model 전달
16. `DispatcherServlet` <------- `View`: Model과 View를 조합하여 최종 결과의 View 전달
17. `ServletContainer` <- `DispatcherServlet`: http response 반환
18. `Client` <- `ServletContainer`: http 응답

XML:
* web.xml: 요청이랑 상관없이 미리 등록함
* root-context.xml: 미리 등록해 놓아야할 객체들
* mybatis-config.xml: mapping 객체 및 SQL mapper 파일
* Mapper.xml: SQL 쿼리
* servlet-context.xml: 요청이 들어왔을 때 등록해 놓아야할 객체들
* pom.xml: Maven 설정

### [MyBatis](https://mybatis.org/mybatis-3/)

MyBatis is a first class persistence framework with support for custom SQL, stored procedures and advanced mappings. MyBatis eliminates almost all of the JDBC code and manual setting of parameters and retrieval of results. MyBatis can use simple XML or Annotations for configuration and map primitives, Map interfaces and Java POJOs (Plain Old Java Objects) to database records.

### [Gradle](https://gradle.org/) | [Building Java Projects with Gradle](https://spring.io/guides/gs/gradle/)

Gradle build tool is a fast, dependable, and adaptable open-source build automation tool with an elegant and extensible declarative build language. Gradle supports Android, Java, Kotlin Multiplatform, Groovy, Scala, Javascript, and C/C++.

---

### Plain Old Java Object (POJO)

POJO is an ordinary Java object that does not have references to any particular framework. It's a term used to refer to a simple, lightweight Java object. A POJO does not use any naming convention for properties and methods.

### JavaBean

A JavaBean is mostly like a POJO, with some strict set of rules on how to implement it. The rules specify that it should be serializable, have a null constructor, and allow access to variable using methods that follow the getX() and setX() convention.

### Data Access Object (DAO) | [Blog (KR)](https://m.blog.naver.com/cjhol2107/221757079506)

Database의 data에 접근하기 위한 object. Database 접근 로직과 비즈니스 로직을 분리하기 위해 사용한다. MyBatis 등을 사용할 경우 connection pool까지 제공되어 DAO를 별도로 만드는 경우는 드물다.

### Data Transfer Object (DTO) | [Blog (KR)](https://m.blog.naver.com/cjhol2107/221757079506)

A DTO encapsulates values to carry data between processes or networks. This helps in reducing the number of methods called. By including multiple parameters or values in a single call, we reduce the network overhead in remote operations. One more advantage of this pattern is the encapsulation of the serialization's logic. It lets the program store and transfer data in a specific format. A DTO does not have any explicity behavior. It basically helps in making the code loosely coupled by decoupling the domain models from the presentation layer.

Database 레코드의 data를 매핑하기 위한 데이터 object이다. DTO는 보통 로직을 갖지 않고 data와 그 data에 접근을 위한 getter, setter만 갖는다. 즉, DTO는 database에서 data를 얻어 service나 controller 등으로 보낼 때 사용하는 object를 말한다.

### Value Object (VO)

VO is a special type of object that can hold values such as java.lang.Integer and java.lang.Long. A VO should always override the equals() and hashCode() methods. VOs generally encapsulate small objects such as numbers, dates, strings, and more. They follow the value semantics, i.e., they directly change the object's value and pass copies around instead of references. It's a good practice to make Value Objects immutable. The change in values occurs only by creating a new object and not by updating values in the old object itself. This helps in understanding the implicit contract that two Value Objects created equal should remain equal.

VO는 immutable하다.

---

### Reference
- JAVA, https://docs.oracle.com/javase/7/docs/technotes/guides/language/, 2020-04-02-Thu.
- Java Paid?, https://mine-it-record.tistory.com/7, 2020-08-10-Mon.
- OpenJDK, https://openjdk.java.net/, 2020-09-22-Tue.
- OpenJDK Wiki, https://en.wikipedia.org/wiki/OpenJDK, 2020-09-22-Tue.
- JDK Wiki, https://en.wikipedia.org/wiki/Java_Development_Kit, 2020-09-22-Tue.
- JVM Wiki, https://en.wikipedia.org/wiki/Java_virtual_machine, 2020-09-22-Tue.
- Java Objects, https://www.baeldung.com/java-pojo-javabeans-dto-vo, 2023-10-31-Tue.
- Spring, https://spring.io/, 2023-11-01-Wed.
- Spring Boot, https://spring.io/projects/spring-boot, 2023-11-01-Wed.
- Spring Framework, https://spring.io/projects/spring-boot, 2023-11-01-Wed.
- DAO DTO VO Blog KR, https://m.blog.naver.com/cjhol2107/221757079506, 2023-11-01-Wed.
- MyBatis, https://mybatis.org/mybatis-3/, 2023-11-01-Wed.
- Java Microsoft, https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-java-programming-language, 2023-11-09-Thu.
- Gradle, https://gradle.org/, 2023-11-09-Thu.
- Gradle, https://gradle.com/, 2023-11-09-Thu.
- Spring Gradle, https://spring.io/guides/gs/gradle/, 2023-11-09-Thu.
- Spring Architecture Blog KR, https://devscb.tistory.com/119, 2023-12-11-Mon.
- Spring XML Blog KR, https://zinisang.tistory.com/62, 2023-12-12-Tue.
