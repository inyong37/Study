# Terminal
(Shell.md와 정리 필요)
```
This page is about Terminal in Unix/Linux, macOS/OS X, and Windows.
- CLI: Command Line Interface
- GUI: Graphic User Interface
```
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
## ii. [PowerShell](https://powershell.org/)
[Documentation](https://docs.microsoft.com/en-us/powershell/)
### A. Commands
```
PS powershell # Turn off PowerShell and turn on CMD
```
### B. Plugin
#### a. Color Tool: Changing Color Theme [Github](https://github.com/Microsoft/Terminal/tree/master/src/tools/ColorTool)
[Download](https://github.com/microsoft/terminal/releases/tag/1904.29002) version `Color Tool April 2019`
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
# II. Unix/Linux
- get a root right `su`
- check `whoami`
- get out a root right `exit`
### Tmux
```
Tmux is an application that can access/process multi terminal/process/session -s.
Tmux consists of session, window, and pane.
```
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

#### Reference
- Tmux commands, https://seulcode.tistory.com/144, 2020-02-02-Tue.
- Tmux scroll, https://superuser.com/questions/209437/how-do-i-scroll-in-tmux, 2020-02-02-Tue.
- Color Tool, https://docs.microsoft.com/en-us/powershell/, 2020-02-19-Wed.
- Color Tool, https://github.com/Microsoft/Terminal/tree/master/src/tools/ColorTool, 2020-02-19-Wed.
- Font, https://www.delmaster.net/149, 2020-02-19-Wed.
- CLI, GUI, Console, CMD, Terminal, https://datascienceschool.net/view-notebook/26ca8377076541b2b514cd5ed97c554d/, 2020-03-10-Tue.
- CMD, https://namu.wiki/w/%EB%AA%85%EB%A0%B9%20%ED%94%84%EB%A1%AC%ED%94%84%ED%8A%B8/%EB%AA%85%EB%A0%B9%EC%96%B4, 2020-03-10-Tue.
