## Google Test & Mock 사용법

unit test란 소스 코드의 특정 모듈이 의도된 대로 정확히 작동하는지 검증, 모든 함수와 메소드에 대한 테스트 케이스를 작성, 통합 테스트란 둘 이상의 모듈을 하나의 그룹으로 테스트하는 것, unit test하는 이유는 문제점 발견이 쉽고, 변경이 쉽고, 통합이 간단함, 테스트 도구에는 Cpp Unit, Google Test 등이 있음

구글에서 만든 C++ 테스트 프레임워크, 통합 테스트, 단위 테스트(unit test), 시나리오 테스트 가능, 크로미윰, OpenCV에서 사용, 특징으로는 다양한 asssertion, user-defined assertions, death test, fatal and non-fatal, value-parameterized test, type-parameterized test, various options runtime test, xml test report 가능, 독립적, 실제 사용하는 것처럼 테스트 케이스 그룹 만들 수 있음, platform 독립적, test case 실패해도 계속 진행 가능, 일일이 지정하지 않아도 찾아줌, 반복 test는 자원을 공유하기 때문에 비용이 적음

`TEST(TestGroupName, TestCaseName){Test Content} ` 자동으로 프로그램 수행 시 실행될 테스트로 등록됨, 순서는 랜덤임, 사용하지 않을 경우 `DISABLED_` 키워드 사용, 필터로 원하는 테스트만 수행 가능, `ASSERT` 결과는 성공, 심각하지 않은 실패, 심각한 실패가 있음, 매크로처럼 사용, `ASSERT_*` 조건문이 참이 아닐 경우 실패를 출력하고 테스트 종료, `EXPECT_*` 조건문이 참이 아닐 경우 실패를 출력하고 다음 테스트 진행

Test Fixtures 여러 테스트에서 공통으로 사용하는 객체 설정 정의, `::testing::Test` 상속받아서 사용, `Setup()` 테스트에 필요한 설정 세팅, 각 테스트 케이스 시작되기 전에 호출, `TearDown()` 테스트에 사용한 자원들을 해제할 때 사용함, 각 테스트 케이스 끝나고 호출

의존성 제거, 클래스 간 복합적인 관계 의존성 존재, 테스트 저해 설계(파일, 스레드, 통신 등 외부 의존물) `stub` 외부 의존물을 대신하기 위해 간접 계층 추가, 간접계층이란 외부 의존물에 접근하기 위해 인터페이스 추가, `stub` constructor, get, set property, parameter, abstract factory, 객체의 대체제, 테스트 가능토록 의존물을 없앰, `Mock` 테스트 통과, 실패 검증, unit test의 통과/실패를 판단하는 가짜 객체, 하나의 테스트에 하나의 `mock` 사용, `mock` 객체, 테스트 객체를 제외한 모든 의존물은 `stub`으로 대체, `assert`는 가급적 테스트 당 1개, `mock` 재사용, 내부에 `assert` 사용 금지

`TEST(), TEST_F(), TEST_P()` 테스트 케이스의 Test Group Name과 Test Name을 지정한다. 여러 테스트가 있는 경우에는 이름의 조합이 중복되지 않도록 해야한다.(빌드 에러 발생) `TEST_F()`에서 첫번째 인자는 테스트 픽처로 정의된 클래스 이름으로 한다. `TEST_P()`는 하나의 테스트 매개 변수를 변경하면서 여러번 수행할 수 있다.

## Installation

gtest 다운로드 및 빌드, 헤더 파일 인클루드, 라이브러리 링크


```c++
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


#### References
- https://www.slideshare.net/jinhwason/ss-69528881
- https://www.slideshare.net/parkpd/kgc2010
- https://www.slideshare.net/zone0000/c-7522148
- https://jacking75.github.io/cpp_GTest_Mock_CheatSeet/
