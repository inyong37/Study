# C
```
This page is from the "Language" page.
```
## Visual Stuido | [Homepage](https://visualstudio.microsoft.com/)

### C 시그널 처리
표준 라이브러리에서 시그널 처리는 프로그램이 실행 중에 다양한 시그널들을 어떻게 처리하는지를 정의한다. 시그널은 프로그램 내에서 몇몇 예외적인 행위를 보고하거나, 프로그램 외부의 비동기적 이벤트를 보고할 수 있다. C 표준 시그널에는 6개가 있따. 이것들은 모두 `signal.h`에 정의되어 있다. (C++의 경우 csignal.h) 1. `SIGABRT` "abort" 비정상 종료, 2. `SIGFPE` 부동소수점, 3. `SIGILL` "illegal" 유효하지 않은 명령어, 4. `SIGINT` "interrupt" 프로그램에 보내진 상호적인 요청, 5. `SIGSEGV` "segmentation violation" 유효하지 않은 메모리 접근, 6. `SIGTERM` "terminate" 프로그램에 보내진 종료 요청이다. 유닉스 계열의 운영 체제는 15개 이상의 추가적인 시그널이 있다. 

## C Language Reference | [MS Docs](https://docs.microsoft.com/en-us/cpp/c-language/c-language-reference?view=msvc-160)

#### Referece
- C, https://en.wikipedia.org/wiki/C_(programming_language), 2020-04-12-Sun.
- C signal process Wiki KR-KO, https://ko.wikipedia.org/wiki/C_%EC%8B%9C%EA%B7%B8%EB%84%90_%EC%B2%98%EB%A6%AC, 2020-11-02-Mon.
- C Wiki KR-KO, https://ko.wikipedia.org/wiki/C_(%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D_%EC%96%B8%EC%96%B4), 2020-11-02-Mon.
- C Language Reference, https://docs.microsoft.com/en-us/cpp/c-language/c-language-reference?view=msvc-160, 2021-04-28-Wed.
