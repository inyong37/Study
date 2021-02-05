# Linux | [Homepage](https://www.linux.org/) | [Wiki](https://en.wikipedia.org/wiki/Linux) | [DOwnload](https://www.linux.org/pages/download/)

```This page is from the 'System' page.```

Linux is a family of open source Unix-like operating systems based on the Linux kernel, an operating system kernel first released on September 17, 1991, by Linus Torvalds. Linux is typically packaged in a Linux distribution.

Distributions include the Linux kernel and supporting system software and libraries, many of which are provided by the GNU Project. Many Linux distributions use the word "Linux" in their name, but the Free Software Foundation uses the name GNU/Linux to emphasize the importance of GNU software, causing some controversy.

Popular Linux distributions include Debian, Fedora, and Ubuntu. Commercial distributions include Red Hat Enterprise Linux and SUSE Linux Enterprise Server. Desktop Linux distributions include a windowing system such as X11 or Wayland, and a desktop environment such as GNOME or KDE Plasma. Distributions intended for servers may omit graphics altogether, or include a solution stack such as LAMP. Because Linux is freely redistributable, anyone may create a distribution for any purpose.

Linux was originally developed for personal computers based on the Intel x86 architecture, but has since been ported to more platforms than any other operating system. Because of the dominance of Android on smartphones, Linux also has the largest installed base of all general-purpose operating systems. Although it is used by only around 2.3 percent of desktop computers, the Chromebook, which runs the Linux kernel-based Chrome OS, dominates the US K–12 education market and represents nearly 20 percent of sub-$300 notebook sales in the US. Linux is the leading operating system on servers (over 96.4% of the top 1 million web servers' operating systems are Linux), leads other big iron systems such as mainframe computers, and is the only OS used on TOP500 supercomputers (since November 2017, having gradually eliminated all competitors).

Linux also runs on embedded systems, i.e. devices whose operating system is typically built into the firmware and is highly tailored to the system. This includes routers, automation controls, smart home technology (like Google Nest), televisions (Samsung and LG Smart TVs use Tizen and WebOS, respectively), automobiles (for example, Tesla, Audi, Mercedes-Benz, Hyundai, and Toyota all rely on Linux), digital video recorders, video game consoles, and smartwatches. The Falcon 9's and the Dragon 2's avionics use a customized version of Linux.

Linux is one of the most prominent examples of free and open-source software collaboration. The source code may be used, modified and distributed commercially or non-commercially by anyone under the terms of its respective licenses, such as the GNU General Public License.

### man page (Manual Page) | [Wiki](https://en.wikipedia.org/wiki/Man_page)
A man page (short for manual page) is a form of software documentation usually found on a Unix or Unix-like operating system. Topics covered include computer programs (including library and system calls), formal standards and conventions, and even abstract concepts. A user may invoke a man page by issuing the man command.

By default, man typically uses a terminal pager program such as more or less to display its output.

Because man pages are distributed together with the software they document, they are a more favourable means of documenting software compared to out-of-band documentation like web pages, as there is a higher likelihood for a match between the actual features of the software to the documented ones.[1] It is for this reason that man-pages are often referred to as an on-line or online form of software documentation, even though the man command does not require internet access, dating back to the times when printed out-of-band manuals were the norm.

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

### Fuzzy Finder
- Install
  - `git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf`
  - `~/.fzf/install`
- How to use
  - `Control` + `t`

### htop | [Wiki](https://en.wikipedia.org/wiki/Htop) | Unix
htop is an interactive system-monitor process-viewer and process-manager. It is designed as an alternative to the Unix program top. It shows a frequently updated list of the processes running on a computer, normally ordered by the amount of CPU usage. Unlike top, htop provides a full list of processes running, instead of the top resource-consuming processes. htop uses color and gives visual information about processor, swap and memory status. htop can also display the processes as a tree.

### top | [Wiki](https://en.wikipedia.org/wiki/Top_(software)) | Unix
top (table of processes) is a task manager program found in many Unix-like operating systems that displays information about CPU and memory utilization.

### hostname
- How to change hostname: `sudo vim /etc/hostname` and reboot(`sudo reboot -n`)

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
- MSDN, https://social.msdn.microsoft.com/forums/en-us/home, 2020-09-16-Wed.
- MSDN Wiki, https://en.wikipedia.org/wiki/Microsoft_Developer_Network, 2020-09-16-Wed.
- Microsoft Docs, https://docs.microsoft.com/en-us/, 2020-09-16-Wed.
- man page Wiki, https://en.wikipedia.org/wiki/Man_page, 2020-09-16-Wed.
- Unix Wiki, https://en.wikipedia.org/wiki/Unix, 2020-09-16-Wed.
- A diagram showing the key Unix and Unix-like operating systems, https://en.wikipedia.org/wiki/Unix#/media/File:Unix_history-simple.svg, 2020-09-16-Wed.
- Linux Wiki, https://en.wikipedia.org/wiki/Linux, 2020-09-16-Wed.
- Windows Wiki, https://en.wikipedia.org/wiki/Microsoft_Windows, 2020-09-16-Wed.
- Differences between Unix and Linux, https://m.blog.naver.com/PostView.nhn?blogId=limoremo&logNo=220533015236&proxyReferer=https:%2F%2Fwww.google.com%2F, 2020-09-16-Wed.
- macOS Wiki, https://en.wikipedia.org/wiki/MacOS, 2020-09-16-Wed.
- Macintosh Wiki, https://en.wikipedia.org/wiki/Macintosh_operating_systems, 2020-09-16-Wed.
- Linux vs. Unix, https://www.diffen.com/difference/Linux_vs_Unix, 20202-09-16-Wed.
- fuzzy finder Blog Kor, https://black7375.tistory.com/15, 2020-10-12-Mon.
- Solaris Wiki KR-KO, https://ko.wikipedia.org/wiki/%EC%86%94%EB%9D%BC%EB%A6%AC%EC%8A%A4_(%EC%9A%B4%EC%98%81_%EC%B2%B4%EC%A0%9C), 2020-10-29-Thu.
- Solaris Homepage, https://www.oracle.com/solaris/solaris11/, 2020-10-29-Thu.
- Unix history image Wiki KR-KO, https://ko.wikipedia.org/wiki/%EC%9C%A0%EB%8B%89%EC%8A%A4#/media/%ED%8C%8C%EC%9D%BC:Unix_history-simple.svg, 2020-10-29-Thu.
- Linux download, https://www.linux.org/pages/download/, 2020-10-29-Thu.
- Ubuntu, https://ubuntu.com/, 2020-10-29-Thu.
- CentOS, https://wiki.centos.org/FrontPage, 2020-10-29-Thu.
- Debian, https://www.debian.org/, 2020-10-29-Thu.
- Fedora, https://getfedora.org/, 2020-10-29-Thu.
- Mint, https://www.linuxmint.com/, 2020-10-29-Thu.
- Red Hat, https://access.redhat.com/, 2020-10-29-Thu.
- MS-DOS GitHub, https://github.com/Microsoft/MS-DOS, 2020-10-29-Thu.
- BSD Wiki KR-KO, https://ko.wikipedia.org/wiki/BSD, 2020-10-29-Thu.
- 86-DOS Wiki KR-KO, https://ko.wikipedia.org/wiki/86-%EB%8F%84%EC%8A%A4, 2020-10-30-Fri.
- PC-DOS Wiki KR-KO, https://ko.wikipedia.org/wiki/PC-DOS, 2020-10-30-Fri.
- MS-DOS Wiki KR-KO, https://ko.wikipedia.org/wiki/MS-DOS, 2020-10-30-Fri.
- CP/M Wiki KR-KO, https://ko.wikipedia.org/wiki/CP/M, 2020-10-30-Fri.
- CP/M, https://web.archive.org/web/20080515232659/http://www.digitalresearch.biz/CPM.HTM, 2020-10-30-Fri.
- 디스크 운영 체제 Wiki KR-KO, https://ko.wikipedia.org/wiki/%EB%94%94%EC%8A%A4%ED%81%AC_%EC%9A%B4%EC%98%81_%EC%B2%B4%EC%A0%9C 2020-10-30-Fri.
- 도스 Wiki KR-KO, https://ko.wikipedia.org/wiki/%EB%8F%84%EC%8A%A4, 2020-10-30-Fri.
- htop Wiki, https://en.wikipedia.org/wiki/Htop, 2020-09-28-Mon.
- top Wiki, https://en.wikipedia.org/wiki/Top_(software), 2020-09-28-Mon.
