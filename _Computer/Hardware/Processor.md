# *Central Processing Unit (CPU)* | [WiKi (KR)](https://ko.wikipedia.org/wiki/%EC%A4%91%EC%95%99_%EC%B2%98%EB%A6%AC_%EC%9E%A5%EC%B9%98)

CPU(중앙 처리 장치)는 컴퓨터 시스템을 통제하고 프로그램의 연산을 실행하고 처리하는 가장 핵심적인 컴퓨터의 제어 장치, 혹은 그 기능을 내장한 칩을 말한다. 컴퓨터 안의 중앙 처리 장치는 외부에서 정보를 입력 받고, 기억하고, 컴퓨터 프로그램의 명령어를 해석하여 연산하고, 외부로 출력하는 역할을 한다. CPU는 컴퓨터 부품과 정보를 교환하면서 컴퓨터 시스템 전체를 제어하는 장치로, 모든 컴퓨터의 작동 과정이 CPU의 제어를 받기 때문에 컴퓨터의 두뇌의 해당한다고 할 수 있다. CPU chip에는 실행 부분뿐만 아니라 캐시 등의 부가 장치가 통합된 경우가 많다. CPU에는 MCU(Micro Control Unit)와 주변 장치(외부 확장 장치에 관한 IC)가 다 들어있는 SoC(System On Chip)가 있다. 주변 IC가 따로 달려 있을 경우에는 MCU이다. CPU의 구성으로는 처리할 명령어를 저장하는 역할을 하는 프로세서 레지스터와 비교, 판단, 연산을 담당하는 산술논리연산장치(ALU), 그리고 명령어의 해석과 올바른 실행을 위하여 CPU를 내부적으로 제어하는 제어부의 내부 버스 등이 있다.

## Micro Processor

Micro processor는 페드리코 페긴이 1970년대에 발명한 것으로, CPU의 설계와 구현에 대한 전반적인 기초를 완전히 바꾸어 놓았다. 최초의 상업용 마이크로프로세스는 1970년에 등장한 Intel 4004, 범용 마이크로프로세서는 1974년의 Intel 8080이다. 각종 전자 부품과 반도체 칩을 하나의 작은 칩에 내장한 전자 부품을 마이크로프로세서라고 한다. 마이크로프로세서는 전기 밥통에 쓰이는 낮은 성능의 저품부터 컴퓨터에 쓰이는 높은 성능의 제품까지 매우 다양하다. 마이크로프로세서들 가운데 가장 복잡하고 성능이 높은 제품은 컴퓨터의 연산 장치로 쓰인다. 이것을 CPU라고 한다.

## System on Chip (SoC) | [Samsung Electronics (KR)](https://www.samsungsemiconstory.com/kr/%EB%B0%98%EB%8F%84%EC%B2%B4-%EC%9A%A9%EC%96%B4-%EC%82%AC%EC%A0%84-soc/)

전체 시스템을 칩 하나에 담은 기술집약적 반도체.

여러 기능을 가진 기기들로 구성된 시스템을 하나의 칩으로 만드는 기술이다. 연산 소자(CPU), 메모리 소자(D램, 플래시 등), 디지털 신호 처리 소자(DSP) 등 주요 반도체 소자를 하나의 칩에 구현해 칩 자체가 하나의 시스템이 되도록 하는 것이다.

즉, PCB(Printed Circuit Board) 상에서 여러 개의 반도체 칩이 모여 구현되던 시스템이 한 개의 칩으로 집적되는 기술을 의미한다.

이렇게 여러 기능을 가진 반도체가 하나의 칩으로 통합되면 칩을 탑재하는 공간이 크게 줄어들어 제품 소형화가 가능하고, 여러 개의 반도체를 별도로 만드는 것 대비 제조 비용이 감소하는 등 여러 장점들이 있다.

## Reduced Instruction Set Computer (RISC) | [WiKi (KR)](https://ko.wikipedia.org/wiki/%EC%B6%95%EC%86%8C_%EB%AA%85%EB%A0%B9%EC%96%B4_%EC%A7%91%ED%95%A9_%EC%BB%B4%ED%93%A8%ED%84%B0)

축소 명령어 집합 컴퓨터(Reduced Instruction Set Computer, RISC, 리스크)는 CPU 명령어의 개수를 줄여 명령어 해석시간을 줄임으로서 명령어 실행속도를 빠르게 한 방식으로, 마이크로프로세서를 설계하는 방법 가운데 하나이며, 주로 신호처리나 실시간제어용으로 설계되며, SPARC, MIPS 등의 아키텍처에서 사용된다.

전통적인 CISC CPU에는 프로그래밍을 돕기 위한 많은 수의 명령어와 주소 모드가 존재했다. 그러나 그중에서 실제로 쓰이는 명령어는 몇 개 되지 않는다는 사실을 바탕으로, 적은 수의 명령어만으로 명령어 집합을 구성한 것이 RISC이다. 그래서, RISC는 CISC보다 구조가 더 단순하다. 복잡한 연산도 적은 수의 명령어들을 조합하는 방식으로 수행이 가능하다.

그리고 CISC 형식의 CPU내 ROM에 소프트웨어적으로 적재된 내부 명령어들을 하드웨어적으로 구성하여 제어기가 제거된 부분에 프로세서 레지스터 뱅크와 캐시를 둔다. 이렇게 함으로써 CPU가, 상대적으로 느린 메인 메모리에 접근하는 횟수를 줄여주어 파이프라이닝 등 시스템 수행속도가 전체적으로 향상된다.

## Microprocessor without Interlocked Pipeline Stages (MIPS) | [WiKi (KR)](https://ko.wikipedia.org/wiki/MIPS_%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98)

MIPS(Microprocessor without Interlocked Pipeline Stages)는 밉스 테크놀로지에서 개발한 RISC ISA이다.

MIPS 디자인은 실리콘 그래픽스 사의 컴퓨터 시스템, 많은 임베디드 시스템과 윈도우 CE 장치, 시스코 시스템즈 라우터에 사용되었다. 그 외에도 소니 플레이스테이션, 닌텐도 64, 플레이스테이션 2, 플레이스테이션 포터블 같은 게임 콘솔에도 사용되었다. 한편 국내에서는 아이스테이션 사의 아이스테이션 T43제품에 쓰인바 있다.

초기 MIPS 아키텍처는 32비트를 사용하였다. 이들은 32비트 레지스터와 데이터 경로를 가지고 있었다. 그 이후의 MIPS 프로세서들은 64비트 구현을 사용하였다. 5종류의 하위 호환성 MIPS 동작 세트가 존재하며, 이들은 각각 MIPS I, MIPS II, MIPS III, MIPS IV, MIPS 32/64라고 불린다. MIPS 32/64 릴리즈 2에서는 동작 세트와 함께 컨트롤 레지스터 셋도 정의하고 있다. MIPS-3D 같은 3차원 그래픽을 위한 SIMD 확장 기능도 존재한다. MDMX(MaDMaX) 확장은 64비트 유동 소수점 레지스터를 활용하는 정수 연산 집합이다. 최근에는 MIPS MT라고 하는 인텔 펜티엄 4 프로세서의 하이퍼스레딩 같은 멀티스레딩 기능이 추가되었다.

MIPS 디자이너들이 명령어 세트를 깔끔하게 설계했기 때문에 많은 대학의 컴퓨터 아키텍처 강좌에서 MIPS 아키텍처를 가르친다. MIPS 프로세서의 디자인은 후기 RISC 아키텍처에 큰 영향을 주었다.

---

## *Application Processor (AP)* | [WiKi (KR)](https://ko.wikipedia.org/wiki/%EB%8B%A8%EC%9D%BC_%EC%B9%A9_%EC%B2%B4%EC%A0%9C#%EC%95%A0%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98_%ED%94%84%EB%A1%9C%EC%84%B8%EC%84%9C)

AP는 PC와 달리 스마트폰, 태블릿에서 명령 해석, 연산, 제어 등 사람의 두뇌 역할을 하는 핵심 부품이다. AP는 CPU와 달리 GPU와 설계에 따라 통신 칩(WiFi, Bluetooth, 3G 등)과 USB와 같은 기능까지 하나의 칩에 포함시켜 놓는 칩셋의 형태로 구성되었기 떄문이다. 칩셋은 SoC라 불리며 CPU, GPU 등 칩 한에 여러 기능을 집적시켜 모든 애플리케이션 구동과 시스템 장치, 여러 인터페이스 장치 등을 제어하고 관장하는 장치로, 부피를 줄이고 전력 소모를 최소화할 수 있게 한손에 들고 다닐 수 있는 초소형의 컴퓨터를 만들 수 있게 되었다고 한다.

## Mobile Application Processor (AP) | [Samsung Electroncis (KR)](https://www.samsungsemiconstory.com/kr/%eb%b0%98%eb%8f%84%ec%b2%b4-%ec%9a%a9%ec%96%b4-%ec%82%ac%ec%a0%84-%eb%aa%a8%eb%b0%94%ec%9d%bc-ap/)

스마트폰, 태블릿 PC와 같은 전자기기에 탑재되어 명령해석, 연산, 제어 등의 두뇌 역할을 하는 시스템 반도체.

일반적으로 PC는 중앙처리장치(CPU), 메모리, 그래픽카드, 하드디스크 등 기타 장비의 연결을 제어하는 칩셋으로 구성된다. 하지만 모바일 AP는 CPU 기능과 다른 장치를 제어하는 칩셋의 기능을 모두 포함한다. 즉, 필요한 OS, application을 구동시키며, 여러 가지 시스템 장치/인터페이스를 컨트롤하는 기능을 하나의 칩에 모두 포함하는 SoC인 것이다.

모바일 AP의 주요 기능은 운영체제 실행, 웹 브라우징, 멀티 터치 스크린 입력 실행 등 스마트 기기의 핵심 기능을 담당하는 CPU와 그래픽과 영상 데이터를 처리해 화면에 표시해주는 GPU 등이 있다.

이외에도 모바일 AP 속에는 비디오 녹화, 카메라 작동, 모바일 게임 실행 등 여러 시스템 구동을 담당하는 많은 서브 프로세서가 있다.

---

### *[Intel](https://www.intel.com/content/www/us/en/homepage.html)* | [WiKi (KR)](https://ko.wikipedia.org/wiki/%EC%9D%B8%ED%85%94)

Intel은 반도체 설계와 제조를 하는 미국의 기업으로, 본사는 캘리포니아 샌타클래라에 있다. Intel은 1968년 7월 18일에 고든 무어와 로버트 노이스가 설립하였고 INTegrated ELectronics의 혼성어이다. 1971년 최초의 마이크로프로세서인 Intel 4004를 만들었으며 이후 만들어진 인텔 8088은 IBM PC에 장착되어 유명해졌다. 이때 만들어진 x86 명령어 아키텍처는 확장을 통해 지금까지 데스크탑 시장에서 널리 쓰이게 되었다. 일반적인 PC는 x86 호환 프로세서를 사용하는 IBM PC 호환기종이다. 이뿐 아니라 메인보드 칩셋, 네트워크 카드, 집접회로, 플래시 메모리, 그래픽 프로세서, 임베디드 프로세서 등의 통신과 컴퓨팅에 관련된 장치도 만든다.

### Intel Xeon Processor | [Homepage](https://www.intel.com/content/www/us/en/products/processors/xeon.html)

### [Intel Xeon Platinum 8180 Processor](https://www.intel.com/content/www/us/en/products/processors/xeon/scalable/platinum-processors/platinum-8180.html) $15,759.99

### Intel Core Processor | [Homepage](https://www.intel.com/content/www/us/en/products/processors/core.html)

### How is a Server Processor Different from a PC Processor? | [Gigabyte](https://www.gigabyte.com/Article/server-processors-the-core-of-a-server-s-performance)

### *[AMD](https://www.amd.com/en)* | [WiKi (KR)](https://ko.wikipedia.org/wiki/%EC%96%B4%EB%93%9C%EB%B0%B4%EC%8A%A4%ED%8A%B8_%EB%A7%88%EC%9D%B4%ED%81%AC%EB%A1%9C_%EB%94%94%EB%B0%94%EC%9D%B4%EC%8B%9C%EC%8A%A4)

AMD(Advanced Micro Devices)는 미국의 집적회로 제조사로 캘리포니아 산타클라라 카운티 서니베일에 위치해있다. Intel에 이어 2번째로 큰 x86 아키텍처 호환 프로세스 제조사이며 플래시 메모리 분야에서도 주도적인 위치에 있다. AMD가 ATI를 2006년에 합병한 이후 GPU 시장에서도 높은 점유율을 차지하고 있다. AMD는 제리 샌더스가 1969년 5월 1일에 페어차일드 반도체의 동료들 중 7명과 함께 설립하였다.

### AMD Ryzen Desktop Processor | [Homepage](https://www.amd.com/en/processors/ryzen) | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/%EB%9D%BC%EC%9D%B4%EC%A0%A0)

Ryzen은 젠과 젠 플러스와 젠 2 아키텍처를 기반으로 하여 AMD가 제조하는 컴퓨터 마이크로프로세서 시리즈에 적용하는 브랜드 이름이다. 젠으로 구동되는 라이젠 프로세서들은 데이터 센터나 서버에 목표를 두지 않고 고성능 데스크탑(HEDT), 저전력 컴퓨팅을 지향하는 랩탑 탑재용 모바일 프로세서 ㅣ장을 목표한다. Ryzen은 Intel의 Core 시리즈에 대응한다.

### ARM: Advanced/Acorn RISC Machine | [Homepage](https://www.arm.com) | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/ARM_아키텍처)
ARM architecture은 임베디드 기기에 많이 사용되는 RISC processor이다. 저전력을 사용하도록 설계하여 arm CPU는 모바일 시장 및 싱글 보드 컴퓨터로 불리는 개인용 컴퓨터에서 뚜렷한 강세를 보인다. arm은 1985년 4월 26일 영국의 캠브릿지에 있는 Acorn Computers에 의해서 탄생되었으며, 1990년 11월 Apple과 VLSI의 조인트 벤처 형식으로 ARM(Advanced RISC Machines)가 생겼다.

### Qualcomm Snapdragon

### Samsung Electronics Exynos

### Apple A

### Freescale Semiconductor i.MX

### Nvidia Tegra

### Intel Atom

### LG Electronics NUCLUN

---

## *Graphics Processing Unit (GPU)* | Videa Graphics Array (VGA)

### [Nvidia](https://www.nvidia.com/en-us/)

### [AMD](https://www.amd.com/en) (takeover ATI)

---

## General Purpose Graphics Processing Unit (GPGPU)

---

## Tensor Procssing Unit (TPU)

### [Google](https://cloud.google.com/tpu)

---

## Nueral Processing Unit (NPU)

---

## PowerPC | [WiKi (KR)](https://ko.wikipedia.org/wiki/%ED%8C%8C%EC%9B%8CPC)

파워PC(PowerPC, Performance Optimization With Enhanced RISC – Performance Computing의 약어, 간단히 PPC)는 1991년 애플, IBM, 모토로라 등이 제휴한 AIM 연합에서 발표한 RISC 방식의 명령 집합 아키텍처(Instruction Set Architecture)를 말한다. PowerPC 명령 집합은 지속적으로 진화하고 있으며, 2006년에 Power ISA로 이름을 바꾸었으나, 그 이후에도 파워PC는 파워 아키텍처 기반의 몇몇 프로세서를 통칭하는 명칭으로 사용되고 있다.

파워PC 아키텍처 자체는 동작의 기본이 되는 명령 집합이나 레지스터 집합, 메모리 어드레싱, 캐시 모델 등을 규정하고 있지만 이들의 구현 방법에 대한 규정은 없다. 그러므로 극단적으로 파워 피씨 아키텍처에서 내부적으로 CISC 또는 소프트웨어를 구현해도 파워 피씨 프로세서라고 부를 수 있다. 이러한 특징으로 실제로 제조되는 모델은 고속화를 위해서 아키텍처 수준에서는 규정되어 있지 않은 부품(2차, 3차 캐시나 관련 레지스터 등)을 갖추고 있는 것이 보통이다.

원래는 AIM(애플, IBM, 모토로라) 플랫폼의 CPU가 이런 의미로 개발된 것이지만, CPU 말고는 개발된 것이 없으므로 오늘날까지 남아 있는 파워피씨 계열 프로젝트의 유일한 성과물이기도 하다. 파워피씨는 애플 컴퓨터사의 파워맥에 사용되었다. 그 밖에는 IBM의 일부 워크스테이션, 서버나 BlueGene/L뿐만 아니라 슈퍼 컴퓨터에도 사용된다.

또한 기판 크기가 작고 소비 전력이 낮으며 자일링스 FPGA용 IP 코어도 제공한다. 현재는 모토로라에서 분리된 프리스케일 세미컨덕터와 IBM에서 개발하여 제조하고 있다.

---

### Reference
- CPU Wiki KR-KO, https://ko.wikipedia.org/wiki/%EC%A4%91%EC%95%99_%EC%B2%98%EB%A6%AC_%EC%9E%A5%EC%B9%98, 2020-11-07-Sat.
- Intel, https://www.intel.com/content/www/us/en/homepage.html, 2020-11-07-Sat.
- Intel Xeon Processor, https://www.intel.com/content/www/us/en/products/processors/xeon.html, 2020-11-07-Sat.
- Intel Core Processor, https://www.intel.com/content/www/us/en/products/processors/core.html, 2020-11-07-Sat.
- Intel Wiki KR-KO, https://ko.wikipedia.org/wiki/%EC%9D%B8%ED%85%94, 2020-11-07-Sat.
- AMD, https://www.amd.com/en, 2020-11-07-Sat.
- AMD Wiki KR-KO, https://ko.wikipedia.org/wiki/%EC%96%B4%EB%93%9C%EB%B0%B4%EC%8A%A4%ED%8A%B8_%EB%A7%88%EC%9D%B4%ED%81%AC%EB%A1%9C_%EB%94%94%EB%B0%94%EC%9D%B4%EC%8B%9C%EC%8A%A4, 2020-11-07-Sat.
- AMD Ryzen Processor, https://www.amd.com/en/processors/ryzen, 2020-11-07-Sat.
- AMD Ryzen Processor Wiki KR-KO, https://ko.wikipedia.org/wiki/%EB%9D%BC%EC%9D%B4%EC%A0%A0, 2020-11-07-Sat.
- AP Wiki KR-KO, https://ko.wikipedia.org/wiki/%EB%8B%A8%EC%9D%BC_%EC%B9%A9_%EC%B2%B4%EC%A0%9C#%EC%95%A0%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98_%ED%94%84%EB%A1%9C%EC%84%B8%EC%84%9C, 2020-11-08-Sun.
- ARM Wiki KR-KO, https://ko.wikipedia.org/wiki/ARM_아키텍처, 2020-11-09-Mon.
- ARM, https://www.arm.com,, 2020-11-09-Mon.
- SoC Samsung Electronics KR, https://www.samsungsemiconstory.com/kr/%EB%B0%98%EB%8F%84%EC%B2%B4-%EC%9A%A9%EC%96%B4-%EC%82%AC%EC%A0%84-soc/, 2022-07-25-Mon.
- Mobile AP Samsung Electronics KR, https://www.samsungsemiconstory.com/kr/%eb%b0%98%eb%8f%84%ec%b2%b4-%ec%9a%a9%ec%96%b4-%ec%82%ac%ec%a0%84-%eb%aa%a8%eb%b0%94%ec%9d%bc-ap/, 2022-07-25-Mon.
- armel vs. armhf vs. arm64 Blog, https://ciksiti.com/ko/chapters/3066-difference-between-arm64-armel-and-armhf--linux-hint, 2022-08-02-Tue.
- Nvidia, https://www.nvidia.com/en-us/, 2022-08-05-Fri.
- Google Cloud TPU, https://cloud.google.com/tpu, 2022-08-05-Fri.
- RISC WiKi KR, https://ko.wikipedia.org/wiki/%EC%B6%95%EC%86%8C_%EB%AA%85%EB%A0%B9%EC%96%B4_%EC%A7%91%ED%95%A9_%EC%BB%B4%ED%93%A8%ED%84%B0, 2022-08-05-Fri.
- MIPS WiKi KR, https://ko.wikipedia.org/wiki/MIPS_%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98, 2022-08-05-Fri.
- PowerPC Wiki KR, https://ko.wikipedia.org/wiki/%ED%8C%8C%EC%9B%8CPC, 
- How is a Server Processor Different from a PC Processor? Gigabyte, https://www.gigabyte.com/Article/server-processors-the-core-of-a-server-s-performance, 2022-11-03-Thu.
- 
