# Python to Execuatable File

## Date

2023-10-16-Monday.

## Environment

* macOS 13.4.1

## I. [PyInstaller](https://pyinstaller.org/en/stable/) on Windows, MacOS X, and Linux

PyInstaller bundles a Python application and all its dependencies into a single package. The user can run the packaged app without installing a Python interpreter or any modules. PyInstaller supports Python 3.8 and newer, and correctly bundles many major Python packages such as numy, matplotlib, PyQt, wxPython, and others.

PyInstaller is tested against Windows, MacOS X, and Linux. However, it is not a cross-compiler; to make a Window app you run PyInstaller on Windows, and to make a Linux app you run it on Linux, etc. x PyInstaller has been used successfully with AIX, Solaris, FreeBSD and OpenBSD but testing against them is not part of its continous integration tests, and the development team offers no guarantee (all code for these platforms comes from external contributions) that PyInstaller will work on these platforms or that they will continue to be supported.

### I.i. Install PyInstaller on Your Environment

`pip install pyinstaller`

and then, move to the workspace.

### I.ii.A. Make an Executable File with Libraries

`pyinstaller {source_code}.py`

### I.ii.B. Make an Execuatble File with Libraries, but without Console Window: `-w` or `--windowed`

`pyinstaller {source_code}.py -w` or `pyinstaller {source_code}.py --windowed`

### I.ii.C. Make an Executable File without Libraries: `-F` or `onefile`

`pyinstaller {source_code}.py -F` or `pyinstaller {source_code.py -onefile`

### I.iii. Verify :tada:

The executable file would be located in "dist" folder.

Execute the "{source_code}.exe".

## II. [py2exe](https://www.py2exe.org/) on Windows

py2exe is a Python Distutils extension which converts Python scripts into executable Windows programs, able to run without requiring a Python installation.

## III. [py2app](https://py2app.readthedocs.io/en/latest/) on macOS

py2app is a Python setuptools command which will allow you to make standalone application bundles and plugins from Python scripts. py2app is similar in purpose and design to py2exe for Windows.

:bulb: py2app must be run on macOS and cannot be used to cross build macOS applications on Windows or Linux.

---

### Reference
- PyInstaller KR, https://wikidocs.net/21952, 2023-10-16-Mon.
- PyInstaller, https://pyinstaller.org/en/stable/, 2023-10-16-Mon.
- py2exe and py2app Blog KR, https://spoqa.github.io/2013/05/21/py2exe-and-py2app.html, 2023-10-16-Mon.
- py2exe, https://www.py2exe.org/, 2023-10-16-Mon.
- py2app, https://py2app.readthedocs.io/en/latest/, 2023-10-16-Mon.
