# Storage

## I. Hard Disk Drive(HDD) | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/%ED%95%98%EB%93%9C_%EB%94%94%EC%8A%A4%ED%81%AC_%EB%93%9C%EB%9D%BC%EC%9D%B4%EB%B8%8C)
HDD(하드 디스크 드라이브/hard disk/hard drive/fixed disk)는 비휘발성, 순차 접근이 가능한 컴퓨터의 보조 기억 장치이다. 보호 케이스 안에 있는 platter를 회전시켜 이것에 자기 패턴으로 정보를 기록한다. 이 platter를 구동시키는 장치는 스팬들 모터로 이루어져있다. 데이터는 platter 표면의 코팅된 자성체에 기록되며 회전하는 platter 위에 부상하는 입출력 헤드에 의해 자기적으로 데이터를 쓰고 읽을 수 있다. HDD는 floppy disk와 같은 자기 기록 매체이나, floppy disk와 다르게 금속 재질의 platter에 데이터를 기록하기 때문에 구분짓기 위해 재질적으로 단단하다는 뜻으로 hard라는 이름이 붙었다. 일반적으로 아직까지는 personal computer의 OS를 담는 용도로 없어서는 안 되는 저장 매체로 많이 쓰이고 있다.

### Platter | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/%ED%95%98%EB%93%9C_%EB%94%94%EC%8A%A4%ED%81%AC_%ED%94%8C%EB%9E%98%ED%84%B0)
Platter는 HDD에서 데이터가 저장되는 원판을 말한다. Platter의 장당 용량은 기록 밀도가 높아질수록 커질 뿐만 아니라, 같은 용량의 데이터를 입출력 하더라도 head가 적게 움직이므로 HDD의 입출력 속도에도 영향을 미친다. 또한 platter의 회전 속도는 HDD의 반응 속도에 영향을 미친다. 대용량의 HDD의 경우 여러 장의 platter를 사용하기도 한다. 하지만 너무 많은 장수의 platter를 장착하면 발열, 소음, 전력 소모, 오작동 등의 문제가 발생하므로 여러 장의 platter를 사용해 고용량을 만드는 방법도 한계가 있다.

HDD의 bad sector 등 오류는 흔히 platter에 발생한 물리적 흠집(스크래치)에 의해 발생한다.

### Longitudinal Magnetic Recording(LMR)
LMR(수평 기록 방식)은 데이터를 저장하는 자기 입자들을 수평으로 배열하므로 만들기 쉽지만 데이터 밀도가 낮아 대용량을 실현하기 어렵다는 단점이 있다.

### Perpendicular Magnetic Recording(PMR)
PMR(수직 기록 방식)은 데이터를 저장하는 자기 입자들을 platter 표면에 수직 방향 배열함으로써 더 높은 데이터 밀도를 실현할 수 있어 작은 면적으로도 더 큰 데이터를 저장할 수 있으며, 오랜 시간이 지나도 자성이 안정되어 있어 수명이 길어 각광받고 있다. 하지만 수직으로 데이터를 기록할 때 생기는 문제인 자화전이점 노이즈와 스파크 노이즈를 해결하기 위해서는 단자극형(single pole type) 기록 헤드를 사용하여 자기 기록층에 수직인 자계를 인가하여 기록하므로, 헤드의 구조가 더욱 복잡해진다. PMR is made by Toshiba.

### Shingled Magnetic Recording(SMR)

### Low Level Format
Record all platters as zero.

1) [드라이브 지우기](https://support.wdc.com/knowledgebase/answer.aspx?ID=1211&s=1211&lang=en#windlg)
2) [초기화: GPT선택](https://support.wdc.com/knowledgebase/answer.aspx?ID=1018&s=1018&lang=en#win8)
3) [Format: NTFS 선택하고 allocation unit size:4096 선택](https://support.wdc.com/knowledgebase/answer.aspx?ID=3865&s=3865&lang=en#win10)

## Floppy Disk | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/%ED%94%8C%EB%A1%9C%ED%94%BC_%EB%94%94%EC%8A%A4%ED%81%AC)
Floppy disk(플로피 디스크) 또는 diskette(디스켓)은 컴퓨터 보조 기억 장치의 일종이다. 컴퓨터에 부착된 floppy disk drive에 넣고 빼면서 사용한다. Diskette은 5.25inch 디스크가 개발되면서 기존의 8inch보다 작다고 하여 floppy disk에 "-ette"의 접미사를 붙인 말이다. 재킷(껍데기) 안에 자성체로 덮여 있는, 회전할 수 있는 원판이 들어 있다. 헤드가 표면과 떨어져있는 HDD와는 달리, floppy disk는 직접 헤드와 맞닿아있다. 그 결과, 데이터와 헤드가 빠르게 닳아버린다. 닳아 없어지는 것을 줄이기 위해서, PC에서는 드라이브가 읽거나 쓰기 않을 때 헤드를 움츠리고 회전을 중지시킨다. 그 다음에 읽거나 쓰는 명령을 받게되면, 멈추었던 모터가 다시 돌아 회전력을 얻기까지 약 0.5초의 지연 시간을 가지게 된다. 이러한 구조 때문에 읽기 쓰기 속도가 HDD보다 느리다.

## OD: Optical Disk | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/%EA%B4%91_%EB%94%94%EC%8A%A4%ED%81%AC)
OD(광 디스크)는 빛의 반사를 이용하여 자료를 읽어내는 저장 매체이다. OD의 효시로는 디지털 방식으로는 음반인 CD가 있고 아날로그 방식으로는 비디오 디스크인 레이저 데스크가 1980년대 초에 개발 완료되어 발매되기 시작하였다. 재기록 가능한 OD로는 자기 방식과 광 방식을 혼합한 광자기 디스크가 1980년대 말에 개발되었고 실용적으로는 1회 기록형 유기광 디스크가 1990년대 초에 개발되었다.

## II. Solid State Drive (SSD)

### Single Level Cell(SLC)

### Multi Level Cell(MLC)

### Triple Level Cell(TLC)

### Quad Level Cell(QLC)

## III. Direct Attached Storage (DAS) | [Wiki](https://en.wikipedia.org/wiki/Direct-attached_storage)
Direct-attached storage (DAS) is digital storage directly attached to the computer accessing it, as opposed to storage accessed over a computer network (i.e. network-attached storage). Examples of DAS include hard drives, solid-state drives, optical disc drives, and storage on external drives. The name "DAS" is a retronym to contrast with storage area network (SAN) and network-attached storage (NAS).

## IV. Network Attached Storage (NAS)

## V. Cloud Storage

### [Google Drive](https://www.google.com/drive/)
 It is made by Google. Google documents, spreadsheets, and presentations are available and are seamlessly compatible with Microsoft Office. Keep photos, documents, designs, pictures, recordings, videos, and more. When you create a Google Account, you get 15 GB of storage for free. Files on your drive can be accessed from your smartphone, tablet, computer, and more, so you can use them anytime, anywhere. Invite others to view, download, and work on files together. Personal; Save and share files and access files from any device. 15GB of free storage is provided for basic storage. For business; Enterprise drives only charge for storage used by employees.[1]

### [OneDrive](https://www.microsoft.com/ko-kr/microsoft-365/onedrive/online-cloud-storage)
 Store files and photos on OneDrive and access them from any device, anywhere. Use your mobile device, tablet, or PC to work anywhere. The file is updated on all devices. Access selected files even when you're not online. There is no problem even if you do not connect to the Internet. If you lose your device, don't worry about losing files and photos stored on OneDrive. Share files, folders and photos with friends and family. You no longer need large email attachments or a USB drive. Just send the link by e-mail or text message.
Create the best work of your life with the latest versions of Word, Excel and other Office apps. OneDrive also offers a variety of features, including 1TB of cloud storage, document sharing, and ransomware recovery.[2]

### [iCloud](https://www.icloud.com/)
 iCloud is built into all Apple devices by default. This means you can keep your precious things, such as photos, files, and notes, up to date, safely, and use them anywhere. Plus, all of this is done automatically, so you just have to keep doing what you like without worrying. By default, 5GB of iCloud storage space is provided to everyone free of charge, and you can easily and easily add it whenever you run out of space.[3]

#### Reference
 1. Google Drive, https://www.google.com/intl/ko_ALL/drive/, 2020-05-05-Tue.
 2. OneDrive, https://www.microsoft.com/ko-kr/microsoft-365/onedrive/online-cloud-storage, 2020-05-05-Tue.
 3. iCloud, https://www.apple.com/kr/icloud/, 2020-05-05-Tue.
- Das Wiki, https://en.wikipedia.org/wiki/Direct-attached_storage, 2020-10-13-Tue.
- HDD Wiki KR-KO, https://ko.wikipedia.org/wiki/%ED%95%98%EB%93%9C_%EB%94%94%EC%8A%A4%ED%81%AC_%EB%93%9C%EB%9D%BC%EC%9D%B4%EB%B8%8C, 2020-11-11-Wed.
- HDD Platter Wiki KR-KO, https://ko.wikipedia.org/wiki/%ED%95%98%EB%93%9C_%EB%94%94%EC%8A%A4%ED%81%AC_%ED%94%8C%EB%9E%98%ED%84%B0, 2020-11-11-Wed.
- Floppy disk Wiki KR-KO, https://ko.wikipedia.org/wiki/%ED%94%8C%EB%A1%9C%ED%94%BC_%EB%94%94%EC%8A%A4%ED%81%AC, 2020-11-11-Wed.
- OD Wiki KR-KO, https://ko.wikipedia.org/wiki/%EA%B4%91_%EB%94%94%EC%8A%A4%ED%81%AC, 2020-11-13-Fri.
