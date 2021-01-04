# Python | [Homepage](https://www.python.org/)
```
This page is from the "Language" page.
```
Python is a programming language that lets you work quickly and integrate systems more effectively.

- Tool: Anaconda (by Anaconda), PyCharm (by JetBrains), Jupyter Notebook (by Jupyter)

## PyCharm | [Homepage](https://www.jetbrains.com/pycharm/)
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

### pip
pip is the package installer for Python.
- Installation: `pip install pip`
- Usage: `pip install/uninstall package_name [options]`

### Copy
기존 객체와 같은 값을 가진 새로운 객체를 만든다는 것임, 객체들은 멤버를 가지고 있고 그 멤버들은 값일 수도 있고 참조 형식일 수도 있음, 이 객체들이 가진 값 형식과 참조 형식의 복제 방식에 따라 얕은 복사와 깊은 복사의 개념이 나뉨.

#### 단순 객체 복사
동일한 객체를 참고하기 때문에 한 곳에서 값을 변경하면 같이 값이 변경된다.

#### 얕은 복사 (Shallow Copy)
얕은 복사는 객체가 가진 멤버들의 값을 새로운 객체로 복사하는데 만약 객체가 참조 타입의 멤버를 가지고 있다면 참조 값만 복사가 됨.
참조는 복사되지만 참조되는 객체가 복사되지 않음.

#### 깊은 복사 (Deep Copy)
깊은 복사는 전체 복사로, 얕은 복사와 달리 객체가 가진 모든 멤버(값과 참조 형식 모두)를 복사하는 것, 객체가 참조 타입의 멤버를 포함할 경우 참조 값의 복사가 아닌 참조된 객체 자체가 복사됨.
각자의 값을 참조하게 됨.

### Special Method, Magic Method aka dunder method
`__getitem()__`

### doctest
test in classes or functions in documentation field
```
import doctest

def bar():
  >>> bar()
  foo
  return foo
```
`python test.py -v`

## Numpy | [Homepage](https://numpy.org/) | `import numpy as np`
The fundamental package for scientific computing with Python.

## SciPy | [Homepage](https://www.scipy.org/) | `import scipy`
The SciPy library is one of the core packages that make up the SciPy stack. It provides many user-friendly and efficient numberical routines, such as routines for numerical integration, interpolation, optimization, linear algebra, and statistics.

## Matplotlib | [Homepage](https://matplotlib.org/) | `from matplotlib import pyplot as plt`
Matplotlib is a comprehensive library for creating static, animated, and interactive visuallizations in Python.

## Scikit-learn | [Homepage](https://scikit-learn.org/) | `import sklearn`
Scikit-learn is a simple and efficient tools for predictive data analysis. It is a accessible to everybody, and reusable in various contexts. It is built on Numpy, SciPy and Matplotlib. It is a open source, commercially usable - BSD license.

## Pandas | [Homepage](https://pandas.pydata.org/) | `import pandas as pd`
Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.

## Argparse
```
import argparse

parser = argparse.ArgumentParser(description='Argument Parse')
parser.add_argument('--argument', '-a', type=str, help='an argument', dest='arg_1')
args = parser.parse_args()
```

### 2to3

### isInstance

### Unicode = str

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
