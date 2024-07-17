# Package

## [PyPI](https://pypi.org/)

The Python Package Index (PyPI) is a repository of software for the Python programming language. PyPI helps you find and install software developed and shared by the Python community.

## [pip](https://pypi.org/project/pip/) | [PEP 453](https://peps.python.org/pep-0453/) | [Tool recommendations](https://packaging.python.org/en/latest/guides/tool-recommendations/)

pip is the package installer for Python. You can use pip to install package from the Python Package Index and other indexes.

## [distutils](https://docs.python.org/3.10/library/distutils.html) | [PEP 229](https://peps.python.org/pep-0229/)

The distutils package provides support for building and installing additional modules into a Python installation. The new modules may be either 100%-pure Python, or may be extension modules written in C, or may be collections of Python packages which include modules coded in both Python and C.

:bulb: distutils is deprecated with removal planned for Python 3.12. 

## [Setuptools](https://setuptools.pypa.io/en/latest/index.html)

Setuptools is a fully-featured, actively-maintained, and stable library designed to facilitate packaging Python projects. It helps developers to easily share reusable code (in the form of a library) and programs (e.g., CLI/GUI tools implemented in Python), that can be installed with pip and uploaded to PyPI.

## Wheel | [PEP 427](https://peps.python.org/pep-0427/)

## pyproject.toml | [PEP 517](https://peps.python.org/pep-0427/) | [PEP 518](https://peps.python.org/pep-0518/)

## Python Project Structure

```Bash
/
/.gitignore
/README.md
/LICENSE
/setup.py
/requirements.txt
/{package_name}
/{package_name}/__init_.py
/{package_name}/{package_name}.py
/{package_name}/info.py
/{package_name}/{package_function}.py
/{package_name}/resources
/{package_name}/resources/__init__.py
/{package_name}/resources/config.yml
/tests
/tests/__init__.py
/tests/{test_case}.py
/tests/resources
/tests/resources/config.yml
```

---

### Reference
- pyproject Blog KR, https://www.bearpooh.com/221, 2024-07-16-Tue.
- Python Package Blog KR, https://ryanking13.github.io/2021/07/11/python-packaging.html, 2024-07-16-Tue.
- PEP 453 - Explicit bootstrapping of pip in Python installations, https://peps.python.org/pep-0453/, 2024-07-16-Tue.
- PEP 427 - The Wheel Binary Package Format 1.0, https://peps.python.org/pep-0427/, 2024-07-16-Tue.
- Why you shouldn't invoke setup.py directly Blog, https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html, 2024-07-16-Tue.
- Python Package Frontend Backend Blog KR, https://devocean.sk.com/blog/techBoardDetail.do?ID=164866, 2024-07-16-Tue.
- pyproject Blog KR, https://www.bearpooh.com/222, 2024-07-16-Tue.
- Python Project Blog KR, https://www.bearpooh.com/76, 2024-07-16-Tue.
- Structuring Your Project, https://docs.python-guide.org/writing/structure/, 2024-07-16-Tue.
- Dependencies Management in Setuptools, https://setuptools.pypa.io/en/latest/userguide/dependency_management.html, 2024-07-16-Tue.
- pyproject Blog KR, https://www.bearpooh.com/223, 2024-07-16-Tue.
- Setuptools, https://setuptools.pypa.io/en/latest/index.html, 2024-07-17-Wed.
- distutils Python 3.10, https://docs.python.org/3.10/library/distutils.html, 2024-07-17-Wed.
- PEP 229, https://peps.python.org/pep-0229/, 2024-07-17-Wed.
- PyPI, https://pypi.org/, 2024-07-17-Wed.
- pip, https://pypi.org/project/pip/, 2024-07-17-Wed.
- PEP 453, https://peps.python.org/pep-0453/, 2024-07-17-Wed.
- Tool recommendations, https://packaging.python.org/en/latest/guides/tool-recommendations/, 2024-07-17-Wed.
- Wheel PEP 427, https://peps.python.org/pep-0427/, 2024-07-17-Wed.
- PEP 517, https://peps.python.org/pep-0517/, 2024-07-17-Wed.
- PEP 518, https://peps.python.org/pep-0518/, 2024-07-17-Wed.
