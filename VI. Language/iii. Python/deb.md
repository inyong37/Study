# Debian Package Made with Python

## Date

2023-10-13-Fri.

2023-10-16-Mon.

## Environment

* Ubuntu 20.04.4 LTS
  * Python 3.8
 
## Debian Package

### 1. Create Directory Architecture

```Bash
{program_version=imhere_0.0.1}
├── DEBIAN
│   └── control
└── usr
    └── bin
        └── {python_code=main.py}
```

In this case, the python code of the program consists of a single file.

:key: With Multiple Files: You should place them under "{program_version}/usr/share/{program}/".

### 2. Change the Directory's Permission

`sudo chown root:root -R {program_version}`

### 3. Change the Script's Persmission

`chmod 0755 {python_code=main.py}`

### 4. Build the Package

`dpkg -b {program_version}`

### :tada: Verify

Install: `sudo dpkg -i {program_version}.deb`

Example:

```Bash
(base) inyong@desktop:~$ sudo dpkg -i imhere_0.0.1.deb
Selecting previously unselected package imhere.
(Reading database ... 270522 files and directories currently installed.)
Preparing to unpack imhere_0.0.1.deb ...
Unpacking imhere (0.0.1) ...
Setting up imhere (0.0.1) ...
```

:bulb: Need superuser privileg:

Execute: `{python_code}`

Example:

```Bash
(base) inyong@desktop:~$ main.py
Hola!
```

Uninstall: `dpkg -r {program}`

Example:

```Bash
(base) inyong@desktop:~$ sudo dpkg -r imhere
(Reading database ... 270523 files and directories currently installed.)
Removing imhere (0.0.1) ...
```

### Appendix

```Bash
(base) inyong@desktop:~$ cat imhere_0.0.1/DEBIAN/control
Package: imhere
Version: 0.0.1
Maintainer: My Name <my@my.com>
Description: My Test Package
Homepage: http://myhomepage.com
Architecture: amd64
```

```Bash
(base) inyong@desktop:~$ cat imhere_0.0.1/usr/bin/main.py
#! /usr/bin/python3

print('Hola!')
```

---

### Reference:
- https://devanix.tistory.com/314, 2023-10-13-Fri.
- https://unix.stackexchange.com/questions/256149/what-does-esac-mean-at-the-end-of-a-bash-case-statement-is-it-required, 2023-10-13-Fri.
- https://lists.debian.org/debian-glibc/1999/11/msg00000.html, 2023-10-13-Fri.
- https://www.cyberciti.biz/faq/create-empty-file-linux-commands/, 2023-10-13-Fri.
- Debian Package Stackoverflow, https://stackoverflow.com/questions/1382569/how-do-i-do-debian-packaging-of-a-python-package, 2023-10-16-Mon.
