# :package: Storage

## :package: Direct Attached Storage (DAS) | [WiKi](https://en.wikipedia.org/wiki/Direct-attached_storage)

Direct-attached storage (DAS) is digital storage directly attached to the computer accessing it, as opposed to storage accessed over a computer network (i.e. network-attached storage). Examples of DAS include hard drives, solid-state drives, optical disc drives, and storage on external drives. The name "DAS" is a retronym to contrast with storage area network (SAN) and network-attached storage (NAS).

## :cloud: Network Attached Storage (NAS)

## :cloud: Cloud Storage

`Cloud Storage is related with the 'Cloud' page.`

### [Google Drive](https://www.google.com/drive/)

It is made by Google. Google documents, spreadsheets, and presentations are available and are seamlessly compatible with Microsoft Office. Keep photos, documents, designs, pictures, recordings, videos, and more. When you create a Google Account, you get 15 GB of storage for free. Files on your drive can be accessed from your smartphone, tablet, computer, and more, so you can use them anytime, anywhere. Invite others to view, download, and work on files together. Personal; Save and share files and access files from any device. 15GB of free storage is provided for basic storage. For business; Enterprise drives only charge for storage used by employees.

### [Microsoft OneDrive](https://www.microsoft.com/ko-kr/microsoft-365/onedrive/online-cloud-storage)

Store files and photos on OneDrive and access them from any device, anywhere. Use your mobile device, tablet, or PC to work anywhere. The file is updated on all devices. Access selected files even when you're not online. There is no problem even if you do not connect to the Internet. If you lose your device, don't worry about losing files and photos stored on OneDrive. Share files, folders and photos with friends and family. You no longer need large email attachments or a USB drive. Just send the link by e-mail or text message.
Create the best work of your life with the latest versions of Word, Excel and other Office apps. OneDrive also offers a variety of features, including 1TB of cloud storage, document sharing, and ransomware recovery.

### [Apple iCloud](https://www.icloud.com/)

iCloud is built into all Apple devices by default. This means you can keep your precious things, such as photos, files, and notes, up to date, safely, and use them anywhere. Plus, all of this is done automatically, so you just have to keep doing what you like without worrying. By default, 5GB of iCloud storage space is provided to everyone free of charge, and you can easily and easily add it whenever you run out of space.
 
### [Naver Ndrive](https://ndrive.naver.com/) -> [Naver Cloud MyBOX](https://mybox.naver.com/)

### Daum Drive -> [Daum 'Cloud' Deprecated](https://cs.daum.net/faq/304/17063.html#34360)

## :package: File System

`This part is from the 'Software/Network' page.`

### [Common Internet File System (CIFS)](https://cifs.com/)

Common Internet File System (CIFS) is a network filesystem protocol used for providing shared access to files and printers between machines on the network. A CIFS client application can read, write, edit and even remove files on the remote server. CIFS client can communicate with any server that is set up to receive a CIFS client request. Microsoft implementations are the de facto CIFS standards. As Wikipedia indicates, the CIPS protocol was developed back in the 1980's by Barry Feigenbaum at IBM. Then known as Server Message Block (SMB). SMB was originally designed to run top of the NetBIOS / NetBEUI API (typically implemented with NBF, NetBIOS over IPX/SPX, or NBT) with the aim of tuning local file access to network file system.

With the release of Windows 95 in the early 1990’s, Microsoft has made considerable modifications to the most commonly used SMB version. Microsoft then merged the updated version of the SMB protocol (and rebranded it as CIFS) with the LAN Manager product bringing both client and server support. This application (CIFS) helps a client make a specific request and server responds according to needs hence exchange data with authenticated computers. However, over years there have been several usage models where CIFS was initially for file sharing and later has been used for network management and other network services - with networks becoming larger the need for privilege separation and scale of use.

Over time CIFS has had various versions to facilitate usage for various operating systems:
- DOS: This is case where the original model was simply for file-sharing in a NETBIOS- environment and this basically worked by specifying the directories list to be shared and name to be shared under and eventually one sets up a password per share.
- Windows NT: A concept of grouping computers into domains was developed. Such terms as DC (Domain Controller), PDC (Primary Domain Controller) and Domain Membership were first introduced.
- Windows 2000: This came as the first operating system that came with a support for Active Directory. This was implemented using modified open protocols. Active domain means there are now central points of authority and there are fewer limits to the domain size e.g., - several domains can exist.
- CIFS / SMB1.0 is used in Windows 2000, Windows XP, Windows Server 2003 and Windows Server 2002 R2. Its redesign to SMB 2.0 has increased the scale of sharing files, boosting performance for compounding request, enhancing larger reads and writes, has become more secure and robust in case of small command setting and that its signature uses HMACSHA-256 instead of MD5. Since the change was radical and Microsoft had to change the concept users had on the buggy CIFS it was decided to drop the name CIFS, and rename it SMB2.
- SMB 2.0 which was integrated in Windows Vista and Windows Server 2008 was much more durable. Its redesign to SMB2.1 in Windows 7 and Windows Server 2008 R2 made improvements in file leasing, ensured large MTU support and Branch Cache.
- SMB 3.0 version is commonly used with Windows 8 and Windows Server 2012, granting SMB multi-channeling, SMBDirect, witnessing and transparent failover that improved performance and scaling-out. It still has more features for back-up, security and management, for SQL Server, Power Shell and others. It also introduces several security enhancements, such as end-to-end encryption and a new AES based signing algorithm. In Windows 8.1 and Windows Server 2012 R2 the SMB 3.02 was implemented where Microsoft introduced the option to completely disable CIFS/SMB1 support, including the actual removal of the related binaries. While this is not the default configuration, MS recommend disabling this older version of the protocol in scenarios where it is useless, like Hyper-V over SMB.
- SMB 3.1.1 was introduced with Windows 10 and Windows Server 2016. This version supports AES-128-GCM encryption in addition to existing AES-128-CCM encryption and implements pre-authentication integrity check using SHA-512 hash. SMB 3.1.1 also makes secure negotiation mandatory when connecting to clients using SMB 2.x and higher.

### [Samba](https://www.samba.org/)

Samba is the standard Windows interoperability suite of programs for Linux and Unix.

Since 1992, Samba has provided secure, stable and fast file print services for all clients using the SMB/CIFS protocol, such as all versions of DOS and Windows, OS/2. Linux and many others.

### [Network File System (NFS)](https://www.ibm.com/docs/en/aix/7.1?topic=management-network-file-system)

The Network File System (NFS) is a mechanism for storing files on a network. It is a distributed file system that allows users to access files and directories located on remote computers and treat those files and directories as if they were local.

### [iSCSI](https://www.ibm.com/docs/en/spectrumvirtualsoftw/8.2.x?topic=planning-iscsi-overview)

iSCSI is an IP-based standard for transferring data that supports host access by carrying SCSI commands over IP networks.

[NFS vs iSCSI - What's the Difference? (Pros and Cons](https://cloudinfrastructureservices.co.uk/nfs-vs-iscsi-whats-the-difference/)

[iSCSI와 NAS 차이점?](https://www.2cpu.co.kr/QnA/346155)

### [Ceph File System (CephFS)](https://docs.ceph.com/en/quincy/cephfs/index.html)

The Ceph File System (CephFS) is a file system compatible with POSIX standards that uses a Ceph Storage Cluster to store its data. The Ceph File System uses the same Ceph Storage Cluster system as the Ceph Block Device, Ceph Object Gateway, or `librados` API.

[쿠버네티스에서 Ceph dashboard, CephFS 설치해 본 후기](https://mokpolar.tistory.com/10): NFS와 달리 다른 pods에서 share가 가능하다.

---

### Reference
- Google Drive, https://www.google.com/intl/ko_ALL/drive/, 2020-05-05-Tue.
- OneDrive, https://www.microsoft.com/ko-kr/microsoft-365/onedrive/online-cloud-storage, 2020-05-05-Tue.
- iCloud, https://www.apple.com/kr/icloud/, 2020-05-05-Tue.
- Das Wiki, https://en.wikipedia.org/wiki/Direct-attached_storage, 2020-10-13-Tue.
- NFS vs iSCSI - What's the Difference? (Pros and Cons, https://cloudinfrastructureservices.co.uk/nfs-vs-iscsi-whats-the-difference/, 2023-01-11-Wed.
- iSCSI와 NAS 차이점?, https://www.2cpu.co.kr/QnA/346155, 2023-01-11-Wed.
- CephFS, https://docs.ceph.com/en/quincy/cephfs/index.html, 2023-01-11-Wed.
- Ndrive, https://ndrive.naver.com/, 2023-01-12-Thu.
- Naver Cloud MyBOX, https://mybox.naver.com/, 2023-01-12-Thu.
- Daum Drive Cloud Deprecated, https://cs.daum.net/faq/304/17063.html#34360, 2023-01-12-Thu.
- What is the Ceph File System (CephFS)?, https://access.redhat.com/documentation/en-us/red_hat_ceph_storage/2/html/ceph_file_system_guide_technology_preview/what_is_the_ceph_file_system_cephfs, 2023-01-11-Thu.
- CIFS, https://cifs.com/, 2022-11-07-Mon.
- Samba, https://www.samba.org/, 2022-11-07-Mon.
- NFS IBM, https://www.ibm.com/docs/en/aix/7.1?topic=management-network-file-system, 2022-11-07-Mon.
- iSCSI IBM, https://www.ibm.com/docs/en/spectrumvirtualsoftw/8.2.x?topic=planning-iscsi-overview, 2023-01-12-Thu.
- 쿠버네티스에서 Ceph dashboard, CephFS 설치해 본 후기, https://mokpolar.tistory.com/10, 2023-01-12-Thu.
