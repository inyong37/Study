# 19장 비트 조작
비트를 조작하느 것은 하드웨어와 관련이 깊다. 1937년 Claude Shannon은 전기회로 스위치의 on/off를 이용한 스위칭 회로를 연구하면서 true, false의 2개 값으로 논리 연산을 설명하는 Boolean Algebra를 회로에 적용했고, Logic Gate를 만들어냈다. 이를 이용한 Logic Circuit는 현대의 모든 디지털 컴퓨터의 기본 개념이자 근간을 이루고 있다.

## 부울 연산자 Boolean Operator
기본 boolean operator: AND, OR, NOT, 보조 boolena operator: XOR
```Python
>>> True and False
False
>>> True or False
True
>>> not True
False
>>> x = y = True
>>> (x and not y) or (not x and y)
False
```

## 비트 연산자 Bitwise Operator
NOT(Bitwise NOT) ~(틸드)
```Python
>>> True & False
False
>>> True | False
True
>>> True ^ False
False
>>> ~ True
-2
```

`>>>`: 오른쪽 shifting, `<<<`: 왼쪽 shifting

## 2의 보수 Two's Complement
컴퓨터가 음수를 저장하기 위해 일반적으로 취하는 여러 방법 중 하나다. 맨 앞 비트는 부호 비트(MSB, Most Significant Bit, 최상위 비트)로 사용한다. Python은 앞에 부호만 덧붙여서 보여준다.

### 2의 보수 수학 연산
2의 보수 연산은 정확히 양수를 음수로 또는 음수를 양수로 만들어준다. 둘을 더하면 당연히 0이 된다.

### 비트 연산자 NOT
기준 비트 내에서 정확히 1을 0으로, 0으 1로 바꿔준다.
