# Terminal
```
This page is about Terminal in Unix/Linux, MAC OS X, and Windows.
```

## Windows

### PowerShell

### Color Tool:Changing Color Theme [Github](https://github.com/Microsoft/Terminal/tree/master/src/tools/ColorTool)

[Download](https://github.com/microsoft/terminal/releases/tag/1904.29002) version `Color Tool April 2019`

```
.\ColorTool.exe -s
.\ColorTool.exe solarized_dark.itermcolors
```

[Reference](https://github.com/Microsoft/Terminal/tree/master/src/tools/ColorTool)

### Changing Font
- 나눔고딕코드.exe 설치
- enter `win` + `R` and search `regedit`
- `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsNT\CurrentVersion\Console\TureTypeFont`
- click `949` and change `*굴림체` to `*나눔고딕코딩`
- open `PowerShell` and enter `alt` + `D`or enter `default setting`
- change font to `나눔고딕코딩`

[Reference](https://www.delmaster.net/149)

## Unix/Linux

### Tmux
```
Tmux is application that can access/process multi terminal/process/session -s.
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
$ 'prefix' + d # pause session
$ 'prefix' + t # time
$ 'prefix' + c # create a window
$ 'prefix' + % # split pane 1
$ 'prefix' + # # split pane 2
$ 'prefix' + 'rudder' # move to each direction pane
$ 'prefix' + q # move to q number pane
$ 'prefix' + o # move to pane by order
$ 'prefix' + d # delete pane 
$ 'prefix' + alt + 'rudder' # modulate size of pane
```

[Reference](https://seulcode.tistory.com/144)
