# Python | [Homepage](https://www.python.org/) | [Document (3.7.10)](https://docs.python.org/3.7/)
```
This page is from the "Language" page.
```
## :computer: Anaconda | [Homepage](https://www.anaconda.com/) | [Document Individual Edition](https://docs.anaconda.com/anaconda/) | [Cheat Sheet](https://docs.anaconda.com/_downloads/9ee215ff15fde24bf01791d719084950/Anaconda-Starter-Guide.pdf) | [Archive](https://repo.anaconda.com/archive/)
The Most Trusted Distribution for Data Science.

Anaconda is a package manager, an environment manager, a Python/R data science distribution, and a collection of over 7,500+ open-source packages. Anaconda is free and easy to install, and it offers free community support.

## :computer: PyCharm | [Homepage](https://www.jetbrains.com/pycharm/) | [Other Versions](https://www.jetbrains.com/pycharm/download/other.html)
The Python IDE for Professional Developers.

### Settings>Keymap
- Settings: `Control` + `Alt` + `s`.
- ~~Settings: `Shift` + `Control` + `Alt` + `F4`.~~
- Main menu
  - Code>Folding
    - Comment with Line Comment: `Control` + `/`.
    - Comment with Block Comment: `Control` + `Shift` + `/`.
  - Navigate
    - Search Everywhere: `Control` + `Shift` + `f`.
    - ~~Search Everywhere: `Shift` + `Shift`.~~
    - Go to File: `Control` + `Shift` + `n`.
    - Go to Line/Column: `Control` + `g`.
    - Next Highlighted Error: `F2`.
    - Previous Highlighted Error: `Shift` + `F2`.
  - Navigate>Navigate in File
    - Go to Declaration or Usgae:
    - Go to Implementation(s):
    - Go to Type Declaration:
    - Go to Super Method:
    - Related Symbol
  - Run
    - Run: `F5`.
    - ~~Run: `Control` + `Shift` + `F5`.~~
    - Debug: `F6`.
    - Step Over: `F10`.
    - Step Into: `F11`.
    - Step Out: `F12`.
    - Pause Program: `F7`.
    - Resume Program: `F8`.
- Tool Windows
  - Terminal: `Alt` + `3`.
  - Python console: `Alt` + `2`.
  - Python console: ~~`Shift` + `Control` + `Alt` + `F6`.~~
- Plug-ins
  - Python Community Edition
    - Run file in console: `Shift` + `F5`.
    - ~~Run file in console: `Control` + `r`~~
    - ~~Run file in console: `Shift` + `Control` + `Alt` + `F5`.~~
    - ~~Run file in console: `Shift` + `Control` + `Alt` + `F5`.~~
- Other
  - Rerun: `Control` + `F5`.
  - ~~Rerun: `Control` + `Shift` + `r`.~~
  - ~~Rerun: `Shift` + `Control` + `Alt` + `F7`.~~
  - Change View: `Alt` + `F1`.

### Setting>Build, Execution, Deployment>Console>Python Console
- Starting script: Add "!chcp 65001" for encoding utf-8

### Settings>Tools>Terminal
- Shell Path:
  - cmd.exe: "C:\Windows\System32\cmd.exe"
  - git base.exe: "C:\Program Files\Git\bin"
  - git-bash: "C:\Program Files\Git\git-bash.exe"
  - git-cmd: "C:\Program Files\Git\git-cmd.exe"

----------

## :books: Built-in Function | [Document Python 3.7.9](https://docs.python.org/3.7/library/functions.html)

----------

## :books: Built-in Constant | [Document Python 3.7.9](https://docs.python.org/3.7/library/constants.html)

----------

## :books: Libraries

### argparse | [Document Python 3.7.9](https://docs.python.org/3.7/howto/argparse.html)
```Python
import argparse

parser = argparse.ArgumentParser(description='Argument Parse')
parser.add_argument('--argument', '-a', type=str, help='an argument', dest='arg_1')
args = parser.parse_args()
```
### dataclasses - Data Classes | [Docs 3.7.10](https://docs.python.org/3.7/library/dataclasses.html) | [PEP 557](https://www.python.org/dev/peps/pep-0557/)
```Python
from dataclasses import dataclass

@dataclass
class SampleDataClass:
  item: str
  def PrintItem(self) -> None:
    print(self.item)
```

### doctest | [Document Python 3.7.9](https://docs.python.org/3.7/library/doctest.html)
The [doctest]() module searches for pieces of next that look like interactive Python sessions, and then executes those sessions to verify that they work exactly as shown. There are several common ways to use doctest:
- To check that a module's docstrings are up-to-date by verifying that all interactive examples still work as documented.
- To perform regression testing by verifying that interactive examples from a test file or a test object work as expected.
- To write tutorial documentation for a package, liberally illustrated with input-output examples. Depending on whether the examples or the expository text are emphasized, this has the flavor of "literate testing" or "executable documentation".

Test in classes or functions in documentation field
```python
import doctest

def bar():
  >>> bar()
  foo
  return foo
```

And

`$ python test.py -v`

### fileinput | [Document Python 3.7.9](https://docs.python.org/3.7/library/fileinput.html)
This module implements a helper class and functions to quickly write a loop over standard input or a list of files. If you just want to read or write on file see [open()]()

### io | [Document Python 3.7.9](https://docs.python.org/3.7/library/io.html)
The [io]() module provides Python’s main facilities for dealing with various types of I/O. There are three main types of I/O: *text I/O*, *binary I/O* and *raw I/O*. These are generic categories, and various backing stores can be used for each of them. A concrete object belonging to any of these categories is called a [file object](). Other common terms are stream and *file-like object*.

Independent of its category, each concrete stream object will also have various capabilities: it can be read-only, write-only, or read-write. It can also allow arbitrary random access (seeking forwards or backwards to any location), or only sequential access (for example in the case of a socket or pipe).

All streams are careful about the type of data you give to them. For example giving a [str]() object to the `write()` method of a binary stream will raise a [TypeError](). So will giving a [bytes]() object to the `write()` method of a text stream.

Changed in version 3.3: Operations that used to raise [IOError]() now raise [OSError](), since [IOError]() is now an alias of [OSError]().

- Python2.x의 경우 Python의 내장 함수 open()에서 encoding keyword가 부적절하다는 에러 발생 시 다음을 사용하면 해결할 수 있다.
```Python
import io
file = io.open(file_name, 'r', encoding='utf-8')
```

### Matplotlib | [Homepage](https://matplotlib.org/) | `from matplotlib import pyplot as plt`
Matplotlib is a comprehensive library for creating static, animated, and interactive visuallizations in Python.

### Numpy | [Homepage](https://numpy.org/) | `import numpy as np`
The fundamental package for scientific computing with Python.

### os | [Document Python 3.7.9](https://docs.python.org/3.7/library/os.html)
This module provides a portable way of using operating system dependent functionality. If you just want to read or write a file see [open()](), if you want to manipulate paths, see the [os.path]() module, and if you want to read all the lines in all the files on the command line see the [fileinput]() module. For creating temporary files and directories see the [tempfile]() module, and for high-level file and directory handling see the [shutil]() module.

- os.**rename**(*src*, *dst*, *, *src_dir_fd=None*, *dst_dir_fd=None*)

Rename the file or directory *src* to *dst*. If *dst* exists, the operations will fail with an [OSError]() subclass in a number of cases: On Windows, if *dst* exosts a [FileExistsError]() is always raised. On Unix, if *src* is a file and *dst* is a directory or vice-versa, an [IsADirectoryError]() or a [NotADirectoryError]() will be raised respectively. If both are directories and *dst* is empty, *dst* will be silently replaced. If *dst* is a non-empty directory, an [OSError]() is raised. If both are files, *dst* it will be replaced silently if the user has permission. The operation may fail on some Unix flavors if *src* and *dst* are on different filesystems. If successful, the renaming will be an atomic operation (this is a POSIX requirement).

### Pandas | [Homepage](https://pandas.pydata.org/) | `import pandas as pd`
Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.

### platform | [Document Python 3.7.9](https://docs.python.org/3.7/library/platform.html)
Access to underlying platform's identifying data

- platform.**system**()
Returns the system/OS name, such as `Linux`, `Darwin`, `Java`, `Windows`. An empty string is returned if the value cannot be determined.

### pywin32

### Scikit-learn | [Homepage](https://scikit-learn.org/) | `import sklearn`
Scikit-learn is a simple and efficient tools for predictive data analysis. It is a accessible to everybody, and reusable in various contexts. It is built on Numpy, SciPy and Matplotlib. It is a open source, commercially usable - BSD license.

### SciPy | [Homepage](https://www.scipy.org/) | `import scipy`
The SciPy library is one of the core packages that make up the SciPy stack. It provides many user-friendly and efficient numberical routines, such as routines for numerical integration, interpolation, optimization, linear algebra, and statistics.

### selenium

### shutil | [Document Python 3.7.9](https://docs.python.org/3.7/library/shutil.html)
The [shutil]() module offers a number of high-level operations on files and collections of files. In particular, functions are provided which support file copying and removal. For operations on individual files, see also the [os]() module.

### subprocess | [Docs 3.7.10](https://docs.python.org/3.7/library/subprocess.html)

### tempfile | [Document Python 3.7.9](https://docs.python.org/3.7/library/tempfile.html)

----------

## :books: Built-in Exceptions | [Document Python 3.7.9](https://docs.python.org/3.7/library/exceptions.html)

----------

## :pencil2: PIP
pip is the package installer for Python.
- Installation: `sudo apt-get install python-pip` or `sudo apt-get install python3-pip` or `pip install pip`
- Usage: `pip install/uninstall package_name [options]`

### :pencil2: Copy
기존 객체와 같은 값을 가진 새로운 객체를 만든다는 것임, 객체들은 멤버를 가지고 있고 그 멤버들은 값일 수도 있고 참조 형식일 수도 있음, 이 객체들이 가진 값 형식과 참조 형식의 복제 방식에 따라 얕은 복사와 깊은 복사의 개념이 나뉨.

#### 단순 객체 복사
동일한 객체를 참고하기 때문에 한 곳에서 값을 변경하면 같이 값이 변경된다.

#### 얕은 복사 (Shallow Copy)
얕은 복사는 객체가 가진 멤버들의 값을 새로운 객체로 복사하는데 만약 객체가 참조 타입의 멤버를 가지고 있다면 참조 값만 복사가 됨.
참조는 복사되지만 참조되는 객체가 복사되지 않음.

#### 깊은 복사 (Deep Copy)
깊은 복사는 전체 복사로, 얕은 복사와 달리 객체가 가진 모든 멤버(값과 참조 형식 모두)를 복사하는 것, 객체가 참조 타입의 멤버를 포함할 경우 참조 값의 복사가 아닌 참조된 객체 자체가 복사됨.
각자의 값을 참조하게 됨.

## :pencil2: Special Method, Magic Method aka dunder method
`__getitem()__`

### :pencil2: Command python
#### If python2 and python3 are both installed
- In Unix
  - Python2: `$ python`
  - Python3: `$ python3`
- In Windows (cmd)
  - Python2: `$ py -2`
  - Python3: `$ py -3`
#### If only one of python verison is installed
`$ python`

### :pencil2: `;`
multiple lines, but not pythonic

## :fire: Python 2.X versus Python 3.X
### 2to3
Coverting a Python 2 code to a Python 3 file.

### Unicode = str
Python 2에서는 unicode type이 있지만, Python 3에서는 str type에 포함된다.

### Parameter vs. Argument | [Blog (KR)](http://taewan.kim/tip/argument_parameter/)
Parameter(매개 변수)는 function 또는 method 정의에 사용되는 variable이고 Argument(전달 인자)는 function 또는 method를 call할 때 주는 실제 value이다. Parameter(매개 변수)는 function과 method의 입력 변수(variable) 이름이고, Argument(전달 인자/인자)는 function 또는 method의 입력 값(value)이다.

### Python `self` vs. C++ `this`
C++의 `this` 포인터는 Python의 self와 비슷한 개념이지만 포인터이기 때문에 객체 자기자신의 주소를 가리킨다는 차이점이 있다.

----------

## :books: PEP 0 -- Index of Python Enhancement Proposals (PEPs) | [Homepage](https://www.python.org/dev/peps/)
This PEP contains the index of all Python Enhancement Proposals, known as PEPs. PEP numbers are assigned by the PEP editors, and once assigned are never changed. The version control history of the PEP texts represent their historical record.

### PEP 8 -- Style Guide for Python Code | [Docs](https://www.python.org/dev/peps/pep-0008/)

### PEP 484 -- Type Hints | [Docs](https://www.python.org/dev/peps/pep-0484/)

----------

## typing - Support for type hints | [Docs](https://docs.python.org/3.7/library/typing.html)
New in version 3.5.

Source code: Lib/typing.py

The Python runtime does not enforce function and variable type annotations. They can be used by third party tools such as type checkers, IDEs, linters, etc.

This module supports type hints as specified by PEP 484 and PEP 526. The most fundamental support consists of the types `Any`, `Union`, `Tuple`, `Callable`, `TypeVar`, and `Generic`. For full specification please see PEP 484. For a simplified introduction to type hints see PEP 483.

The function below takes and returns a string and is annotated as follows:
```Python
def greeting(name: str) -> str:
  return 'Hello ' + name
```
In the function `greeting`, the argument `name` is expected to be of type `str` and the return type `str`. Subtypes are accepted as arguments.

## :bulb: Error
### UnicodeEncodeError: 'ascii' codec can't encode characters in position: ordinal not in range(128)
Python 2.x는 기본 인코딩이 ASCII이기 때문에 UNIX에서 encoding이 맞지 않아서 발생하는 에러이다. Python 3.x는 기본 인코딩으로 UTF-8을 사용하기 때문에 문제가 발생하지 않는다. 이를 Python 파일 내에서 기본 인코딩을 변경하는 방법을 통해 수정할 수 있다.
```Python
import sys
reload(sys)
sys.setdefaultencoding("UTF-8")
```

----------

## :books: Implementation | [Docs](https://docs.python.org/3.7/reference/introduction.html)

### :bulb: CPython
This is the original and most-maintained implementation of Python, wirtten in C. New language features generally appear here first.

### Jython | [Homepage](https://www.jython.org)
Python implemented in Java. This implementatin can be used as a scripting language for Java applications, or can be used to create applications using the Java class libraries. It is also often used to create tests for Java libraries. 

### Python for .NET (pythonnet) | [Homepage](https://pythonnet.github.io)
This implementation actually uses the CPython implementation, but is a managed .NET application and makes .NET libraries available. It was create by Brian Lloyd.

### IronPython | [Homepage](https://ironpython.net)
An alternate Python for .Net. Unlike Python.Net, this is a complete Python implementation that generates IL, and compiles Python code directly to .NET assemblies. It was created by Jim Hugunin, the original creator of Jython.

### :bulb: PyPy | [Homepage](https://www.pypy.org)
A fast, compliant alternative implementation of Python. On average, PyPy is 4.2 times faster than CPython.

"If you want your code to run faster, you should probably just use PyPy." -- Guido van Rossum (creator of Python).

An implementation of Python written completely in Python. It supports several advanced features not found in other implementations like stackless support and a Just in Time compiler. One of the goals of the project is to encourage experimentation with language itself by making it easier to modify the interpreter (since it is written in Python).

### RPython

## Information
```python
# Author      : Inyong Hwang (inyong1020@gmail.com).
# Date        : 2020-01-01-Mon.
# Description : None.
# State       : Done/Todo/Deprecated.
# Laptop  Environment : Python 3.6.8(Anaconda), PyCharm 2018.1(Professional Edition), Microsoft Windows 10.0.18362.720.
# Desktop Environment : Python 3.6.7(Anaconda custom), PyCharm 2018.3.2(Professional Edition), Microsoft Windows 10.0.18363.720.
# Input       : None.
# Output      : None.
# Reference   : None.
```

----------

## :books: Glossary | [Docs 3.7.10](https://docs.python.org/3.7/glossary.html)

### special method
A method that is called implicitly by Python to execute a certain operation on a type, such as addition. Such methods have names starting and ending with double underscores. Special methods are documented in Special method names.

### statement
A statement is part of a suite (a "block" of code). A statement is either an expression or one of several constructs with a keyword, such as if, while or for.

### text encoding
A codec which encodes Unicode strings to bytes.

### text file
A file object able to read and write str objects. Often, a text file actually accesses a byte-oriented datastream and handles the text encoding automatically. Examples of text files are files opened in text mode (`'r'` or `'w'`), sys.stdin, sys.stdout, and instance of io.StringIO.

See also binary file for a file object able to read and write bytes-like objects.

### triple-quoted string
A string which is bound by three instances of either a quotation mark (") or an apostrophe ('). While they don't provide any functionality not available with single-quoted strings, they are useful for a number of reasons. They allow you to include unescaped single and double quotes within a string and they can span multiple lines without the use of the continuation character, making them especially useful when writing docstrings.

### type
The type of a Python object determines what kind of object it is; every object has a type. An object's type is accessible as its __classes__ attribute or can be retrieved with `type(obj)`.

### type alias
A synonym for a type, created by assigning the type to an identifier.

Type aliases are useful for simplifying type hints. For example:
```Python
from typing import List, Tuple

def remove_gray_shades(colors: List[Tuple[int, int, int]]) -> List[Tuple[int, int, int]]:
  pass
```
could be made more readable like this:
```Python
from typing import List, Tuple

Color = Tuple[int, int, int]

def remove_gray_shades[colors: List[Color]] -> List[Color]:
  pass
```

### type hint
An annotation that specifies the expected type for a variable, a class attribute, or a function parameter or return value.

Type hints are optional and are not enforced by Python but they are useful to static type analysis tools, and aid IDEs with code completion and refactoring.

Type hints of global variables, class attributesm and functions, but not local variables, can be access using typing.get_type_hints().

See typing and PEP 484, which describe this functionality.

### Callback | [Wiki](https://en.wikipedia.org/wiki/Callback_(computer_programming))
A callback, also known as a "call after function", is any executable code that is passed as an arguemtn to other code; that other code is expected to call back (execute) the argument at a given time. This execution may be immediate as in a synchronous callback, or it might happen at a later point in time as in an asynchronous callback. Programming languages supports callbacks in different ways, often implementing them with subroutines, lambda expressions, blocks, or function pointers.

----------

#### Reference
- Python, https://www.python.org/, 2020-04-02-Thu.
- Python, Deep Copy, Shallow Copy, https://blueshw.github.io/2016/01/20/shallow-copy-deep-copy/, 2020-05-31-Sun.
- C++, Deep Copy, Shallow Copy, https://wonjayk.tistory.com/256, 2020-05-31-Sun.
- Numpy, https://numpy.org/, 2020-12-04-Fri.
- Pandas, https://pandas.pydata.org/, 2020-12-04-Fri.
- SciPy, https://www.scipy.org/, 2020-12-04-Fri.
- Scikit-learn, https://scikit-learn.org/, 2020-12-04-Fri.
- Matplotlib, https://matplotlib.org/ 2020-12-04-Fri.
- Argparse Blog KR, https://greeksharifa.github.io/references/2019/02/12/argparse-usage/, 2020-12-17-Thu.
- PIP, https://pypi.org/project/pip/, 2021-01-04-Mon.
- UnicodeEncodeError Handling Blog KR, https://www.snoopybox.co.kr/2059, 2021-01-04-Mon.
- Typeerror Handling Blog KR, https://m.blog.naver.com/P
tView.nhn?blogId=robot7887&logNo=221376966064&proxyReferer=https:%2F%2Fwww.google.com%2F, 2021-01-04-Mon.
- Python 3 Built-in Functions Book KR, https://wikidocs.net/32, 2021-01-26-Tue.
- Python 3 Built-in Functions KR, https://docs.python.org/ko/3/library/functions.html#built-in-functions, 2021-01-26-Tue.
- Python 3 Built-in Functions EN, https://docs.python.org/3/library/constants.html, 2021-01-26-Tue.
- Python 3 Built-in Constants KR, https://docs.python.org/ko/3/library/constants.html, 2021-01-26-Tue.
- Python 3 Built-in Constants EN, https://docs.python.org/3/library/constants.html, 2021-01-26-Tue.
- Python 3.7.9 Built-in Functions EN, https://docs.python.org/3.7/library/functions.html, 2021-01-26-Tue.
- Python 3.7.9 Built-in Constants EN, https://docs.python.org/3.7/library/constants.html, 2021-01-26-Tue.
- Python Screentshot Blog EN, https://datatofish.com/screenshot-python/, 2021-02-12-Fri.
- Python Debugging
- Python pytest, https://docs.pytest.org/en/stable/, 2021-02-15-Mon.
- Parameter vs. Argument Blog KR, http://taewan.kim/tip/argument_parameter/, 2021-02-23-Tue.
- Errors and Exceptions Python 3.7, https://docs.python.org/3.7/tutorial/errors.html, 2021-04-12-Mon.
- PyPy, https://www.pypy.org, 2021-05-02-Sun.
- Introduction, https://docs.python.org/3.7/reference/introduction.html, 2021-05-02-Sun.
- Jython, https://www.jython.org, 2021-05-02-Sun.
- Python.Net(pythonnet), https://pythonnet.github.io, 2021-05-02-Sun.
- IronPython, https://ironpython.net, 2021-05-02-Sun.
- typing, https://docs.python.org/3.7/library/typing.html, 2021-05-12-Wed.
- PEP 0, https://www.python.org/dev/peps/, 2021-05-12-Wed.
- PEP 8, https://www.python.org/dev/peps/pep-0008/, 2021-05-12-Wed.
- PEP 484, https://www.python.org/dev/peps/pep-0484/
- Callback Wiki, https://en.wikipedia.org/wiki/Callback_(computer_programming), 2021-06-01-Tue.
- Callback Blog KR, https://satisfactoryplace.tistory.com/18, 2021-06-01-Tue.
- Anaconda, https://www.anaconda.com/, 2021-06-09-Wed.
- Anaconda Document Individual Edition, https://docs.anaconda.com/anaconda/, 2021-06-09-Wed.
- PyCharm Python console Blog KR, https://www.martinii.fun/76, 2021-06-15-Tue.
