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

## [pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/) | [PEP 517](https://peps.python.org/pep-0427/) | [PEP 518](https://peps.python.org/pep-0518/)

pyproject.toml is a configuration file used by pakcaging tools, as well as other tools such as linters, type checkers, etc. There are three possible TOML tables in this file.

* The `[build-system]` table is strongly recommended. It allows you to declare which build backend you use and which other dependencies are needed to build your project.
* The `[project]` table is the format that most build backends use to specify your project's basic metadata, such as the dependencies, your name, etc.
* The `[tool]` table has tool-specific subtables, e.g., `[tool.hatch]`, `[tool.black]`, `[tool.mypy]`. We only touch upon this table here because its contents are defined by each tool. Consult the particular tool's documentation to know what it can contain.

:bulb: There is a significant difference between the `[build-system]` and `[project]` tables. The former should always be present, regardless of which build backend you use (since it defines the tool you use). The latter is understood by most build backends, but some build backends use a different format.

:bulb: At the time of writing this (November 2023), Poetry is a notable build backend that does not use the `[project]` table (it uses the `[tool.poetry]` table instead).

:bulb: Also, the setupstools build backend supports both the `[project]` table, and the older format in `setup.cfg` or `setup.py`. For new projects, it is recommended to use the `[project]` table, and keep `setup.py` only if some programmatic configuration is needed (such as building C extensions), but the `setup.cfg` and `setup.py` formats are still valid.

## [Poetry](https://python-poetry.org/)

Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you. Poetry offers a lockfile to ensure repeatable installs, and can build your project for distribution.

## [Flit](https://flit.pypa.io/en/stable/)

Flit is a simple way to put Python packages and modules on PyPI. It tries to require less thought about packaging and help you avoid common mistakes.

Install: `python3 -m pip install flit`

Usage:
1. Make sure that module's docstring starts with a one-line summary of what the module is, and that it has a `__version__`.
2. Install flit if you don't already have it.
3. Run `flit init` in the directory containing the module to create a `pyproject.toml` file.
4. Run `flit publish` to upload your code to PyPI
5. Once your package is published, people can install it using pip just like any other package. In most cases, pip will download a 'wheel' package, a standard format it knows how to install. If you specifically ask pip to install an 'sdist' package, it will install and use Flit in a temporary environment.
6. To install a package locally for development, run `flit install [--symlink] [--python path/to/python]`
7. Flit packages a single importable module or package at a time, using the import name as the name on PyPI. All subpackages and data files within a package are included automatically.

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
- Poetry, https://python-poetry.org/, 2024-07-17-Wed.
- Flit, https://flit.pypa.io/en/stable/, 2024-07-17-Wed.
- Writing your pyproject.toml, https://packaging.python.org/en/latest/guides/writing-pyproject-toml/, 2024-07-17-Wed.
