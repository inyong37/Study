# Compile

## Process

### 1. Preprocessing
- foo.c -> foo.i
- Preprocessor(전처리기, cpp0)가 `#`에 대한 처리를 한다. `#include`의 라이브러리를 불러오는 역할도 한다.

### 2. Compile
- foo.i -> foo.s
- Compiler(컴파일러, cc1)가 불러온 라이브러리를 참조하여 소스코드를 어셈블리 코드로 변환한다.

### 3. Assemble
- foo.s -> foo.o
- Assembler(어셈블러, as, collect2)가 어셈블리 코드에서 기계어 코드(오브젝트 파일)로 변환한다.

### 4. Link
- foo.o -> foo (elf, exe)
- Linker(링커, ld)가 a, so 라이브러리와 연결시켜 실행 파일을 만든다.

## Compiler

### gcc (GNU C Compiler)

#### How to use
- `gcc`: compile C source code
  -`gcc foo.c`
- `g++`: compile C++ source code
  -`g++ foo.cpp`
- `-l` option: library linking
  - without prefix `lib` and suffix `.a`(Linux static link library) or `.so`(Linux dynamic link library) or `.lib`(Windows static link library) or `.dll`(Windows dynamic link library)
  - `-l library` or `-llibrary`
- `-L` option: optional library directory
  - defualt library directory: `/lib`, `/usr/lib`, and `/usr/local/lib`
  - `-L /home/directory` or `-L/home/directory`

#### Reference
- gcc library option, https://nicewoong.github.io/development/2018/02/24/c-library-gcc-compile/, 2020-08-07-Fri.
- Compile process, https://m.blog.naver.com/s2kiess/220058401829, 2020-08-07-Fri.
