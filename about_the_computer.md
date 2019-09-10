# Computer

## Software

### VPN (Virtual Private Network, 가상사설망)
```
네트워크를 통해 그룹이 내부적으로 통신할 목적으로 사용하는 사설 통신망이다.
```

### Proxy Server (프록시 서버)
```
클라이언트가 다른 네트워크 서비스에 간접적으로 접속할 수 있게 해주는 시스템 또는 프로그램이다.
서버와 클라이언트 사이 중계기로서 대리로 통신하는 것을 '프록시' 중계를 해주는 것을 '프록시 서버'라 한다.
```

### ego-motion vs odometry
```
both can be used interchangeably in general
```
[reference](https://answers.ros.org/question/296686/what-is-the-differences-between-ego-motion-and-odometry/)

#### ego-motion
```
3D motion of a system within an environment
```

#### visual odometry/odometry
```
the estimation of ego-motion using computer vision techniques
```

### http vs https
[reference](https://www.keycdn.com/blog/difference-between-http-and-https)

#### http
```
HyperTxet Trnasfer Protocol 
```

#### https
```
HyperTxet Trnasfer Protocol Secure
also referred to as http over TLS or http over SSL
```

# 'Program Files' versus 'Program Files (x86)'
### 'Program Files' 에는 64-bit program 이, 'Program Files (x86)' 에는 32-bit program 들이 나눠서 설치된다.
```
옛날 컴퓨터는 Intel 의 8086 칩을 사용했는데 처음에는 16-bit 였고 그 이후 32-bit 가 되었다.
따라서 16-bit와 32-bit는 x86 이라 불리고 64-bit 는 x64 라 불린다.
(지금 대부분의 컴퓨터는 16-bit 는 지원하지 않는다.)
현재 컴퓨터는 다양한 칩을 사용하는데 대부분 64-bit 를 지원한다.
32-bit 로 만들어진 응용 프로그램들은 'WOW64 (Windows on Windows 64-bit)' 를 통해 64-bit 에서도 실행이 가능하다.
따라서 Windows 에서는 32-bit 프로그램과 64-bit 프로그램을 섞이지 않고 나눠서 저장하고자 했다.
그래서 'C:/' 에는 'Program Files' 와 'Program Files (x86)' 2개의 폴더에 각각 나눠서 저장하게 설계되었다.
2019-03-21-Thu
```

## Hardware

### HDD (Hard Disk Drive)
#### 'LMR' versus 'PMR' versus 'SMR'
```
LMR(Longitudinal Magnetic Recording)
PMR(Perpendicular Magnetic Recording) by Toshiba
SMR(Shingled Magnetic Recording)
```
#### Low Level Format
```
Record all platters as zero.
```
1) 드라이브 지우기 [about](https://support.wdc.com/knowledgebase/answer.aspx?ID=1211&s=1211&lang=en#windlg)

2) 초기화: GPT선택 [about](https://support.wdc.com/knowledgebase/answer.aspx?ID=1018&s=1018&lang=en#win8)

3) Format: NTFS선택하시고 allocation unit size:4096으로 선택 [about](https://support.wdc.com/knowledgebase/answer.aspx?ID=3865&s=3865&lang=en#win10)

### SSD (Solid State Drive)
#### 'SLC' versus 'MLC' versus 'TLC' versus 'QLC'
```
SLC (Single Level Cell)
MLC (Multi Level Cell)
TLC (Triple Level Cell)
QLC (Quad Level Cell)
```

# Monitor
## Resolution (해상도)
```
VGA: 640 * 480   (Video Graphics Array)
HD : 1280 * 720  (High Definition)
FHD: 1920 * 1080 (Full HD)
QHD: 2560 * 1440 (Quad HD)
UHD: 3840 * 2160 (Ultra HD)
4K : 4096 * 2160
5K : 5120 * 2880
```
```
PPI (Pixel Per Inch)
DPI (Dots Per Inch)
```
```
1080i vs 1080p
```
