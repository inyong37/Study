# os | [3.7.9](https://docs.python.org/3.7/library/os.html) | [3.8.17](https://docs.python.org/3.8/library/os.html)

'This page has been moved from Python/readme.md`

This module provides a portable way of using operating system dependent functionality. If you just want to read or write a file see `open()`, if you want to manipulate paths, see the `os.path` module, and if you want to read all the lines in all the files on the command line see the `fileinput` module. For creating temporary files and directories see the `tempfile` module, and for high-level file and directory handling see the `shutil` module.

## File Names, Command Line Arguments, and Environment Variables

## Process Parameters

## File Object Creation

## File Descriptor Operations

### Querying the Size of a Terminal

### Inheritance of File Descriptors

## Files and Directories

On some Unix platforms, many of these functions support one or more of these features:

1. specifying a file descriptor: Normally the path argument provided to functions in the os module must be a string specifying a file path. However, some functions now alternatively accept an open file descriptor for their path argument. The function will then operate on the file referred to by the descriptor. (For POSIX systems, Python will call the variant of the function prefixed with f (e.g. call fchdir instead of chdir).)

You can check whether or not path can be specified as a file descriptor for a particular function on your platform using os.supports_fd. If this functionality is unavailable, using it will raise a NotImplementedError.

If the function also supports dir_fd or follow_symlinks arguments, it’s an error to specify one of those when supplying path as a file descriptor.

2. paths relative to directory descriptors: If dir_fd is not None, it should be a file descriptor referring to a directory, and the path to operate on should be relative; path will then be relative to that directory. If the path is absolute, dir_fd is ignored. (For POSIX systems, Python will call the variant of the function with an at suffix and possibly prefixed with f (e.g. call faccessat instead of access).

You can check whether or not dir_fd is supported for a particular function on your platform using os.supports_dir_fd. If it’s unavailable, using it will raise a NotImplementedError.

3. not following symlinks: If follow_symlinks is False, and the last element of the path to operate on is a symbolic link, the function will operate on the symbolic link itself rather than the file pointed to by the link. (For POSIX systems, Python will call the l... variant of the function.)

You can check whether or not follow_symlinks is supported for a particular function on your platform using os.supports_follow_symlinks. If it’s unavailable, using it will raise a NotImplementedError.

* `os.rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)`

Rename the file or directory `src` to `dst`. If `dst` exists, the operations will fail with an `OSError` subclass in a number of cases:

On Windows, if `dst` exists a `FileExistsError` is always raised.

On Unix, if `src` is a file and `dst` is a directory or vice-versa, an `IsADirectoryError` or a `NotADirectoryError` will be raised respectively. If both are directories and `dst` is empty, `dst` will be silently replaced. If `dst` is a non-empty directory, an `OSError` is raised. If both are files, `dst` it will be replaced silently if the user has permission. The operation may fail on some Unix flavors if `src` and `dst` are on different filesystems. If successful, the renaming will be an atomic operation (this is a POSIX requirement).

This funciton can support specifying `src_dir_fd` and/or `dst_dir_fd` to supply paths relative to directory descriptors.

If you want cross-platform overwirting of the destination, use `replace()`.

Raises an auditing event `os.rename` with arguments `src`, `dst`, `src_dir_fd`, `dst_dir_fd`.

New in version 3.3: The `src_dir_fd` and `dst_dir_fd` arguments.

Changed in version 3.6: Accepts a path-like object for `src` and `dst`.

* `os.renames(old, new)`

* `os.replace(src, dst, *, src_dir_fd=None, dst_dir_fd=None)`

* `os.rmdir(path, *, dir_fd=None)`

* `os.walk(top, topdown=True, onerror=None, followlinks=False)`

### Linux Extended Attributes

New in version 3.3.

These functions are all available on Linux only.

## Process Management

These functions may be used to create and manage processes.

The various exec* functions take a list of arguments for the new program loaded into the process. In each case, the first of these arguments is passed to the new program as its own name rather than as an argument a user may have typed on a command line. For the C programmer, this is the argv[0] passed to a program’s main(). For example, os.execv('/bin/echo', ['foo', 'bar']) will only print bar on standard output; foo will seem to be ignored.

* `os._exit(n)`

* `os.fork()`

* `os.kill(pid, sig)`

* `os.popen(cmd, mode='r', buffering=-1)`

* `os.system(command)`

* `os.times()`

* `os.wait()`

## Interface to the Scheduler

These functions control how a process is allocated CPU time by the operating system. They are only available on some Unix platforms. For more detailed information, consult your Unix manpages.

## Miscellaneous System Information

* `os.cpu_count()`

* `os.curdir`

* `os.pardir`

* `os.pathsep`

* `os.linesep`

* `os.devnull`

## Random Numbers

* `os.getrandom(size, flags=0)`

Get up to size random bytes. The function can return less bytes than requested.

* `os.urandom(size)`

Return a string of size random bytes suitable for cryptographic use.

---

### Reference
- os 3.7.9, https://docs.python.org/3.7/library/os.html, 2021-03-19-Fri.
- os 3.8.17, https://docs.python.org/3.8/library/os.html, 2023-10-16-Mon.
