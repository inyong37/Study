# [Linux](https://www.linux.org/) | [WiKi](https://en.wikipedia.org/wiki/Linux) | [Download](https://www.linux.org/pages/download/)

`This page is from the 'System' page.`

Linux is a family of open source Unix-like operating systems based on the Linux kernel, an operating system kernel first released on September 17, 1991, by Linus Torvalds. Linux is typically packaged in a Linux distribution.

Distributions include the Linux kernel and supporting system software and libraries, many of which are provided by the GNU Project. Many Linux distributions use the word "Linux" in their name, but the Free Software Foundation uses the name GNU/Linux to emphasize the importance of GNU software, causing some controversy.

Popular Linux distributions include Debian, Fedora, and Ubuntu. Commercial distributions include Red Hat Enterprise Linux and SUSE Linux Enterprise Server. Desktop Linux distributions include a windowing system such as X11 or Wayland, and a desktop environment such as GNOME or KDE Plasma. Distributions intended for servers may omit graphics altogether, or include a solution stack such as LAMP. Because Linux is freely redistributable, anyone may create a distribution for any purpose.

Linux was originally developed for personal computers based on the Intel x86 architecture, but has since been ported to more platforms than any other operating system. Because of the dominance of Android on smartphones, Linux also has the largest installed base of all general-purpose operating systems. Although it is used by only around 2.3 percent of desktop computers, the Chromebook, which runs the Linux kernel-based Chrome OS, dominates the US K–12 education market and represents nearly 20 percent of sub-$300 notebook sales in the US. Linux is the leading operating system on servers (over 96.4% of the top 1 million web servers' operating systems are Linux), leads other big iron systems such as mainframe computers, and is the only OS used on TOP500 supercomputers (since November 2017, having gradually eliminated all competitors).

Linux also runs on embedded systems, i.e. devices whose operating system is typically built into the firmware and is highly tailored to the system. This includes routers, automation controls, smart home technology (like Google Nest), televisions (Samsung and LG Smart TVs use Tizen and WebOS, respectively), automobiles (for example, Tesla, Audi, Mercedes-Benz, Hyundai, and Toyota all rely on Linux), digital video recorders, video game consoles, and smartwatches. The Falcon 9's and the Dragon 2's avionics use a customized version of Linux.

Linux is one of the most prominent examples of free and open-source software collaboration. The source code may be used, modified and distributed commercially or non-commercially by anyone under the terms of its respective licenses, such as the GNU General Public License.

### _Live Booting Linux_ | [List of live CDs Wiki](https://en.wikipedia.org/wiki/List_of_live_CDs)

The concept of live booting is actually quite simple. With a live Linux distribution (not all distributinos come in live flavors), you can boot your machine from either a CD/DVD disk or from a USB flash drive and choose to try out the operating system without making any changes to your hard drive.

How this works is by running the entire system from volatile memory (RAM). The operating system and all programs are usable, but run from memory. Because of this, you can boot the live system, test/use it for as long as you need, and then reboot the system (remembering to remove the live media) to return to your original system.

---

### [man](https://man7.org) | [Project](https://www.kernel.org/doc/man-pages/)

The Linux man-pages project documents the Linux kernel and C library interfaces that are employed by user-space programs. With respect to the C library, the primary focus is the GNU C library (glibc), although, where known, documentation of variations in other C libraries available for Linux is also included.

---

## [Daemon](https://man7.org/linux/man-pages/man7/daemon.7.html)

A daemon is a service process that runs in the background and supervises the system or provides functionality to other processes. Traditionally, daemons are implemented following a scheme originating in SysV Unix. Modern daemons should follow a simpler yet more powerful scheme (here called "new style" daemons), as implemented by systemd.

### SysV Daemons

When a traditional SysV daemon starts, it should execute the following steps as part of the initialization. Note that these steps are unnecessary for new-style daemons, and should only be implemented of compatibility with SysV is essential.

1. Close all open file descriptors except standard input, output, and error (i.e. the first three file descriptors 0, 1, 2). This ensures that no accidentally passed file descriptor stays around in the daemon process. On Linux, this is best implemented by iterating through /proc/self/fd, with a fallback of iterating from file descriptor 3 to the value returned by getrlimit() for RLIMIT_NOFILE.

2. Reset all signal handlers to their default. This is best done by iterating through the available signals up to the limit of _NSIG and resetting them to SIG_DFL.

3. Reset the signal mask using sigprocmask().

4. Sanitize the environment block, removing or resetting environment variables that might negatively impact daemon runtime.

5. Call fort(), to create a background process.

6. In the child, cakk setsid() to detach from any terminal and create an independent session.

7. In the child, call fort() again, to ensure that the daemon can never re-acquire a terminal again. (This relevant if the program - and all its dependencies - does not carefully specify `0_NOCTTY` on each and every single `open()` call that might potentially open a TTY device node.

8. Call exit() in the first child, so that only the second child (the actual daemon process) stays around. This ensures that the daemon process is re-parented to init/PID 1, as all daemons should be.

9. In the daemon process, connect /dev/null to standard input, output, and error.

10. In the daemon process, reset the umask to 0, so that the file modes passed to open(), mkdir() and suchlike directly control the access mode of the created files and directories.

11. In the daemon process, change the current directory to the root directory (.), in order to avoid that the daemon involuntarily blocks mount points from being unmounted.

12. In the daemon processs, write the daemon PID (as returned by getpid()) to a PID file, for example /run/foobar.pid (for a hypothetical daemon "foobar") to ensure that the aemon cannot be started more than once. This must be implemented in race-free fashion so that the PID file is only updated when it is verified at the same time that the PID previously stored in the PID file no longer exists or belongs to a foreign process.

13. In the daemon process, drop privileges, if possible and applicable.

14. From the daemon process, notify the original process started that initialization is complete. This can be implemented via an unnamed pipe or similar communication channel that is created before the first fork() and hence available in both the original and the daemon process.

15. Call exit() in the original process. The process that invoked the daemon must be able to rely on that this exit() happens after initialization is complete and all external communication channels are established and accessible.

The BSD daemon() function should not be used, as it implements only a subset of these steps.

A daemon that needs to provide compatibility with SysV systems should implement the scheme pointed out above. However, it is recommended to make this behavior optional and configurable via a command line argument to ease debugging as well as to simplify integration into systems using systemd.

###  New-Style Daemons

Modern services for Linux should be implemented as new-style daemons. This makes it easier to supervise and control them at runtime and simplifies their implementation.

For developing a new-style daemon, none of the initialization steps recommended for SysV daemons need to be implemented. New-style init systems such as systemd make all of them redundant. Moreover, since some of these steps interfere with process monitoring, file descriptor passing and other functionality of the init system, it is recommended not to execute them when run as new-style service.

Note that new-style init systems guarantee execution of daemon processes in a clean process context: it is guaranteed that the environment block is sanitized, that the signal handlers and mask is reset and that no left-over file descriptors are passed. Daemons will be executed in their own session, with standard input connected to /dev/null and standard output/error connected to the systemd-journald.service logging service, unless otherwise configured. The umask is reset.

It is recommended for new-style daemons to implement the following:

1. If SIGTERM is received, shut down the daemon and exit cleanly.

2. If SIGHUP is received, reload the configuration files, if this applies.

3. Provide a correct exit code from the main daemon process, as this is used by the init system to detect service errors and problems. It is recommended to follow the exit code scheme as defined in the LSB recommendations for SysV init scripts.

4. If possible and applicable, expose the daemon's control interface via the D-Bus IPC system and grab a bus name as last step of initialization.

5. For integration in systemd, provide a .service unit file that carries information about starting, stopping and otherwise maintaining the daemon. See systemd.service for details.

6. As much as possible, rely on the init system's functionality to limit the access of the daemon to files, services and other resources, i.e. in the case of systemd, rely on systemd's resource limit control instead of implementing your own, rely on systemd's privilege dropping code instead of implementing it in the daemon, and similar. See systemd.exec for the available controls.

7. If D-Bus is used, make your daemon bus-activatable by supplying a D-Bus service activation configuration file. This has multiple advantages: your daemon may be started lazily on-demand; it may be started in parallel to other daemons requiring it — which maximizes parallelization and boot-up speed; your daemon can be restarted on failure without losing any bus requests, as the bus queues requests for activatable services.

8. If your daemon provides services to other local processes or remote clients via a socket, it should be made socket-activatable following the scheme pointed out below. Like D-Bus activation, this enables on-demand starting of services as well as it allows improved parallelization of service start-up. Also, for state-less protocols (such as syslog, DNS), a daemon implementing socket-based activation can be restarted without losing a single request.

9. If applicable, a daemon should notify the init system about startup completion or status updates via the sd_notify interface.

10. Instead of using the syslog() call to log directly to the system syslog service, a new-style daemon may choose to simply log to standard error via fprintf(), which is then forwarded to syslog by the init system. If log levels are necessary, these can be encoded by prefixing individual log lines with strings like "<4>" (for log level 4 "WARNING" in the syslog priority scheme), following a similar style as the Linux kernel's printk() level system. For details, see sd-daemon and systemd.exec.

11. As new-style daemons are invoked without a controlling TTY (but as their own session leaders) care should be taken to always specify `O_NOCTTY` on `open()` calls that possibly reference a TTY device node, so that no controlling TTY is accidentally acquired.

These recommendations are similar but not identical to the Apple MacOS X Daemon Requirements.

### SYSTEMD(1): systemd, init - systemd system and service manager

systemd is a system and service manager for Linux operating systems. When run as first process on boot (as PID 1), it acts as init system that brings up and maintains userspace services. Separate instances are started for logged-in users to start their services.

systemd is usually not invoked directly by the user, but is installed as the /sbin/init symlink and started during early boot. The user manager instances are started automatically through the user@.service(5) service.

For compatibility with SysV, if the binary is called as init and is not the first process on the machine (PID is not 1), it will executed telinit and pass all command line arguments unmodified. That means init and telinit are mostly equivalent when invoked from normal login sessions. See telinit(8) for more information.

### SERVICE(8): service - run a System V init script

service runs a System V init script or systemd unit in as predictable an environment as possible, removing most environment variables and with the current working directory set to /.

The SCRIPT parameter specifies a System V init script, located in /etc/init.d/SCRIPT, or the name of a systemd unit. The existence of a systemd unit of the same name as a script in /etc/init.d will cause the unit to take precedence over the init.d script. The supported values of COMMAND depend on the invoked script. service passes COMMAND and OPTIONS to the init script unmodified. For systemd units, start, stop, status, and reload are passed through to their systemctl/initctl equivalents.

All scripts should support at least the start and stop commands. As a special case, if COMMAND is --full-restart, the script is run twice, first with the stop command, then with the start command. Note, that unlike update-rc.d(8), service does not check /usr/sbin/policy-rc.d.

service --status-all runs all init scripts, in alphabetical order, with the status command. The status is [ + ] for runnung services, [ - ] for stopped services and [ ? ] for services without a status command. This option only calls status for sysvinit jobs.

### init

리눅스 커널이 부팅된 뒤 실행되는 첫번째 프로레스임. 커널이 직접 실행하는 유일한 프로세스임. 부모 프로세스를 가지지 않는 유일한 프로세스임. Init을 제외한 모든 프로세스의 조상임. 프로세스와 시스템의 초기화와 관리함. initrc에 기록된 백그라운드 서비스와 시스템 서비스를 실행함. GUI를 사용할 수 있게 디스플레이 매니저(GDM, LightDM)를 실행함. 시스템 서비스, 커널 등에서 발생하는 로그를 모아서 저널링함. 데몬 프로세스나 고아가 된 프로세스의 부모가 됨. 동작 과정은 1. 파일 시스템 초기화, 네트워크 등 시스템 서비스 실행, 백그라운드 서비스 실행, GUI 쉘 실행함(systemd 기준).

* SysV: 가장 오래된 시스템임.
* Upstart: 이벤트 기반 서비스 관리 및 Ubuntu에서 옛날에 사용함(현재는 systemd).
* Runit: 부팅, shutdown 속도 빠름, 작은 코드 베이스, 포팅 용이, 임베디드에서 사용함.
* Systemd: 서비스를 등록하여 실행, 이벤트 기반, 저널링, 알람 기능 제공, 시스템 관련 라이브러리(sdbus, sd-event) 제공, 가장 많이 사용, 기능이 많음.

---

## Package

### [Debian Packaging](https://wiki.debian.org/Packaging) | [Introduction](https://wiki.debian.org/Packaging/Intro) | [Learn](https://wiki.debian.org/Packaging/Learn)

A Debian package is a collection of files that allow for applications or libraries to be distributed via the package management system. The aim of packaging is to allow the automation of installing, upgrading, configuring, and removing computer programs for Debian in a consistent manner. A package consists of one source package, and one or more binary packages. The Debian Policy specifies the standard format for a package, which all packages must follow.

deb 파일은 설치되어야 하는 파일과 그 위치가 지정된 채로 압축되어 있는 형태. 패키지 설치란 압축 해제된 결과를 리눅스 루트 디렉토리에 이동.

[Binary packages (.deb)](https://wiki.debian.org/Packaging/BinaryPackage) contain executables, standard configuration files, other resources required for executables to run, documentation, data, ...

[Source packages (.dsc)](https://wiki.debian.org/Packaging/SourcePackage) contain the upstream source distribution, configuration for the package build system, list of runtime dependencies and conflicting packages, a machine-readable description of copyright and license information, initial configuration for the software, and more.

### [Debian Python](https://wiki.debian.org/Python/LibraryStyleGuide) | [Debian Python Policy](https://www.debian.org/doc/packaging-manuals/python-policy/)

Debian 11 (bullseye) removed unversioned packages. Debian 11은 `python` command를 사용하면 Python 2를 지정하지만, 12부터는 처음에 설치되지 않음. Unversioned python command를 build dependencies, dependencies, recommendations, suggestions에 포함하면 안됨.

“control 파일의 Depends의 “python3-simplejson”을 설치할 때 pip/conda install simplejson이랑 apt install python3-simplejson 같음.

### [Backports](https://backports.wiki.kernel.org/index.php/Main_Page)

The Backports Project enables old kernels to run the latest drivers. "Backporting" is the process of making new software run on something old. A version of something new that's been modified to run on something old is called a "backport".

### Build Debian Package deb File | [Blog (KR)](https://devanix.tistory.com/314) | [Blog (KR)](https://blog.djjproject.com/406)

1. package folder 생성 `mkdir {package_name}_{version}-{revision}` such as `mkdir dummydeb_0.0.1-1`
2. DEBIAN folder 생성 `mkdir {package_name}/DEBIAN`
3. control file 생성 및 content 기입
4. content 생성 such as `cd {package_name}/ && dd if=/dev/zero of=dummyfile bs=1024 count=102400`
5. build: `dpkg -b {package_folder_name} {package_name}`

### [Required Files Under the Debian Directory](https://www.debian.org/doc/manuals/maint-guide/dreq.en.html)

### control

This file contains various values which dpkg, dselect, apt-get, apt-cache, aptitude, and other package management tools will use to manage the package. It is defined by the Debian Policy Manula, 5 "Control files and their fields".

### copyright

This file contains information about the copyright and license of the upstream sources. Debian Policy Manual, 12.5 "Copyright information" dictates its content and DEP-5: Machine-parseable debian/copyright provides guidelines for its format.

### changelog

This is a required file, which has a special format described in Debian Policy Manual, 4.4 "debian/changelog". This format is used by dpkg and other programs to obtain the version number, revision, distribution, and urgency of your package.

### [Debian Package Management](https://wiki.debian.org/PackageManagement)

Much of why Debian is a strong Linux distribution comes from its package management. Everything in Debian - every application, every component - everything - is built into a package.

There are many software packages available for Debian - everything from the Linux kernel to games. And their number has been growing with every release.

The Apt (Advanced Package Tool) package management system is a set of tools to download, install, remove, upgrade, configure and manage Debian packages, and therefore all software installed on a Debian system.

### [Debian Package Management Tool](https://wiki.debian.org/PackageManagementTools)

Many tools available on a Debian system can be used for Package management. Commonly used ones include:

- Command-line
  - apt: The main command-line package management tool
  - aptitude: command-line and text-based interface (ncurses) for Apt
- Graphical
  - Synaptic: Graphical package manager
  - gdebi: Graphical installer for standalone Debian Packages
  - gnome-software: Software Center for GNOME

### [apt](https://www.debian.org/doc/manuals/apt-guide/index.en.html) - command-line interface

apt provides a high-level commandline interface for the package management system. It is intended as an end user interface and enables some options better suited for interactive usage by default compared to more specialized APT tools like apt-get(8) and apt-cache(8).

The apt package provides commandline tools for searching, managing, and querying information about packages, and access all features of the libapt-pkg library: 

- apt: high-level commandline interface for the package management system.
- apt-cache: performs a variety of operations on APT's package cache.
- apt-cdrom: used to add a new CD-ROM to APT's list of available sources.
- apt-config: This program is used by the other apt utilities to provide a standard interface to the apt configuration settings.
- apt-get: command-line tool for handling packages
- apt-key: manage the list of keys used by apt to authenticate packages. This command is deprecated!

### [dpkg](https://www.debian.org/doc/manuals/debian-faq/pkgtools.en.html#dpkg) - package manager for Debian

The dpkg package provides low-level infrastructure for handling the installation and removal of Debian software packages:

dpkg is a tool to install, build, remove and manage Debian packages. The primary and more user-friendly front-end for dpkg is aptitude(1). dpkg itself is controlled entirely via command line parameters, which consist of exactly one action and zero or more options. The action-parameter tells dpkg what to do and options control the behavior of the action in the same way.

dpkg can also be used as a front-end to dpkg-deb(1) and dpkg-query(1). The list of supported actions can be found later on in the ACTIONS section. If any such action is encounterd dpkg just runs dpkg-deb or dpkg-query with the parameters given to it, but no specific options are currently passed to them, to use any such option the back-ends need to be called directly.

### [apt vs. dpkg](https://www.linuxfordevices.com/tutorials/debian/apt-vs-dpkg-debian)

* Can download packages from remote repositories: apt can, but dpkg can't
* Can resolve dependences: apt can, but dpkg can't
* Install local packages: both apt(using dpkg) and dpkg can
  * `apt install {package.deb}` or `dpkg -i {package.deb}`
* Install remote pakcage: apt(using dpkg) can, but dpkg can't(users need to manually download a package if they wish to use dpkg)
* List installed packages: both apt and dpkg can
  * `apt list` or `dpkg -l`
 
dpkg does have exclusive uses such as configuring, unpacking, repacking and comparing packages.

### Editing Ubuntu Package Repository | [Blog (KR)](https://zetawiki.com/wiki/%EC%9A%B0%EB%B6%84%ED%88%AC_%EC%A0%80%EC%9E%A5%EC%86%8C_%EB%B3%80%EA%B2%BD) | [Blog (KR)](https://www.fun25.co.kr/blog/ubuntu-1604-software-properties-common/?category=001) | [StackOverflow](https://askubuntu.com/questions/197564/how-do-i-add-a-line-to-my-etc-apt-sources-list)

Change main repo:
- edit `/etc/apt/sources.list` such as `sed -i 's=http://archive.ubuntu.com/ubuntu=http://my-repo-serve:port=g' /etc/apt/sources.list`

Add custom repo:
- add file under `/etc/apt/sources.list.d` with following commands

```bash
sudo apt-get update && sudo apt-get install software-properties-common -y
sudo add-apt-repository "deb http://my-repo-server:port distribution main" -y
```

### [RPM](https://rpm.org/about.html)

The RPM Package Manager (RPM) is a powerful command line driven package management system capable of installing, uninstalling, verifying, querying, and updating computer software packages. Each software package consists of an archive of files along with information about the package like its version, a description, and the like. There is also a library API, permitting advanced developers to manage such transactions from programming languages such as C or Python.

### [YUM](https://access.redhat.com/solutions/9934)

`yum` is the primary tool for getting, installing, deleting, querying, and managing Red Hat Enterprise Linux RPM software packages from official Red Hat software repositories, as well as other third-party repositories. `yum` is used in Red Hat Enterprise Linux version 5 and later. Versions of Red Hat Enterprise Linux 4 and earlier used up2date.

### [DNF](https://docs.fedoraproject.org/en-US/quick-docs/dnf/)

DNF is a software package manager that installs, updates, and removes packages on Fedora and is the successor to YUM (Yellow-Dog Updater Modified). DNF makes it easy to maintain packages by automatically checking for dependencies and etermines the actions required to install packages. This method eliminates the need to manually install or update the package, and its dependencies, using the `rpm` command. DNF is now the default software package management tool in Fedora.

### [YUM vs. DNF](http://www.differencebetween.net/technology/difference-between-yum-and-dnf/)

While the main purpose of YUM or DNF is to manage actual RPM packages on your system, DNF sports better dependency resolution because it uses the more modern and advanced 'libsolv' for improved dependency solving. Libsolv is a proven code base and one of the most sophisticated dependency solving implementations. YUM, on the other hand, uses the public API for dependency resolution.

## _Repository_

### _[Debian Repository](https://wiki.debian.org/DebianRepository)_

A Debian repository is a set of Debian binary or source packages organized in a special directory tree and with various infrastructure files - checksums, indices, signatures, descriptions translations, ... - added. Client computers can connect to the repository to download and install the package using an Apt-based PackageManagement tool.

### _aptly_ | [Create](https://www.aptly.info/doc/aptly/repo/create/) | [add](https://www.aptly.info/doc/aptly/repo/add/) | [publish](https://www.aptly.info/doc/aptly/publish/repo/) | [publish drop](https://www.aptly.info/doc/aptly/publish/drop/)

Create repo:
- `aptly repo create {repo_name}`

Add package to the repo:
- `aptly repo add {repo_name} {package_name}`

Publish repo:
- `aptly publish repo -distribution='jammy' -architectures='all' {repo_name}`

Drop published repo:
- `aptly publish drop jammy`

### *Manual Page (man page)* | [WiKi](https://en.wikipedia.org/wiki/Man_page)

A man page (short for manual page) is a form of software documentation usually found on a Unix or Unix-like operating system. Topics covered include computer programs (including library and system calls), formal standards and conventions, and even abstract concepts. A user may invoke a man page by issuing the man command.

By default, man typically uses a terminal pager program such as more or less to display its output.

Because man pages are distributed together with the software they document, they are a more favourable means of documenting software compared to out-of-band documentation like web pages, as there is a higher likelihood for a match between the actual features of the software to the documented ones. It is for this reason that man-pages are often referred to as an on-line or online form of software documentation, even though the man command does not require internet access, dating back to the times when printed out-of-band manuals were the norm.

### Link `ln`

`ln`은 Link의 약어로 Linux 파일 시스템에서 링크 파일을 만드는 명령어이다. Linux에서는 symbolic link와 hard link 2가지 링크 파일이 존재한다.

### _Symbolic Link_

단순히 원본 파일을 가리키도록 링크만 시켜둔 것으로 Windows의 shortcut과 같은 것이며, 원본 파일을 가리키고만 있으므로 원본 파일의 크기와는 무관하다. 그리고 symbolic link에서는 원본 파일이 삭제되어 존재하지 않을 경우에 링크 파일은 깜박거리면서 링크 파일의 원본 파일이 없다는 것을 알려준다.

### _Hard Link_

원본 파일과 다른 이름으로 존재하는 동일한 파일이며 원본 파일과 동일한 내용의 다른 파일이다. 그리고 hard link에서는 원본 파일과 링크 파일 2개가 서로 다른 파일이기 때문에 둘 중 하나를 삭제하더라도 나머지 하나는 그대로 남아 있다. 또한 hard link에서는 원본 파일의 내용이 변경될 경우에는 링크 파일의 내용 또한 자동으로 변경된다.

Usage: 
- `ln -s /tmp /var/tmp`
- `ln hard_source hard_link`
- `--backup`: 대상 파일이 이미 존재할 경우에 백업 파일을 만든 후에 링크 파일 생성
- `-b`: 링크 파일 생성 시에 대상 파일이 이미 존재하면 백업 파일을 만든 후에 링크 파일을 생성
- `-d`: 디렉토리에 대한 하드 링크 파일 생성을 가능하게 함
- `-f`: 대상 파일이 존재할 경우에 대상 파일을 지우고 링크 파일을 생성
- `-i`: 대상 파일이 존재할 경우에 대상 파일을 지울 것인가를 확인 요청
- `-s`: Create Symbolic link file 생성
- `-S`: 백업 파일 생성 시에 원하는 suffix 지정
- `-t`: 링크 파일을 생성할 디렉토리를 지정

### *Alias*

Usage:
- show: `alias`
- setup at '.bashrc'
```bash
alias ll='ls -al'
alias ls='ls --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'
alias grep='grep --color=auto'
alias tn='tmux new'
alias tl='tmux ls'
alias ta='tmux attach'
```

### *tmux*

Install:
```bash
$ sudo apt-get install tmux
```

### *openssh server*

Install: 
```bash
$ sudo apt-get install openssh-server
```

Usage:
```bash
$ sudo service ssh start
$ sudo systemctl enable ssh
```

### *Symbolic Link*

리눅스 심볼릭 링크는 특정 파일이나 디렉토리에 대하여 참조를 하는 특수한 파일이다. 윈도우에서 바로가기와 동일하다고 할 수 있다.

---

## _Command_

### *dd* | [Blog](https://www.web-workers.ch/index.php/2017/06/23/how-to-create-a-1gb-100mb-10mb-file-for-testing/)

Create 1MB dummyfile:
- `dd if=/dev/zero of=dummyfile bs=1024 count=1024`

Create 100MB dummyfile:
- `dd if=/dev/zero of=dummyfile bs=1024 count=102400`

Create 1GB dummyfile:
- `dd of=/dev/zero pf=dummyfile bs=1024 count=10240000`

### *Fuzzy Finder*

Install:
- `git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf`
- `~/.fzf/install`

Usage:
- `Control` + `t`

### *htop* | [WiKi](https://en.wikipedia.org/wiki/Htop) | Unix

htop is an interactive system-monitor process-viewer and process-manager. It is designed as an alternative to the Unix program top. It shows a frequently updated list of the processes running on a computer, normally ordered by the amount of CPU usage. Unlike top, htop provides a full list of processes running, instead of the top resource-consuming processes. htop uses color and gives visual information about processor, swap and memory status. htop can also display the processes as a tree.

### *top* | [WiKi](https://en.wikipedia.org/wiki/Top_(software)) | Unix

top (table of processes) is a task manager program found in many Unix-like operating systems that displays information about CPU and memory utilization.

### sed | [Stackoverflow](https://unix.stackexchange.com/questions/211834/slash-and-backslash-in-sed)

Replace content without saving `sed 's/foo/bar/g' output.txt`

Replace content with saving `sed 's/foo/bar/g' output.txt`

### *hostname*

- How to change hostname: `sudo vim /etc/hostname` and reboot; `sudo reboot now`

### Show Symbolic Link, Command `$ nm`

A command nm shows a list of symbolic links in object files.

### How to use command nm

Default:
```bash
$ nm foo.o
          U _IO_getc
00000000  Y main
```

Option:
- format: `-f`, POSIX `-f posix`, BSD `-f bsd`, sysv `-f sysv`

Target acrchive file shows libraries as object files

### [wget](https://www.gnu.org/software/wget/)

GNU Wget is a free software package for retrieving files using HTTP, HTTPS, FTP and FTPS, the most widely used Internet protocols. It is a non-interactive commandline tool, so it may easily be called from scripts, `cron` jobs, terminals without X-Windows supports, etc.

### [timedatectl](https://www.freedesktop.org/software/systemd/man/timedatectl.html) - Control the system time and date

timedatactl may be used to query and change the system clock and its settings, and enable or disable time synchronization services. Use systemd-firstboot to initialize the system time zone for mounted (but no booted) system images. timedatectl may be used to show the current status of time synchronization services.

### [chrony](https://chrony.tuxfamily.org/)

chrony is a versatile implementation of the Network Time Protocol (NTP). It can synchronise the system clock with NTP servers, reference clocks (e.g. GPS receiver), and manual input using wristwatch and keyboard. It can also operate as an NTPv4 (RFC 5905) server and peer to provide a time service to other computers in the network.

---

## _File_ | _Extension_

`This part has moved to the 'File' page.`

---

### [OSTree](https://ostreedev.github.io/ostree/introduction/) | libostree | [GitHub](https://github.com/ostreedev/ostree)

OSTree is an upgrade system for Linux-based operating systems that performs atomic upgrades of complete filesystem trees. It is not a package system; rather, it is intended to complement them. A primary model is composing packages on a server, and then replicating them to clients.

The underlying architecture might be summarized as “git for operating system binaries”. It operates in userspace, and will work on top of any Linux filesystem. At its core is a git-like content-addressed object store with branches (or “refs”) to track meaningful filesystem trees within the store. Similarly, one can check out or commit to these branches.

Layered on top of that is bootloader configuration, management of /etc, and other functions to perform an upgrade beyond just replicating files.

---

### [Snaps](https://snapcraft.io/)

Snaps are app packages for desktop, cloud and IoT that are easy to install, secure, cross-platform and dependency-free. Snaps are discoverable and installable from the Snap Store, the app store for Linux with an audience of millions.

Snap:
- A snap is a bundle of an app and its dependencies that works without modification across Linux distributions.

Snapd:
- Snapd is the background service that manages and maintains your snaps, automatically.

Snap Store:
- The Snap Store provides a place to upload snaps, and for users to browse and install the software they want.

Snapcraft:
- Snapcraft is the command and the framework used to build and publish snaps.

### [Logical Volume Manager (LVM)](https://wiki.archlinux.org/title/LVM)

Logical Volume Manager (LVM) is a device mapper framework that provides logical volume management for the Linux kernel.

### Physical volume (PV)

Unix block device node, usable for storage by LVM. Examples: a hard disk, an MBR or GPT partition, a loopback file, a device mapper device (e.g. dm-crypt). It hosts an LVM header.

### Volume group (VG)

Group of PVs that serves as a container for LVs. PEs are allocated from a VG for a LV.

### Logical volume (LV)

"Virtual/logical partition" that resides in a VG and is composed of PEs. LVs are Unix block devices analogous to physical partitions, e.g. they can be directly formatted with a file system.

### Physical extent (PE)

The smallest contiguous extent (default 4MiB) in the PV that can be assigned to a LV. Think of PEs as parts as PVs that can be allocated to any LV.

### [Logical Volume Manager (LVM) vs. standard partitioning in Linux](https://www.redhat.com/sysadmin/lvm-vs-partitioning)

With tranditional storage, three 1TB disks are handled individually. Wuth LVM, those same three disks are considered to be 3TB of aggregated storage capacity. This is accomplished by designating the stoarge disks as Physical Volumes (PV), or storage capacity useable by LVM. The PVs are then added to one or more Volume Groups (VGs). The VGs are carved into one or more Logical Volumes (LVs), which then treated as tranditional partitions.

---

## _Tuning Kernel_

### _TCP Kernel Parameter_ | [NHN (KR)](https://meetup.toast.com/posts/53)

Enable TCP window scaling:
- `sysctl -w net.ipv4.tcp_window_scaling="1"` (Windows, macOS, iOS, Android는 default enabled)

Increase TCP socket buffer size:
- Auto-tuned by Linux kernel, but usually 128KB which is for general purpose PC
- Trand-off: Bandwidth <-> memory usage
  - `sysctl -w net.core.rmem_default="253952"`
  - `sysctl -w net.core.wmem_default="253952"`
  - `sysctl -w net.core.rmem_max="16777216"`
  - `sysctl -w net.core.wmem_max="16777216"`
- Memory for per individual TCP socket
- ipv4의 옵션이 ipv6에서도 같이 사용됨(ip_, ip_local_portrange, tcp, ipv4.icmp_)
  - `sysctl -w net.ipv4.tcp_rmem="253952 253952 16777216"` # min / default / max
  - `sysctl -w net.ipv4.tcp_wmem="253952 253952 16777216"` # min / default / max
- Memory for all TCP sockets
- TCP socket 전체에서 사용되는 메모리가 이 값을 초과하면 TCP memory pressure 상태가 되어 min memory buffer size를 갖게 됨
  - 부팅 시 system memory에 맞추어 auto-tuned 최적화 되었기 때문에, 수정하지 말 것
  - 구글링 검색 내용들이 말도 안되는 값을 가이드함
    - 예: `systcl -w net.ipv4.tcp_mem="8388608 8388608 8388608"`: 단위가 page(4096byte)이므로 32GB
  - `sysctl net.ipv4.tcp_mem`

### _Network Capacity Kernel Parameter_ | [NHN (KR)](https://meetup.toast.com/posts/54)

Maximize file count:
- Unix/Linux socket is treated as a file
  - Check maximum file count for system 
    - `sysctl fs.file-max`
  - Check maximum file count for user/process
    - `ulimit -a` 
  - Change maximum file count for user/process
    - `ulimit -SHn @@@`
  - Check opened-file opened-unusing-file max-openable-file
    - `sysctl fs.file-nr`

Backlogs:
- in-bound queue를 증가시켜 버려지는 packet을 최소화
- Kernel의 packet 처리 속도가 queue에 추가되는 packet 속도보다 느리면, queue에 추가되지 못한 packet들은 버려짐
- Trade-off: memory <-> queue size
  - `sysctl -w net.core.netdev_max_backlog="30000"`
- Increase hard limit of accept socket count (ESTABLISHED, connection completed)
  - `sysctl -w net.core.somaxconn="1024"` # default=128, match with application count
- Increase hard limit of listen socket count (SYN_RECEIVED, connection incompleted)
  - `sysctl -w net.ipv4.tcp_max_syn_backlog="1024"`
  - Kernel parameter를 변경해도, 실제 server application에서 listen backlog를 증가시키려면 listen() 시스템 콜 호출 시 매개변수 backlog에 필요한 값을 전달해야함

Port Range:
- TCP 연결을 맺을 때, client socket은 하나의 port를 선점, bind() system call로 source port를 지정하지 않으면 임의 port 할당 - ephemeral port
- TCP 연결은 source address/port, destination address/port를 갖음
- Client는 연결할 때, port를 소모
- 일반적으로 listen()하는 server는 추가적인 port 소모하지 않음
  - Proxy server는 다른 backend server로 전달을 위해 client port가 필요
  - Port 확인
    - `sysctl net.ipv4.ip_local_port_range` # 3278 61000 - 28232개의 ephemeral port 할당 가능
  - 가용한 port 설정
    - `sysctl -w net.ipv4.ip_local_port_range="1024 65535"` # well-known port는 제외해야함
  - TCP socket 종료 시, gracefully shutdown 하기 때문에 자원을 늦게 반환
  - Client socket에서 close()로 socket을 닫는 경우 socket은 TIME_WAIT 상태에 머뭄 - ephemeral port 사용 불가, socket 수 제한

### _Time Wait_ | [NHN (KR)](https://meetup.toast.com/posts/55)

TCP socket states:
- ESTABLISHED -> CLOSE/FIN (close() system call)-> Active CLOSE -> FIN WAIT 1 -> FIN WAIT 2 -> "TIME WAIT"
  - TIME_WAIT 상태에서 RFC793 정의로 2MSL(Maximum Segment Lifetime, 2분 대기)
  - 실제로 대부분의 OS에서는 최적화를 위해 1분 정도 TIME_WAIT 상태에서 대기
    - Linux 또한 1분으로 kernel에 상수로 정해져있음
  - `net.ipv4.fin_timeout`은 FIN_WAIT_2 상태의 timeout 시간
    - 대부분의 시스템에서 FIN_WAIT_2 상태에서 머무르는 socket은 드뭄
    - 대부분 TIME_WAIT로 전이됨
    - 수정해도 변화 거의 없음
  - TIME_WAIT는 gracefully shutdown을 위해 필요
    - 데이터 유실 문제 등 방지

- ESTABLISHED -> FIN/ACK -> Passive CLOSE -> CLOSE WAIT -> LAST ACK -> CLOSED

### [iptables](https://linux.die.net/man/8/iptables) - administration tool for IPv4 packet filtering and NAT

---

## Desktop Environment (DE) | [Wiki](https://en.wikipedia.org/wiki/Desktop_environment)

In computing, a desktop environment (DE) is an implementation of the desktop metaphor made of a bundle of programs running on top of a computer operating system that share a common graphical user interface (GUI), sometimes described as a graphical shell. The desktop environment was seen mostly on personal computers until the rise of mobile computing. Desktop GUIs help the user to easily access and edit files, while they usually do not provide access to all of the features found in the underlying operating system. Instead, the traditional command-line interface (CLI) is still used when full control over the operating system is required.

A desktop environment typically consists of icons, windows, toolbars, folders, wallpapers and desktop widgets (see Elements of graphical user interfaces and WIMP). A GUI might also provide drag and drop functionality and other features that make the desktop metaphor more complete. A desktop environment aims to be an intuitive way for the user to interact with the computer using concepts which are similar to those used when interacting with the physical world, such as buttons and windows.

While the term desktop environment originally described a style of user interfaces following the desktop metaphor, it has also come to describe the programs that realize the metaphor itself. This usage has been popularized by projects such as the Common Desktop Environment, K Desktop Environment, and GNOME.

### [freedesktop.org](https://www.freedesktop.org/wiki/) | [Software](https://www.freedesktop.org/wiki/Software/) | [GitLab](https://gitlab.freedesktop.org/explore/groups)

freedesktop.org hosts the development of free and open source software, focused on interoperability and shared technology for open-source graphical and desktop systems. We do not ourselves produce a desktop, but we aim to help others to do so.

### [GNOME](https://www.gnome.org/) | [Wiki](https://en.wikipedia.org/wiki/GNOME)

GNOME, originally an acronym for GNU Network Object Model Environment, is a free and open-source desktop environment for Linux and other Unix-like operating systems.

GNOME is the default desktop environment of many major Linux distributions, including Debian, Endless OS, Fedora Linux, Red Hat Enterprise Linux, SUSE Linux Enterprise, Ubuntu, and Tails; it is also the default in Oracle Solaris, a Unix operating system.

### [GNOME Platform](https://developer.gnome.org/documentation/introduction.html) | [Components](https://developer.gnome.org/documentation/introduction/components.html)

The GNOME platform consists of libraries, services and tools which provide everything you need to create and distribute high-quality apps. The platform covers everything from basic UI creation, code editing and building, and app distribution, through to more specialised libraries and services.

GNOME libraries include things like GTK, for building application user interfaces, GStreamer, for multimedia playback, and GSocket networking APIs. These are available to use through the GNOME Flatpak runtime, as well as through the main Linux distributions.

GNOME services are included in the system and give apps access to things like email, calendaring, contacts, and password storage. One of the most useful services for apps is portals, which provides sandboxed apps with access to a wide range of system features.

### [Flatpak](https://flatpak.org/) - installs, manages and runs sandboxed desktop application bundles. | [Docs](https://docs.flatpak.org/en/latest/introduction.html) | [FlatHub](https://flathub.org/home)

Flatpak is a framework for distributing desktop applications across various Linux distributions. It has been created by developers who have a long history of working on the Linux desktop, and is run as an indepedent open source project.

Terminology:
- Flatpak: a system for building, distributing, and running sandboxed desktop applications on Linux.
- Flatpak application: these are the applications the user installs via the `flakpak` command or via a different UI like GNOME Software or KDE Discover.
- Runtime: also called platforms, these are integrated platforms to provide basic utilities needed for a Flatpak application to work.
- BaseApp: these are integrated platforms for frameworks like Electron.
- Flatpak bundle: a specific single-file export format which contains a Flatpak app or runtime.

### [Flatpak Repositories](https://docs.flatpak.org/en/latest/repositories.html)

Flatpak repositories are the primary mechanism for publishing applications, so that they can be installed by users.

### [Hosting a repository](https://docs.flatpak.org/en/latest/hosting-a-repository.html)

---

### Reference
- Linux, https://www.linux.org/, 2020-08-05-Wed.
- Library, https://jasonjason.tistory.com/15, 2020-08-06-Thu.
- Shortcut, https://ko.wikipedia.org/wiki/%EB%B0%94%EB%A1%9C_%EA%B0%80%EA%B8%B0, 2020-08-08-Sat.
- Alias, https://webdir.tistory.com/107, 2020-08-25-Tue.
- openssh, https://jimnong.tistory.com/713, 2020-09-08-Tue.
- man page Wiki, https://en.wikipedia.org/wiki/Man_page, 2020-09-16-Wed.
- Unix Wiki, https://en.wikipedia.org/wiki/Unix, 2020-09-16-Wed.
- A diagram showing the key Unix and Unix-like operating systems, https://en.wikipedia.org/wiki/Unix#/media/File:Unix_history-simple.svg, 2020-09-16-Wed.
- Linux Wiki, https://en.wikipedia.org/wiki/Linux, 2020-09-16-Wed.
- Differences between Unix and Linux, https://m.blog.naver.com/PostView.nhn?blogId=limoremo&
- Linux vs. Unix, https://www.diffen.com/difference/Linux_vs_Unix, 20202-09-16-Wed.
- fuzzy finder Blog Kor, https://black7375.tistory.com/15, 2020-10-12-Mon.
- htop Wiki, https://en.wikipedia.org/wiki/Htop, 2020-09-28-Mon.
- top Wiki, https://en.wikipedia.org/wiki/Top_(software), 2020-09-28-Mon.
- readelf Blog KR, https://m.blog.naver.com/PostView.nhn?blogId=yon7961&logNo=50097076949&proxyReferer=https:%2F%2Fwww.google.com%2F, 2020-08-12-Wed.
- readelf Option Blog KR, https://devanix.tistory.com/186, 2020-08-12-Wed.
- ln Blog KR, https://webdir.tistory.com/148, 2020-08-13-Thu.
- Dependency Management, https://architecture101.blog/2008/12/07/dependency_managment/, 2020-08-13-Thu.
- Command nm Blog KR, https://devanix.tistory.com/190, 2021-03-31-Wed.
- Snaps, https://snapcraft.io/, 2022-07-20-Wed.
- Live Booting Linux, https://www.linux.com/training-tutorials/live-booting-linux/, 2022-07-21-Thu.
- List of live CDs Wiki, https://en.wikipedia.org/wiki/List_of_live_CDs, 2022-07-21-Thu.
- Build Debian Package deb File Blog KR, https://devanix.tistory.com/314, 2022-10-27-Thu.
- Build Debian Package deb File Blog KR, https://blog.djjproject.com/406, 2022-10-27-Thu.
- dd Blog, https://www.web-workers.ch/index.php/2017/06/23/how-to-create-a-1gb-100mb-10mb-file-for-testing/, 2022-10-27-Thu.
- Change Ubuntu Package Repository Blog KR, https://zetawiki.com/wiki/%EC%9A%B0%EB%B6%84%ED%88%AC_%EC%A0%80%EC%9E%A5%EC%86%8C_%EB%B3%80%EA%B2%BD, 2022-10-27-Thu.
- Aptly create, https://www.aptly.info/doc/aptly/repo/create/, 2022-10-27-Thu.
- Aptly add, https://www.aptly.info/doc/aptly/repo/add/, 2022-10-27-Thu.
- Aptly publish, https://www.aptly.info/doc/aptly/publish/repo/, 2022-10-27-Thu.
- Add Custom Repo Server Stackoverflow, https://askubuntu.com/questions/197564/how-do-i-add-a-line-to-my-etc-apt-sources-list, 2022-10-28-Fri.
- Install add-apt-repo tool Blog KR, https://www.fun25.co.kr/blog/ubuntu-1604-software-properties-common/?category=001, 2022-10-28-Fri.
- Aptly publish drop, https://www.aptly.info/doc/aptly/publish/drop/, 2022-10-28-Fri.
- Debian Repository, https://wiki.debian.org/DebianRepository, 2022-11-03-Thu.
- Debian Package Management, https://wiki.debian.org/PackageManagement, 2022-11-03-Thu.
- Debian Package Management Tools, https://wiki.debian.org/PackageManagementTools, 2022-11-03-Thu.
- Linux TCP Kernel Parameter NHN KR, https://meetup.toast.com/posts/53, 2022-11-10-Thu.
- Network Capacity Parameter NHN KR, https://meetup.toast.com/posts/54, 2022-11-10-Thu.
- Time Wait NHN KR, https://meetup.toast.com/posts/55, 2022-11-10-Thu.
- APT, https://www.debian.org/doc/manuals/debian-faq/pkgtools.en.html#apt-get, 2022-12-01-Thu.
- ATP User's Guide, https://www.debian.org/doc/manuals/apt-guide/index.en.html, 2022-12-01-Thu.
- dpkg, https://www.debian.org/doc/manuals/debian-faq/pkgtools.en.html#dpkg, 2022-12-01-Thu.
- LVM Wiki, https://en.wikipedia.org/wiki/Logical_Volume_Manager_(Linux), 2023-03-02-Thu.
- LVM Arch Linux, https://wiki.archlinux.org/title/LVM, 2023-03-02-Thu.
- LVM vs. standard partitioning Red Hat, https://www.redhat.com/sysadmin/lvm-vs-partitioning, 2023-03-02-Thu.
- GNU Wget, https://www.gnu.org/software/wget/, 2023-03-14-Tue.
- timedatectl, https://www.freedesktop.org/software/systemd/man/timedatectl.html, 2023-03-14-Tue.
- chrony, https://chrony.tuxfamily.org/, 2023-03-14-Tue.
- Flatpak, https://flatpak.org/, 2023-03-16-Thu.
- Flatpak Docs, https://docs.flatpak.org/en/latest/introduction.html, 2023-03-16-Thu.
- Repositories Flatpak, https://docs.flatpak.org/en/latest/repositories.html, 2023-03-20-Mon.
- Hosting a repository Flatpak, https://docs.flatpak.org/en/latest/hosting-a-repository.html, 2023-03-20-Mon.
- FaltHub, https://flathub.org/home, 2023-03-20-Mon.
- RPM, https://rpm.org/about.html, 2023-03-22-Wed.
- YUM Red Hat, https://access.redhat.com/solutions/9934, 2023-03-22-Wed.
- DNF Fedora, https://docs.fedoraproject.org/en-US/quick-docs/dnf/, 2023-03-22-Wed.
- YUM vs. DNF, http://www.differencebetween.net/technology/difference-between-yum-and-dnf/, 2023-03-22-Wed.
- iptables, https://linux.die.net/man/8/iptables, 2023-03-22-Wed.
- Desktop Environment Wiki, https://en.wikipedia.org/wiki/Desktop_environment, 2023-03-24-Fri.
- freedesktop.org, https://www.freedesktop.org/wiki/, 2023-03-24-Fri.
- freedesktop.org Software, https://www.freedesktop.org/wiki/Software/, 2023-03-24-Fri.
- freedesktop GitLab, https://gitlab.freedesktop.org/explore/groups, 2023-03-24-Fri.
- GNOME, https://www.gnome.org/, 2023-03-24-Fri.
- GNOME Wiki, https://en.wikipedia.org/wiki/GNOME, 2023-03-24-Fri.
- GNOME Platform, https://developer.gnome.org/documentation/introduction.html, 2023-03-24-Fri.
- GNOME Components, https://developer.gnome.org/documentation/introduction/components.html, 2023-03-24-Fri.
- OSTree, https://developer.toradex.com/torizon/in-depth/ostree/, 2023-03-24-Fri.
- OSTree, https://ostreedev.github.io/ostree/introduction/, 2023-03-24-Fri.
- libostree GitHub, https://github.com/ostreedev/ostree, 2023-03-24-Fri.
- Backports, https://backports.wiki.kernel.org/index.php/Main_Page, 2023-03-30-Thu.
- Init KR, https://www.kernelpanic.kr/5, 2023-05-11-Thu.
- Linux man pages online, https://man7.org/linux/man-pages/index.html, 2023-10-11-Wed.
- The Linux man-pages project, https://www.kernel.org/doc/man-pages/, 2023-10-11-Wed.
- daemon, https://man7.org/linux/man-pages/man7/daemon.7.html, 2023-10-11-Wed.
- man, https://man7.org/, 2023-10-11-Wed.
- Debian Packaging, https://wiki.debian.org/Packaging, 2023-10-12-Thu.
- Debian Python Library Style Guide, https://wiki.debian.org/Python/LibraryStyleGuide, 2023-10-12-Thu.
- Debian Style Guide for Packaging Python Libraries, https://wiki.debian.org/Python/LibraryStyleGuide, 2023-10-12-Thu.
- Debian Python Policy, https://www.debian.org/doc/packaging-manuals/python-policy/, 2023-10-12-Thu.
- Debian Packaging Introduction, https://wiki.debian.org/Packaging/Intro, 2023-10-12-Thu.
- Debian Binary Package DEB, https://wiki.debian.org/Packaging/BinaryPackage, 2023-10-12-Thu.
- Debian Source Package DSC, https://wiki.debian.org/Packaging/SourcePackage, 2023-10-12-Thu.
- Debian Packaging Learn, https://wiki.debian.org/Packaging/Learn, 2023-10-12-Thu.
- apt vs. dpkg, https://www.linuxfordevices.com/tutorials/debian/apt-vs-dpkg-debian, 2023-10-13-Fri.
- DEB Architecture, https://w.cublr.com/linux/ubuntu/deb-architecture/, 2023-10-13-Fri.
- Python Debian, https://stackoverflow.com/questions/1382569/how-do-i-do-debian-packaging-of-a-python-package, 2023-10-16-Mon.
- Debian Directory, https://www.debian.org/doc/manuals/maint-guide/dreq.en.html, 2023-10-17-Tue.
- Required Files Under the Debian Directory, https://www.debian.org/doc/manuals/maint-guide/dreq.en.html, 2023-10-19-Thu.
