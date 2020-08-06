# Operating System

## Windows | [Windows 10](https://www.microsoft.com/en-us/windows/)
### Download | [Windows 10 Download](https://www.microsoft.com/en-us/software-download/windows10) | [Windows 8.1 Download](https://www.microsoft.com/en-us/software-download/windows8ISO) | [Windows 7 Download](https://www.microsoft.com/en-us/software-download/windows7)

### Program Files
Program Files 폴더에는 64-bit 프로그램들이 설치되고 Program Files (x86) 폴더에는 32-bit 프로그램들이 나눠서 설치된다. 옛날 컴퓨터는 Intel 의 8086 칩을 사용했는데 처음에는 16-bit 였고 그 이후 32-bit 가 되었다. 따라서 16-bit와 32-bit는 x86 이라 불리고 64-bit 는 x64 라 불린다. (지금 대부분의 컴퓨터는 16-bit 는 지원하지 않는다.) 현재 컴퓨터는 다양한 칩을 사용하는데 대부분 64-bit 를 지원한다. 32-bit 로 만들어진 응용 프로그램들은 'WOW64 (Windows on Windows 64-bit)' 를 통해 64-bit 에서도 실행이 가능하다. 따라서 Windows 에서는 32-bit 프로그램과 64-bit 프로그램을 섞이지 않고 나눠서 저장하고자 했다. 그래서 'C:/' 에는 'Program Files' 와 'Program Files (x86)' 2개의 폴더에 각각 나눠서 저장하게 설계되었다.

### EXE | [Wiki (Kor)](https://ko.wikipedia.org/wiki/EXE)
EXE는 일반적인 파일 확장자로 컴퓨터 프로그램의 실행 파일을 가리킨다. 오픈VMS, 도스, 마이크로소프트 윈도우, 리엑트오에스, OS/2 운영 체제에서 사용할 수 있다.

실행 프로그램 자체뿐 아니라, 많은 EXE 파일들은 비트맵, 실행 프로그램이 그래픽 사용자 인터페이스를 사용하는, 아이콘과 같은 리소스라고 불리는 다른 구성 요소들을 포함할 수 있다.

도스 실행 파일 포맷은 64 킬로바이트로 크기가 제한되는 COM 실행 파일과 다르다. 도스 실행 파일 헤더는 여러 개의 세그먼트가 DMA에서 로드될 수 있으며 64 킬로바이트 이상의 실행 파일을 지원하는 리로케이션 정보를 포함하고 있다.

### DLL | [MS (Kor)](https://support.microsoft.com/ko-kr/help/815065/what-is-a-dll)

## Unix | [Homepage](https://www.opengroup.org/membership/forums/platform/unix)

### ELF (Executable and Linkable Format) | [Wiki (Kor)](https://ko.wikipedia.org/wiki/ELF_%ED%8C%8C%EC%9D%BC_%ED%98%95%EC%8B%9D)
ELF(Executable and Linkable Format)는 실행 파일, 목적 파일, 공유 라이브러리 그리고 코어 덤프를 위한 표준 파일 형식이다. 1999년 86open 프로젝트에 의해 x86 기반 유닉스, 유닉스 계열 시스템들의 표준 바이너리 파일 형식으로 선택되었다.

ELF 형식은 다양한 환경들에서 오래된 실행 파일 포맷을 대체했다. 이것은 유닉스 계열 운영체제에서 a.out과 COFF 포맷을 대체하였다. 리눅스, 솔라리스, IRIX, FreeBSD, NetBSD, OpenBSD, DragonFly BSD, Syllable, HP-UX, QNX Neutrino, 미닉스, 그리고 유닉스 계열이 아닌 OpenVMS (아이테니엄 버전), BeOS Revions 4 이후 x86 기반, 하이쿠, RISC OS, Stratus VOS, Pa-RISC와 x86 버전, 그리고 게임 콘솔인 플레이스테이션 포터블, 플레이스테이션 비타, 플레이스테이션 2, 플레이스테이션 3, 플레이스테이션 4, GP2X, 드림캐스트, 닌텐도 게임큐브, Wii, Wii U.

## Linux | [Homepage](https://www.linux.org/)

### Symbolic Link
리눅스 심볼릭 링크는 특정 파일이나 디렉토리에 대하여 참조를 하는 특수한 파일이다. 윈도우에서 바로가기와 동일하다고 할 수 있다.

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
