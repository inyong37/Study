# *Unix*

# *Linux* | [Homepage](https://www.linux.org/) | [Wiki](https://en.wikipedia.org/wiki/Linux) | [Download](https://www.linux.org/pages/download/)
```This page is from the 'System' page.```

Linux is a family of open source Unix-like operating systems based on the Linux kernel, an operating system kernel first released on September 17, 1991, by Linus Torvalds. Linux is typically packaged in a Linux distribution.

Distributions include the Linux kernel and supporting system software and libraries, many of which are provided by the GNU Project. Many Linux distributions use the word "Linux" in their name, but the Free Software Foundation uses the name GNU/Linux to emphasize the importance of GNU software, causing some controversy.

Popular Linux distributions include Debian, Fedora, and Ubuntu. Commercial distributions include Red Hat Enterprise Linux and SUSE Linux Enterprise Server. Desktop Linux distributions include a windowing system such as X11 or Wayland, and a desktop environment such as GNOME or KDE Plasma. Distributions intended for servers may omit graphics altogether, or include a solution stack such as LAMP. Because Linux is freely redistributable, anyone may create a distribution for any purpose.

Linux was originally developed for personal computers based on the Intel x86 architecture, but has since been ported to more platforms than any other operating system. Because of the dominance of Android on smartphones, Linux also has the largest installed base of all general-purpose operating systems. Although it is used by only around 2.3 percent of desktop computers, the Chromebook, which runs the Linux kernel-based Chrome OS, dominates the US K–12 education market and represents nearly 20 percent of sub-$300 notebook sales in the US. Linux is the leading operating system on servers (over 96.4% of the top 1 million web servers' operating systems are Linux), leads other big iron systems such as mainframe computers, and is the only OS used on TOP500 supercomputers (since November 2017, having gradually eliminated all competitors).

Linux also runs on embedded systems, i.e. devices whose operating system is typically built into the firmware and is highly tailored to the system. This includes routers, automation controls, smart home technology (like Google Nest), televisions (Samsung and LG Smart TVs use Tizen and WebOS, respectively), automobiles (for example, Tesla, Audi, Mercedes-Benz, Hyundai, and Toyota all rely on Linux), digital video recorders, video game consoles, and smartwatches. The Falcon 9's and the Dragon 2's avionics use a customized version of Linux.

Linux is one of the most prominent examples of free and open-source software collaboration. The source code may be used, modified and distributed commercially or non-commercially by anyone under the terms of its respective licenses, such as the GNU General Public License.

### *Manual Page (man page)* | [Wiki](https://en.wikipedia.org/wiki/Man_page)
A man page (short for manual page) is a form of software documentation usually found on a Unix or Unix-like operating system. Topics covered include computer programs (including library and system calls), formal standards and conventions, and even abstract concepts. A user may invoke a man page by issuing the man command.

By default, man typically uses a terminal pager program such as more or less to display its output.

Because man pages are distributed together with the software they document, they are a more favourable means of documenting software compared to out-of-band documentation like web pages, as there is a higher likelihood for a match between the actual features of the software to the documented ones.[1] It is for this reason that man-pages are often referred to as an on-line or online form of software documentation, even though the man command does not require internet access, dating back to the times when printed out-of-band manuals were the norm.

### *Executable and Linkable Format (ELF)* | [Wiki (KR)](https://ko.wikipedia.org/wiki/ELF_%ED%8C%8C%EC%9D%BC_%ED%98%95%EC%8B%9D)
Executable and Linkable Format(ELF)는 실행 파일, 목적 파일, 공유 라이브러리 그리고 코어 덤프를 위한 표준 파일 형식이다. 1999년 86open 프로젝트에 의해 x86 기반 유닉스, 유닉스 계열 시스템들의 표준 바이너리 파일 형식으로 선택되었다.

ELF은 다양한 환경들에서 오래된 실행 파일 포맷을 대체했다. 유닉스 계열 운영체제 (리눅스, 솔라리스, IRIX, FreeBSD, NetBSD, OpenBSD, DragonFly BSD, Syllable, HP-UX, QNX Neutrino, 미닉스)에서 a.out과 COFF 포맷을 대체했으며, 유닉스 계열이 아닌 운영체제 (OpenVMS 아이테니엄 버전, BeOS Revions 4 이후 x86 기반, 하이쿠, RISC OS, Stratus VOS, Pa-RISC와 x86 버전)에서도 사용하고, 게임 콘솔 (플레이스테이션 포터블, 플레이스테이션 비타, 플레이스테이션 2, 플레이스테이션 3, 플레이스테이션 4, GP2X, 드림캐스트, 닌텐도 게임큐브, Wii, Wii U)에서도 사용한다.

### *ELF Symbol Visibility*
Dynamic linker의 symbol resolution을 도와주는 역할을 한다. `readelf`로 읽는 표에서 Vis 항목은 4가지 default, hidden, protected, internal 4종류가 있다.
- default는 visibilty를고려하지 않고 해당 symbol binding이 global인지 local(static)인지를 이용한다.
- hidden은 주로 사용되는 속성으로 해당 symbol을 외부로 공개하지 않게 만든다.
- protected는 잘 사용되지 않는 속성으로 공개하지만 다른 모듈에 의해 대체되지 않는다.
- internal은 잘 사용되지 않는 속성으로 해당 symbol을 공개하지 않으며 각 architecture 별로 약간씩 다른 효과를 가질 수 있다.

default는 외부로 공개할 symbol은 전역 변수, 함수, 내부에서만 사용할 symbol은 static으로 선언하면 된다. static으로 선언한 symbol은 항상 해당 파일 내의 symbol을 접근하는 것이므로 간접 접근이 필요없이 직접 접근이 가능하므로 컴파일러가 더 빠른 코드를 만들어 낼 수 있다. 또한 symbol이 외부로 공개되지 않으므로 relocation 및 symbol resolution 시에도 고려해야할 요소가 적어지므로 추가적인 성능 향상이 있다.

### Link `ln`
`ln`은 Link의 약어로 Linux 파일 시스템에서 링크 파일을 만드는 명령어이다. Linux에서는 symbolic link와 hard link 2가지 링크 파일이 존재한다.

### Symbolic Link
단순히 원본 파일을 가리키도록 링크만 시켜둔 것으로 Windows의 shortcut과 같은 것이며, 원본 파일을 가리키고만 있으므로 원본 파일의 크기와는 무관하다. 그리고 symbolic link에서는 원본 파일이 삭제되어 존재하지 않을 경우에 링크 파일은 깜박거리면서 링크 파일의 원본 파일이 없다는 것을 알려준다.

### Hard Link
원본 파일과 다른 이름으로 존재하는 동일한 파일이며 원본 파일과 동일한 내용의 다른 파일이다. 그리고 hard link에서는 원본 파일과 링크 파일 2개가 서로 다른 파일이기 때문에 둘 중 하나를 삭제하더라도 나머지 하나는 그대로 남아 있다. 또한 hard link에서는 원본 파일의 내용이 변경될 경우에는 링크 파일의 내용 또한 자동으로 변경된다.

#### Usage
- `ln -s /tmp /var/tmp`
- `ln hard_source hard_link`
- `--backup`: 대상 파일이 이미 존재할 경우에 백업 파일을 만든 후에 링크 파일 생성
- `-b`: 링크 파일 생성 시에 대상 파일이 이미 존재하면 백업 파일을 만든 후에 링크 파일을 생성
- `-d`: 디렉토리에 대한 하드 링크 파일 생성을 가능하게 함
- `-f`: 대상 파일이 존재할 경우에 대상 파일을 지우고 링크 파일을 생성
- `-i`: 대상 파일이 존재할 경우에 대상 파일을 지울 것인가를 확인 요청
- `-s`: Create Symbolic link file 생성
- `-S`: 백업 파일 생성 시에 원하는 suffix 지정
- `-t`: 링크 파일을 생성할 디렉토리를 지정

### *.a*
Linux의 정적 라이브러리로, 동적 라이브러리에 비해 실행 속도가 빠르고 배포에 제약이 없지만, 링크 되기에 실행 파일 또는 배포 파일의 사이즈가 커진다. 그러나 유닉스의 경우 필요한 부분만 메모리에 로딩하는 demand paging을 사용하기 때문에 정적인 라이브러리의 메모리와 공유 라이브러리의 메모리 사용량 차이가 크지 않다.

Shared library와 dynamic link library는 다르다. 그러나 대부분 shard library를 만들 때 dynamic link library를 사용한다.

.a에서 .o(object)를 뽑아낸 다음 ld로 so 타켓으로 만들면 된다.

### *.so*
Linux의 동적 라이브러리이다.

### *Alias*
#### Usage
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

### *tmux*
#### Install
```
$ sudo apt-get install tmux
```

### *openssh server*
#### Install
```
$ sudo apt-get install openssh-server
```
#### Usage
```
$ sudo service ssh start
$ sudo systemctl enable ssh
```

### *Symbolic Link*
리눅스 심볼릭 링크는 특정 파일이나 디렉토리에 대하여 참조를 하는 특수한 파일이다. 윈도우에서 바로가기와 동일하다고 할 수 있다.

### *Fuzzy Finder*
#### Install
  - `git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf`
  - `~/.fzf/install`
#### Usage
  - `Control` + `t`

### *htop* | [Wiki](https://en.wikipedia.org/wiki/Htop) | Unix
htop is an interactive system-monitor process-viewer and process-manager. It is designed as an alternative to the Unix program top. It shows a frequently updated list of the processes running on a computer, normally ordered by the amount of CPU usage. Unlike top, htop provides a full list of processes running, instead of the top resource-consuming processes. htop uses color and gives visual information about processor, swap and memory status. htop can also display the processes as a tree.

### *top* | [Wiki](https://en.wikipedia.org/wiki/Top_(software)) | Unix
top (table of processes) is a task manager program found in many Unix-like operating systems that displays information about CPU and memory utilization.

### *hostname*
- How to change hostname: `sudo vim /etc/hostname` and reboot; `sudo reboot now`

### Show Symbolic Link, Command `$ nm`
A command nm shows a list of symbolic links in object files.

#### How to use command nm
- Default
```bash
$ nm foo.o
          U _IO_getc
00000000  Y main
```
- Options
  - format: `-f`, POSIX `-f posix`, BSD `-f bsd`, sysv `-f sysv`
- Target acrchive file shows libraries as object files

#### Reference
- Program Files, Program Files (x86), https://www.howtogeek.com/129178/why-does-64-bit-windows-need-a-separate-program-files-x86-folder/, 2019-03-21-Thu
- Symbolic Link, https://fruitdev.tistory.com/85, 2020-08-05-Wed.
- Linux, https://www.linux.org/, 2020-08-05-Wed.
- ELF Wiki (Kor), https://ko.wikipedia.org/wiki/ELF_%ED%8C%8C%EC%9D%BC_%ED%98%95%EC%8B%9D, 2020-08-06-Thu.
- EXE Wiki (Kor), https://ko.wikipedia.org/wiki/EXE, 2020-08-06-Thu.
- 실행 파일 Wiki (Kor), https://ko.wikipedia.org/wiki/%EC%8B%A4%ED%96%89_%ED%8C%8C%EC%9D%BC, 2020-08-06-Thu.
- What is the DLL?, https://support.microsoft.com/ko-kr/help/815065/what-is-a-dll, 2020-08-06-Thu.
- DLL, https://goddaehee.tistory.com/185, 2020-08-06-Thu.
- Library, https://jasonjason.tistory.com/15, 2020-08-06-Thu.
- Shortcut, https://ko.wikipedia.org/wiki/%EB%B0%94%EB%A1%9C_%EA%B0%80%EA%B8%B0, 2020-08-08-Sat.
- Alias, https://webdir.tistory.com/107, 2020-08-25-Tue.
- openssh, https://jimnong.tistory.com/713, 2020-09-08-Tue.
- man page Wiki, https://en.wikipedia.org/wiki/Man_page, 2020-09-16-Wed.
- Unix Wiki, https://en.wikipedia.org/wiki/Unix, 2020-09-16-Wed.
- A diagram showing the key Unix and Unix-like operating systems, https://en.wikipedia.org/wiki/Unix#/media/File:Unix_history-simple.svg, 2020-09-16-Wed.
- Linux Wiki, https://en.wikipedia.org/wiki/Linux, 2020-09-16-Wed.
- Differences between Unix and Linux, https://m.blog.naver.com/PostView.nhn?blogId=limoremo&
- Linux vs. Unix, https://www.diffen.com/difference/Linux_vs_Unix, 20202-09-16-Wed.
- fuzzy finder Blog Kor, https://black7375.tistory.com/15, 2020-10-12-Mon.
- htop Wiki, https://en.wikipedia.org/wiki/Htop, 2020-09-28-Mon.
- top Wiki, https://en.wikipedia.org/wiki/Top_(software), 2020-09-28-Mon.
- Windows vs. Linux, http://tmmse.xyz/2020/04/22/linuxandwindows/, 2021-03-29-Mon.
- Library Visibility, https://cmake.org/cmake/help/latest/command/target_link_libraries.html, 2020-08-14-Fri.
- ELF Symbol Visibility Blog KR, http://egloos.zum.com/studyfoss/v/5257309, 2020-08-12-Wed.
- readelf Blog KR, https://m.blog.naver.com/PostView.nhn?blogId=yon7961&logNo=50097076949&proxyReferer=https:%2F%2Fwww.google.com%2F, 2020-08-12-Wed.
- readelf Option Blog KR, https://devanix.tistory.com/186, 2020-08-12-Wed.
- ln Blog KR, https://webdir.tistory.com/148, 2020-08-13-Thu.
- Dependency Management, https://architecture101.blog/2008/12/07/dependency_managment/, 2020-08-13-Thu.
- Command nm Blog KR, https://devanix.tistory.com/190, 2021-03-31-Wed.