# Kernel | [WiKi (KR)](https://ko.wikipedia.org/wiki/%EC%BB%A4%EB%84%90_(%EC%BB%B4%ED%93%A8%ED%8C%85))

커널은 컴퓨터 과학에서 컴퓨터의 운영 체제의 핵심이 되는 컴퓨터 프로그램의 하나로, 시스템의 모든 것을 완전히 통제한다. 운영 체제의 다른 부분 및 응용 프로그램 수행에 필요한 여러 가지 서비스를 제공한다. 핵심이라고도 한다. 커널의 역할은 보안, 자원 관리, 추상화이다.

[The Linux Kernel Archives](https://www.kernel.org/)

## Monolithic Kernel | [WiKi (KR)](https://ko.wikipedia.org/wiki/%EB%AA%A8%EB%86%80%EB%A6%AC%EC%8B%9D_%EC%BB%A4%EB%84%90)

운영체제에서 모놀리식 커널은 커널의 구조 및 설계 사상을 가리킨다. 단일형 커널이라고도 한다. 입출력 기능, 네트워크 기능, 장치 지원 등 운영 체제의 일반적인 기능을 커널과 동일한 메모리 공간에 적재, 실행하는 기법을 말한다. 대표적인 모놀리식 커널 OS로서는 고전적인 유닉스 계열 운영 체제들을 들 수 있다.

운영 체제의 구성 요소를 단일의 메모리 공간에서 실행하는 모놀리식 커널에 대해, OS를 구성하는 몇 개의 요소, 기능을 커널 공간으로부터 떼어내어, 외부 모듈화하는 등으로 추가하는 기법을 마이크로 커널이라고 부른다. 모놀리식 커널의 설계 사상 및 개념 그 자체는 예전부터 존재했지만, 모놀리식 커널이라고 하는 용어가 성립된 것은, 마이크로 커널이라는 개념이 등장하면서 그 반대 개념으로 명명되었다.

## Microkernel | [WiKi (KR)](https://ko.wikipedia.org/wiki/%EB%A7%88%EC%9D%B4%ED%81%AC%EB%A1%9C%EC%BB%A4%EB%84%90)

마이크로 커널은 컴퓨터 과학에서 운영 체제에 추가되어야하는 메커니즘을 최소한으로 제공하는 초소형 커널이다. 이러한 미니멀리티 메커니즘에는 낮은 수준의 주소 공간 관리, 스레드 관리, 프로세스 간 통신을 포함한다. 하드웨어가 여러 개의 링과 CPU 모드를 제공한다면 마이크로커널은 최소 권한 수준(일반적으로 수퍼바이저 및 커널 모드로 부름)에서 실행되는 유일한 소프트웨어가 된다. 소스 코드 크기 측면에서 마이크로커널은 일반적으로 10,000줄 이하의 코드를 지니는 경향이 있다. 이를테면 미닉스 3의 경우 6,000줄 이하의 코드이다.

## Hybrid Kernel | [WiKi (KR)](https://ko.wikipedia.org/wiki/%ED%95%98%EC%9D%B4%EB%B8%8C%EB%A6%AC%EB%93%9C_%EC%BB%A4%EB%84%90)

하이브리드 커널은 컴퓨터 운영 체제에서 쓰이는 마이크로 커널과 모노리딕 커널 아키텍처라는 양면을 합쳐 놓은 커널 아키텍처이다. 이 구조는 모노리딕 커널과 유사성 때문에 논란이 되기도 한다. 어떤 사람들은 이 용어가 단지 마케팅을 위한 용어일뿐이라며 일축하기도 한다. 보통 모노리딕 커널과 마이크로커널이라는 구분이 받아들여진다.

## Nanokernel, Picokernel | [WiKi (KR)](https://ko.wikipedia.org/wiki/%EB%A7%88%EC%9D%B4%ED%81%AC%EB%A1%9C%EC%BB%A4%EB%84%90#%EB%82%98%EB%85%B8%EC%BB%A4%EB%84%90)

나노 커널 또는 피코 커널이라는 용어는 모든 커널 코드의 양이 매우 작은 커널, 운영 체제 밑에 존재하는 가상화 계층(하이퍼바이저), 가장 낮은 수준의 커널 부분을 형성하는 하드웨어 추상화 계층(HAL)이다.

[Kernel types image](https://ko.wikipedia.org/wiki/%EB%AA%A8%EB%86%80%EB%A6%AC%EC%8B%9D_%EC%BB%A4%EB%84%90#/media/%ED%8C%8C%EC%9D%BC:OS-structure2.svg)

#### Reference
- Kernel Wiki KR-KO, https://ko.wikipedia.org/wiki/%EC%BB%A4%EB%84%90_(%EC%BB%B4%ED%93%A8%ED%8C%85), 2020-11-04-Wed.
- Monolithic Kernel Wiki KR-KO, https://ko.wikipedia.org/wiki/%EB%AA%A8%EB%86%80%EB%A6%AC%EC%8B%9D_%EC%BB%A4%EB%84%90, 2020-11-04-Wed.
- Microkernel Wiki KR-KO, https://ko.wikipedia.org/wiki/%EB%A7%88%EC%9D%B4%ED%81%AC%EB%A1%9C%EC%BB%A4%EB%84%90 2020-11-04-Wed.
- Hybrid Kernel Wiki KR-KO, https://ko.wikipedia.org/wiki/%ED%95%98%EC%9D%B4%EB%B8%8C%EB%A6%AC%EB%93%9C_%EC%BB%A4%EB%84%90, 2020-11-04-Wed.
- Nanokernel/Picokernel Wiki KR-KO in Microkernel, https://ko.wikipedia.org/wiki/%EB%A7%88%EC%9D%B4%ED%81%AC%EB%A1%9C%EC%BB%A4%EB%84%90#%EB%82%98%EB%85%B8%EC%BB%A4%EB%84%90, 2020-11-04-Wed.
- Kernel types image, https://ko.wikipedia.org/wiki/%EB%AA%A8%EB%86%80%EB%A6%AC%EC%8B%9D_%EC%BB%A4%EB%84%90#/media/%ED%8C%8C%EC%9D%BC:OS-structure2.svg, 2020-11-04-Wed.
- The Linux Kernel Archives, https://www.kernel.org/, 2023-01-12-Thu.
