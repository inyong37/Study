# :hammer_and_wrench: _Debug_

‘디버깅’이라는 용어는 여러 다양한 것을 의미할 수 있지만 대부분의 경우 코드에서 버그를 제거하는 것을 의미한다. 현재 이 작업을 수행하는 방법은 여러 가지가 있다. 예를 들어 오타를 찾는 코드를 검사하거나 코드 분석기를 사용하여 디버그할 수 있다. 성능 프로파일러를 사용하여 코드를 디버그할 수도 있다. 또는 ‘디버거’를 사용하여 디버그할 수 있다.[Ref]

## _[GDB: The GNU Project Debugger](https://www.gnu.org/software/gdb/)_ | Unix

GDB, the GNU Project debugger, allows you to see what is going on `inside' another program while it executes -- or what another program was doing at the moment it crashed.

GDB can do four main kinds of things (plus other things in support of these) to help you catch bugs in the act:
- Start your program, specifying anything that might affect its behavior.
- Make your program stop on specified conditions.
- Examine what has happened, when your program has stopped.
- Change things in your program, so you can experiment with correcting the effects of one bug and go on to learn about another.

Those programs might be executing on the same machine as GDB (native), on another machine (remote), or on a simulator. GDB can run on most popular UNIX and Microsoft Windows variants, as well as on Mac OS X.
#### Language
- Ada, Assembly, C, C++, D, Fortran, Go, Objective-C, OpenCL, Modula-2, Pascal, Rust
#### How to use
- Start GDB `gdb .ProgramName`
- Set breakpoint `b SourceCode.cc`
- Run `r`
- Continue `c`
- Stop `ctrl` + `c`
- See source code `ctrl` + `x` + `a`
- Step `s`
- Next `n`
- Up `up`
- Down `down`
- Fin `fin`
- Quit `quit`

## Visual Studio | [Homepage](https://visualstudio.microsoft.com/vs/) | Windows
### Debug an app that isn't part of a Visual Studio solution (C++, C#, Visual Basic, F#) | [MS Docs](https://docs.microsoft.com/en-us/visualstudio/debugger/how-to-debug-an-executable-not-part-of-a-visual-studio-solution?view=vs-2019)
### Develop code in Visual Studio without projects or solutions | [MS Docs](https://docs.microsoft.com/en-us/visualstudio/ide/develop-code-in-visual-studio-without-projects-or-solutions?view=vs-2019#run-and-debug-your-code)
#### Run and debug your code
You can debug your code in Visual Studio without a project or solution! To debug some languages, you may need to specify a valid startup file in the codebase, such as a script, executable, or project. The drop-down list box next to the Start button on the toolbar lists all of the startup items that Visual Studio detects, as well as items you specifically designate. Visual Studio runs this code first when you debug your code.

Configuring your code to run in Visual Studio differs depending on what kind of code it is, and what the build tools are.
### Open Folder support for C++ build systems in Visual Studio | [MS Docs](https://docs.microsoft.com/en-us/cpp/build/open-folder-projects-cpp?view=vs-2019#configure-debugging-parameters-with-launchvsjson)
#### CMake and Qt
CMake is integrated in the Visual Studio IDE as a component of the C++ desktop workload. The workflow for CMake is not identical to the workflow described in this article. If you are using CMake, see CMake projects in Visual Studio. You can also use CMake to build Qt projects, or you can use the Qt Visual Studio Extension for either Visual Studio 2015 or Visual Studio 2017.
#### How to use
- Start/Continue debuggin: `F5`
- Stop debugging: `Shift` + `F5`
- Restart debugging: `Control` + `Shift` + `F5`
- Step into: `F11`
- Step over: `F10`
- Step out: `Shift` + `F11`

---

### Reference
- What is debugging?, https://docs.microsoft.com/ko-kr/visualstudio/debugger/what-is-debugging?view=vs-2019, 2020-07-21-Tue.
- Debug an app that isn't part of a Visual Studio solution (C++, C#, Visual Basic, F#), https://docs.microsoft.com/en-us/visualstudio/debugger/how-to-debug-an-executable-not-part-of-a-visual-studio-solution?view=vs-2019, 2020-09-18-Fri.
- Develop code in Visual Studio without projects or solutions, https://docs.microsoft.com/en-us/visualstudio/ide/develop-code-in-visual-studio-without-projects-or-solutions?view=vs-2019#run-and-debug-your-code, 2020-09-18-Fri.
- Open Folder support for C++ build systems in Visual Studio, https://docs.microsoft.com/en-us/cpp/build/open-folder-projects-cpp?view=vs-2019#configure-debugging-parameters-with-launchvsjson, 2020-09-18-Fri.
- GDB, https://www.gnu.org/software/gdb/, 2020-09-18-Fri.
- Visual Studio, https://visualstudio.microsoft.com/vs/, 2020-09-18-Fri.
- How to use Visual Studio debugging, https://zapiro.tistory.com/entry/Visual-Studio-%EB%94%94%EB%B2%84%EA%B1%B0-%EC%82%AC%EC%9A%A9%EB%B2%95, 2020-09-18-Fri.
