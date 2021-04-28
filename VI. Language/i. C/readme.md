# C | [Wiki](https://en.wikipedia.org/wiki/C_(programming_language)) | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/C_(%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D_%EC%96%B8%EC%96%B4))
```
This page is from the "Language" page.
```
C는 1972년 켄 톰슨과 데니스 리치가 벨 연구소에서 일할 당시 새로 개발된 유닉스 운영 체제에서 사용하기 위해 개발한 프로그래밍 언어이다. 켄 톰슨은 BCPL언어를 필요에 맞추어 개조해서 B언어(언어를 개발한 벨 연구소의 B를 땀)라 명명했고 데니스 리치가 이것을 개선하여 C언어가 탄생했다. 유닉스 시스템의 바탕 프로그램은 모두 C로 작성되었고 수많은 운영 체제의 커널 또한 C로 만들어졌다. 오늘날 많이 쓰이는 C++는 C에서 객체 지향형 언어로 발전된 것이다. 또 다른 다양한 최신 언어들도 그 뿌리를 C에 두고 있다.

C (/siː/, as in the letter c) is a general-purpose, procedural computer programming language supporting structured programming, lexical variable scope, and recursion, while a static type system prevents unintended operations. By design, C provides constructs that map efficiently to typical machine instructions and has found lasting use in applications previously coded in assembly language. Such applications include operating systems and various application software for computers, from supercomputers to embedded systems. C was originally developed at Bell Labs by Dennis Ritchie between 1972 and 1973 to make utilities running on Unix. Later, it was applied to re-implementing the kernel of the Unix operating system. During the 1980s, C gradually gained popularity. It has become one of the most widely used programming languages, with C compilers from various vendors available for the majority of existing computer architectures and operating systems. C has been standardized by the ANSI since 1989 (see ANSI C) and by the International Organization for Standardization. C is an imperative procedural language. It was designed to be compiled using a relatively straightforward compiler to provide low-level access to memory and language constructs that map efficiently to machine instructions, all with minimal runtime support. Despite its low-level capabilities, the language was designed to encourage cross-platform programming. A standards-compliant C program written with portability in mind can be compiled for a wide variety of computer platforms and operating systems with few changes to its source code. The language is available on various platforms, from embedded microcontrollers to supercomputers.

- Tool: Visual Studio (by Microsoft), CLion (by JetBrains), CppCode (by Apple)

### Visual Stuido | [Homepage](https://visualstudio.microsoft.com/)

### C 시그널 처리
표준 라이브러리에서 시그널 처리는 프로그램이 실행 중에 다양한 시그널들을 어떻게 처리하는지를 정의한다. 시그널은 프로그램 내에서 몇몇 예외적인 행위를 보고하거나, 프로그램 외부의 비동기적 이벤트를 보고할 수 있다. C 표준 시그널에는 6개가 있따. 이것들은 모두 `signal.h`에 정의되어 있다. (C++의 경우 csignal.h) 1. `SIGABRT` "abort" 비정상 종료, 2. `SIGFPE` 부동소수점, 3. `SIGILL` "illegal" 유효하지 않은 명령어, 4. `SIGINT` "interrupt" 프로그램에 보내진 상호적인 요청, 5. `SIGSEGV` "segmentation violation" 유효하지 않은 메모리 접근, 6. `SIGTERM` "terminate" 프로그램에 보내진 종료 요청이다. 유닉스 계열의 운영 체제는 15개 이상의 추가적인 시그널이 있다. 

## C Language Reference | [MS Docs](https://docs.microsoft.com/en-us/cpp/c-language/c-language-reference?view=msvc-160)

#### Referece
- C, https://en.wikipedia.org/wiki/C_(programming_language), 2020-04-12-Sun.
- C signal process Wiki KR-KO, https://ko.wikipedia.org/wiki/C_%EC%8B%9C%EA%B7%B8%EB%84%90_%EC%B2%98%EB%A6%AC, 2020-11-02-Mon.
- C Wiki KR-KO, https://ko.wikipedia.org/wiki/C_(%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D_%EC%96%B8%EC%96%B4), 2020-11-02-Mon.
- C Language Reference, https://docs.microsoft.com/en-us/cpp/c-language/c-language-reference?view=msvc-160, 2021-04-28-Wed.
