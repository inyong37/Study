# _Interpreter_ | [WiKi (KR)](https://ko.wikipedia.org/wiki/%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4_%EB%B9%8C%EB%93%9C)

Interpreter(인터프리터/해석기)는 프로그래밍 언어의 소스 코드를 바로 실행하는 컴퓨터 프로그램 또는 환경을 말한다. 원시 코드를 기계어로 번역하는 compiler와는 대비된다. Interpreter는 다음의 과정 3개 가운데 적어도 1가지 기능을 가진 프로그램이다. 1. 소스 코드를 직접 실행한다. 2. 소스 코드를 효율적인 다른 중간 코드로 변환하고, 변환한 것을 바로 실행한다. 3. Interpreter 시스템의 일부인 compiler가 만든, 미리 complied 저장 코드의 실행을 호출한다.

Interpreter는 고급 언어로 작성된 원시 코드 명령어들을 한번에 한 줄씩 읽어들여서 실행하는 프로그램이다. 고급 언어로 작성된 프로그램들을 실행하는 데에는 2가지 방법이 있다. 1. 가장 일반적인 방법은 프로그램을 compile하는 것이고, 다른 1가지는 프로그램을 interpreter에 통과시키는 방법이다. Interpreter는 고급 명령어들을 중간 형태로 번역한 다음, 그것을 실행한다. 이와는 대조적으로 compilter는 고급 명령어들을 직접 기계어로 번역한다.

Complied 프로그램은 일반적으로 interpreter를 이용해 실행시키는 것보다 더 빠르게 실행된다. 그러나 interpreter의 장점은 기계어 명령어들이 만들어지는 compile 단계를 거칠 필요가 없다는데 있다. Compile 과정은 만약 원시 프로그램의 크기가 크다면, 상당한 시간이 걸릴 수 있다. 이와는 달리 interpreter는 고급 프로그램을 즉시 실행시킬 수 있다. 이런 이유 때문에 interpreter는 종종 프로그램의 개발 단계에서 사용되는데, 그것은 프로그래머가 한번에 적은 양의 내용을 추가하고 그것을 빠르게 테스트 해보길 원하기 때문이다. 이외에도 interpreter를 이용하면 프로그래밍을 대화식으로 할 수 있기 때문에, 학생들의 교육용으로 사용되는 경우도 많다.

Interpreter와 compiler 둘 다 대부분의 고급 언어에 적용이 가능하지만 BASIC이나 LISP와 같은 일부 언어들은 개발 당시에는 특별히 interpreter에 의해서만 실행되도록 설계되었다. 그 외에도 PostScript와 같은 페이지 기술 언어들도 interpreter를 사용한다. 모든 PostScript 프런티너느 PostScript 명령문을 실행할 수 있도록 interpreter가 내장되어 있다.

최초의 interpreter 방식의 고급 언어는 LISP였다. LISP는 1958년 스티브 러셀이 IBM 704 컴퓨터에 최초로 구현하였다. 러셀은 존 매카시의 논문을 읽고 LISP의 eval 함수가 기계어로 구현될 수 있었다는 것을 발견했는데, 이는 맥캐시를 놀라게 했다. 작업 중인 LISP interpreter가 그 결과 만들어졌으며 LISP 프로그램의 실행, 더 정확히 말해, "LISP 식의 평가"에 사용될 수 있었다.

---

### Reference
- Interpreter Wiki KR-KO, https://ko.wikipedia.org/wiki/%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4_%EB%B9%8C%EB%93%9C, 2020-11-12-Thu.
