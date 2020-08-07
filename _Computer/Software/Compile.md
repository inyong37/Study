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
  
## File

### Object file `.o`
- Executable object file
  - 링크까지 끝나 실행이 가능한 파일이다.
- Shared object file
  - 동적 링크가 가능한 파일이다.
- Relocatable object file
  - 링크를 하지 않은 파일, 링커를 통해 재배치가 가능하다는 뜻이다.

### Executable and Linking Format `.elf`
UNIX, Linux 환경에서 실행하는 프로그램의 바이너리 파일, 오브젝트 파일을 나타낸다.

### Library
- Linux Library
  - Static
  
  Static Library(정적 라이브러리)로 컴파일 타임에 symbol reference resolve(프로그램에 라이브러리 적재)되며 컴파일 시 라이브러리를 적재한 그 프로그램만 라이브러리 코드를 사용한다.
  
  - Shared
    - Dynamic Linking
    
    Dynamic Linking(공유 라이브러리)로 프로그램 메모리에 적재 런타임에 symbol reference resolve되며 메모리에 라이브러리 적재되어 있으면 해당 라이브러리를 사용하는 프로그램끼리 공유한다.
    
    - Dynamic Loading
    
    Dynamic Loading(동적 라이브러리)로 프로그램 실행 중 필요할 때, 즉 사용하는 응용 프로그램이 결정하는 런타임에 symbol reference resolve되며 프로그램끼리 공유한다.

### Static Library `.a` archive
컴파일 시 라이브러리를 사용해 relocatable symbol들을 reference resolving (linking)한다. 즉 컴파일 시 필요한 코드(라이브러리)를 프로그램에 적재하고 하나의 프로그램을 만들어낸다.

#### Reference
- gcc library option, https://nicewoong.github.io/development/2018/02/24/c-library-gcc-compile/, 2020-08-07-Fri.
- Compile process, https://m.blog.naver.com/s2kiess/220058401829, 2020-08-07-Fri.
- Object file, https://m.blog.naver.com/s2kiess/220058707917, 2020-08-07-Fri.
- ELF, https://m.blog.naver.com/s2kiess/220064366133, 2020-08-07-Fri.
- Linux library, http://blog.naver.com/PostView.nhn?blogId=xogml_blog&logNo=130138049704, 2020-08-07-Fri.
