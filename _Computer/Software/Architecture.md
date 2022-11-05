# _Architecture_

## 32

### i386

### mips

### mipsel

### x86

## 64

### i686

### amd64

### mips64el

### s390x

## ARM

### armel

## Power

### ppc64el

## Debian on arm

- The ARM EABI (armel) port targets a range of older 32-bit ARM devices, particularly those used in NAS hardware and a variety of *plug computers.
- THe newer ARM hard-float (armhf) port supports newer, more powerful 32-bit devices using version 7 of the ARM architecture specification.
- The 64-bit ARM (arm64) port supports the latest 64-bit ARM-powered devices.
  - known in some other places as AArch64.
  - This port was released for the first time with Jessie (Debian 8).
  - 'arm64' is the Debian port name for the 64-bit Armv8 architecture, referred to as 'aarch64' in upstream toolchains (GNU triplet aarch64-linux-gnu), and some other distros.
  - The port was started in 2010 (by Arm and Linaro working with the community in commendable fashion) long before hardware was available so that there would be something to run when it arrived.
  - Hardware started to becoming available in October 2013, but access was restricted. Debian was very kindly donated two 8-core APM machines, installed in March 2014 running two buildds in Debian-ports. One was split with xen so we also had an unofficial porterbox. Arm supplied two Junos in August 2014, and Linaro 3 APM boxes in October, which are the current official build and porter machines.

---

### Reference
- debian ARM Ports, https://www.debian.org/ports/arm/, 2022-08-05-Fri.
