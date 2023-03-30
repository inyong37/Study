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

## _Package_

### [Backports](https://backports.wiki.kernel.org/index.php/Main_Page)

The Backports Project enables old kernels to run the latest drivers. "Backporting" is the process of making new software run on something old. A version of something new that's been modified to run on something old is called a "backport".

### _Build Debian Package deb File_ | [Blog (KR)](https://devanix.tistory.com/314) | [Blog (KR)](https://blog.djjproject.com/406)

1. package folder 생성 `mkdir {package_name}_{version}-{revision}` such as `mkdir dummydeb_0.0.1-1`
2. DEBIAN folder 생성 `mkdir {package_name}/DEBIAN`
3. control file 생성 및 content 기입
4. content 생성 such as `cd {package_name}/ && dd if=/dev/zero of=dummyfile bs=1024 count=102400`
5. build: `dpkg -b {package_folder_name} {package_name}` 

### _[Debian Package Management](https://wiki.debian.org/PackageManagement)_

Much of why Debian is a strong Linux distribution comes from its package management. Everything in Debian - every application, every component - everything - is built into a package.

There are many software packages available for Debian - everything from the Linux kernel to games. And their number has been growing with every release.

The Apt (Advanced Package Tool) package management system is a set of tools to download, install, remove, upgrade, configure and manage Debian packages, and therefore all software installed on a Debian system.

### _[Debian Package Management Tool](https://wiki.debian.org/PackageManagementTools)_

Many tools available on a Debian system can be used for Package management. Commonly used ones include:

- Command-line
  - apt: The main command-line package management tool
  - aptitude: command-line and text-based interface (ncurses) for Apt
- Graphical
  - Synaptic: Graphical package manager
  - gdebi: Graphical installer for standalone Debian Packages
  - gnome-software: Software Center for GNOME

### [apt](https://www.debian.org/doc/manuals/apt-guide/index.en.html)

The apt package provides commandline tools for searching, managing, and querying information about packages, and access all features of the libapt-pkg library: 

- apt: high-level commandline interface for the package management system.
- apt-cache: performs a variety of operations on APT's package cache.
- apt-cdrom: used to add a new CD-ROM to APT's list of available sources.
- apt-config: This program is used by the other apt utilities to provide a standard interface to the apt configuration settings.
- apt-get: command-line tool for handling packages
- apt-key: manage the list of keys used by apt to authenticate packages. This command is deprecated!

### [dpkg](https://www.debian.org/doc/manuals/debian-faq/pkgtools.en.html#dpkg)

The dpkg package provides low-level infrastructure for handling the installation and removal of Debian software packages:

- dpkg: a tool to install, build, remove and manage Debian packages.

### _Editing Ubuntu Package Repository_ | [Blog (KR)](https://zetawiki.com/wiki/%EC%9A%B0%EB%B6%84%ED%88%AC_%EC%A0%80%EC%9E%A5%EC%86%8C_%EB%B3%80%EA%B2%BD) | [Blog (KR)](https://www.fun25.co.kr/blog/ubuntu-1604-software-properties-common/?category=001) | [StackOverflow](https://askubuntu.com/questions/197564/how-do-i-add-a-line-to-my-etc-apt-sources-list)

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

### _KVM_ | [Red Hat](https://www.redhat.com/en/topics/virtualization/what-is-KVM)

Kernel-based Virtual Machine (KVM) is an open source virtualization technology built into Linux. Specifically, KVM lets you turn Linux into a hypervision that allows a host machine to run multiple, isolated virtual environments called guests or virtual machines (VMs).

KVM is part of Linux. If you've got Linux 2.6.20 or newer, you've got KVM. KVM was first announced in 2006 and merged into the mainline Linux kernel version a year later. Because KVM is part of existing Linux code, it immediately benefits from every new Linux feature, fix, and advancement without additional engineering.

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
- What is KVM Red Hat, https://www.redhat.com/en/topics/virtualization/what-is-KVM, 2022-07-20-Wed.
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
