# I. Ubuntu 18.04.2 LTS (Bionic Beaver)

## i. Install Nvidia Driver
```
$ sudo apt-get purge nvidia*
$ sudo add-apt-reository ppa:graphcs-drivers
$ sudo apt-get update
$ sudo apt-get install screen
$ screen
$ sudo apt-get install nvidia-390
$ sudo reboot
$ lsmod | grep nvidia
$ nvidia-smi
$ dpkg -L nvidia-driver-390
```
Reference: https://www.mvps.net/docs/install-nvidia-drivers-ubuntu-18-04-lts-bionic-beaver-linux/

# II. Ubuntu 16.04.6 LTS (Xenial Xerus)

