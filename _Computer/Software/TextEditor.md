# Text Editor
```
This page is about text editor.
```
# I. Windows
- (That I'm using in)
## i. [Notepad (Directed to Notepad++)](https://notepad-plus-plus.org/) :sparkling_heart:
```
Notepad is basic text editor in Windows.
```
## ii. [Notepad++](https://notepad-plus-plus.org/) :heart:
```
Notepad++ is free source code editor and Notepad replacement that supports several languages. Running in the MS Windosws environment, its use is governed by GPL License.
```
## iii. [Atom](https://atom.io/) :green_heart:
```
Atom is made by Github. It is open source. It is based on Chromium project. It is made with Electron framework based on Chromium and Node.js.
```
## iv. [Sublime Text 3](https://www.sublimetext.com/) :yellow_heart:
```
Sublime Text is made by Sublime HQ. It is usually used for frontend and backend programming.
```
- Install packages: `Control` + `Shift` + `p`, `install package`
- Change theme: colorsublime

## v. [Visual Studio Code](https://code.visualstudio.com/) :blue_heart:
```
Visual Studio Code is made by Microsoft. It is based on Chromium project. It is made with Electron framework based on Chromium and Node.js.
```
- Find: `Control` + `f`
- Find and replace: `Control` + `h`,' `Enter`
- Find and replace all: `Control` + `h`, `Control` + `Alt` + `Enter`

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
### A. Commands
#### a. Basic
- Quit and Save
```
:q # quit
:qa # quit all
:q! # quit forced
:w # save
:wq # save and quit
```
- `u`: undo, `Control` + `r`: redo, `U`: only undo in cursor(caret) line.
- `:vs %:r.h`: open same name of header file.
- Search
```
/asdf # search asdf
n # see next 'asdf'
N # see previous 'asdf'
```
- Copy and Paste
```
yy # copy one line
Y # copy one line
p # paste the line under
P # paste the line above
dd # delete cursor line
```
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
### B. Plugin
- Plugin Manager [Vundle(Vim Bundle)](https://github.com/VundleVim/Vundle.vim) [for Windows](https://github.com/VundleVim/Vundle.vim/wiki/Vundle-for-Windows)
#### a. Ctags [Exuberant Ctags](http://ctags.sourceforge.net/) [Universal Ctags](https://ctags.io/)
```
Ctags generates an index (or tag) file of language objects found in sources files that allows these items to be quickly and easily located by a text editor and other utility. (from ctags.sourceforge.net, Exuberant Ctags)
Universal-ctags has the objective of continuing the development from what existed in the Sourceforge area. (from ctags.io, Universal-Ctags)
```
- `sudo apt-get install ctags`: install ctags.
- `ctags filename`: build tags for 'filename', `ctags -R`: build tags for all directory under current directory.
- `vim tags`: turn on tags file.
- Or use it in `vim`.
- `:tj functionname/variablename`: find 'functionname/variablename' declaration tags.
- `Control` + `]`: find current cursor's declaration tag.
- `:po`: go back to `vim`.
- `Control` + `t`: go back to `vim`.
- `:stj functionname/variablename`: find 'functionname/variablename' declaration tags in splited window.
#### b. [Tagbar](http://majutsushi.github.io/tagbar/) [Github](https://github.com/majutsushi/tagbar)
```
Tagbar is a Vim plugin that provides an easy way to browse the tags of the current file and get an overview of its structure.
```
- `:Tagbar` or `F8`: Open tagbar. # `nmap <F8> :TagbarToggle<CR>` in `~/.vimrc`.
- `Control` + `w` + `w`: change vim window.
#### c. [cscope]()
#### d. [fuzzy-finder]()
#### e. [you complete me]()

## Markdown Editor
### [Typora](https://typora.io/)
- [How to add as a command in windows](https://superuser.com/questions/689333/how-to-add-installed-program-to-command-prompt-in-windows)

##### Reference
1. Using Vi in windows with git, https://m.blog.naver.com/PostView.nhn?blogId=callor88&logNo=221051415755&proxyReferer=https%3A%2F%2Fwww.google.com%2F, 2020-01-29-Wed.
2. Notepad++, https://notepad-plus-plus.org/, 2020-01-29-Wed.
3. Vi and Vim, https://blockdmask.tistory.com/25, 2020-01-29-Wed.
4. Vim, https://www.vim.org/, 2020-01-29-Wed.
5. Ctags, https://ctags.io/, 2020-03-10-Tue.
6. Ctags commands, https://bowbowbow.tistory.com/15, 2020-03-23-Mon.
