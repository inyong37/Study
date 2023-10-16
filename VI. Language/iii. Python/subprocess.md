# subprocess | [3.7.10](https://docs.python.org/3.7/library/subprocess.html) [3.8.17](https://docs.python.org/3.8/library/subprocess.html)

`This page has been moved from Python/readme.md`

The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. This module intends to replace several older modules and functions: `os.system` and `os.spawn*`.

:key: See also: PEP 324 - PEP proposing the subprocess module.

* `subprocess.PIPE`

Special value that can be used as the stdin, stdout or stderr argument to Popen and indicates that a pipe to the standard stream should be opened. Most useful with `Popen.communicate()`.

---

### Reference
- surprocess 3.7.10, https://docs.python.org/3.7/library/subprocess.html, 2021-03-28-Sun.
- subprocess 3.8.17, https://docs.python.org/3.8/library/subprocess.html, 2023-10-16-Mon.
- subprocess Blog KR, https://hbase.tistory.com/341, 2023-10-16-Mon.
