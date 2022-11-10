# _Terminal_ | [WiKi (KR)](https://ko.wikipedia.org/wiki/%EB%8B%A8%EB%A7%90%EA%B8%B0)

Terminal(단말기)는 컴퓨터나 컴퓨팅 시스템에 데이터를 입력하거나 표시하는데 쓰이는 전자 하드웨어 기기이다. 컴퓨터 터미널은 인간과 컴퓨터의 인터페이스(HMI)의 한 예이다. 터미널의 기능은 데이터를 보여 주고 입력하는데 제한을 받는다. 중대한 로컬 프로그래밍 데이터 기능이 있는 장치는 스마트 터미널(smart terminal) 또는 thin client라고 부른다. PC는 terminal 기능을 에뮬레이트하는 소프트웨어를 실행할 수 있으며 이따금 로컬 프로그램을 이용하여 먼 거리의 호스트 시스템에 접근할 수 있다.

- CLI: Command Line Interface
- GUI: Graphic User Interface

# _Shell_ | [WiKi (KR)](https://ko.wikipedia.org/wiki/%EC%85%B8)

Shell은 OS에서 다양한 OS 기능과 서비스를 구현하는 인터페이스를 제공하는 프로그램이다. Shell은 사용자와 OS kernel 사이의 인터페이스를 감싸는 층이기 때문에 이러한 이름이 붙었다. Shell은 일반적으로 명령 줄과 그래픽 형의 2종류로 분류된다. 명령 줄 shell은 OS에서 CLI를 제공하고, 그래픽 shell은 GUI를 제공한다. CLI와 GUI 기반 shell의 상대적 장점에 대해서는 논쟁이 많다. CLI 지지자는 CLI shell 상에서 일반적인 수행(파일 이동 등)을 훨씬 빠르게 할 수 있다고 주장한다. 반대로 GUI 지지자는 GUI shell의 상대적 사용성과 간편함을 내세운다. 일반적으로는 성능을 중시하고 숙련된 관리자의 작업에 주로 사용되는 서버의 경우는 CLI가 많이 쓰이며, 반면 일상적인 업무에 사용되는 컴퓨터엔 GUI가 많이 사용된다.

최초의 Unix shell인 켄 톰프슨의 sh는 Multix shell을 따라 모형화한 것이다. Bourne shell(sh)는 첫 Unix shell에서 파생했다. sh 이후에는 Bill Joy가 만든 csh(C shell)이 등장했으며, shell script를 작성하는 언어가 C 언어를 닮았기에 C shell이라 불린다. 다음에는 TC shell(tcsh)로 C shell의 기능에다가 command-completion(명령어-완성) 기능을 추가시켜 만든 public domain version이다. 실질적으로 모든 OS shell은 상호 작용과 일괄 방식으로 사용될 수 있으며 일괄 방식의 경우 여러 명령어를 나열하여 둔 텍스트 파일의 이름을 지정함으로써 사용하는 것이 보통이다. Shell을 이용하는 일괄 방식은 프로그래밍 언어의 구조, 조건, 변수 등을 동반한다.

### Bourne Shell | [WiKi (KR)](https://ko.wikipedia.org/wiki/%EB%B3%B8_%EC%85%B8)

Bourne shell(sh)는 Unix version 7의 기본 Unix shell이었다. 톰프슨 shell을 대체하는 shell로서 실행파일 이름이 sh로서 같다. AT&T Bell 연구소의 Stephen Bourne이 개발했고 1977년에 처음으로 Unix version 7에 포함되었다. 많은 Unix 계정에서 기본 shell로 사용될만큼 오랫동안 인기를 누렸다.

### _Bash, Bourne-again Shell, Unix Shell_ | [WiKi (KR)](https://ko.wikipedia.org/wiki/%EB%B0%B0%EC%8B%9C_(%EC%9C%A0%EB%8B%89%EC%8A%A4_%EC%85%B8))

Bash는 Bourne shell을 대체하는 free software로서 GNU project를 위해 Brian Fox가 작성한 Unix shell이다. Bash는 1989년 발표되어 GNU OS와 Linux, mac os X 그리고 Dawin 등 OS의 기본 shell로 탑재되어 광범위하게 배포되었다. Bash는 또한 DJGPP와 노벨 넷웨어에 의해 DOS로 이식되었고 Cygwin과 MinGW의 배포로 Microsoft Windows로 이식되었다.

### _[Zsh](https://www.zsh.org/)_ | [Zsh Web Pages](https://zsh.sourceforge.io/)

Zsh is a shell designed for interactive use, although it is also a powerful scripting language. Many of the useful features of bash, ksh, and tcsh were incorporated into zsh; many original features were added.

---

# I. _Windows_ | [Windows Commands](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands)

`This contents are from the 'Windows' page and the 'System' page.`

## i. _Command-line Shells_ | CMD (Command Prompt)

The Command shell was the first shell built into Windows to automate routine tasks, like user account management or nightly backups, with batch (.bat) files. With Windows Script Host, you could run more sophisticated scripts in the Command shell. For more information, see cscript or wscript. You can perform operations more efficiently by using scripts than you can by using the user interface. Scripts accept all commands that are available at the command line.

### A. _Commands_

```cmd
> exit # Exit Prompt
> powershell # Turn off CMD and turn on PowerShell
> Taskkill OPTION PROCESS_NAME PROCESS_PID_NUMBER # /f: forced, /im: 
```

Python:
- activate env 

doskey:
`doskey vi=vim`
`doskey clear=cls`
`doskey nn = cd D:\office\out\win && ninja`
`doskey ls=dir`

## ii. _[PowerShell](https://powershell.org/)_ | [Documentation](https://docs.microsoft.com/en-us/powershell/) | [What is PowerShell?](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.2)

PowerShell is a cross-platform task automation solution made up of a command-line shell, a scripting language, and a configuration management framework. PowerShell runs on Windows, Linux, and macOS.

PowerShell was designed to extend the capabilities of the Command shell to run PowerShell commands called cmdlets. Cmdlets are similar to Windows Commands but provide a more extensible scripting language. You can run both Windows Commands and PowerShell cmdlets in PowerShell, but the Command shell can only run Windows Commands and not PowerShell cmdlets.

### A. _Commands_

```powershell
PS powershell # Turn off PowerShell and turn on CMD
```

### B. _Plugin_

a. Color Tool (Changing Color Theme) | [Github](https://github.com/Microsoft/Terminal/tree/master/src/tools/ColorTool) | [Download](https://github.com/microsoft/terminal/releases/tag/1904.29002) version `Color Tool April 2019`:
```powershell
.\ColorTool.exe -s
.\ColorTool.exe solarized_dark.itermcolors
```

b. Changing a Font:
- 나눔고딕코드.exe 설치
- enter `win` + `R` and search `regedit`
- `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsNT\CurrentVersion\Console\TureTypeFont`
- click `949` and change `*굴림체` to `*나눔고딕코딩`
- open `PowerShell` and enter `alt` + `D`or enter `default setting`
- change font to `나눔고딕코딩`

Python:
- activate env 안됨

## iii. _Terminal_ | [GitHub](https://github.com/Microsoft/Terminal)

Windows 터미널은 명령 프롬프트, PowerShell 및 WSL과 같은 명령 줄 도구 및 셸 사용자를 위한 최신의 빠르고 효율적이며 강력한 생산성의 터미널 응용 프로그램입니다. 주요 기능으로는 여러 탭, 창, 유니 코드 및 UTF-8 문자 지원, GPU 가속 텍스트 렌더링 엔진 및 사용자 정의 테마, 스타일 및 구성이 있습니다.

### _Cygwin_ | [WiKi (KR)](https://ko.wikipedia.org/wiki/%EC%8B%9C%EA%B7%B8%EC%9C%88)

Cygwin은 원래 시그너스 솔루션스가 개발한 free software 모음집으로, Microsoft Windows에서 POSIX 기반 소프트웨어를 구동 및 개발할 수 있는 환경을 제공한다. GNU GPL로 배포되어 자유롭게 사용할 수 있다.

### _MinGW_ | [WiKi (KR)](https://ko.wikipedia.org/wiki/MinGW)

MinGW(과거 mingw32, Minimalist GNU for Windows 32-bit)는 Microsoft Windows로 포팅한 GNU software 도구 모음이다. MinGW은 Windows API를 구현할 수 있는 헤더 파일들을 가지고 있으며 이로써 자유롭게 쓸 수 있는 컴파일러인 GCC를 사용할 수 있다. Cygwin 포팅을 사용할 경우 컴파일한 프로그램 결과물이 Unix 계통의 기능을 가상으로 구현하는 run-time에 의존하는 반면, MinGW의 경우 이러한 기능에 의존하지 않고 Microsoft Windows 기반 프로그램들을 만들 수 있다. 이 MinGW 프로젝트는 2개의 기본 꾸러미를 관리하고 배포한다. 첫째로는 포팅된 GCC 컴파일러들은 Windows command line에서, 아니면 IDE에 통합된 채로 쓸 수 있다. 아니면 둘째로는 MSYS(Minimal System)를 쓸 수도 있는데, 이것은 가벼운 Unix 계통의 shell 환경을 제공한다. 이러한 환경은 rxvt와 autoconf scripts를 실행하는 데에 충분한 POSIX 도구들이 집약되어 있다. 2개의 꾸러미들은 원래 Cygwin 일부의 forks였으며 forks는 native Winodws 기능 덕에 더 포괄적인 Unix 계통의 지원을 제공한다. 2개의 꾸러미들은 free software이다. Win32 header 파일들은 공용 도메인에 공개된다. 반면 GNU에서 포팅되는 프로그램들은 GNU 일반 공중 사용 허가서 하에서 사용할 수 있다. 완전한 MSYS 꾸머리와 개별 MinGW GNU 유틸리티들의 바이너리 파일들은 MinGW 사이트에서 내려 받을 수 있다.

---

# II. _Unix & Linux & macOS_

`This contents are from the 'Linux' page and the 'System' page.`

Get root right:
- `su`
Check:
- `whoami`
Get out a root right:
- `exit`

## _Shell_

- Change Color:
```bash
 46 force_color_prompt=yes
 59 if [ "$color_prompt" = yes ]; then
 60     PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\[\033[00;32m\]\u\[\033[01;33m\]@\[\033[01;34m\]\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
```

### _Tmux_

Tmux is an application that can access/process multi terminal/process/session -s.

Tmux consists of session, window, and pane.

Session:
- base unit, consists of several windows, kind of a project

Window:
- terminal window, kind of a tab

Pane:
- spliting screens in a window

prefix for command:
- `ctrl` + `b`

```bash
$ tmux new -s SessionName # new session with SessionName
$ tmux new -s SessionName -n WindowName # new session and window with SessionName and WindowName
$ tmux list # tmux list
$ exit # tmux exit
$ tmux attach -t SessionName # restart
$ 'prefix' + d # pause session = detach
$ 'prefix' + t # time
$ 'prefix' + c # create a window
$ 'prefix' + % # split pane vertical
$ 'prefix' + " # split pane horizontal
$ 'prefix' + 'rudder' # move to each direction pane
$ 'prefix' + q # move to q number pane
$ 'prefix' + o # move to pane by order
$ 'prefix' + d # delete pane 
$ 'prefix' + alt + 'rudder' # modulate size of pane
$ 'prefix' + [ + 'up/down arrow' or 'page up/down' # Scroll up/down
$ 'prefix' + z # select only the pane
```

### _grep_

How to use:
- show line number: `-n` or `--line-number`
- ignore upper case and lower case: `-i` or `--ignore-case
- show only file name: `-l` or `--files-with-matches`
- search for sub directories: `-r` or `--recursive`
- except the string: `-v` or `--invert-match`
- include binary files as a text file: `-a` or `--text`
- search without binary files: `-I` same as another option `binary-files=without-match`

egrep: 
- Extended version of grep, it can search multiple strings and more meta regression.

fgrep: 
Search everything as a string. So it is faster than any other greps.

### _Terminal Pager_ | [WiKi](https://en.wikipedia.org/wiki/Terminal_pager)

A terminal pager, or paging program, is a computer program used to veiw (but not modify) the contents of a text file moving down the file one line or one screen at a tome. Some, but not all, pagers allow movement up a file. A popular cross-platform terminal pager is more, which can move forwards and backwards in text files but cannot move backwards in pipes. less is a more advanced pager that allows movement forward and backward, and contains extra functions such as search.

Some programs incorporate their own paging function, for example bash's tab completion function.

---

### Reference
- Tmux commands, https://seulcode.tistory.com/144, 2020-02-02-Tue.
- Tmux scroll, https://superuser.com/questions/209437/how-do-i-scroll-in-tmux, 2020-02-02-Tue.
- Color Tool, https://docs.microsoft.com/en-us/powershell/, 2020-02-19-Wed.
- Color Tool, https://github.com/Microsoft/Terminal/tree/master/src/tools/ColorTool, 2020-02-19-Wed.
- Font, https://www.delmaster.net/149, 2020-02-19-Wed.
- CLI, GUI, Console, CMD, Terminal, https://datascienceschool.net/view-notebook/26ca8377076541b2b514cd5ed97c554d/, 2020-03-10-Tue.
- CMD, https://namu.wiki/w/%EB%AA%85%EB%A0%B9%20%ED%94%84%EB%A1%AC%ED%94%84%ED%8A%B8/%EB%AA%85%EB%A0%B9%EC%96%B4, 2020-03-10-Tue.
- Shell 종류와 특징, https://jhnyang.tistory.com/57, 2020-03-10-Tue.
- Shell 종류, https://mclee.tistory.com/197, 2020-03-10-Tue.
- Console, Terminal, Shell 차이, https://infosecguide.tistory.com/15, 2020-03-10-Tue.
- Windows Terminal, https://github.com/Microsoft/Terminal, 2020-05-22-Fri.
- Windows Terminal, https://www.microsoft.com/ko-kr/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab, 2020-05-22-Fri.
- grep commands, https://geundi.tistory.com/113, 2020-08-28-Fri.
- - Change shell color, https://askubuntu.com/questions/123268/changing-colors-for-user-host-directory-information-in-terminal-command-prompt, 2020-10-29-Thu.
- Shell Wiki KR-KO, https://ko.wikipedia.org/wiki/%EC%85%B8, 2020-11-19-Thu.
- Bourne Shell Wiki KR-KO, https://ko.wikipedia.org/wiki/%EB%B3%B8_%EC%85%B8, 2020-11-19-Thu.
- Terminal Wiki KR-KO, https://ko.wikipedia.org/wiki/%EB%8B%A8%EB%A7%90%EA%B8%B0, 2020-11-19-Thu.
- Terminal, Console, Shell Blog KR-KO, http://blog.naver.com/asianchairshot/221383363419, 2020-11-19-Thu.
- Bash Wiki KR-KO, https://ko.wikipedia.org/wiki/%EB%B0%B0%EC%8B%9C_(%EC%9C%A0%EB%8B%89%EC%8A%A4_%EC%85%B8), 2020-11-20-Fri.
- Cygwin Wiki KR-KO, https://ko.wikipedia.org/wiki/%EC%8B%9C%EA%B7%B8%EC%9C%88, 2020-11-20-Fri.
- MinGW Wiki KR-KO, https://ko.wikipedia.org/wiki/MinGW, 2020-11-20-Fri.
- Zsh, https://www.zsh.org/, 2022-05-14-Sat.
- Zsh Web Pages, https://zsh.sourceforge.io/, 2022-05-14-Sat.
- Windows Commands, https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands, 2022-05-14-Sat.
- What is PowerShell?, https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.2, 2022-05-14-Sat.
- Terminal Pager WiKi, https://en.wikipedia.org/wiki/Terminal_pager, 2022-11-10-Thu.
