# 2장 프로그래밍 언어 선택

## 경진대회 통계로 알아본 언어 선호도

## 프로그래밍 언어별 특징

### 루프

### 제네릭 프로그래밍
제네릭(Generic)이란 파라미터의 타입이 나중에 지정(to-be-specified-later)되게 해서 재활용성을 높일 수 있는 프로그래밍 스타일로서, 1989년 David Musser와 Alexander Stepanov가 고안했다. 특히 알렉산더 스테파노프는 C++ STL(C++의 템플릿을 이용해 제네릭 프로그래밍으로 구현한 C++의 사실상 표준 자료구조, 알고리즘 라이브러리)의 창안자로도 유명하다.

파이썬은 원래 동적 파이팅(Dynamic Typing) 언어이기 때문에 제네릭이 필요없다. PEP(Python Enhancement Proposals) 484에 추가된 타입 힌트(Type Hints)를 통해 제네릭을 사용할 수 있게 됐다. PEP 484는 파이썬 3.5부터 사용할 수 있다.

### 배열 반복
C++는 버전 11 이후를 모던 C++라 일컬으며, 언어 문볍에 대대적인 변화가 있었다. 그 중 가장 큰 변화 중 하나는 : 연산자의 지원이다. 이로 인해 C++도 사실상 파이썬과 큰 차이 없는 문법으로 이처럼 배열 반복(Iterate throught Array)이 가능해졌다.

### 구조체
C에서 구조체(Struct)는 특별한 의미가 있다. 순차적으로 메모리를 할당하는 배열과 달리 구조체는 메모리의 어느 영역에나 어떤 크기로든 할당할 수 있는 사실상 유일한 복합 자료형이기 때문이다. 연결 리스트를 포함해 배열을 제외한 모든 추상 자료형(ADT, Abstract Data Type, 추상 자료형이란 자료혀으이 연산을 정의한 것으로 실제 구현 방법은 명시하지 않는다)의 구현은 사실상 구조체를 한 번 이상 이용한다고 할 수 있다. C++에서 클래스의 등장으로(원래 C++의 이름은 C with Classes였다) 이후 등장한 언어들에는 사용 빈도가 줄었지만 여전히 구조체는 널리 쓰이고 있다.

C++에서 클래스를 소개했지만 여전히 구조체 문법을 지원하며 사용할 수 있다. C++에서는 구조체와 클래스가 공존하지만 자바는 더 이상 구조체를 지원하지 않는다. 클래스만 지원한다. 

파이썬에는 구조체가 없을 뿐더러 클래스 또한 데이터 타입을 지정할 수 없어, 구조체와 같은 형태를 정의할려면 네임드 튜플(Named Tuple)을 사용해야 했다. 이처럼 정의해 사용하는 방법밖에 없었는데, 파이썬 3.7부터 dataclass를 지원하며, @dataclass 데코레이션(Decoration, 자바에서는 동일한 문법을 애노테이션, Annotation이라 부른다)으로 타입 힌트와 함께 활용함으로써 class를 이용해 구조체 형태로 정의할 수 있다. 3.6 이하 버전에서도 하위 호환성을 위해 백포트(Backport) 버전을 제공하므로 필요한 경우 설치하여 사용할 수 있다.

```Python
from collections import namedtuple

MyStruct = namedtuple('MyStruct', 'field1', 'field2', 'field3')

m = MyStruct('foo', 'bar', 'baz')
```

```Python
from dataclasses import dataclass

@dataclass
class Product:
  weight: int = None
  price: float = None

apple = Product()
apple.price = 10
```

### 클래스
클래스는 C++의 가장 큰 특징 중 하나로 구조는 요즘 언어들에 비해 복잡해 보이지만 크게 선언부와 구현부로 구분할 수 있다. 여기서는 하나의 파일로 표시했지만 이를 통해 헤더 파일과 소스 파일로 각각 분리할 수 있으며, 이처럼 선언과 구현을 분리하는 방식은 컴파일 속도를 높일 수 있는 등 여러모로 장점이 있다. dataclass 데코레이션을 이용해 선언하게 되면 여러 가지 내부 함수의 기능도 자동으로 구현해주기 때문에 편리하게 활용할 수 있다.

```Python
from dataclasses import dataclass

@dataclass
class Rectangle:
  width: int
  height: int
  
  def area(self):
    return self.width * self.height

rect = Rectangle(3, 4)
print(rect.area())
```

다형성(Polymorphism)이란 서로 다른 유형의 개체(Entity)에 단일 인터페이스를 제공하는 것을 말하며 어떤 유형(Type)이냐에 따라 다양한 방법으로 구현할 수 있다.

## 코딩 테스트에 최적인 프로그래밍 언어는?
- 면접관이 쉽게 이해할 수 있는가?
- 코딩 플랫폼에서 지원하는가?
- 유연한 언어인가?
- 언어 레벨에서 풍부한 기능을 지원하는가?
