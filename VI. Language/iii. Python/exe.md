# Python to Execuatable File of Windows

## Date

2023-10-16-Monday.

## Environment

* macOS 13.4.1

## PyInstaller

### Install PyInstaller

`pip3 install pyinstaller`

### A. Make an Executable File with Libraries

Move to the workspace

`pyinstaller {source_code}.py`

### B. Make an Execuatble File with Libraries, but without Console Window: `-w` or `--windowed`

`pyinstaller {source_code}.py -w` or `pyinstaller {source_code}.py --windowed`

### C. Make an Executable File without Libraries: `-F` or `onefile`

`pyinstaller {source_code}.py -F` or `pyinstaller {source_code.py -onefile`

### :tada: Verify

The executable file would be located in "dist" folder.

Execute the "{source_code}.exe".

---

### Reference
- PyInstaller KR, https://wikidocs.net/21952, 2023-10-16-Mon.
