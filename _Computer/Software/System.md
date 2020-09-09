# Operating System

## Windows | [Windows 10](https://www.microsoft.com/en-us/windows/)
### Download | [Windows 10 Download](https://www.microsoft.com/en-us/software-download/windows10) | [Windows 8.1 Download](https://www.microsoft.com/en-us/software-download/windows8ISO) | [Windows 7 Download](https://www.microsoft.com/en-us/software-download/windows7)

### HRESULT

### Program Files
Program Files 폴더에는 64-bit 프로그램들이 설치되고 Program Files (x86) 폴더에는 32-bit 프로그램들이 나눠서 설치된다. 옛날 컴퓨터는 Intel 의 8086 칩을 사용했는데 처음에는 16-bit 였고 그 이후 32-bit 가 되었다. 따라서 16-bit와 32-bit는 x86 이라 불리고 64-bit 는 x64 라 불린다. (지금 대부분의 컴퓨터는 16-bit 는 지원하지 않는다.) 현재 컴퓨터는 다양한 칩을 사용하는데 대부분 64-bit 를 지원한다. 32-bit 로 만들어진 응용 프로그램들은 'WOW64 (Windows on Windows 64-bit)' 를 통해 64-bit 에서도 실행이 가능하다. 따라서 Windows 에서는 32-bit 프로그램과 64-bit 프로그램을 섞이지 않고 나눠서 저장하고자 했다. 그래서 'C:/' 에는 'Program Files' 와 'Program Files (x86)' 2개의 폴더에 각각 나눠서 저장하게 설계되었다.

### 바로 가기 Shortcut | [Wiki (Kor)](https://ko.wikipedia.org/wiki/%EB%B0%94%EB%A1%9C_%EA%B0%80%EA%B8%B0)
바로 가기(Shortcut)는 다른 파일의 위치를 포함하는 작은 파일이며, 실행을 위해 특정한 매개 변수를 사용하기도 한다. 이 바로 가기 아이콘은 다양한 운영 체제의 바탕 화면, 시작 메뉴, 작업 표시줄에 놓이며, 명령 줄에서가 아닌 GUI에서만 동작한다. "링크 파일", "LNK 파일"이라고도 부른다.

마이크로소프트 윈도는 .lnk를 파일 확장자로 사용하며, 아이콘에 굽은 화살표 모양을 기본으로 보여 준다. 이 확장자는 폴더 옵션의 "알려진 파일 형식의 파일 확장명 숨기기"에 체크를 없애도 윈도 탐색기에서는 보이지 않는다.[Ref]

### EXE | [Wiki (Kor)](https://ko.wikipedia.org/wiki/EXE)
EXE는 일반적인 파일 확장자로 컴퓨터 프로그램의 실행 파일을 가리킨다. 오픈VMS, 도스, 마이크로소프트 윈도우, 리엑트오에스, OS/2 운영 체제에서 사용할 수 있다.

실행 프로그램 자체뿐 아니라, 많은 EXE 파일들은 비트맵, 실행 프로그램이 그래픽 사용자 인터페이스를 사용하는, 아이콘과 같은 리소스라고 불리는 다른 구성 요소들을 포함할 수 있다.

도스 실행 파일 포맷은 64 킬로바이트로 크기가 제한되는 COM 실행 파일과 다르다. 도스 실행 파일 헤더는 여러 개의 세그먼트가 DMA에서 로드될 수 있으며 64 킬로바이트 이상의 실행 파일을 지원하는 리로케이션 정보를 포함하고 있다.[Ref]

### .dll (Dynamic Link Library) | [MS (Kor)](https://support.microsoft.com/ko-kr/help/815065/what-is-a-dll)
Windows의 동적 라이브러리로, DLL은 여러 프로그램에서 동시에 사용할 수 있는 코드와 데이터를 포함하는 라이브러리이다. 코드를 쉽게 재사용할 수 있으며 메모리 사용 효율성을 높일 수 있다. DLL을 사용하면 프로그램을 여러 개별 구성 요소로 모듈화할 수 있다. 각 모듈은 설치되어 있는 경우 런타임에 주 프로그램으로 로드할 수 있다. 모듈은 서로 분리되어 있으므로 프로그램의 로드 시간이 빨라지며 해당 기능을 요청할 때만 모듈이 로드된다. 또한 프로그램의 다른 부분에 영향을 주지 않고 업데이트를 각 모듈에 더 쉽게 적용할 수 있다. 변경 내용이 DLL 하나에만 적용되는 경우 전체 프로그램을 다시 빌드하거나 설치할 필요 없이 업데이트를 적용할 수 있다.

동적 링크로 실행 파일에서 라이브러리의 기능을 사용 시에만, 라이브러리 파일을 참조 또는 다운로드해서 기능을 호출한다. 정적 링크와 다르게 컴파일 시점에 실행 파일에 함수를 복사하지 않고, 함수의 위치 정보만 갖고 그 함수를 호출할 수 있게 한다.

더 적은 리소스를 사용하며, 모듈식 구조를 사용할 수 있으며, 배포와 설치가 비교적 쉬우며, 개발을 나눠서 할 수 있으며 재사용이 가능하며 디버깅도 용이하다.

종속성을 유의해야한다. [Ref]

### .lib (Static Link Libray)
Windows의 정적 라이브러리로, 정적 링크로 컴파일 시점에 라이브러리가 링커에 의해 연결되어 실행 파일의 일부분이 된다.[Ref]

## Unix | [Homepage](https://www.opengroup.org/membership/forums/platform/unix)

### ELF (Executable and Linkable Format) | [Wiki (Kor)](https://ko.wikipedia.org/wiki/ELF_%ED%8C%8C%EC%9D%BC_%ED%98%95%EC%8B%9D)
ELF(Executable and Linkable Format)는 실행 파일, 목적 파일, 공유 라이브러리 그리고 코어 덤프를 위한 표준 파일 형식이다. 1999년 86open 프로젝트에 의해 x86 기반 유닉스, 유닉스 계열 시스템들의 표준 바이너리 파일 형식으로 선택되었다.

ELF 형식은 다양한 환경들에서 오래된 실행 파일 포맷을 대체했다. 이것은 유닉스 계열 운영체제에서 a.out과 COFF 포맷을 대체하였다. 리눅스, 솔라리스, IRIX, FreeBSD, NetBSD, OpenBSD, DragonFly BSD, Syllable, HP-UX, QNX Neutrino, 미닉스, 그리고 유닉스 계열이 아닌 OpenVMS (아이테니엄 버전), BeOS Revions 4 이후 x86 기반, 하이쿠, RISC OS, Stratus VOS, Pa-RISC와 x86 버전, 그리고 게임 콘솔인 플레이스테이션 포터블, 플레이스테이션 비타, 플레이스테이션 2, 플레이스테이션 3, 플레이스테이션 4, GP2X, 드림캐스트, 닌텐도 게임큐브, Wii, Wii U.[Ref]

### .a
Linux의 정적 라이브러리로, 동적 라이브러리에 비해 실행 속도가 빠르고 배포에 제약이 없지만, 링크 되기에 실행 파일 또는 배포 파일의 사이즈가 커진다. 그러나 유닉스의 경우 필요한 부분만 메모리에 로딩하는 demand paging을 사용하기 때문에 정적인 라이브러리의 메모리와 공유 라이브러리의 메모리 사용량 차이가 크지 않다.

Shared library와 dynamic link library는 다르다. 그러나 대부분 shard library를 만들 때 dynamic link library를 사용한다.

.a에서 .o(object)를 뽑아낸 다음 ld로 so 타켓으로 만들면 된다.[Ref]

### .so
Linux의 동적 라이브러리이다.[Ref]

### Library, Header
라이브러리는 기계어로 번역된 라이브러리이며, 헤더는 컴파일 하기 전의 프로그래머가 이해할 수 있고 문법에 맞게 작성되어 있는 선언들의 집합이다. 컴파일된 산물인 .o(object) 파일을 여러개 모아놓은 것이 라이브러리이다. 라이브러리를 사용하기 위해서는 해당 라이브러리의 헤더가 필요하다. 링커가 이해할 수 있는 symbol name을 가지고 library를 찾아 link하게 된다. compilier가 이런 header를 가지고 symbol name을 만들어서 object 파일을 넣어주면 linker가 해당 symbol name을 가지고 library를 검색해서 link하게 된다.[Ref]

## Linux | [Homepage](https://www.linux.org/)

### Alias

#### How to use
- show: `alias`
- setup at '.bashrc'
```
alias ll='ls -al'
alias ls='ls --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'
alias grep='grep --color=auto'
alias tn='tmux new'
alias tl='tmux ls'
alias ta='tmux attach'
```
### tmux
```
$ sudo apt-get install tmux
```

### ssh server with openssh server
```
$ sudo apt-get install openssh-server
$ sudo service ssh start
$ sudo systemctl enable ssh
```

### Symbolic Link
리눅스 심볼릭 링크는 특정 파일이나 디렉토리에 대하여 참조를 하는 특수한 파일이다. 윈도우에서 바로가기와 동일하다고 할 수 있다.[Ref]

## macOS | [Catalina](https://www.apple.com/macos/catalina/)

#### Reference
- Program Files, Program Files (x86), https://www.howtogeek.com/129178/why-does-64-bit-windows-need-a-separate-program-files-x86-folder/, 2019-03-21-Thu
- 20세기 맥 OS는 어떤 모습이었을까, https://blog.naver.com/PostView.nhn?blogId=tech-plus&logNo=222046025324, 2020-08-03-Mon.
- Symbolic Link, https://fruitdev.tistory.com/85, 2020-08-05-Wed.
- Unix, https://www.opengroup.org/membership/forums/platform/unix, 2020-08-05-Wed.
- Linux, https://www.linux.org/, 2020-08-05-Wed.
- macOS, https://www.apple.com/macos/catalina/, 2020-008-05-Wed.
- ELF Wiki (Kor), https://ko.wikipedia.org/wiki/ELF_%ED%8C%8C%EC%9D%BC_%ED%98%95%EC%8B%9D, 2020-08-06-Thu.
- EXE Wiki (Kor), https://ko.wikipedia.org/wiki/EXE, 2020-08-06-Thu.
- 실행 파일 Wiki (Kor), https://ko.wikipedia.org/wiki/%EC%8B%A4%ED%96%89_%ED%8C%8C%EC%9D%BC, 2020-08-06-Thu.
- DLL 이란?, https://support.microsoft.com/ko-kr/help/815065/what-is-a-dll, 2020-08-06-Thu.
- DLL, https://goddaehee.tistory.com/185, 2020-08-06-Thu.
- Library, https://jasonjason.tistory.com/15, 2020-08-06-Thu.
- Shortcut, https://ko.wikipedia.org/wiki/%EB%B0%94%EB%A1%9C_%EA%B0%80%EA%B8%B0, 2020-08-08-Sat.
- Alias, https://webdir.tistory.com/107, 2020-08-25-Tue.
- openssh, https://jimnong.tistory.com/713, 2020-09-08-Tue.
