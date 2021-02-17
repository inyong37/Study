# Python | [Homepage](https://www.python.org/)
```
This page is from the "Language" page.
```
Python is a programming language that lets you work quickly and integrate systems more effectively.

- Tool: Anaconda (by Anaconda), PyCharm (by JetBrains), Jupyter Notebook (by Jupyter)

## :computer: PyCharm | [Homepage](https://www.jetbrains.com/pycharm/)
#### Keymap
- Setting for Key mapping: `Control` + `Alt` + `s`.
- Comment: `Control` + `/`.
- Run: `Control` + `Shift` + `F5`.
#### My keymap #1
- Run file in console: `Control` + `r`, `Shift` + `Control` + `Alt` + `F5`, 
- Rerun: `Control` + `Shift` + `r`
#### My keymap #2
- Setting: `Shift` + `Control` + `Alt` + `F4`
- Run file in console: `Shift` + `Control` + `Alt` + `F5`
- Python console: `Shift` + `Control` + `Alt` + `F6`
- Rerun: `Shift` + `Control` + `Alt` + `F7`

## :books: Built-in Function | [Documentation Python 3.7.9](https://docs.python.org/3.7/library/functions.html)
### **abs**(*x*)
Return the absolute value of a number. The argument may be an integer or a floating point number. If the arguemtn is a complex number, its magnitude is returned.

### **all**(*iterable*)
Return `True` if all elements of the *iterable* are true (or if the iterable is empty).

### **any**(*iterable*)
Return `True` if any element of the *iterable* is true. If the iterable is empty, return `False`.

### **ascii**(*object*)
As [repr()](), return a string containing a printable representation of an object, but escape the non-ASCII characters in the string returned by [repr()]() using `\x`, `\u` or `\U` escapes. This generates a string similar to that returned by [repr()]() in Python 2.

### **bin**(*x*)
Convert an integer number to a binary string prefixed with "0b". The result is a valid Python expression. If *x* is not a Python [int]() object, it has to define an [__index__()]() method that returns an integer.

### *class* **bool**([*x*])
Return a Boolean value, i.e. one of `True` or `False`. *x* is converted using the standard [truth testing procedure](). If *x* is false or omitted, this returns `False`; otherwise it returns `True`. The bool class is a subclass of [int]() (see [Numeric Types - int, float, complex]()). It cannot be subclassed futher. Its only instances are `Flase` and `True` (see [Boolean Values]().

### **breakpoint**(* *args* , ** *kws*)
This function drops you into the debugger at the call site. Specifically, it calls [sys.breakpointhook()](), passing `args` and `kws` straight through. By default, `sys.breakpointhook()` calls [pdb.set_trace()]() expecting no arguments. In this case, it is purely a convenience function so you don't have to explicitly import [pdb]() or type as much code to enter the debugger. However, [sys.breakpointhook()]() can be set to some other function and [breakpoint()]() will automatically call that, allowing you to drop into the debugger of choice.

### *class* **bytearray**([*source*[, *encoding*[, *errors*]]])
Return a new array of bytes. The [bytearray]() class is a mutable sequence of integers in the range `0 <= x < 256`. It has most of the usual methods of mutable sequences, described in [Mutable Sequence Types](), as well as most methods that the [bytes]() type has, see [Bytes and Bytearray Operations]().

### *class* **bytes**([*source*[, *encoding*[, *errors*]]])
Return a new "bytes" object, which is an immutable sequence of integers in the range `0 <= x < 256`. [bytes]() is an immutable version of [bytearray]() - it has the same non-mutating methods and the same indexing and slicing behavior.

### **callable**(*object*)
Return [True]() if the *object* argument appears callable, [False]() if not. If this returns `True`, it is still possible that a call fails, but if it is `False`, calling *object* will never succeed. Note that classes are callable (calling a class returns a new instance); instances are callable if their class has a [__call__()]() method.

### **chr**(*i*)

### **@classmethod**

### **compile**(*source, filename, mode, flags=0, dont_inherit=False, optimize=-1*)

### *class* **complex**([*real*[, *imag*]])

### **delattr**(*object*, *name*)

### *class* **dict**(***kwarg*)

### *class* **dict**(*mapping*, **kwarg)

### *class* **dict**(*iterable*, **kwarg)

### **dir**([*object*])

### **divmod**(*a*, *b*)
Take tow (non complex) numbers as arguments and return a pair of numbers consisting of their quotient and remainder when using integer division. With mixed oprand types, the rules for binary arithmetic operators apply. For integers, the result is the same as `( a // b, a % b)`. For floating point numbers the result is `(q, a % b)`, where *q* is usually `math.floor(a / b)` but may be 1 less than that. In any case `q * b + a % b` is very close to *a*, if `a % b` is non-zero it has the same sign as *b*, and `0 <= abs(a % b) < abs(b)`.

### **enumerate**(*iterable*, *start=0*)
Return as enumerate object. *iteralbe* must be a sequence, an [iterator], or some other object which supports iteration. The [__next__()]() method of the iterator returned by [enumerate()] returns a tuple containing a count (from *start* which defaults to 0) and the values obtained from iterating over *iterable*.

### **eval**(*expression*[, *globals*[, *locals*]])

### **exec**(*object*[, *globals*[, *locals*]])

### **filter**(*function*, *iterable*)

### *class* **float**([*x*])

### **format**(*value*[, *format_spec*])
Convert a *value* to a "formatted" representation, as controlled by *format_spec*. The interpretation ofr *format_spec* will depend on the type of the *value* argument, however there is a standard formatting syntax that is used by most built-in types: [Format Specification Mini-Language]().

### *class* **frozenset**([*iterable*])
Return a new [frozenset]() object, optionally with elements taken from *iterable*. `frozenset` is a built-in class.

### **getattr**(*object*, *name*[, *default*])
Return the value of the named attributed of *object*. *name* must be a string. If the string is the name of one of the object's attributes, the result is the value of that attribute. For example, `getattr(x, 'foobar')` is equivalent to `x.foobar`. If the named attributes does not exist, *default* is returned if provided, otherwise [AttributeError]() is raised.

### **globals**()
Return a dictionary representing the current global symbol table. This is always the dictionary of the current module (inside a function or method, this is the module where it is defined, not the module from which it is called).

### **hasattr**(*object*, *name*)
The arguments are an object and a string. The result is `True` if the string is the name of one of the object's attributes. `False` if not. (This is implemented by calling `getattr(object, name)` and seeing whether it raises an [AttributeError]() or not).

### **hash**(*object*)

### **help**([*object*])

### **hex**(*x*)

### **id**(*object*)

### **input**([*prompt*])

### *class* **int**([*x*])

### *class* **int**(*x*, *base=10*)

### **isinstance**(*object*, *classinfo*)
Return `True` if the object argument is an instance of the classinfo argument, or of a (direct, indirect or [virtual]()) subclass thereof. If *object* is not an object of the given type, the function always returns `False`. If *classinfo* is a tuple of type objects (or recursively, other such tuples), return `True` if *object* is an instance of any of the types. If *classinfo* is not a type or tuple of types and such tuples, a [TypeError]() exception is raised.

### **issubclass**(*class*, *classinfo*)

### **iter**(*object*[, *sentinel*])

### **len**(*s*)

### *class* **list**([*iterable*])

### **locals**()

### **map**(*funtion*, *iterable*, *...*)

### **max**(*iterable*, *[, *key*, *default*])

### **max**(*arg1*, *arg2*, * *args*[, *key*])

### **min**(*iterable*, *[, *key*, *default*])

### **min**(*arg1*, *arg2*, * *args*[, *key*])

### **next**(*iterator*[, *default*])

### *class* **object**

### **oct**(*x*)

### **open**(*file*, *mode='r'*, *buffering=-1*, *encoding=None*, *errors=None*, *newline=None*, *closefd=True*, *opener=None*)

### **ord**(*c*)

### **pow**(*x*, *y*[, *z*])

### **print**(* *objects*, *sep=''*, *end='\n'*, *file=sys.stdout*, *flush=False*)

### *class* **property**(*fget=None*, *fset=None*, *fdel=None*, *doc=None*)

### *class* **range**(*stop*)

### *class* **range**(*start*, *stop*[, *step*])

### **repr**(*object*)

### **reversed**(*seq*)

### **round**(*number*[, *ndigits*])

### *class* **set**([*iterable*])

### **setattr**(*object*, *name*, *value*)

### *class* **slice**(*stop*)

### *class* **slice**(*start*, *stop*[, *step*])

### **sorted**(*iterable*, *, *key=None*, *reverse=False*)

### **@staticmethod**
Transform a method into a static method.

### *class* **str**(*object=''*)

### *class* **str**(*object=b''*, *encoding='utf-8'*, *errors='strict'*)

### **sum**(*iterable*[, *start*])

### **super**(*type*[, *object-or-type*]])

### *class* **tuple**([iterable*])

### *class* **type**(*object*)

### *class* **type**(*name*, *bases*, *dict*)

### **vars**([*object*])

### **zip**(* *iterables*)

### **__import__**(*name*, *globals=None*, *locals=None*, *fromlist=()*, *level=0*)

## :books: Built-in Constant | [Documentation Python 3.7.9](https://docs.python.org/3.7/library/constants.html)

## :books: Library

### argparse | [Documentation Python 3.7.9](https://docs.python.org/3.7/howto/argparse.html)
```Python
import argparse

parser = argparse.ArgumentParser(description='Argument Parse')
parser.add_argument('--argument', '-a', type=str, help='an argument', dest='arg_1')
args = parser.parse_args()
```

### doctest | [Documentation Python 3.7.9](https://docs.python.org/3.7/library/doctest.html)
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

### fileinput | [Documentation Python 3.7.9](https://docs.python.org/3.7/library/fileinput.html)
This module implements a helper class and functions to quickly write a loop over standard input or a list of files. If you just want to read or write on file see [open()]()

### io | [Documentation Python 3.7.9](https://docs.python.org/3.7/library/io.html)
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

### os | [Documentation Python 3.7.9](https://docs.python.org/3.7/library/os.html)
This module provides a portable way of using operating system dependent functionality. If you just want to read or write a file see [open()](), if you want to manipulate paths, see the [os.path]() module, and if you want to read all the lines in all the files on the command line see the [fileinput]() module. For creating temporary files and directories see the [tempfile]() module, and for high-level file and directory handling see the [shutil]() module.

- os.**rename**(*src*, *dst*, *, *src_dir_fd=None*, *dst_dir_fd=None*)

Rename the file or directory *src* to *dst*. If *dst* exists, the operations will fail with an [OSError]() subclass in a number of cases: On Windows, if *dst* exosts a [FileExistsError]() is always raised. On Unix, if *src* is a file and *dst* is a directory or vice-versa, an [IsADirectoryError]() or a [NotADirectoryError]() will be raised respectively. If both are directories and *dst* is empty, *dst* will be silently replaced. If *dst* is a non-empty directory, an [OSError]() is raised. If both are files, *dst* it will be replaced silently if the user has permission. The operation may fail on some Unix flavors if *src* and *dst* are on different filesystems. If successful, the renaming will be an atomic operation (this is a POSIX requirement).

### Pandas | [Homepage](https://pandas.pydata.org/) | `import pandas as pd`
Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.

### platform | [Documentation Python 3.7.9](https://docs.python.org/3.7/library/platform.html)
Access to underlying platform's identifying data

- platform.**system**()

Returns the system/OS name, such as `Linux`, `Darwin`, `Java`, `Windows`. An empty string is returned if the value cannot be determined.

### Scikit-learn | [Homepage](https://scikit-learn.org/) | `import sklearn`
Scikit-learn is a simple and efficient tools for predictive data analysis. It is a accessible to everybody, and reusable in various contexts. It is built on Numpy, SciPy and Matplotlib. It is a open source, commercially usable - BSD license.

### SciPy | [Homepage](https://www.scipy.org/) | `import scipy`
The SciPy library is one of the core packages that make up the SciPy stack. It provides many user-friendly and efficient numberical routines, such as routines for numerical integration, interpolation, optimization, linear algebra, and statistics.

### shutil | [Documentation Python 3.7.9](https://docs.python.org/3.7/library/shutil.html)
The [shutil]() module offers a number of high-level operations on files and collections of files. In particular, functions are provided which support file copying and removal. For operations on individual files, see also the [os]() module.

### tempfile | [Documentation Python 3.7.9](https://docs.python.org/3.7/library/tempfile.html)

## :books: Built-in Exceptions | [Documentation Python 3.7.9](https://docs.python.org/3.7/library/exceptions.html)

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

## :bulb: Error
### UnicodeEncodeError: 'ascii' codec can't encode characters in position: ordinal not in range(128)
Python 2.x는 기본 인코딩이 ascii이라 Unix에서 인코딩이 안 맞아서 발생하는 에러이다. Python 3.x는 기본 "UTF-8"을 사용하기 때문에 문제가 발생하지 않는다. 이를 Python 파일 내에서 기본 인코딩을 변경하는 방법을 통해 수정할 수 있다.
```Python
import sys
reload(sys)
sys.setdefaultencoding("UTF-8")
```

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
