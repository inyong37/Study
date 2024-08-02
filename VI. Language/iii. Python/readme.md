# *[Python](https://www.python.org/)* | [Document (3.7.10)](https://docs.python.org/3.7/)

```
This page is from the "Language" page.
```

:books: Built-in Function | [Document Python 3.7.9](https://docs.python.org/3.7/library/functions.html)

:books: Built-in Constant | [Document Python 3.7.9](https://docs.python.org/3.7/library/constants.html)

:books: Built-in Exceptions | [Document Python 3.7.9](https://docs.python.org/3.7/library/exceptions.html)

## :computer: *[Anaconda](https://www.anaconda.com/)* | [Document Individual Edition](https://docs.anaconda.com/anaconda/) | [Cheat Sheet](https://docs.anaconda.com/_downloads/9ee215ff15fde24bf01791d719084950/Anaconda-Starter-Guide.pdf) | [Archive](https://repo.anaconda.com/archive/) | [Uninstall](https://docs.anaconda.com/anaconda/install/uninstall/)

The Most Trusted Distribution for Data Science.

Anaconda is a package manager, an environment manager, a Python/R data science distribution, and a collection of over 7,500+ open-source packages. Anaconda is free and easy to install, and it offers free community support.

### Environement

Making requirements.txt:

```Bash
conda list > requirements.txt
pip freeze > requirements.txt
pip list --format=freeze > requirements.txt
```

Making tree of requirements.txt:

* requirements.txt:
```txt
-r requirements/tensorflow.txt
-r requirements/pytorch.txt
```

* requirements/tensorflow.txt:
```txt
tensorflor==1.0.0
```

* requirements/pytorch.txt:
```txt
torch==1.0.0
```

## :computer: *[PyCharm](https://www.jetbrains.com/pycharm/)* | [Other Versions](https://www.jetbrains.com/pycharm/download/other.html) | [Share Setting (Professional Version)](https://www.jetbrains.com/help/pycharm/sharing-your-ide-settings.html) | [Learn](https://www.jetbrains.com/pycharm/learn/)

The Python IDE for Professional Developers.

### non-project file issue | [Solution](https://intellij-support.jetbrains.com/hc/en-us/community/posts/360010640479-all-files-in-my-project-became-non-project)

Edit `.idea/modules.xml` to contain its iml file such as below.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="ProjectModuleManager">
    <modules>
      <module fileurl="file://$PROJECT_DIR$/.idea/Project.iml" filepath="$PROJECT_DIR$/.idea/Project.iml" />
    </modules>
  </component>
</project>
```

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

---

## :books: The Python Standard Libraries

### __future__ - Future statement definitions | [Docs](https://docs.python.org/3.7/library/__future__.html#module-__future__)
__future__ is a real module, and serves three purpose:
- To avoid confusing existing tools that analyze import statements and expect to find the modules they're importing.
- To ensure that future statements run under relases prior to 2.1 at least yield runtime exceptions (the import of __future__ will fail, because there was no module of that name prior to 2.1).
- To document when incompatible changes were introduced, and when they will be - or were - made mandatory. This is a form of executable documentation, and can be inspected programmatically via importing __future__ and examping its contents.

### __main__ - Top-level script environment | [Docs](https://docs.python.org/3.7/library/__main__.html#module-__main__)

### argparse | [Document Python 3.7.9](https://docs.python.org/3.7/howto/argparse.html)
```Python
import argparse

parser = argparse.ArgumentParser(description='Argument Parse')
parser.add_argument('--argument', '-a', type=str, help='an argument', dest='arg_1')
args = parser.parse_args()
```

### asyncio - Asynchronous I/O | [Docs 3.10.6](https://docs.python.org/3/library/asyncio.html)

asyncio is a library to write concurrent code using the async/await syntax.

asyncio is used as a foundation for multiple Python asynchronous frameworks that provide high-performance network and web-servers, database connection libraries, distributed task queues, etc.

asyncio is often a perfect fit for IO-bound and high-level structured network code.

asyncio provides a set of high-level APIs to: run Python corountines concurrently and have full control over their execution; perform network IO and IPC; control subprocesses; distribute tasks via queues; synchronize concurrent code;

Additionally, there are low-level APIs for library and framework developers to: create and manage event loops, which provide asynchronous APIs for networking, running subprocesses, handling OS signals, etc; implement efficient protocols using transports; bridge callback-based libraries and code with async/await syntax.

### asyncio - Asynchronous I/O >> Event Loop | [Docs 3.10.6](https://docs.python.org/3/library/asyncio-eventloop.html)

The event loop is the core of every asyncio application. Event loops run asynchronous tasks and callbacks, perform network IO operations, and run subprocesses.

- Obtaining the Event Loop: the following low-level functions can be used to get, set, or create an event loop:
  - `asyncio.get_running_loop()`: Return the running event loop in the current OS thread. If there is no running event loop a RuntimeError is raised. This function can only be called from a coroutine or a callback.
  - `asyncio.get_event_loop()`: Get the current event loop. If there is no current event loop set in the current OS thread, the OS thread is main, and `set_event_loop()` has not yet been called, asyncio will create a new event loop and set it as the current one. Because this function has rather complex behavior (especially when custom event loop policies are in use), using the `get_running_loop()` function is preferred to `get_event_loop()` in corountines and callbacks. Consider also using the `asyncio.rin()` function instead of using lower level functions to manually create and close an event loop. Deprecated since version 3.10: Deprecation warning is emitted if there is no running event loop. In future Python releases, this function will be an alias of `get_running_loop()`.
  - `asyncio.set_event_loop(loop)`: Set loop as a current event loop for the current OS thread.
  - `asyncio.new_event_loop()`: Create and return a new event loop object.

- `class asyncio.AbstractEventLoop`: Abstract base class for asyncio-compliant event loops. The Event Loop Methods section lists all methods that an alternative implementation of AbstractEventLoop should have defined.

### asyncio - Event Loop Implementation | [Docs 3 (KR)](https://docs.python.org/ko/3/library/asyncio-eventloop.html#event-loop-implementations)

asyncio에는 두 가지 이벤트 루프 구현이 함께 제공됩니다: SelectorEventLoop 및 ProactorEventLoop.

기본적으로 asyncio는 유닉스에서 SelectorEventLoop를, 윈도우에서 ProactorEventLoop를 사용하도록 구성됩니다.

### asyncio - SelectorEventLoop

selectors 모듈을 기반으로 하는 이벤트 루프.

주어진 플랫폼에서 사용할 수 있는 가장 효율적인 selector를 사용합니다. 정확한 셀렉터 구현을 수동으로 구성하여 사용할 수도 있습니다:

```Python
import asyncio
import selectors

selector = selectors.SelectSelectors()
loop = asyncio.SelectorEventLoop(selector)
asyncio.set_event_loop(loop)
```

가용성: 유닉스, 윈도우.

### asyncio - ProactorEventLoop

"I/O 완료 포트"(IOCP)를 사용하는 윈도우용 이벤트 루프.

가용성: 윈도우.

### asyncio - AbstractEventLoop

asyncio 호환 이벤트 루프의 추상 베이스 클래스.

이벤트 루프 메서드 절은 AbstractEventLoop의 다른 구현이 정의해야 하는 모든 메서드를 나열합니다.

### [Bunch](https://github.com/dsc/bunch)

A Bunch is a Python dictionary that provides attribute-style access (a la JavaScript objects).

### [configparser](https://docs.python.org/3/library/configparser.html)

This module provides the ConfigParser class which implements a basic configuration language which provides a structure similar to what's found in Microsoft Windows INI files. You can use this to write Python programs which can be customized by end users easily.

### dataclasses - Data Classes | [Docs 3.7.10](https://docs.python.org/3.7/library/dataclasses.html) | [PEP 557](https://www.python.org/dev/peps/pep-0557/)

```Python
from dataclasses import dataclass

@dataclass
class SampleDataClass:
  item: str
  def PrintItem(self) -> None:
    print(self.item)
```

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

### [json](https://docs.python.org/3/library/json.html) | [3.7.2](https://docs.python.org/3.7/library/json.html)
`from json import dump, dumps, load, loads`

### [Matplotlib](https://matplotlib.org/) | `from matplotlib import pyplot as plt`
Matplotlib is a comprehensive library for creating static, animated, and interactive visuallizations in Python.

### [Munch](https://github.com/Infinidat/munch)

A Munch is a Python dictionary that provides attribute-style access (a la JavaScript objects). Munch is a fork of Bunch package.

### [Numpy](https://numpy.org/) | `import numpy as np`
The fundamental package for scientific computing with Python.

### os

`This content has been moved to the` [os](os.md) `page`.

### [Pandas](https://pandas.pydata.org/) | `import pandas as pd`
Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.

### platform | [Document Python 3.7.9](https://docs.python.org/3.7/library/platform.html)
Access to underlying platform's identifying data

- platform.**system**()
Returns the system/OS name, such as `Linux`, `Darwin`, `Java`, `Windows`. An empty string is returned if the value cannot be determined.

### [Prodict](https://github.com/ramazanpolat/prodict)

Prodict, what Python dict meant to be. Prodict si Dictionary with IDE friendly(auto code completion) and dot-accessible attributes and more.

### pywin32

### PyYAML | [Docs](https://pyyaml.org/wiki/PyYAMLDocumentation) | [YAML](https://wiki.python.org/moin/YAML)

YAML is a human-friendly format for structured data, that is both easy to write for humans and still parsable by computers.

PyYAML is the most-used and go-to YAML package, which tries to be as compliant as possible with the YAML specs. It is, at its core, C-based. It can both read and write YAML.

Installtion: `pip install pyyaml`

Use: `load, load_all, safe_load, safe_load_all, dump, dump_all, safe_dump, safe_dump_all`
```Python
import yaml
data = yaml.load(stream, Loader=yaml.Loader) # or yaml.CLoader
output = yaml.dump(data, Dumper=yaml.Dumper) # or yaml.CDumper
```

### [Scikit-learn](https://scikit-learn.org/) | `import sklearn`

Scikit-learn is a simple and efficient tools for predictive data analysis. It is a accessible to everybody, and reusable in various contexts. It is built on Numpy, SciPy and Matplotlib. It is a open source, commercially usable - BSD license.

### [SciPy](https://www.scipy.org/) | `import scipy`

The SciPy library is one of the core packages that make up the SciPy stack. It provides many user-friendly and efficient numberical routines, such as routines for numerical integration, interpolation, optimization, linear algebra, and statistics.

### select - Waiting for I/O completion | [Docs 3](https://docs.python.org/3/library/select.html#module-select)

This module provides access to the `select()` and `poll()` functions available in most operating systems, `devpoll()` available on Solaris and derivates, `epoll()` available on Linux 2.5+ and `kqueue()` available on most BSD. Note that on Windows, it only works for sockets; on other operating systems, it also works for other file types (in particular, on Unix, it works on pipes). It cannot be used on regular files to determine whether a file has grown since it was last read.

Note: The `selectors` module allows high-level and efficient I/O multiplexing, built upon the `select` module primitives. Users are encouraged to use the `selectors` module instead, unless they want precise control over the OS-level primitives used.

### selectors - High-level I/O multiplexing | [Docs 3](https://docs.python.org/3/library/selectors.html#module-selectors)

This module allows high-level and efficient I/O multiplexing, built upon the select module primitives. Users are encouraged to use this module instead, unless they want precise control over the OS-level primitives used.

It defines a `BaseSelector` abstarct base class, along with several concrete implementations (`KqueueSelector`, `EpollSelector`...), that can be used to wait for I/O readiness notification on multiple file objects. In the following, "file object" refers to any object with a fileno() method, or a raw file descriptor. See file object.

`DefaultSelector` is an alias to the most efficient implementation available on the current platform: this should be the default choice for most users.

Note: The type of file objects supported depends on the platform: on Windows, sockets are supported, but not pipes, whereas on Unix, both are supported (some other types may be supported as well, such as fifos or special file devices).

See also: select - Low-level I/O multiplexing module.

### selector - Classes

Class hierarchy:

```
BaseSelector
+-- SelectSelector
+-- PollSelector
+-- EpollSelector
+-- DevpollSelector
+-- KqueueSelector
```
In the following, events is a bitwise mask indicating which I/O events should be waited for on a given file object. It can be a combination of the modules constants below:

|Constant|Meaning|
|:-|:-|
|`EVENT_READ`|Available for read|
|`EVENT_WRITE`|Available for write|

### selenium

### shutil | [Document Python 3.7.9](https://docs.python.org/3.7/library/shutil.html)

The [shutil]() module offers a number of high-level operations on files and collections of files. In particular, functions are provided which support file copying and removal. For operations on individual files, see also the [os]() module.

### subprocess

`This content has been moved to the` [subprocess](subprocess.md) `page.`

### tempfile | [Document Python 3.7.9](https://docs.python.org/3.7/library/tempfile.html)

### [paho](https://www.eclipse.org/paho/)

The Eclipse Paho MQTT Python client library. This code provides a client class which enable applications to connect to an MQTT broker to publish messages, and to subscribe to topcis and receive published messages. It also provides some helper functions to make publishing one off messages to an MQTT server very straightforward.

The MQTT protocol is a machine-to-machine (M2M)/Internet of Things connectivity protocol. Designed as an extremely lightweight publish/subscribe messaging transport, it is useful for connections with remote locations where a small code footprint is required and/or network bandwidth is at a premium.

Paho is an Eclipse Foundation project.

### PyQt
There is an installation error with PyQt5 on macOS. The latest version is 5.15.7 in Jul. 2022. The solution is PyQt5 needs XCode to install and run PyQt5 on macOS.

---

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

---

## :pencil2: Special Method, Magic Method aka dunder method

`__getitem()__`

---

### :pencil2: Command

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

---

## :fire: Python 2.X versus Python 3.X

### 2to3
Coverting a Python 2 code to a Python 3 file.

### Unicode = str
Python 2에서는 unicode type이 있지만, Python 3에서는 str type에 포함된다.

### Parameter vs. Argument | [Blog (KR)](http://taewan.kim/tip/argument_parameter/)
Parameter(매개 변수)는 function 또는 method 정의에 사용되는 variable이고 Argument(전달 인자)는 function 또는 method를 call할 때 주는 실제 value이다. Parameter(매개 변수)는 function과 method의 입력 변수(variable) 이름이고, Argument(전달 인자/인자)는 function 또는 method의 입력 값(value)이다.

### Python `self` vs. C++ `this`
C++의 `this` 포인터는 Python의 self와 비슷한 개념이지만 포인터이기 때문에 객체 자기자신의 주소를 가리킨다는 차이점이 있다.

---

## :books: PEP 0 -- Index of Python Enhancement Proposals (PEPs) | [Homepage](https://www.python.org/dev/peps/)

This PEP contains the index of all Python Enhancement Proposals, known as PEPs. PEP numbers are assigned by the PEP editors, and once assigned are never changed. The version control history of the PEP texts represent their historical record.

### PEP 8 -- Style Guide for Python Code | [Docs](https://www.python.org/dev/peps/pep-0008/)

### PEP 484 -- Type Hints | [Docs](https://www.python.org/dev/peps/pep-0484/)

---

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

---

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

---

## :books: Glossary | [Docs 3.7.10](https://docs.python.org/3.7/glossary.html)

### `>>>`
The default Python prompt of the interactive shell. Often seen for code examples which can be executed interactively in the interpreter.

### `...`
The default Python prompt of the interactive shell when entering the code for an indented code block, when within a pair of matching left and right delimiters (parentheses, square brackets, curly braces or triple quotes), or after specifying a decorator.

### 2to3
A tool that tries to convert Python 2.x code to Python 3.x code by handling most of the incompatibilites which can be detected by parsing the source and traversing the parse tree.

### class
A template for creating user-defined objects. Class definition normally contain method definitions which operate on instances of the class.

### class variable
A variable defined in a class and intended to be modified only at class level (i.e., not in an instance of the class).

### coercion
The implicit conversion of an instance of one type to another during an operation which involves two arguments of the same type. For example, `int(3.15)` converts the floating point number to the integer `3`, but in `3+4.5`, each argument is of a different type (one int, one float), and both mush be converted to the same type before they can be added or it will raise a TypeError. Without coercion, all arguments of even compatible types would have to be normalized to the same value by the programmer, e.g., `float(3)+4.5` rather than just `3+4.5`.

### decorator
A function returning another function, usually applied as a function transformation using the `@wrapper` syntax. Common examples for decorators are `classmethod()` and `staticmethod()`.

The decorator syntax is merely syntactic sugar, the following two function definitions are semantically equivalent:
```Python
def f(..):
  ...
f = staticmethod(f)
@staticmethod
def f(...):
  ...
```
The same concept exists for classes, but is less commonly used there.

### descriptor
Any ob

### garbage collection
The process of freeing memory when it is not used anymore. Python performs garbage collection via reference counting and a cyclic garbage collector that is able to detect and break refernece cycles. The garbage collector can be controlled uising the `gc` module.

### generator
A function which returns a generator iterator. It looks like a normal function except that is contains `yield` expressions for producing a series of values usable in a for-loop or that can be retrieved one at a time with the `next()` function.

### generator iterator
An object created by a generator function.

Each `yield` temporarily suspends processing, remembering the location execution state (including local variables and pending try-statements). When the generator iterator resumes, it picks up where it left off (in contrast to functions which start fresh on every invocation).

### generator expression
An expression that returns an iterator. It looks like a normal expression followed by a `for` clause defining a loop variable, range, and an optional `if` clause. The combined expression generates values for an enclosing function:
```bash
>>> sum(i*i for i in range(10)) # sum of suqares 0, 1, 4, ... 81
285
```

### generic function
A function composed of multiple functions implementing the same operation for different types. Which implementation should be used during a call is determined by the dispatch algorithm.

### GIL
see global interpreter lock.

### global interpreter lock
The mechanism used by the CPython interpreter to assure that only one thread executes Python bytecode at a time. This simplifies the CPython implementation by making the object model (including critical built-in types such as `dict`) implicitly safe against concurrent access. Locking the entire interpreter makes it easier for the interpreter to be multi-threaded, at the expense of much of the parallelism afforded by multi-processor machines.

However, some extension modules, either standard or third-party, are desinged so as to release the GIL when doing computationally-intensive tasks such as compression or hasing. Also, the GIL is alwasy released when doing I/O.

Past efforts to create a "free-threaded" interpreter (one which locks shared data at a much finer granularity) have not been successful because performance suffered in the common single-processor case. It is believed that overcoming this performance issue would make the implementation much more complicated and therefore costlier to maintain.

### IDLE
An Integrated Development Environment for Python. IDLE is a basic editor and interpreter environment which ships with the standard distribution of Python.

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

### Closure | [Blog (KR)](https://shoark7.github.io/programming/python/closure-in-python)

Function Nesting, First Class Object (can be Parameter/Argument, Return, Assign/Mutable), and refernce nonlocal (Global-scope and Outer-scope = not Inner-scope/namespace) variable.

### Unpacking Operator * | [Blog](https://towardsdatascience.com/unpacking-operators-in-python-306ae44cd480)

```Python
l = [1, 2, 3, 4]
print(l) # [1, 2, 3, 4]
print(*l) # 1 2 3 4
```

```Python
first, *middle, last = 'ma' # first = 'm', middle = [], last = 'a'
```

### three dots | [Stackoverflow]

---

## *Web Framework*

### *aiohttp* | [AIOHTTP Docs](https://docs.aiohttp.org/en/stable/)

Asynchronous HTTP Client/Server for asyncio and Python.

- Supports both Client and HTTP Server.
- Supports both Server WebSockets and Client WebSockets out-of-the-box without the Callback Hell.
- Web-server has Middlewares, Signals and plugable routing.

### *Flask* | [Flask Docs 2.2.x](https://flask.palletsprojects.com/en/2.2.x/)

### *[Django](https://www.djangoproject.com/)*

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It's free and open source.

---

### Reference
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
- Parameter vs. Argument Blog KR, http://taewan.kim/tip/argument_parameter/, 2021-02-23-Tue.
- os 3.7.9, https://docs.python.org/3.7/library/os.html, 2021-03-19-Fri.
- surprocess 3.7.10, https://docs.python.org/3.7/library/subprocess.html, 2021-03-28-Sun.
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
- __future__, https://docs.python.org/3.7/library/__future__.html#module-__future__, 2021-06-24-Thu.
- __main__, https://docs.python.org/3.7/library/__main__.html#module-__main__, 2021-06-24-Thu.
- Closure Blog KR, https://shoark7.github.io/programming/python/closure-in-python, 2022-01-07-Fri.
- Unpacking Operator * Blog, https://towardsdatascience.com/unpacking-operators-in-python-306ae44cd480, 2022-01-07-Fri.
- Three Dots Stackoverflow, https://stackoverflow.com/questions/42190783/what-does-three-dots-in-python-mean-when-indexing-what-looks-like-a-number, 2022-01-18-Tue.
- Install PyQt5 with pip, https://pypi.org/project/PyQt5/, 2022-07-12-Tue.
- PyQt5 Tutorial KR, https://wikidocs.net/21849, 2022-07-12-Tue.
- macOS Solution for installing PyQt5, https://www.clien.net/service/board/cm_app/17041820, 2022-07-12-Tue.
- asyncio, https://docs.python.org/3/library/asyncio.html, 2022-08-25-Thu.
- Global Interpreter Lock Blog KR, https://dgkim5360.tistory.com/entry/understanding-the-global-interpreter-lock-of-cpython, 2022-08-26-Fri.
- asyncio Blog KR, https://brownbears.tistory.com/540, 2022-08-26-Fri.
- asyncio Event Loop Coroutine Blog KR, https://tech.buzzvil.com/blog/asyncio-no-1-coroutine-and-eventloop/, 2022-08-26-Fri.
- paho Eclipse, https://www.eclipse.org/paho/, 2022-08-30-Tue.
- asyncio event loop, https://docs.python.org/3/library/asyncio-eventloop.html, 2022-08-30-Tue.
- asyncio Event Loop Implementations KR, https://docs.python.org/ko/3/library/asyncio-eventloop.html#event-loop-implementations, 2022-09-01-Thu.
- selectors, https://docs.python.org/3/library/selectors.html#module-selectors, 2022-09-01-Thu.
- select, https://docs.python.org/3/library/select.html#module-select, 2022-09-01-Thu.
- AIOHTTP, https://docs.aiohttp.org/en/stable/, 2022-09-10-Sat.
- Flask, https://flask.palletsprojects.com/en/2.2.x/, 2022-09-10-Sat.
- Django, https://www.djangoproject.com/, 2022-09-10-Sat.
- Socket Blog KR, https://webnautes.tistory.com/1381, 2022-09-21-Wed.
- FastAPI ASGI Blog KR, https://breezymind.com/start-asgi-framework/, 2022-09-21-Wed.
- Learn PyCharm, https://www.jetbrains.com/pycharm/learn/, 2022-10-18-Tue.
- PyCharm non-project file, https://intellij-support.jetbrains.com/hc/en-us/community/posts/360010640479-all-files-in-my-project-became-non-project, 2022-11-01-Tue.
- Linux Python Daemon KR, https://github.com/HatsuneMiku3939/python3-daemon, 2023-10-10-Tue.
- Executable File (ELF), Binary, Program KR, https://codingdojang.com/scode/272, 2023-10-10-Tue.
- PyYAML Documentation, https://pyyaml.org/wiki/PyYAMLDocumentation, 2024-04-12-Fri.
- YAML, https://wiki.python.org/moin/YAML, 2024-04-12-Fri.
- Munch, https://github.com/Infinidat/munch, 2024-04-16-Tue.
- Bunch, https://github.com/dsc/bunch, 2024-04-18-Thu.
- Prodict, https://github.com/ramazanpolat/prodict, 2024-04-18-Thu.
- args kwargs Blog KR, https://brunch.co.kr/@princox/180, 2024-04-18-Thu.
- configparser, https://docs.python.org/3/library/configparser.html, 2024-04-22-Mon.
- Reflection Blog KR, https://jins-sw.tistory.com/28, 2024-05-03-Fri.
- Partial Blog KR, https://hamait.tistory.com/823, 2024-05-03-Fri.
- Partial Blog KR, https://jost-do-it.tistory.com/entry/Python-functools%EC%9D%98-partial-%ED%95%A8%EC%88%98-%EC%95%8C%EC%95%84%EB%B3%B4%EA%B8%B0#google_vignette, 2024-05-03-Fri.
- Abstract Wikidocs KR, https://wikidocs.net/16075, 2024-05-03-Fri.
- Wrapper Decorator Wikidocs KR, https://wikidocs.net/84429, 2024-05-03-Fri.
- Metaprogramming Wiki, https://en.wikipedia.org/wiki/Metaprogramming, 2024-05-03-Fri.
- `__init__.py` Stackoverflow, https://stackoverflow.com/questions/448271/what-is-init-py-for, 2024-06-28-Fri.
- `pyproject.toml`, https://packaging.python.org/en/latest/guides/writing-pyproject-toml/, 2024-06-29-Sat.
- getattr Blog KR, https://blog.naver.com/PostView.naver?blogId=siniphia&logNo=221796316521, 2024-07-12-Fri.
- functools.partial KR, https://wikidocs.net/109304, 2024-07-12-Fri.
- Google Python Style Guide, https://google.github.io/styleguide/pyguide.html, 2024-08-02-Fri.
