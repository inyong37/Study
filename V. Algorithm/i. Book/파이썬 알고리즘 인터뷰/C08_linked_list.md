:bulb: 숫자형 리스트를 단일 값으로 병합하기

```Python
''.join(str(e) for e in a)
''.join(map(str, a))
functools.reduce(lambda x, y: 10 * x + y, a, 0)
```

functions는 '함수를 다루는 함수'를 뜻하는 고계 함수(Higher-Order Function)를 지원하는 함수형 언어 모듈이며, 리트코드에서 기본적으로 import 되어 있다. 여기서 reduct는 두 인수(Argument)의 함수를 누적 적용하라는 메소드다.

```Python
>>> functools.reduct(lambda x, y: x + y, [1, 2, 3, 4, 5])
15
```

이 코드의 결과는 ((((1+2)+3)+4)+5)이다. functools.reduce(lambda x, y: 10 * x + y, a, 0)의 결과를 보면, 값 x에 계속 10을 곱하면서 자릿수 10^n의 형태로 올려나가고 그 뒤에 y를 더해서 10^0의 자릿수를 채워나가는 방식이다. 애초에 문자형과 달리 숫자형은 이런 방식으로 자릿수를 올려나가는 방법밖에 없으며, 또한 이 방식이 숫자형답게 우아한 방식이다.

이외에도 좀 더 가독성을 높일 수 있도록 operator 모듈을 활용하는 방법도 있다. 이 경우 연산자 명칭(함수)을 reduce() 메소드의 파라미터로 지정할 수 있어 가독성이 매우 높다. 이 또한 고계 함수이기 때문에 이처럼 파라미터로 함수를 넘기는 것이 가능하다.

```Python
>>> from operator import add, mul
>>> functools.reduce(add, [1, 2, 3, 4, 5])
15
>>> functools.reduce(mul, [1, 2, 3, 4, 5])
120
```
