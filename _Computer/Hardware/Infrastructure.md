# :hammer_and_wrench: _Infrastructure_ | [IBM (KR)](https://www.ibm.com/kr-ko/topics/infrastructure) | [Red Hat (KR)](https://www.redhat.com/ko/topics/cloud-computing/what-is-it-infrastructure)

## _Component_

### _Components in IBM_

IT 인프라의 컴포넌트는 상호 종속적인 요소들로 구성되어 있다. 두 개의 핵심 컴포넌트 그룹은 하드웨어와 소프트웨어이다. 하드웨어의 작동을 위해서는 운영 체제 등의 소프트웨어를 사용한다. 운영 체제는 시스템 리소스와 하드웨어를 관리한다. 운영 체제는 네트워킹 컴포넌트를 사용하여 소프트웨어 애플리케이션과 물리적 리소스를 서로 간에 연결한다.

하드웨어:
- 데스크탑 컴퓨터
- 네트워크
  - 스위치
    - 스위치는 라우터, 서버 및 기타 스위치 등 근거리 통신망(LAN)의 네트워크 디바이스를 연결한다.
  - 라우터
    - 라우터를 사용하면 서로 다른 LAN의 디바이스가 통신을 하고 네트워크 간에 패킷을 교환할 수 있다.
  - 허브
    - 허브는 다수의 네트워크 디바이스를 연결함으로써 단일 컴포넌트로서 작동하도록 한다.
  - 서버
    - 엔터프라이즈 IT 인프라에 필요한 핵심 하드웨어 컴포넌트는 서버이다.
    - 서버는 본질적으로 다수의 사용자가 리소스에 액세스하고 이를 공유할 수 있도록 해주는 컴퓨터이다.
- 서버룸/데이터 센터
  - 기업들은 서버 룸 또는 데이터 센터라고 부르는 공간에 다수의 서버를 수용한다.
  - 데이터 센터는 대부분의 네트워크의 핵심이다.
- 설비
  - 설비 또는 실제 시설은 네트워킹 하드웨어, 서버 및 데이터 센터를 위한 공간을 제공한다.
  - 또한 여기에는 IT 인프라의 컴포넌트를 함께 연결하기 위한 사무실 빌딩의 네트워크 케이블링도 포함된다.

소프트웨어:
- 콘텐츠 관리 시스템(CMS)
- 고객 관계 관리(CRM)
- 전사적 자원 관리(ERP)
- 운영 체제
- 웹 서버

최적화:
- 고성능 스토리지 시스템
  - 데이터를 저장 및 백업하며, 장애 시의 데이터 복구 시스템이 포함된다.
- 저지연 네트워크
  - 엔터프라이즈 레벨 인프라 컴포넌트를 사용하여 데이터 플로우의 지연을 줄여준다.
- 보안 인프라
  - 정보 액세스와 데이터 가용성을 통제하는 시스템이 포함된다.
  - 이는 또한 데이터가 상주하는 모든 위치에서 위반과 사이버 공격으로부터 기업을 보호함으로써 고객들의 신뢰를 유지할 수 있다.
- WAN
  - 트래픽의 우선순위를 지정하고 필요에 따라 특정 애플리케이션에 제공되는 대역폭을 가감함으로써 네트워크를 관리한다.
- 가상화
  - 보다 빠른 서버 프로비저닝을 제공하고, 가동 시간을 늘리며, 재해 복구를 향상시키고, 에너지를 절감한다.
- 제로 중단 시간
  - 목적은 비즈니스 운영에 대한 장애를 줄이는 것이며, 이는 시스템 중단 시간을 제거함으로써 비용을 낮추고 수익을 높인다.

### _Components in Red Hat_

하드웨어:
- 서버, 데이터센터, 개인용 컴퓨터, 라우터, 스위치, 기타 장비가 포함된다.
- 데이터센터를 보관하고, 냉각하고, 동력을 공급하는 시설 또한 인프라로 간주될 수 있다.

소프트웨어:
- 웹 서버, 콘텐츠 관리 시스템, Linux와 같은 OS 등 기업에서 사용하는 애플리케이션을 의미한다.
  - OS는 시스템 리소스 및 하드웨어를 관리하며, 애플리케이션과 하드웨어 사이에서 모든 소프트웨어와 작업을 수행하는 물리적 리소스를 연결한다.

네트워킹:
- 네트워크 운영, 관리, 내부 및 외부 시스템 간 커뮤니케이션을 지원한다.
- 인터넷 연결, 네트워크 활성화, 방화벽 및 보안을 비롯해 라우터, 스위치, 케이블 같은 하드웨어로 구성된다.

## _Type_

### _Classic Infra_ | _On-Premises_

일반적으로, 이 인프라 셋업에서는 기타 인프라 유형보다 많은 전력, 물리적 공간 및 비용이 요구된다. 일반적으로, 기존 인프라는 기업 전용 또는 개인용으로 온프레미스에 설치된다.

### _Cloud Infra_ | _Public Cloud_ | _Private Cloud_

가상화를 통해 온프레미스 설치 없이도 컴퓨팅 리소스를 이용하는 기능을 사용하여 인터넷을 통해 인프라에 액세스할 수 있다. 가상화는 임의의 또는 다수의 지리적 위치에서 서비스 제공자가 유지보수하는 물리적 서버들을 연결한다. 그리고 이는 스토리지 등의 리소스를 분할하고 추상화함으로써 인터넷 연결이 가능한 거의 모든 위치에서 사용자가 리소스에 액세스할 수 있도록 해준다. 클라우드 인프라는 대개 공용이므로, 이를 통상적으로 퍼블릭 클라우드라고 한다.

---

### Hardware Development | Infra Engineering | [Naver (KR)](https://recruit.navercorp.com/cnts/tech)

### Hardware

기술을 통해 새로운 물리적 경험을 제공합니다. 자율 주행 로봇, 다관절 로봇 등 완성도 높은 로봇들을 설계하고 개발하며 제작, 실증하는 NAVER LABS HW, 클라우드 서비스의 데이터 트래픽 및 지연 시간을 단축하고 성능을 향상시킬 수 있도록 지원하며 HW 가속화 기술을 적용한 가상화 기술을 연구 개발하는 클라우드 HW가 있습니다.

### Infra Engineering

사용자가 가장 안정적인 서비스를 경험할 수 있는 환경을 구축합니다. 대규모 서버, 스토리지, 네트워크 등의 인프라를 관리하며 프로그램과 서비스의 안정적인 운영을 지원하고, 적합한 솔루션을 제공합니다. 시스템 엔지니어링, 데이터 엔지니어링, 네트워크 엔지니어링, CDN 엔지니어링, 서비스 엔지니어 등의 영역을 포괄합니다.

[무선 네트워크 엔지니어](https://recruit.navercorp.com/rcrt/view.do?annoId=30000281&sw=&subJobCdArr=1030001&sysCompanyCdArr=&empTypeCdArr=&entTypeCdArr=&workAreaCdArr=):
- 역할
  - 무선 네트워크 설계/구축/운영/최적화
  - 무선 단말기 인증 시스템 설계/구축/운영/최적화
- Requirements
  - 무선 네트워크 기술
    - TCP/IP, Switching, Routing 네트워크 인프라에 대한 이해
    - 무선 네트워크 표준 이해
    - 무선 네트워크 주파수 특성 및 전송/변조 기술 관련 지식
    - 대규모 무선 네트워크 설계, 구축 경험
    - 무선 네트워크 품질 관리 & Troubleshooting & 장애대응 경험
  - 네트워크 인증 기술
    - 무선 네트워크 사용자 인증 시스템 구축 경험
  - Preferred
    - Aruba Solution(Controller & AP) 설계, 구축, 운영 경험
    - Aruba Clearpass Solution 구축, 운영 경험
    - 네트워크 자동화 Scripts 활용 능력
    - 무선 관련 자격증

[시스템 엔지니어](https://recruit.navercorp.com/rcrt/view.do?annoId=30000280&sw=&subJobCdArr=1030001&sysCompanyCdArr=&empTypeCdArr=&entTypeCdArr=&workAreaCdArr=):
- 역할
  - 시스템 운영 플랫폼 개발 및 운영
  - 운영 자동화를 위한 아키텍쳐 설계 및 구축
  - 리눅스 기반 시스템 운영 및 트러블슈팅
- Requirements
  - 리눅스 기반 서버 운영 플랫폼 개발 역량
  - CI/CD를 통한 소스 형상관리 기술 (GitHub, Jenkins)
  - 자동화 개발 경험 및 기술 (PHP 혹은 Python, Bash)
  - 시스템 운영 플랫폼 트러블슈팅 및 기술지원
  - 오픈소스를 활용한 다양한 운영 플랫폼 구축 기술
  - 클라우드 관련 요소 기술 (가상화, K8S)
  - 리눅스 시스템 운영 경험 (CentOS, RHEL)
  - Linux OS 구성 및 운영
  - Linux 튜닝 및 트러블슈팅

[Cloud Network Engineering](https://recruit.navercorp.com/rcrt/view.do?annoId=30000733&sw=&subJobCdArr=1030001&sysCompanyCdArr=&empTypeCdArr=&entTypeCdArr=&workAreaCdArr=):
- 역할
  - 상시 운영/서스테이닝
    - 네트워크 이슈에 대한 트러블 슈팅 및 고객 대응
    - 운영 및 정책 가이드 작성 및 배포
    - OS Upgrade 및 H/W Fault 대응
  - 설계/구축/개선
    - 각 종 상품 관련 네트워크 설계/구축/개선
    - VPC 네트워크 설계/구축/개선
    - 네트워크 관련 최신 기술/솔루션 도입
- Requirements
  - TCP/IP, Switching, Routing 네트워크 인프라에 대한 이해
  - IPSec VPN 및 전용회선 서비스에 대한 이해
  - 네트워크 이슈 Troubleshooting & 장애 대응 경험
  - Preferred
    - Cloud 및 네트워크 관련 지식
    - Public Cloud 사용 경험
    - 네트워크 관련 구축/운영 경험
    - MPLS L2/L3 VPN 사용 경험
    - EVPN 사용 경험
    - 패킷 분석 경험
    - Python, Ansible 등 사용 능력

### Data Center Engineering

다양한 서비스가 안정적으로 공급될 수 있도록 데이터센터를 운영하고 지원합니다. 데이터센터와 임대 IDC의 인프라 설비부터 건축/전기/기계/소방/안전 관리까지 다방면의 관리 업무를 수행하며 IT 인프라 구축에 필요한 최적의 환경을 지원합니다.

---

### Reference
- Infrastructure Blog KR, https://velog.io/@yon3115/%EA%B0%9C%EB%B0%9C%EC%9E%90%EC%9D%98-%EA%B8%B0%EB%B3%B8-%EC%9D%B8%ED%94%84%EB%9D%BC-%EB%9E%80, 2022-11-18-Fri.
- Middleware Blog KR, https://velog.io/@unyoi/%EC%9D%B8%ED%94%84%EB%9D%BC-%EB%BF%8C%EC%8B%9C%EA%B8%B01-%EB%AF%B8%EB%93%A4%EC%9B%A8%EC%96%B4-%EA%B0%9C%EB%85%90%EC%9D%84-%EC%95%8C%EC%95%84%EB%B3%B4%EC%9E%90, 2022-11-18-Fri.
- IT 인프라란 IBM KR, https://www.ibm.com/kr-ko/topics/infrastructure, 2022-11-21-Mon.
- IT 인프라란? Red Hat KR, https://www.redhat.com/ko/topics/cloud-computing/what-is-it-infrastructure, 2022-11-21-Mon.
- Hardware Development Infra Engineering Naver KR, https://recruit.navercorp.com/cnts/tech, 2022-11-30-Wed.
- 무선 네트워크 엔지니어 Naver KR, https://recruit.navercorp.com/rcrt/view.do?annoId=30000281&sw=&subJobCdArr=1030001&sysCompanyCdArr=&empTypeCdArr=&entTypeCdArr=&workAreaCdArr=, 2022-11-30-Wed.
- 시스템 엔지니어 Naver KR, https://recruit.navercorp.com/rcrt/view.do?annoId=30000280&sw=&subJobCdArr=1030001&sysCompanyCdArr=&empTypeCdArr=&entTypeCdArr=&workAreaCdArr=, 2022-11-30-Wed.
- Cloud Network Enginerring Naver KR, https://recruit.navercorp.com/rcrt/view.do?annoId=30000733&sw=&subJobCdArr=1030001&sysCompanyCdArr=&empTypeCdArr=&entTypeCdArr=&workAreaCdArr=, 2022-11-30-Wed.
