# Terminal
```
This page is about Terminal in Unix/Linux, macOS/OS X, and Windows.
```
- CLI: Command Line Interface
- GUI: Graphic User Interface

# I. Windows
## i. CMD(Command Prompt)
### A. Commands
```
> exit # Exit Prompt
> powershell # Turn off CMD and turn on PowerShell
> Taskkill OPTION PROCESS_NAME PROCESS_PID_NUMBER # /f: forced, /im: 
```
#### Python
- activate env 
## ii. PowerShell | [Homepage](https://powershell.org/) | [Documentation](https://docs.microsoft.com/en-us/powershell/)
### A. Commands
```
PS powershell # Turn off PowerShell and turn on CMD
```
### B. Plugin
#### a. Color Tool (Changing Color Theme) | [Github](https://github.com/Microsoft/Terminal/tree/master/src/tools/ColorTool) | [Download](https://github.com/microsoft/terminal/releases/tag/1904.29002) version `Color Tool April 2019`
```
.\ColorTool.exe -s
.\ColorTool.exe solarized_dark.itermcolors
```

#### b. Changing Font
- 나눔고딕코드.exe 설치
- enter `win` + `R` and search `regedit`
- `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsNT\CurrentVersion\Console\TureTypeFont`
- click `949` and change `*굴림체` to `*나눔고딕코딩`
- open `PowerShell` and enter `alt` + `D`or enter `default setting`
- change font to `나눔고딕코딩`

#### Python
- activate env 안됨

## iii. Terminal | [GitHub](https://github.com/Microsoft/Terminal)
 Windows 터미널은 명령 프롬프트, PowerShell 및 WSL과 같은 명령 줄 도구 및 셸 사용자를 위한 최신의 빠르고 효율적이며 강력한 생산성의 터미널 응용 프로그램입니다. 주요 기능으로는 여러 탭, 창, 유니 코드 및 UTF-8 문자 지원, GPU 가속 텍스트 렌더링 엔진 및 사용자 정의 테마, 스타일 및 구성이 있습니다.

# II. Unix/Linux
- get a root right `su`
- check `whoami`
- get out a root right `exit`

### Tmux
Tmux is an application that can access/process multi terminal/process/session -s.

Tmux consists of session, window, and pane.

- Session: base unit, consists of several windows, kind of a project
- Window: terminal window, kind of a tab
- Pane: spliting screens in a window
- `prefix` = `ctrl` + `b`

```
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

### grep

#### egrep
Extended version of grep, it can search multiple strings and more meta regression.

#### fgrep
Search everything as a string. So it is faster than any other greps.

#### Reference
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
