# Colab
## I. Tutorial
[welcome.ipynb](https://colab.research.google.com/notebooks/welcome.ipynb)

## II. Google Drive
### i. import and attach
```
from google.colab import drive
drive.mount('/content/drive/')
```
### ii. check directory
```
!ls '/content/drive/My Drive/'
!ls '/content/drive/My Drive/PUBLIC/GITHUB/Study/Book/C. Korean/실전 예제로 배우는 GAN/'
```

## III. Check Environment
### i. check development environment
[IN]
```
import platform
print(platform.platform())
!python --version # python version
import tensorflow as tf # tensorflow version
print('TensorFlow', tf.__version__)
import keras
print('Keras', keras.__version__)
import torch
print('Torch', torch.__version__)
```
[OUT]
```
Linux-4.14.79+-x86_64-with-Ubuntu-18.04-bionic
Python 3.6.7
TensorFlow 1.13.1
Keras 2.2.4
Using TensorFlow backend.
Torch 1.1.0
```
### ii. check system environment
[IN]
```
!cat /etc/issue.net # os
!cat /proc/cpuinfo # cpu information
!cat /proc/meminfo # memory information
!nvidia-smi # gpu
!df -h # storage
```
[OUT]
```
Ubuntu 18.04.2 LTS
processor	: 0
vendor_id	: GenuineIntel
cpu family	: 6
model		: 63
model name	: Intel(R) Xeon(R) CPU @ 2.30GHz
stepping	: 0
microcode	: 0x1
cpu MHz		: 2300.000
cache size	: 46080 KB
physical id	: 0
siblings	: 2
core id		: 0
cpu cores	: 1
apicid		: 0
initial apicid	: 0
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss ht syscall nx pdpe1gb rdtscp lm constant_tsc rep_good nopl xtopology nonstop_tsc cpuid tsc_known_freq pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx f16c rdrand hypervisor lahf_lm abm invpcid_single pti ssbd ibrs ibpb stibp fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid xsaveopt arat arch_capabilities
bugs		: cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass l1tf
bogomips	: 4600.00
clflush size	: 64
cache_alignment	: 64
address sizes	: 46 bits physical, 48 bits virtual
power management:

processor	: 1
vendor_id	: GenuineIntel
cpu family	: 6
model		: 63
model name	: Intel(R) Xeon(R) CPU @ 2.30GHz
stepping	: 0
microcode	: 0x1
cpu MHz		: 2300.000
cache size	: 46080 KB
physical id	: 0
siblings	: 2
core id		: 0
cpu cores	: 1
apicid		: 1
initial apicid	: 1
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss ht syscall nx pdpe1gb rdtscp lm constant_tsc rep_good nopl xtopology nonstop_tsc cpuid tsc_known_freq pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx f16c rdrand hypervisor lahf_lm abm invpcid_single pti ssbd ibrs ibpb stibp fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid xsaveopt arat arch_capabilities
bugs		: cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass l1tf
bogomips	: 4600.00
clflush size	: 64
cache_alignment	: 64
address sizes	: 46 bits physical, 48 bits virtual
power management:

MemTotal:       13335276 kB
MemFree:        10774664 kB
MemAvailable:   12554852 kB
Buffers:           69584 kB
Cached:          1864592 kB
SwapCached:            0 kB
Active:           724952 kB
Inactive:        1575972 kB
Active(anon):     337116 kB
Inactive(anon):      356 kB
Active(file):     387836 kB
Inactive(file):  1575616 kB
Unevictable:           0 kB
Mlocked:               0 kB
SwapTotal:             0 kB
SwapFree:              0 kB
Dirty:               412 kB
Writeback:             0 kB
AnonPages:        366604 kB
Mapped:           335500 kB
Shmem:               912 kB
Slab:             148172 kB
SReclaimable:     115676 kB
SUnreclaim:        32496 kB
KernelStack:        3820 kB
PageTables:         5836 kB
NFS_Unstable:          0 kB
Bounce:                0 kB
WritebackTmp:          0 kB
CommitLimit:     6667636 kB
Committed_AS:    1907172 kB
VmallocTotal:   34359738367 kB
VmallocUsed:           0 kB
VmallocChunk:          0 kB
AnonHugePages:         0 kB
ShmemHugePages:        0 kB
ShmemPmdMapped:        0 kB
HugePages_Total:       0
HugePages_Free:        0
HugePages_Rsvd:        0
HugePages_Surp:        0
Hugepagesize:       2048 kB
DirectMap4k:       98292 kB
DirectMap2M:     5144576 kB
DirectMap1G:    10485760 kB
Wed Jun  5 00:43:19 2019       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 418.67       Driver Version: 410.79       CUDA Version: 10.0     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  Tesla T4            Off  | 00000000:00:04.0 Off |                    0 |
| N/A   54C    P8    16W /  70W |      0MiB / 15079MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
Filesystem      Size  Used Avail Use% Mounted on
overlay         359G   25G  316G   8% /
tmpfs           6.4G     0  6.4G   0% /dev
tmpfs           6.4G     0  6.4G   0% /sys/fs/cgroup
tmpfs           6.4G   12K  6.4G   1% /var/colab
/dev/sda1       365G   30G  336G   9% /opt/bin
shm             6.0G  4.0K  6.0G   1% /dev/shm
tmpfs           6.4G     0  6.4G   0% /sys/firmware
```
## IV. Others
Keras [Reference](https://yamalab.tistory.com/80)

## V. Annotation
```
# -*- coding: utf-8 -*-
# Author: Inyong Hwang (inyong1020@gmail.com)
# Date: *-*-*-*
# Code Explanation
```
