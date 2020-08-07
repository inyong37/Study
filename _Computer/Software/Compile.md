# Compile

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
