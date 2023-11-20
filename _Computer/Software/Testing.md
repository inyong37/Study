# :hammer_and_wrench: [Testing](https://www.ibm.com/topics/software-testing) | [Blog (KR)](https://angel927.tistory.com/150)

Software testing is the process of evaluating and verifying that a software product or application does what it is supposed to do. The benefits of testing include preventing bugs, reducing development costs and improving performance.

품질이 전제되지 않는 ‘지속적인 배포’는 단지 고객에게 ‘지속적으로’ 버그 투성이 코드를 전달하는 것과 같다.

### Types of Software Testing | [Blog](https://www.atlassian.com/continuous-delivery/software-testing/types-of-software-testing)

- Acceptance testing
  - Verifying whether the whole system works as intended.
- Integration testing
  - Ensuring that software components or functions operate together.
- Unit testing
  - Validating that each software unit performs as expected
  - A unit is the smallest testable component of an application.
- Functional testing
    - Checking functions by emulating business scenarios, based on functional requirements.
    - Black-box testing is a common way to verify functions.
- Performance testing
    - Testing how the software performs under different workloads.
    - Load testing, for example, is used to evaluate performance under real-life load conditions.
- Regression testing
    - Checking whether new features break or degrade functionality.
    - Sanity testing can be used to verify menus, functions and commands at the surface level, when there is no time for a full regression test.
- Stress testing
    - Testing how much strain the system can take before it fails.
    - Consdiered to be a type of non-functional testing.
- Usability testing
    - Validating how well a customer can use a system or web application to complete a task.

---

## Smoke Test a.k.a. Build Verification Testing | [Blog (KR)](https://sambalim.tistory.com/139)

스모크 테스트란 본격적인 테스트 이전에, 시스템, 컴포넌트, 프로그램 등 테스트 대상이나 제품의 빌드, 패키지가 구축된 테스트 환경에서 테스트가 가능한지를 판단하기 위해 주요 모듈이나 시스템을 간단하게 테스트하는 단계이다.

---

## Unit Test

Unit test란 소스 코드의 특정 모듈이 의도된 대로 정확히 작동하는지 검증, 모든 함수와 메소드에 대한 테스트 케이스를 작성, 통합 테스트란 둘 이상의 모듈을 하나의 그룹으로 테스트하는 것, unit test하는 이유는 문제점 발견이 쉽고, 변경이 쉽고, 통합이 간단함, 테스트 도구에는 Cpp Unit, Google Test 등이 있음

### GoogleTest (gtest)

gtest는 구글에서 만든 C++ 테스트 프레임워크, 통합 테스트, 단위 테스트(unit test), 시나리오 테스트 가능, 크로미윰, OpenCV에서 사용, 특징으로는 다양한 asssertion, user-defined assertions, death test, fatal and non-fatal, value-parameterized test, type-parameterized test, various options runtime test, xml test report 가능, 독립적, 실제 사용하는 것처럼 테스트 케이스 그룹 만들 수 있음, platform 독립적, test case 실패해도 계속 진행 가능, 일일이 지정하지 않아도 찾아줌, 반복 test는 자원을 공유하기 때문에 비용이 적음

### GoogleTest 사용법

`TEST(TestGroupName, TestCaseName){Test Content} ` 자동으로 프로그램 수행 시 실행될 테스트로 등록됨, 순서는 랜덤임, 사용하지 않을 경우 `DISABLED_` 키워드 사용, 필터로 원하는 테스트만 수행 가능, `ASSERT` 결과는 성공, 심각하지 않은 실패, 심각한 실패가 있음, 매크로처럼 사용, `ASSERT_*` 조건문이 참이 아닐 경우 실패를 출력하고 테스트 종료, `EXPECT_*` 조건문이 참이 아닐 경우 실패를 출력하고 다음 테스트 진행

Test Fixtures 여러 테스트에서 공통으로 사용하는 객체 설정 정의, `::testing::Test` 상속받아서 사용, `Setup()` 테스트에 필요한 설정 세팅, 각 테스트 케이스 시작되기 전에 호출, `TearDown()` 테스트에 사용한 자원들을 해제할 때 사용함, 각 테스트 케이스 끝나고 호출

의존성 제거, 클래스 간 복합적인 관계 의존성 존재, 테스트 저해 설계(파일, 스레드, 통신 등 외부 의존물) `stub` 외부 의존물을 대신하기 위해 간접 계층 추가, 간접계층이란 외부 의존물에 접근하기 위해 인터페이스 추가, `stub` constructor, get, set property, parameter, abstract factory, 객체의 대체제, 테스트 가능토록 의존물을 없앰, `Mock` 테스트 통과, 실패 검증, unit test의 통과/실패를 판단하는 가짜 객체, 하나의 테스트에 하나의 `mock` 사용, `mock` 객체, 테스트 객체를 제외한 모든 의존물은 `stub`으로 대체, `assert`는 가급적 테스트 당 1개, `mock` 재사용, 내부에 `assert` 사용 금지

`TEST(), TEST_F(), TEST_P()` 테스트 케이스의 Test Group Name과 Test Name을 지정한다. 여러 테스트가 있는 경우에는 이름의 조합이 중복되지 않도록 해야한다.(빌드 에러 발생) `TEST_F()`에서 첫번째 인자는 테스트 픽처로 정의된 클래스 이름으로 한다. `TEST_P()`는 하나의 테스트 매개 변수를 변경하면서 여러번 수행할 수 있다.

### GoogleTest Installation

gtest 다운로드 및 빌드, 헤더 파일 인클루드, 라이브러리 링크

```C++
// 1
TEST(TestGroupName, TestName) {
    ... Test Content ...
}
// 2
class FixtureSample : public testing::Test
{
public:
    FixtureSample();
    ~FixtureSample();
    void SetUp();
    void TearDown();
};
// 3
class fixture_sample : public testing::Test
{
public:
    fixture_sample();
    ~fixture_sample();
    void SetUp();
    void TearDown();
};

TEST(fixture_sample, case_name)
{
    ... test content ...
}
```

---

## Performance Test | [Blog (KR)](https://loosie.tistory.com/821)

성능 테스트는 시스템 구성 요소가 특정 상황에서 어떤 성능을 보이는지 확인하기 위해 수행되는 테스트이다. 제품의 리소스 사용, 확장성 및 안정성도 이 테스트를 통해 검증할 수 있다. 

~~성능 테스트는 load, endurance, volume, scalability, spike, and stress 테스트의 상위 집합이다.~~

---

## Regression Test | [Blog (KR)](https://velog.io/@dahunyoo/Regression-Test)

Regression test는 regression bug를 찾는 테스트 방식이다. Regression bug는 이전에 제대로 작동하던 소프트웨어 기능에 문제가 생기는 것이다. Regression test 방식에는 retest all, selective, priority 방식이 있다.

---

## Stress Test

스트레스 테스트는 기존 자원에 과잉 작업을 과부하시키는 다양한 활동을 수행하여 시스템을 무너뜨리는 시도를 한다. 네커티브 테스트: 시스템에서 구성 요소를 제거하는 작업도 스트레스 테스트의 일부로 수행된다. 피로 테스트: 대역폭 용량을 넘을 정도로 테스트하여 애플리케이션의 안정성을 확인한다. 스트레스 테스트는 최대 부하 및 정상 조건을 넘어서는 애플리케이션의 동작을 테스트한다. 스트레스 테스트의 목적은 시스템의 오류를 확인하고 시스템이 어떻게 정상적으로 복구되는지 모니터링한다. 

### Spike Test

스파이크 테스트는 사용자 수가 갑자기 증가하는 상황에서 시스템이 어떻게 작동하는지 확인하는 테스트이다.

### Absorb Test

흡수 테스트는 사용자 수의 느린 증가를 통해 일정 기간 동안 시스템의 지속 가능성을 확인하는 테스트이다.

### Load Test | [Load Testing Tools for Server](https://testguild.com/load-testing-tools/#P1) | [Load Testing Tools for Server (KR)](https://goodsharp.tistory.com/10)

부하 테스트는 임계치 한계에 도달할 때 까지 시스템의 부하를 지속적으로 증가시켜 시스템을 테스트한다. 부하 테스트의 목적은 내구성을 테스트하고 결과를 모니터링하기 위해 처리할 수 있는 가장 큰 작업을 시스템에 할당한다. 모니터링되는 속성에는 최대 성능, 서버 처리량, 다양한 부하 수준에서의 응답 시간, HW 환경의 적절성, 성능에 영향을 주지 않고 처리할 수 있는 사용자 수 등이 있다.

---

## *Security Test* | [Blog (KR)](https://ko.theastrologypage.com/security-testing)

보안 테스트는 하드웨어, 소프트웨어, 네트워크 또는 IT/정보 시스템 환경의 정보 보안을 평가하고 테스트하는 프로세스이다.

---

## *Lint* | [WiKi](https://en.wikipedia.org/wiki/Lint_(software)) | [List of tools for static code analysis](https://en.wikipedia.org/wiki/List_of_tools_for_static_code_analysis)

Lint, or a linter, is a static code analysis tool used to flag programming errors, bugs, stylistic errors and suspicious constructs. The term originates from a Unix utility that examined C language source code.

## C, C++

Astree, BLAST (retired), Clang, Coccinelle, Coverity, CPAChecker, Cppcheck, Cppdepend, cpplint, ECLAIR, Eclipse, Fluctuat, Frama-C, Helix QAC, Inter, Lint, LDRA Testbed, Parasoft C/C++test, PC-Lint, Polyspace, SLAM project, Sparse, SonarQube, Splint, Visual Studio.

## Fortran

Fortran-Lint (Information Processing Techniques, Inc)

## Java

Checkstyle, Coverity, Eclipse, FindBugs, Infer, IntelliJ IDEA, JArchitect, JTest, LDRA Testbed, PMD, RIPS, Semgrep, SemmleCode, Soot, Squale, SourceMeter, ThreadSafe,.

## JavaScript

### ESLint | [WiKi](https://en.wikipedia.org/wiki/ESLint)

JavaScript syntax checker and formatter.

---

## Python

### PyCharm

Cross-platform IDE with code inspections available for analyzing code on-the-fly in the editor and bulk analysis of the whole project.

### PyDev

Eclipse-based Python IDE with code analysis available on-the-fly in the editor or at save time.

### Pylink

Static code analyzer. Quite stringent; includes many stylistic warnings as well.

---

### Semgrep

Static code analyzer that helps expressing code standards and surfacing bugs early. A CI service and a rule library is also available.

---

### [Postman](https://www.postman.com/)

Postman is an API platform for building and using APIs. Postman simplifies each step of the API lifecycle and streamlines collaboration so you can create better APIs-faster.

[Test Server via Postman (Blog KR)](https://iamdaeyun.tistory.com/entry/Postman%EC%9C%BC%EB%A1%9C-%EC%84%9C%EB%B2%84-%EC%9A%94%EC%B2%AD-%ED%85%8C%EC%8A%A4%ED%8A%B8)

### [JMeter](https://jmeter.apache.org/)

The Apache JMeter application is open source software, a 100% pure Java application designed to load test functional behavior and measure performance. It was originally designed for testing Web Applications but has since expanded to other test functions.

[Read data from a CSV file in JMeter with Azure Load Testing](https://learn.microsoft.com/en-us/azure/load-testing/how-to-read-csv-data?tabs=portal) | [Blog (KR)](https://blog.naver.com/asemansa/221681591957)

---

### References
- googletest(gtest) GitHub, https://github.com/google/googletest
- gtest-demo GitHub, https://github.com/bast/gtest-demo
- googltetest, https://github.com/google/googletest/blob/master/docs/primer.md
- gMock, https://github.com/google/googletest/blob/master/googlemock/README.md
- 구글 테스트 Slide, https://www.slideshare.net/jinhwason/ss-69528881
- C++ 프로젝트에 단위 테스트 도입하기 Slide, https://www.slideshare.net/zone0000/c-7522148
- 낡은 코드에 단위테스트 넣기 Slide, https://www.slideshare.net/parkpd/kgc2010
- Google Test/Mock 정리 Blog, https://jacking75.github.io/cpp_GTest_Mock_CheatSeet/
- Lint Wiki, https://en.wikipedia.org/wiki/Lint_(software), 2021-06-25-Fri.
- List of tools for static code analysis, https://en.wikipedia.org/wiki/List_of_tools_for_static_code_analysis, 2021-06-25-Fri.
- ESLint, https://en.wikipedia.org/wiki/ESLint, 2021-06-25-Fri.
- Types of Software Testing, https://www.atlassian.com/continuous-delivery/software-testing/types-of-software-testing, 2022-10-25-Tue.
- What is software testing IBM, https://www.ibm.com/topics/software-testing, 2022-10-25-Tue.
- Smoke Test Blog KR, https://sambalim.tistory.com/139, 2022-10-24-Mon.
- Regression Test Blog KR, https://velog.io/@dahunyoo/Regression-Test, 2022-10-24-Mon.
- Performance Test Blog KR, https://loosie.tistory.com/821, 2022-10-24-Mon.
- Security Test Blog KR, https://ko.theastrologypage.com/security-testing, 2022-10-24-Mon.
- Load Testing Tools for Server, https://testguild.com/load-testing-tools/#P1, 2022-10-25-Tue.
- Load Testing Tools for Server Blog KR, https://goodsharp.tistory.com/10, 2022-10-25-Tue.
- Postman, https://www.postman.com/, 2023-11-14-Tue.
- Test Server via Postman Blog KR, https://iamdaeyun.tistory.com/entry/Postman%EC%9C%BC%EB%A1%9C-%EC%84%9C%EB%B2%84-%EC%9A%94%EC%B2%AD-%ED%85%8C%EC%8A%A4%ED%8A%B8, 2023-11-14-Tue.
- JMeter Apache, https://jmeter.apache.org/, 2023-11-16-Thu.
- Read data from a CSV file in JMeter with Azure Load Testing, https://learn.microsoft.com/en-us/azure/load-testing/how-to-read-csv-data?tabs=portal, 2023-11-16-Thu.
- CSV JMeter Blog KR, https://blog.naver.com/asemansa/221681591957, 2023-11-16-Thu.
