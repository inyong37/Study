# Motherboard | [Wiki](https://en.wikipedia.org/wiki/Motherboard)
A motherboard (also called mainboard, main circuit board, system board, baseboard, planar bload, logic board, or mobo) is the main printed circuit board in general purpose computers and other expandable systems. It holds and allows communication between many of the crucial electronic components of a system, and provides connectors for other peripherals. Unlike a backplane, a motherboard usually contains significant sub-systems, such as the central processor, the chipset's input/output and memory controllers, interface connectors, and other components integrated for general use.

# Backplane | [Wiki](https://en.wikipedia.org/wiki/Backplane)
A backplane (or backplane system) is a group of electrical connectors in parallel with each other, so that each pin of each connector is linked to the same relative pin of all the other connectors, forming a computer bus. It is used as a backbone to connect several printed circuit boards together to make up a complete computer system. Backpanes commonly use a printed circuit board, but wire-wrapped backplanes have also been used in minicomputerse and high-reliability applications.

### Motherboard vs. Backplane
A backplane is generally differentiated from a motherboard by the lack of on-board processing and storage elements. A backplane uses plug-in cards for storage and processing.

### Single Board Computer (SBC)

### Jetson Nano vs. Raspberry Pi 4 | [Blog](https://all3dp.com/2/raspberry-pi-vs-jetson-nano-differences/)

The Raspberry Pi was first released all the way back in 2012. With it, you could get into the heart of a computer, by being able to set up an operating system and then connect wires and circuits directly to the pins on the board!

The Pi was designed to teach young people about physical computing and programming. Soon, it became popular with hobbyists and several models and clones have been released since. In June 2019, the Raspberry Pi 4 was released.

On the other hand, NVIDIA had been producing its own line of AI computers for years, but they were priced out of reach for maker projects. This changed with the release of the Jetson Nano in March 2019. Now, it comes in two versions, the 2-GB and 4-GB developer kits, and is one of the most popular boards to compete with the Raspberry Pi.  After all, it comes with a full suite of ports and 40 GPIO pins on a relatively small form.

As you can see, the primary features of the Raspberry Pi 4 and NVIDIA Jetson Nano are similar. But there is one unique distinction. The biggest difference lies in the graphics capabilities between the two boards, specifically their graphical processing units (GPU).

GPUs have been around a long time, since early gaming applications in the 1970s. Later, GPUs were used to accelerate geometric calculations used in machine learning (ML). These days, GPUs are valued in machine learning due to their parallel processing ability.

According to Oracle, GPUs are a safer bet for fast machine learning. This is because at its heart, data science model training is composed of simple matrix math calculations. Therefore, if these computations can be carried out in parallel, the speed of these calculations can be greatly enhanced!

The NVIDIA Jetson Nano has a 128-core Maxwell GPU at 921 MHz. Compared side by side, the Jetson Nano has a much more capable GPU than the Raspberry Pi 4. This makes the Jetson Nano more suitable for AI and ML applications, which could be a specific advantage, depending on your intended end-use.

|Component\Board|Nvidia Jetson Nano|Raspberry Pi 4|
|:-:|:-|:-|
|Processor|The Jetson Nano runs on a quad-core ARM Cortex-A57 64-bit @ 1.42 GHz.|The Raspberry Pi 4 has a Broadcom BCM2711 system-on-chip, and it runs on a 1.5-GHz quad-core 64-bit ARM Cortex-A72 CPU @ 1.5 GHz.|
|Memory|The Jetson Nano comes in a 4-GB LPDDR4 version or a 2-GB alternative.|The Raspberry Pi 4 has four versions for RAM: 1-GB, 2-GB, 4-GB, and 8-GB LPDDR4-2400 SDRAM.|
|Display|The Jetson Nano 4 GB supports HDMI 2.0 and DisplayPort (eDP 1.4). The 2-GB version only supports HDMI 2.0.|Through two micro-HDMI ports, the Raspberry Pi 4 offers 4K 60 fps with dual-screen functionality.|
|I/O|The Jetson Nano 4-GB has four USB 3.0 ports, one USB 2.0 Micro-B port, two MIPI CSI-2 DPHY lanes, an HDMI 2.0 port, and a DisplayPort. The 2-GB model has one USB 3.0 port, two USB 2.0 ports, one USB 2.0 Micro-B port, a MIPI CSI-2 D-PHY lane, and an HDMI 2.0 port.|The Raspberry Pi 4 is equipped with two USB 3.0 ports, two USB 2.0 ports, a USB C port for power, a 3.5-mm analog audio-video jack, two micro-HDMI ports, Camera Serial Interface (CSI), and Display Serial Interface (DSI).
|Ethernet|The Jetson Nano 4 GB supports Gigabit Ethernet and M.2 Key E for Wi-Fi support, while the 2-GB version includes a USB 802.11ac wireless adapter.|The Raspberry Pi 4 supports Gigabit Ethernet. It also has built-in Wi-Fi and Bluetooth functionality.|
|OS|The official operating system for the Jetson Nano is the Linux4Tegra, based on Ubuntu 18.04. This is available via the included SD card image, which is designed to run NVIDIA hardware.|The Raspberry Pi 4 supports Raspberry Pi OS (formerly known as Raspbian), Ubuntu, OSMC, RetroPie, and other third-party images.|
|Price|The Jetson Nano costs around $60 for the 2-GB kit, or about $100 for the 4-GB kit.|The Raspberry Pi 4’s 1-GB and 2-GB variants cost around $35, with the 4-GB version at around $55 and the 8-GB model available for about $75.|

#### Reference
- Motherboard Wiki, https://en.wikipedia.org/wiki/Motherboard, 2021-03-30-Tue.
- Backplane Wiki, https://en.wikipedia.org/wiki/Backplane, 2021-03-30-Tue.
- Jetson Nano vs. Raspberry Pi 4 Blog, https://all3dp.com/2/raspberry-pi-vs-jetson-nano-differences/, 2022-08-02-Tue.
