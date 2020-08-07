# Debug
‘디버깅’이라는 용어는 여러 다양한 것을 의미할 수 있지만 대부분의 경우 코드에서 버그를 제거하는 것을 의미합니다. 현재 이 작업을 수행하는 방법은 여러 가지가 있습니다. 예를 들어 오타를 찾는 코드를 검사하거나 코드 분석기를 사용하여 디버그할 수 있습니다. 성능 프로파일러를 사용하여 코드를 디버그할 수도 있습니다. 또는 ‘디버거’를 사용하여 디버그할 수 있습니다.[Ref]

## GDB (GNU Debugger)
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

#### Reference
- What is debugging?, https://docs.microsoft.com/ko-kr/visualstudio/debugger/what-is-debugging?view=vs-2019, 2020-07-21-Tue.
