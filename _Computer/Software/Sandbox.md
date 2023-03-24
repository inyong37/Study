# :package: Sandbox | [Wiki](https://en.wikipedia.org/wiki/Sandbox_(computer_security))

In computer security, a sandbox is a security mechanism for separating running programs, usually in an effort to mitigate system failures and/or software vulnerabilities from spreading. The isolation metaphor is taken from the idea of children who do not play well together, so each is given their own sandbox to play in alone. It is often used to execute untested or untrusted programs or code, possibly from unverified or untrusted third parties, suppliers, users or websites, without risking harm to the host machine or operating system. A sandbox typically provides a tightly controlled set of resources for guest programs to run in, such as storage and memory scratch space. Network access, the ability to inspect the host system, or read from input devices are usually disallowed or heavily restricted.

In the sense of providing a highly controlled environment, sandboxes may be seen as a specific example of virtualization. Sandboxing is frequently used to test unverified programs that may contain a virus or other malicious code without allowing the software to harm the host device.

### [Virtualization vs. Sandboxing](https://security.stackexchange.com/questions/167564/what-is-the-differerence-between-virtualization-and-sandboxing)

Sandboxing is a high-level concept that can be implemented in several ways.

Virtualization in practice is a specific type of sandboxing - usually by emulating of "the system", i.e., the CPU and the related hardware.

### [Virtual Machine vs. Sandbox](https://askleo.com/whats-the-difference-between-a-sandbox-and-a-virtual-machine/)

### [Virtualization vs. Container vs. Sandboxes](https://okaythis.com/blog/containers-virtualization-and-sandboxes-meaning)

Virtualization: physical/hardwares including resources as storage and network, operating system.

Container - operating system level virtualization: user space environment, shares kernel

### [Windows Sandbox architecture](https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-sandbox/windows-sandbox-architecture)

lightweight desktop environment to safely run aplications in isolation.

A sandbox is temporary. When it's closed, all the software and files and the state are deleted.

Memory sharing, integrated kernel scheduler

### [Using Container for Sandbox (KR)](https://steemit.com/kr/@asbear/sandbox)

---

### Reference
- Sandbox Wiki, https://en.wikipedia.org/wiki/Sandbox_(computer_security), 2023-03-24-Fri.
- Sandboxing CheckPoint, https://www.checkpoint.com/cyber-hub/threat-prevention/what-is-sandboxing/, 2023-03-24-Fri.
- Virtualization vs. Sandboxing StackExchange, https://security.stackexchange.com/questions/167564/what-is-the-differerence-between-virtualization-and-sandboxing, 2023-03-24-Fri.
- Virtual Machine vs. Sandbox AskLeo, https://askleo.com/whats-the-difference-between-a-sandbox-and-a-virtual-machine/, 2023-03-24-Fri.
- Windows Sandbox architecture, https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-sandbox/windows-sandbox-architecture, 2023-03-24-Fri.
- Using Container for Sandbox Blog KR, https://steemit.com/kr/@asbear/sandbox, 2023-03-24-Fri.
