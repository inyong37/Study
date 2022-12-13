# Editor
This page is about (text) editor.

# I. Windows
## i. [Notepad (Directed to Notepad++)](https://notepad-plus-plus.org/) :sparkling_heart:
Notepad is basic text editor in Windows.

## ii. [Notepad++](https://notepad-plus-plus.org/) :heart:
Notepad++ is free source code editor and Notepad replacement that supports several languages. Running in the MS Windosws environment, its use is governed by GPL License.

## iii. [Atom](https://atom.io/) :green_heart:
Atom is made by Github. It is open source. It is based on Chromium project. It is made with Electron framework based on Chromium and Node.js.

## iv. [Sublime Text 3](https://www.sublimetext.com/) :yellow_heart:
Sublime Text is made by Sublime HQ. It is usually used for frontend and backend programming.
### Keymap
- Install packages: `Control` + `Shift` + `p`, `install package`
- Change theme: colorsublime
- Find keyword in file: `Contorl` + `f`
- Find keyword in project: `Control` + `Shift` + `f`
- Find file in project: `Control` + `p`
- Show/hide side bar(folder): `Control` + `k` + `Control` + `b`
### Custom Keymap: Preferences>Key Bindings>"Default (Windows).sublime-keymap - User"
- Show/hide side bar(folder/project): `alt` + `1` (as PyCharm)
- Go to file(find file in project): `Control` + `Shift` + `n` (as PyCharm)
```
[
  { "keys": ["alt+1"], "command": "toggle_side_bar" },
  { "keys": ["ctrl+shift+n"], "command": "show_overlay", "args": {"overlay": "goto", "show_files": true} },
  { "keys": ["ctrl+shift+f"], "command": "show_panel", "args": {"panel": "find_in_files"} }
]
```

## v. [Visual Studio Code](https://code.visualstudio.com/) :blue_heart:
Visual Studio Code is made by Microsoft. It is based on Chromium project. It is made with Electron framework based on Chromium and Node.js.

- Find file: `Control` + `e` or `Control` + `p`
- Find in file: `Control` + `f`
- Find in files: `Control` + `Shift` + `f`
- Find and replace: `Control` + `h`,' `Enter`
- Find and replace all: `Control` + `h`, `Control` + `Alterate` + `Enter`
- Show/Hide Side Bar: `Control` + `b`
- Show/Hide Panel: `Control` + `j`
### Custom Keyboard Shortcuts
File-Preferences-Keyboard Shortcuts
- Go to File: `ctrl+p` -> `Control + Shift + n`
- Show/Hide Side Bar: `ctrl+b` -> `Alternate + 1`

# II. Unix/Linux
- (That I'm using in)
## i. [Nano](https://www.nano-editor.org/) :sparkling_heart:
```
Nano is an UNIX GNU text editor.
```
## ii. [Emacs](https://www.gnu.org/software/emacs/) :blue_heart:
```
GNU Emacs is an extensible, customizable, free/libre text editor.
```
## iii. [Vi (Directed to vim)](https://www.vim.org/) :purple_heart:
```
Vi is basic text editor in Unix.
```
## iv. [Vim (Vi IMproved)](https://www.vim.org/) :star:
```
Vim is basic text editor in Linux. Vim is a highly configurable text editor for efficiently creating and changing any kind of text. It is included as "vi" with most UNIX systems and with Apple OS X.
```
It has 3 modes, command mode, insert mode, visual mode.
### A. Commands
#### a. Basic
- Enter editing mode: `i` or `I` or `a` or `A` or `r` or `R` or `o` or `O`
  - Insert: `I` or `i`
  - Add: `A` or `a`
  - Revise: `R` or `r`
  - `O` or `o`
- Quit and Save
  - Quit: `q`
  - Quit all: `qa`
  - Quit without saved: `q!`
  - Save: `w`
  - Save and quit: `wq`
- Undo and Redo
  - Undo: `u`
  - Undo cursor/caret line: `U`
  - Redo: `Control` + `r`
- Open
  - Open same name of header file: `:vs %:r.h`
  - Open same name of source code file: `:vs %:r.cc`
- Search
  - Search 'word' `/word`
  - See next: `n`
  - See previous `N`
- Copy and Paste
  - Copy cursor/caret line: `yy`
  - Copy cursor/caret line: `Y`
  - Paste under: `p`
  - Paste above: `P`
  - Delete/cut cursor/caret line: `dd`
- Block
  - Visual mode: `v`
- 

#### b. Window
```
:help windows # see window's contents
:split # split window horizontal like tmux's prefix + "
:vsplit # split window vertical like tmux's prefix + %
'Control' + 'w' + 'h' # move window far left
'Control' + 'w' + 'j' # move window very bottom
'Control' + 'w' + 'k' # move window very top
'Control' + 'w' + 'l' # move window far right
'Control' + 'w' + 'x' # change the windows' position with before one
'Control' + 'w' + 'r' # change the windows' position by oreder
'Control' + 'w' + '=' # make every windows' size the same
'Control' + 'w' + '_' # make window's size the biggest in horizontal
'Control' + 'w' + '|' # make window's size the biggest in vertical
```
#### c. Tab
```
:help tabpage # see tab's contents
:tab help tabpage # new tab with tab's contents
:tabnew # new tab
:tabclose # close tab
#gt # move to #-th tab
:tabfirst # move to first tab
:tablast # move to last tab
:tabs # show all tabs' information
```
- Move
  - Move to right tab: `gt`
  - Move to left tab: `gT`

#### d. Buffer
- Open: `vi a.cc b.h`
- List: `:ls` or `:buffers` or `:files`
- Move to # number: `:b#`
  - `:b1`
- Delete # number: `:bd#` or `:bw#`
- Move previous #: `:bp#`
- Move next #: `:bn#`
- Seperate parallel and load #: `:sb#`
- Move to first buffer: `:bf`
- Move to last buffer: `:bl`


### B. Plugin
- Plugin Manager [Vundle(Vim Bundle)](https://github.com/VundleVim/Vundle.vim) [for Windows](https://github.com/VundleVim/Vundle.vim/wiki/Vundle-for-Windows)

### a. Ctags | [Exuberant Ctags](http://ctags.sourceforge.net/) | [Universal Ctags](https://ctags.io/)
Ctags generates an index (or tag) file of language objects found in sources files that allows these items to be quickly and easily located by a text editor and other utility. (from ctags.sourceforge.net, Exuberant Ctags)

Universal-ctags has the objective of continuing the development from what existed in the Sourceforge area. (from ctags.io, Universal-Ctags)

#### How to use ctags
- Install ctags: `$ sudo apt-get install ctags`
- Build ctags for all directory under current directory: `$ ctags -R`
- Build ctags for 'file_name': `ctags file_name`
- Find current cursor's declaration tag: `Control` + `]`
- Go back to vim after tag: `control` + `t`
- Find declaration/definition 'name': `:ta name`
- `vim tags`: turn on tags file.
- Or use it in `vim`.
- `:tj functionname/variablename`: find 'functionname/variablename' declaration tags.
- `:po`: go back to `vim`.
- `:stj functionname/variablename`: find 'functionname/variablename' declaration tags in splited window.

### b. [Tagbar](http://majutsushi.github.io/tagbar/) [Github](https://github.com/majutsushi/tagbar)
Tagbar is a Vim plugin that provides an easy way to browse the tags of the current file and get an overview of its structure.
#### How to use tagbar
- `:Tagbar` or `F8`: Open tagbar. # `nmap <F8> :TagbarToggle<CR>` in `~/.vimrc`.
- `Control` + `w` + `w`: change vim window.

#### c. [cscope]()
#### d. [fuzzy-finder]()
#### e. [you complete me]()

---

### _[Neovim](https://neovim.io/)_

hyperextensible Vim-based text editor

---

## Markdown Editor

### _[Typora](https://typora.io/)_

- [How to add as a command in windows](https://superuser.com/questions/689333/how-to-add-installed-program-to-command-prompt-in-windows)

- Keybinding, Keymap
File - Preference - General - Open Advanced Setting - `config.user.json`
```xml
    "keyBinding": {
    // for example: 
    // "Always on Top": "Ctrl+Shift+P"
    "Toggle Sidebar": "Alt+1"
  },
```

---

### Reference
1. Using Vi in windows with git, https://m.blog.naver.com/PostView.nhn?blogId=callor88&logNo=221051415755&proxyReferer=https%3A%2F%2Fwww.google.com%2F, 2020-01-29-Wed.
2. Notepad++, https://notepad-plus-plus.org/, 2020-01-29-Wed.
3. Vi and Vim, https://blockdmask.tistory.com/25, 2020-01-29-Wed.
4. Vim, https://www.vim.org/, 2020-01-29-Wed.
5. Ctags, https://ctags.io/, 2020-03-10-Tue.
6. Ctags commands, https://bowbowbow.tistory.com/15, 2020-03-23-Mon.
- Vim-undo, https://techlog.gurucat.net/175, 2020-07-13-Mon.
- Vim-Block, https://jinnydown.tistory.com/entry/vim-%EC%9E%98%EB%9D%BC%EB%82%B4%EA%B8%B0%EB%B3%B5%EC%82%AC-%ED%9B%84-%EB%B6%99%EC%9D%B4%EA%B8%B0, 2020-07-13-Mon.
- pathogen.vim, https://www.vim.org/scripts/script.php?script_id=2332, 2020-08-11-Tue.
- pathogen.vim GitHub, https://github.com/tpope/vim-pathogen, 2020-08-11-Tue.
- useful .vimrc, https://eldora.tistory.com/171, 2020-08-11-Tue.
- pathogen, vundle, https://medium.com/@breadmj/pathogen-%EC%97%90%EC%84%9C-vundle-%EB%A1%9C-110104a57833, 2020-08-11.Tue.
- vundle.vim, https://github.com/VundleVim/Vundle.vim, 2020-08-11-Tue.
- useful .vimrc, https://blog.outsider.ne.kr/518, 2020-08-11-Tue.
- Vim Buffer, https://opentutorials.org/course/730/4571, 2020-08-12-Wed.
- ctags commands, https://harryp.tistory.com/130, 2020-09-02-Wed.
- Sublime Text Keymap Blog (KR), https://webclub.tistory.com/323, 2021-02-26-Fri.
- Neovim, https://neovim.io/, 2022-12-13-Tue.
