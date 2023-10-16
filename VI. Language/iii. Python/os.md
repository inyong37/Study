# os | [3.7.9](https://docs.python.org/3.7/library/os.html) | [3.8.17](https://docs.python.org/3.8/library/os.html)

'This page has been moved from Python/readme.md`

This module provides a portable way of using operating system dependent functionality. If you just want to read or write a file see [open()](), if you want to manipulate paths, see the [os.path]() module, and if you want to read all the lines in all the files on the command line see the [fileinput]() module. For creating temporary files and directories see the [tempfile]() module, and for high-level file and directory handling see the [shutil]() module.

- os.**rename**(*src*, *dst*, *, *src_dir_fd=None*, *dst_dir_fd=None*)

Rename the file or directory *src* to *dst*. If *dst* exists, the operations will fail with an [OSError]() subclass in a number of cases: On Windows, if *dst* exosts a [FileExistsError]() is always raised. On Unix, if *src* is a file and *dst* is a directory or vice-versa, an [IsADirectoryError]() or a [NotADirectoryError]() will be raised respectively. If both are directories and *dst* is empty, *dst* will be silently replaced. If *dst* is a non-empty directory, an [OSError]() is raised. If both are files, *dst* it will be replaced silently if the user has permission. The operation may fail on some Unix flavors if *src* and *dst* are on different filesystems. If successful, the renaming will be an atomic operation (this is a POSIX requirement).

---

### Reference
- os 3.7.9, https://docs.python.org/3.7/library/os.html, 2021-03-19-Fri.
- os 3.8.17, https://docs.python.org/3.8/library/os.html, 2023-10-16-Mon.
