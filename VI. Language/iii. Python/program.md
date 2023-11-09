# Python Program

- Python은 interpreter가 포함되어 사이즈가 커지는 단점이 있어서 binary를 안 만드는 편임
- Windows에서는 py2exe를 이용해 exe 파일을 만듦
- Unix에서는 OS에 포함되어 있기 때문에 만들지 않으며, 만들 경우 freeze를 이용함
- OS에서 사용자가 직접 제어하지 않아도 백그라운드에서 작업을 하는 프로그램
- 메모리에 머무르고 있으면서 요청이 오면 바로 대응을 하는 대기 중인 프로세스
- 데몬이 되는 방식은 자식 프로세스를 fork하여 생성하고 자식을 분기한 자신을 죽이면서 init이 고아가 된 자식 프로세스를 init 밑으로 가져감: fort off and die, 데몬은 부모 프로세스가 없어서 PPID는 1임
- Windows의 service와 유사하며 실제로 service라 부르기도 함
- 데몬 프로그램의 명령어는 d로 끝남; syslogd, ftpd, mysqld, httpd 등
- standalone type daemon:
  - 독립적으로 실행, 요청에 의해 실행되기 때문에 메모리에 항상 대기
- 요청에 대한 응답속도가 빠름, 메모리 효율이 좋지 않음
- “/etc/init.d/”나 “/etc/rc.d/init.d/”에 있는 스크립트 파일로 실행
- super daemon - inetd type daemin (xinetd)
    - super daemon이라는 특별한 데몬에 의해 간접적으로 실행되는 데몬
    - 사용자 요청이 발생할 경우, xinetd 프로그램이 해당 요청을 분석해 필요한 데몬을 메모리에서 실행
        - xinetd는 standalone 방식, 원래는 inetd 였으나 xinetd로 보안상 이유로 변경
    - standalone에 비해 응답속도는 느림, 메모리 효율은 좋음
    - Ubuntu에는 package manager를 통해 설치가 필요함: `sudo apt install netkit-inetd`
    - “/etc/xinetd.d/” 디렉토리의 각 서비스 파일에 등록되어 있는 데몬들이 root로 실행되고 있는지 확인 필요 - 일반 유저의 권한은 실행, 읽기, 쓰기 모두 없어야됨 - 읽기 권한이 있다면 서버에서 어떤 서비스를 하고 있는지 알고 실행 파일의 위치까지도 파악이 가능하기 때문
    - “/etc/xinetd.d/” 내의 파일들에게 쓰기 권한이 설정되어 있다면 어떤 프로그램이든지 만들어서 이 파일에 등록해 두면 root 권한으로 실행이 가능하게 됨
- systemctl, service 모두 기본적으로 데몬 (서비스)를 실행하기 위한 command line임
- daemon 만들기
- {unit}.service 파일을 unit 문법에 맞게 systemd에 생성

```Bash
[Unit]
Description=Sample Service
Requires=local-fs.target
After=local-fs.target

[Service]
Type=simple
PIDFile=/var/run/sample.pid
ExecStart=/usr/sbin/sampled -d
ExecStop=/usr/sbin/sampled -k

[Install]
WantedBy=Multi-user.target
```

- `systemctl enable {unit}` 명령으로 설치 및 컨트롤 할 수 있음
- `service`, `init` 모두 `systemctl`로 리다이렉트됨

---

### Reference
- Linux Python Daemon, https://github.com/HatsuneMiku3939/python3-daemon, 2023-10-10-Tue.
- Executable File (ELF) Binary Program, https://codingdojang.com/scode/272, 2023-10-10-Tue.
- Linux Daemon Blog KR, https://velog.io/@qlgks1/리눅스-데몬Daemon, 2023-10-11-Wed.
- Systemd, https://www.freedesktop.org/wiki/Software/systemd/, 2023-10-11-Wed.
- systemd unit, https://kim-dragon.tistory.com/202, 2023-10-11-Wed.
- subprocess 3.8.17, https://docs.python.org/3.8/library/subprocess.html, 2023-10-16-Mon.
- subprocess Popen Class Blog KR, https://hbase.tistory.com/341, 2023-10-16-Mon.
- subproces Popen method KR, https://wikidocs.net/14350, 2023-10-16-Mon.
