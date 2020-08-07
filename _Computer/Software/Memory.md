# Memory

## Section
|Memory Section |
|:-------------:|
|CODE |
|DATA |
|BSS  |
|HEAP |
|STACK|

실행 파일의 크기는 CODE, DATA, BSS의 영역에서 결정되며 컴파일 이후에는 고정된다.

### CODE (TEXT)
함수, 제어문, 상수 영역으로 기계어로 구성되어 있다.

### DATA

### BSS

### HEAP

### STACK

## Swap Memory
Swap memory 또는 가상 메모리는 주 메모리가 부족할 때 하드디스크와 같은 저장 공간을 메모리로 사용하는 것이다. 윈도우에서는 가상 메모리/페이징 메모리라고 한다. 일반 메모리에 비해 하드디스크(HDD), SSD는 속도가 느리기 때문에 데이터 처리 속도가 느려진다.

### How to use
- `top`: show memory usage by process
- `htop`: show cpu usage by process
- `free -m`: show memory

## Shared Memory
프로세스에서 메모리는 해당 프로세스만 사용하는 것이 일반적이다. 메모리에는 명령어, 지역 변수, 동적 변수, 전역 변수와 같이 데이터가 존재하는데 그 프로세스만 접근할 수 있고 변경 가능하다. 하지만 공유 메모리라는 IPC 기법으로 이 데이터를 다른 프로세스에서 쓸 수 있도록 할 수 있다. 서로 다른 프로세스가 특정 메모리를 공유하면 데이터를 더 빠르게 접근할 수 있어 프로그램을 더 효율적으로 만들 수 있다.

#### Reference
- Swap memory, https://m.blog.naver.com/PostView.nhn?blogId=blueday9404&logNo=221032460184&proxyReferer=https:%2F%2Fwww.google.com%2F, 2020-08-07-Fri.
- Swap memory, http://wiki.pchero21.com/wiki/Swap_memory, 2020-08-07-Fri.
- Paging Wiki Kor, https://ko.wikipedia.org/wiki/%ED%8E%98%EC%9D%B4%EC%A7%95, 2020-08-07-Fri.
- Virtual memory and paging, https://jins-dev.tistory.com/entry/%EA%B0%80%EC%83%81-%EB%A9%94%EB%AA%A8%EB%A6%ACVirtual-Memory%EC%99%80-%ED%8E%98%EC%9D%B4%EC%A7%95Paging%EC%97%90-%EB%8C%80%ED%95%9C-%EC%A0%95%EB%A6%AC, 2020-08-07-Fri.
- Shared Memory, https://reakwon.tistory.com/96, 2020-08-07-Fri.
- Memory Section, https://kama1204.tistory.com/entry/%EB%A9%94%EB%AA%A8%EB%A6%AC%EC%9D%98-5-%EC%98%81%EC%97%AD, 2020-08-07-Fri.
