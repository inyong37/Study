# Package

## [Setuptools](https://setuptools.pypa.io/en/latest/index.html)

Setuptools is a fully-featured, actively-maintained, and stable library designed to facilitate packaging Python projects. It helps developers to easily share reusable code (in the form of a library) and programs (e.g., CLI/GUI tools implemented in Python), that can be installed with pip and uploaded to PyPI.

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
