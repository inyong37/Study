# RAM: Random Access Memory | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/%EB%9E%9C%EB%8D%A4_%EC%95%A1%EC%84%B8%EC%8A%A4_%EB%A9%94%EB%AA%A8%EB%A6%AC)
RAM(임의 접근 기억 장치)은 임의의 영역에 접근하여 읽고 쓰기가 가능한 주기억 장치이다. 반도체 회로로 구성되어 있으며 휘발성 메모리이다. 흔히 RAM을 "읽고 쓸 수 있는 메모리"라는 뜻으로 알고 있는데 이것은 오해다. RAM은 어느 위치에 저장되 데이터든지 접근(읽기 및 쓰기)하는 데 동일한 시간이 거리는 메모리이기에 random(무작위)이다. 반면 HDD 등의 자기 디스크나 자기 테이프는 저장된 위치에 따라 접근하는 데 시간이 다르게 걸린다.

### Parity

### ECC: Error Correcting Code

### SRAM: Static RAM | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/%EC%A0%95%EC%A0%81_%EB%9E%A8)
SRAM(정적 막기억장치)는 반도체 기억 장치의 한 종류로 주기적으로 내용을 갱신해 주어야하는 DRAM과 달리 기억 장치에 전원이 공급되는 한 그 내용이 계속 보존된다. SRAM은 RAM이므로 데이터의 쓰고 읽기가 이루어지는 주소와 관계없이 입출력에 걸리는 시간이 일정하다. SRAM은 DRAM의 일종인 SDRAM과 전혀 다른 기억 소자이다. SRAM에서 각각의 비트들은 4개의 transistor로 이루어진 2쌍의 inverter에 저장된다. 2쌍의 inverter가 1과 0의 값을 안정된 상태로 유지하고 2개의 접근 transistor가 읽기와 쓰기 기능을 수행한다. 따라서 1개의 비트를 저장하기 위해 일반적으로 8개의 transistor를 필요로 한다. SRAM은 회로의 대칭 구조로 인해 DRAM보다 훨씬 빠른 입출력을 가능하게 한다. 또한 메모리 주소에 접근할 때 상위 비트와 하위 비트 순서로 2번 접근해야 하는 DRAM과 달리 SRAM은 한번에 접근할 수 있는 장점이 있다.

### DRAM: Dynamic RAM | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/%EB%8F%99%EC%A0%81_%EB%9E%A8)
DRAM(동적 막기억장치)는 RAM의 한 종류로 정보를 구성하는 개개의 비트를 각기 분리된 capacitor에 저장하는 기억 장치이다. 각각의 capacitor가 담고 있는 전자의 수의 따라 비트의 1과 0을 나타내지만 결국 capacitor가 전자를 누전하므로 기억된 정보를 잃게 된다. 이를 방지하기 위해 기억 장치의 내용을 일정 시간마다 재생시켜야 되는 것을 일컬어 dynamic이란 명칭이 주어졌다. 정보를 유지하려면 지속적인 전기 공급이 필요하기 때문에 DRAM은 휘발성 기억 장치(volatile memory)에 속한다.

### SDRAM: Synchronous DRAM | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/SDRAM)
SDRAM은 DRAM의 발전된 형태로, 보통 DRAM과는 달리 제어 장치 입력을 clock pulse와 동시에 일어나도록 하는 동기식 DRAM이다. SDRAM은 DDR SDRAM의 보급으로 SDR SDRAM이라는 관례적인 명칭이 주어졌따. SDR은 Single Data Rate의 약자이다. 이 의미는 기존의 SDRAM이 각 pusle clock이 상승 또는 하강하는 시점에서 한번만 정보를 전송하는 것에서 나온 명칭이다.

### SDR SDRAM: Single Data Rate SDRAM

### DDR SDRAM: Double Data Rate SDRAM

### GDDR SDRAM: Graphics Double Data Rate SDRAM

# ROM: Read Only Memory | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/%EA%B3%A0%EC%A0%95_%EA%B8%B0%EC%96%B5_%EC%9E%A5%EC%B9%98)
ROM(고정 기억 장치)는 반도체 기억 장치의 하나로 사람의 본능에 비유할 수 있으며, 컴퓨터를 구동하기 위한 기본적인 정보가 담겨있고 그 정보들을 기억하기 위해 다른 정보들은 기억하지 않는다. ROM은 RAM과 달리 자유롭게 읽고 쓰기가 어려우며, 전원을 꺼도 데이터가 지워지지 않기 때문에 BIOS, UEFI, OS, firmware의 저장에 사용되었다. 최근에는 일부분이 읽고 쓰기가 가능한 flash memory 등으로 일부 대체되었다. ROM은 ROM writer로 수정이 가능하다. ROM은 1956년에 PROM이 발명되었고, 1971년에 EPROM이 발명되었으며, 1983년 EEPROM이 발명되었고, 1980년대 중반에는 Toshiba가 flash memory를 발명하여 1990년대 초에 상용화하였으며 이는 EEPROM의 일종으로 손상을 일으키지 않고 수천번이나 삭제와 재프로그래밍을 가능하게 하였다. 가장 최근 방식은 NAND flash 이며 이또한 Toshiba가 발명하였다.

### EPROM: Erasable PROM | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/EPROM)
EPROM(Erasable PROM)은 필요할 때 기억된 내용을 지우고 다른 내용을 기록할 수 있는 ROM이다. 지우는 방법에 따라 자외선으로 지울 수 있는 UVEPROM(Ultra-Violet Erasable Programmable Read Only Memory)과 높은 전압으로 지울 수 있는 EEPROM(Electrically Erasble Programmable Read Only Memory)로 나뉜다. 하지만 EPROM은 일반적으로 UVEPROM을 가리킨다. UVEPROM은 1971년 Intel의 Dov Frohman이 발명했으며 최초의 제품은 Intel 1702A이다. 기록은 floating-gate 트랜지스터에 고전압(12V)으로 전자를 주입하여 기록하며 플로팅 게이트는 절연되어 있어서 전원을 꺼도 전자는 보존되어 ROM으로 사용할 수 있다. 그러나 강한 자외선(234nm)을 쬐게되면 전자는 게이트의 절연막을 통과해 기록이 지워지게 된다. 보통 UVEPROM에는 석영유리창이 있어 다른 ROM과는 확연히 구분한다. 기록횟수는 고전압이 실리콘에 영향을 주기 때문에 20회 전후이며 차광 씰을 잘 부착하여 최적으로 보관한다면 약 10년 정도 데이터 보관이 가능하다. UVEPROM은 과거 메인보드, 그래픽카드의 BIOS chip이나 게임기의 ROM으로 많이 사용되었다. 그리고 칩 패키지에서 창을 없앤 UVEPROM을 OTP(One Time Programmable)라고 하는데 소거창이 없기 떄문에 한번 기록 후 지울 수 없으며 주로 마이크로컨트롤러에서 볼 수 있다.

# Flash Memory | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/%ED%94%8C%EB%9E%98%EC%8B%9C_%EB%A9%94%EB%AA%A8%EB%A6%AC)
Flash memory(전기 일괄소거형 기억기)는 전기적으로 데이터를 지우고 다시 기록할 수 있는 비휘발성 컴퓨터 기억 장치이다.(Electrically erased and reprogrammed) Flash memory는 EEPROM과 다르게 여러 구역으로 구성된 블록 안에서 지우고 쓸 수 있다. 이제는 flash memory의 가격이 EEPROM보다 훨씬 싸기 때문에 비휘발성 고체 상태(Solid State) 저장 매체가 상당량 필요한 곳에서는 가장 많이 사용되는 메모리 종류가 되었다. USB drive에도 flash memory가 사용된다. 옛날 게임팩으로는 EEPROM으로 만들었으나 요즘은 flash memory가 주로 사용되고 있다. Flash memory는 메모리 칩 안에 정보를 유지시키는데 전력이 필요 없는 비휘발성 메모리이다. Flash memory는 DRAM보다는 느리지만 읽기 속도가 빠르며 HDD보다 충격에 강하다. 이러한 특징으로 배터리로 동작하는 장치에서 저장 장치로 많이 사용되며 강한 압력이나 끓는 물에도 견딜 만큼 물리적인 힘으로 거의 파괴되지 않는다.

### V-NAND
V-NAND(Vertical NAND) 메모리는 메모리 셀들을 수직으로 쌓아올리며 차지 트랩 플래시 아키텍처를 사용한다. 이 수직층들은 개개의 작은 셀들의 필요 없이 더 큰 면적의 비트 밀도를 가능케 한다.

#### Reference
- ECC blog KO-KR, https://m.blog.naver.com/PostView.nhn?blogId=jamiet1&logNo=221557521166&proxyReferer=https%3A%2F%2Fwww.google.com%2F, 2020-10-19-Mon.
- SDRAM, DDR1, DDR2, DDR3, DDR4 blog KO-KR, https://kr.transcend-info.com/Support/FAQ-296, 2020-10-19-Mon.
- DDR, GDDR, https://m.post.naver.com/viewer/postView.nhn?volumeNo=7144098&memberNo=5148059, 2020-10-19-Mon.
- ROM Wiki KR-KO, https://ko.wikipedia.org/wiki/%EA%B3%A0%EC%A0%95_%EA%B8%B0%EC%96%B5_%EC%9E%A5%EC%B9%98, 2020-11-07-Sat.
- Flash Memory, https://ko.wikipedia.org/wiki/%ED%94%8C%EB%9E%98%EC%8B%9C_%EB%A9%94%EB%AA%A8%EB%A6%AC, 2020-11-07-Sat.
- EPROM, https://ko.wikipedia.org/wiki/EPROM, 2020-11-08-Sun.
- RAM, https://ko.wikipedia.org/wiki/%EB%9E%9C%EB%8D%A4_%EC%95%A1%EC%84%B8%EC%8A%A4_%EB%A9%94%EB%AA%A8%EB%A6%AC, 2020-11-09-Mon.
- DRAM, https://ko.wikipedia.org/wiki/%EB%8F%99%EC%A0%81_%EB%9E%A8, 2020-11-09-Mon.
- SRAM, https://ko.wikipedia.org/wiki/%EC%A0%95%EC%A0%81_%EB%9E%A8, 2020-11-09-Mon.
- SDRAM, https://ko.wikipedia.org/wiki/SDRAM, 2020-11-09-Mon.
