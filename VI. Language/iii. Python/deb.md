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

### Appendix. Files

imhere_0.0.1/DEBIAN/control

```Bash
Package: imhere
Version: 0.0.1
Maintainer: My Name <my@my.com>
Description: My Test Package
Homepage: http://myhomepage.com
Architecture: amd64
```

imhere_0.0.1/DEBIAN/conffiles

```Bash
/etc/imhereconf.ini
/usr/local/imhere/conf/config.ini
```

imhere_0.0.1/DEBIAN/postinst

```Bash
#!/bin/bash
##############################
# postinst script
##############################
case "$1" in
configure)
    # When configure,
    ;;
upgrade)
    # When upgrade,
    ;;
*)
    echo "Unrecognized postinst argument '$1'"
esac
```
imhere_0.0.1/DEBIAN/postrm

```Bash
#!/bin/bash
##############################
# postrm script
##############################
case "$1" in
remove)
    # When remove, delete binary except configuration
    ;;
purge)
    # When purge, delete all configuration
    ;;
*)
    echo "Unrecognized postrm argument '$1'"
esac
```
imhere_0.0.1/DEBIAN/preinst

```Bash
#!/bin/bash
##############################
# preinst script
##############################
case "$1" in
install)
    # When install,
    ;;
upgrade)
    # When upgrade,
    ;;
*)
    echo "Unrecognized preinst argument '$1'"
esac
```
imhere_0.0.1/DEBIAN/prerm

```Bash
#!/bin/bash
##############################
# prerm script
##############################
case "$1" in
upgrade)
    # When upgrade, called by package of next version
    ;;
remove)
    # When remove, stop process, revert postinst
    ;;
*)
    echo "Unrecognized prerm argument '$1'"
esac
```

imhere_0.0.1/usr/bin/main.py

```Python
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
