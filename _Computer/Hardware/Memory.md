# Memory

## Random Access Memory(RAM) | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/%EB%9E%9C%EB%8D%A4_%EC%95%A1%EC%84%B8%EC%8A%A4_%EB%A9%94%EB%AA%A8%EB%A6%AC)
Random access memory (RAM, 임의 접근 기억 장치)은 임의의 영역에 접근하여 읽고 쓰기가 가능한 주기억 장치이다. 반도체 회로로 구성되어 있으며 휘발성 메모리이다. 흔히 RAM을 "읽고 쓸 수 있는 메모리"라는 뜻으로 알고 있는데 이것은 오해다. RAM은 어느 위치에 저장되 데이터든지 접근(읽기 및 쓰기)하는 데 동일한 시간이 거리는 메모리이기에 random(무작위)이다. 반면 HDD 등의 자기 디스크나 자기 테이프는 저장된 위치에 따라 접근하는 데 시간이 다르게 걸린다.

### Static RAM(SRAM) | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/%EC%A0%95%EC%A0%81_%EB%9E%A8)
Static RAM(SRAM, 정적 막기억장치)는 반도체 기억 장치의 한 종류로 주기적으로 내용을 갱신해 주어야하는 DRAM과 달리 기억 장치에 전원이 공급되는 한 그 내용이 계속 보존된다. SRAM은 RAM이므로 데이터의 쓰고 읽기가 이루어지는 주소와 관계없이 입출력에 걸리는 시간이 일정하다. SRAM은 DRAM의 일종인 SDRAM과 전혀 다른 기억 소자이다. SRAM에서 각각의 비트들은 4개의 transistor로 이루어진 2쌍의 inverter에 저장된다. 2쌍의 inverter가 1과 0의 값을 안정된 상태로 유지하고 2개의 접근 transistor가 읽기와 쓰기 기능을 수행한다. 따라서 1개의 비트를 저장하기 위해 일반적으로 8개의 transistor를 필요로 한다. SRAM은 회로의 대칭 구조로 인해 DRAM보다 훨씬 빠른 입출력을 가능하게 한다. 또한 메모리 주소에 접근할 때 상위 비트와 하위 비트 순서로 2번 접근해야 하는 DRAM과 달리 SRAM은 한번에 접근할 수 있는 장점이 있다.

### Dynamic RAM(DRAM) | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/%EB%8F%99%EC%A0%81_%EB%9E%A8)
Dynamic RAM(DRAM, 동적 막기억장치)는 RAM의 한 종류로 정보를 구성하는 개개의 비트를 각기 분리된 capacitor에 저장하는 기억 장치이다. 각각의 capacitor가 담고 있는 전자의 수의 따라 비트의 1과 0을 나타내지만 결국 capacitor가 전자를 누전하므로 기억된 정보를 잃게 된다. 이를 방지하기 위해 기억 장치의 내용을 일정 시간마다 재생시켜야 되는 것을 일컬어 dynamic이란 명칭이 주어졌다. 정보를 유지하려면 지속적인 전기 공급이 필요하기 때문에 DRAM은 휘발성 기억 장치(volatile memory)에 속한다.

### Synchronous DRAM(SDRAM) | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/SDRAM)
Synchronous DRAM(SDRAM)은 DRAM의 발전된 형태로, 보통 DRAM과는 달리 제어 장치 입력을 clock pulse와 동시에 일어나도록 하는 동기식 DRAM이다. SDRAM은 DDR SDRAM의 보급으로 SDR SDRAM이라는 관례적인 명칭이 주어졌다. SDR은 Single Data Rate의 약자이다. 이 의미는 기존의 SDRAM이 각 pusle clock이 상승 또는 하강하는 시점에서 한번만 정보를 전송하는 것에서 나온 명칭이다.

### Single Data Rate(SDD) SDRAM
Single data rate(SDR) SDRAM은 clock cycle 1개 당 1개의 command를 받거나 1개의 word만큼의 data를 주고 받을 수 있는 SDRAM을 말한다. 전형적인 clock frequency는 100 및 133MHz였다. 데이터 버스 사이즈는 4비트, 8비트, 16비트 등으로 다양하였는데, 단 일반적으로 SDR SDRAM 칩들은 64 (non-ECC) 혹은 72 (ECC) 비트를 한번에 읽을 수 있는 168 핀 DIMM 형태로 조립되었다.

### Double Data Rate(DDR) SDRAM | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/DDR_SDRAM)
Double data rate(DDR) SDRAM은 컴퓨터에 쓰이는 메모리 집적 회로 계열로, clock frequency를 높이지 않고도 SDR SDRAM에 비해 대역폭이 거의 2배나 늘어났다. JEDEC는 DDR SDRAM의 속도에 대한 표준을 2가지로 지정하였다. 첫 규격은 메모리 칩에 대한 것이고, 두번째 규격은 메모리 모듈에 대한 것이다. DDR2 SDRAM이 나오면서 기존의 DDR SDRAM은 DDR1 SDRAM으로 불리우게 되었다.

### Multi Channel Memory Architecture | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/%EB%8B%A4%EC%A4%91_%EC%B1%84%EB%84%90_%EB%A9%94%EB%AA%A8%EB%A6%AC_%EA%B5%AC%EC%A1%B0)
Multi channel memory architecture(다중 채널 메모리 구조)는 DRAM과 memory controller 사이에 통신 채널을 하나 이상 더 추가하여 데이터 전송 속도를 빠르게 하는 기술이다. 듀얼 채널, 트리플 채널, 그리고 쿼드 채널 등이 여기에 속한다. Dual channel architecture은 RAM에서 memory controller를 거치는 데이터를 2배로 만드는 기술을 말한다. Dual channel을 사용하는 memory controller는 2개의 64비트 데이터 채널을 이용함으로써 RAM에서 CPU로 데이터를 이동할 때 128비트의 대역을 활용할 수 있다. Dual channel은 DDR SDRAM, DDR2 SDRAM, DDR3 SDRAM에서 사용된다. Dual channel은 병목 문제를 해결하는 것이 목적으로, processor의 속도가 빨라지면서 다른 부품들의 상대적으로 낮은 속도는 시스템 병목 원인으로 지적되어 왔다. Triple channel architecture은 Intel Core i7-900 시리즈부터 사용된 구조로, LGA 1366 platform은 DDR3 triple channel(보통 1333, 1600MHz)에서 지원하지만, 일부 mainboard에서는 더 높은 클럭 속도로 구동할 수 있다. Quard channel은 Intel LGA 2011, AMD G34 platform에서 지원한다.

### Graphics DDR(GDDR) SDRAM | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/GDDR_SDRAM)
Graphics DDR(GDDR) SDRAM은 GPU(그래픽 처리 장치)용으로 설계된 일종의 SDRAM으로, DDR3 등 더 널리 알려져 있는 유형의 DDR SDRAM과 구별되지만 double data rate 전송을 포함한 동일한 기능 중 일부를 공유한다. 2014년을 기점으로 GDDR SDRAM 이후로 GDDR2, GDDR3, GDDR4, GDDR5, 그리고 GDDR6가 공개되었다.

### Error Correcting Code(ECC) Memory | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/ECC_%EB%A9%94%EB%AA%A8%EB%A6%AC)
Error correcting code(ECC) memory는 가장 일반적인 종류의 내부 데이터 손상을 감지하고 수정하는 기억 장치의 일종이다. ECC memory는 계산 과학, 금융 컴퓨팅 등 모든 상황에서 데이터 손상에 대처해야하는 컴퓨터에서 사용된다. 일반적으로 ECC memory는 single bit 오류에 memory system이 면역되도록 관리한다. 각 워드로부터 읽은 데이터는 무조건 기록되는 데이터와 동일해야 하는데, 이는 실제로 저장되는 하나 이상의 bit가 잘못된 상태로 flip되더라도 마찬가지이다. 대부분의 비 ECC memory는 오류를 감지할 수 없으며, parity bit를 지원하는 일부 비 ECC memory는 오류를 감지할 수는 있으나 정정 기능은 없다.

DRAM의 single bit가 컴퓨터 시스템 내부의 전기적 또는 자기적 간섭으로 인해 자연스럽게 반대 상태로 바뀔 수 있는데, 처음에는 주로 칩 포장재의 오염물질에 의해 방출되는 알파 입자 때문이라고 생각되었으나, 연구를 통해 DRAM 칩의 일회성 소프트 에러의 대부분은 주로 2차 우주선의 중성자에 의한 배경 방사능의 결과로 발생하며, 이는 하나 이상의 memory cell의 내용을 변경하거나 읽기 또는 쓰기에 사용되는 회로를 방해할 수 있다는 것을 밝혀냈다. 이러한 이유로 오류율은 고도가 증가할수록 급격히 증가하는데, 예를 들어 해수면 대비 중성자 선속은 1.5km에서 3.5배, 10~12km(상용 항공기의 순항 고도)에서 300배 더 빠르다. 결과적으로 높은 고도에서 작동하는 시스템은 신뢰성을 위해 특별한 규정이 필요하다. 이러한 예로 1997년에 발사된 우주선 카시니-하위헌스는 2개의 동일한 비행 기록기에 각각 상용 DRAM 칩 배열의 형태로 2.5GB memory를 탑재했으며, EDAC가 내장되어 있어, 키시니 하위헌스의 인제니어링 telemetry는 single bit 워드 오류(수정 가능) 수와 dual bit 워드 오류(수정 불가능) 수를 보고했다. 처음 2년 6개월간 비행하는 동안, 카시니-하위헌스는 하루에 약 280개의 오류를 보고했으며, 거의 일정한 single bit error rate를 보였다. 그러나 1997년 11월 6일, 우주에서의 첫 달 동안, 오류의 수는 하루에 4배 이상 증가했는데, 증가의 원인은 인공위성 GOE9에 의해 탐지된 태양 입자 방출(solor particle event)이었다.

### Parity Bit | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/%ED%8C%A8%EB%A6%AC%ED%8B%B0_%EB%B9%84%ED%8A%B8)
Parity bit는 정보의 전달 과정에서 오류가 생겼는지 검사하기 위해 추가된 bit이다. 문자열 내 1비트의 모든 숫자가 odd 또는 even인지를 보증하기 위해 전송하고자 하는 데이터의 각 문자에 1bit를 더하여 전송하는 방법으로, 2가지 종류의 parity(odd, even)가 있다. Parity bit는 오류 검출 부호에서 가장 간단한 형태로 쓰인다. Odd parity는 전체 bit에서 1의 개수가 odd이 되도록 parity bit를 정하는 방법이다. Even parity는 전체 bit에서 1의 개수가 even이 되도록 parity bit를 정하는 방법이다. 예를 들어 data bit에서 1의 개수가 odd이면 parity bit를 1로 정한다. 이렇게 parity bit를 정하여 데이터를 보내면 받는 쪽에서는 수신된 데이터의 전체 bit를 계산하여 parity bit를 다시 계산함으로써 데이터 오류 발생 여부를 알 수 있다. 그러나 parity bit는 오류 발생 여부만 알 수 있지, 오류를 수정할 수는 없다.

### Hamming Code | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/%ED%95%B4%EB%B0%8D_%EB%B6%80%ED%98%B8)
Hamming code(해밍 부호)는 이진 선형 부호의 일종으로, 거리가 3이므로 1개 이하의 오류를 교정할 수 있으며 2개 이하의 오류를 발견할 수 있다. Hamming code는 임의의 소수 거듭제곱 진법에 대하여 정의되는 거의 3의 선형 부호이다. 이 가운데 이진 해밍 부호는 정의하기가 특별히 간단하다.

# Non Volatile Memory(NVM) | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/%EB%B9%84%ED%9C%98%EB%B0%9C%EC%84%B1_%EB%A9%94%EB%AA%A8%EB%A6%AC)
NVM(비휘발성 메모리)는 전원이 공급되지 않아도 저장된 정보를 계속 유지하는 컴퓨터 메모리이다. 비휘발성 메모리 종류에는 ROM, flash memory, HDD, diskette, magnetic tape, OD 등이 있으며 초창기 컴퓨터 저장 장치였던 천공 카드, 페이퍼 테이프 같은 것도 있다.

NVM은 보통 제 2차 저장 장치(secondary storage), 즉 장기간의 영구적 저장 공간으로서 이용된다. 현재 가장 널리 쓰이고 있는 제 1차 저장 장치는 휘발성 메모리인 RAM이다. 이것은 컴퓨터의 전원이 꺼졌을 때, RAM 안에 있던 모든 데이터가 지워진다. 불행하게도 현재 나와 있는 비휘발성 메모리는 제 1차 저장 장치에는 적합하지가 않다. 일반적으로 비휘발성 메모리는 RAM보다 가격 단가가 비싸다던가, 성능이 잘 나오지 않던가 한다. IBM은 MRAM을 개발 중이고, 삼성전자 Intel, STMicroelectronics 등은 PRAM을 개발 중이다.

### Magnetoresistive Random Access Memory(MRAM) | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/%EC%9E%90%EA%B8%B0_%EC%A0%80%ED%95%AD_%EB%A9%94%EB%AA%A8%EB%A6%AC)
MRAM은 비휘발성 컴퓨터 메모리 기술이며 1990년대부터 개발이 진행 중이다. 현재의 메모리, 특히 flasy RAM과 DRAM의 밀도가 꾸준히 늘어나면서, 시장에서 MRAM은 틈새 제품이라는 위치를 벗어나지 못하였다. 그러나 MRAM을 지지하는 사람들은 MRAM의 뛰어난 이점 때문에 MRAM이 결국 시장을 지배하여 universal memory가 될 것으로 생각한다. 에버스핀에서 생산 중이며 글로벌 파운드리와 삼성을 포함한 다른 기업들은 제품 계획을 발표하였다.

### Phase Change Memory(PCM, PCRAM, CRAM) | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/PRAM)
PRAM은 비휘발성 메모리의 한 종류로, flash memory의 비휘발성과 RAM의 빠른 속도의 장점을 모두 가지고 있는 차세대 메모리 반도체이다. PRAM은 열을 가함에 따라 비정질 상태와 결정질 상태로 바뀌는 칼코게나이드 유리의 독특한 특성을 이용하여 데이터를 저장한다.

## Read Only Memory(ROM) | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/%EA%B3%A0%EC%A0%95_%EA%B8%B0%EC%96%B5_%EC%9E%A5%EC%B9%98)
ROM(고정 기억 장치)는 반도체 기억 장치의 하나로 사람의 본능에 비유할 수 있으며, 컴퓨터를 구동하기 위한 기본적인 정보가 담겨있고 그 정보들을 기억하기 위해 다른 정보들은 기억하지 않는다. ROM은 RAM과 달리 자유롭게 읽고 쓰기가 어려우며, 전원을 꺼도 데이터가 지워지지 않기 때문에 BIOS, UEFI, OS, firmware의 저장에 사용되었다. 최근에는 일부분이 읽고 쓰기가 가능한 flash memory 등으로 일부 대체되었다. ROM은 ROM writer로 수정이 가능하다. ROM은 1956년에 PROM이 발명되었고, 1971년에 EPROM이 발명되었으며, 1983년 EEPROM이 발명되었고, 1980년대 중반에는 Toshiba가 flash memory를 발명하여 1990년대 초에 상용화하였으며 이는 EEPROM의 일종으로 손상을 일으키지 않고 수천번이나 삭제와 재프로그래밍을 가능하게 하였다. 가장 최근 방식은 NAND flash 이며 이또한 Toshiba가 발명하였다.

### Erasable PROM(EPROM) | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/EPROM)
EPROM(Erasable PROM)은 필요할 때 기억된 내용을 지우고 다른 내용을 기록할 수 있는 ROM이다. 지우는 방법에 따라 자외선으로 지울 수 있는 UVEPROM(Ultra-Violet Erasable Programmable Read Only Memory)과 높은 전압으로 지울 수 있는 EEPROM(Electrically Erasble Programmable Read Only Memory)로 나뉜다. 하지만 EPROM은 일반적으로 UVEPROM을 가리킨다. UVEPROM은 1971년 Intel의 Dov Frohman이 발명했으며 최초의 제품은 Intel 1702A이다. 기록은 floating-gate 트랜지스터에 고전압(12V)으로 전자를 주입하여 기록하며 플로팅 게이트는 절연되어 있어서 전원을 꺼도 전자는 보존되어 ROM으로 사용할 수 있다. 그러나 강한 자외선(234nm)을 쬐게되면 전자는 게이트의 절연막을 통과해 기록이 지워지게 된다. 보통 UVEPROM에는 석영유리창이 있어 다른 ROM과는 확연히 구분한다. 기록횟수는 고전압이 실리콘에 영향을 주기 때문에 20회 전후이며 차광 씰을 잘 부착하여 최적으로 보관한다면 약 10년 정도 데이터 보관이 가능하다. UVEPROM은 과거 메인보드, 그래픽카드의 BIOS chip이나 게임기의 ROM으로 많이 사용되었다. 그리고 칩 패키지에서 창을 없앤 UVEPROM을 OTP(One Time Programmable)라고 하는데 소거창이 없기 떄문에 한번 기록 후 지울 수 없으며 주로 마이크로컨트롤러에서 볼 수 있다.

## Flash Memory | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/%ED%94%8C%EB%9E%98%EC%8B%9C_%EB%A9%94%EB%AA%A8%EB%A6%AC)
Flash memory(전기 일괄소거형 기억기)는 전기적으로 데이터를 지우고 다시 기록할 수 있는 비휘발성 컴퓨터 기억 장치이다.(Electrically erased and reprogrammed) Flash memory는 EEPROM과 다르게 여러 구역으로 구성된 블록 안에서 지우고 쓸 수 있다. 이제는 flash memory의 가격이 EEPROM보다 훨씬 싸기 때문에 비휘발성 고체 상태(Solid State) 저장 매체가 상당량 필요한 곳에서는 가장 많이 사용되는 메모리 종류가 되었다. USB drive에도 flash memory가 사용된다. 옛날 게임팩으로는 EEPROM으로 만들었으나 요즘은 flash memory가 주로 사용되고 있다. Flash memory는 메모리 칩 안에 정보를 유지시키는데 전력이 필요 없는 비휘발성 메모리이다. Flash memory는 DRAM보다는 느리지만 읽기 속도가 빠르며 HDD보다 충격에 강하다. 이러한 특징으로 배터리로 동작하는 장치에서 저장 장치로 많이 사용되며 강한 압력이나 끓는 물에도 견딜 만큼 물리적인 힘으로 거의 파괴되지 않는다.

### Vertical NAND(V-NAND)
V-NAND(Vertical NAND) 메모리는 메모리 셀들을 수직으로 쌓아올리며 차지 트랩 플래시 아키텍처를 사용한다. 이 수직층들은 개개의 작은 셀들의 필요 없이 더 큰 면적의 비트 밀도를 가능케 한다.

## Floppy Disk | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/%ED%94%8C%EB%A1%9C%ED%94%BC_%EB%94%94%EC%8A%A4%ED%81%AC)
Floppy disk(플로피 디스크) 또는 diskette(디스켓)은 컴퓨터 보조 기억 장치의 일종이다. 컴퓨터에 부착된 floppy disk drive에 넣고 빼면서 사용한다. Diskette은 5.25inch 디스크가 개발되면서 기존의 8inch보다 작다고 하여 floppy disk에 "-ette"의 접미사를 붙인 말이다. 재킷(껍데기) 안에 자성체로 덮여 있는, 회전할 수 있는 원판이 들어 있다. 헤드가 표면과 떨어져있는 HDD와는 달리, floppy disk는 직접 헤드와 맞닿아있다. 그 결과, 데이터와 헤드가 빠르게 닳아버린다. 닳아 없어지는 것을 줄이기 위해서, PC에서는 드라이브가 읽거나 쓰기 않을 때 헤드를 움츠리고 회전을 중지시킨다. 그 다음에 읽거나 쓰는 명령을 받게되면, 멈추었던 모터가 다시 돌아 회전력을 얻기까지 약 0.5초의 지연 시간을 가지게 된다. 이러한 구조 때문에 읽기 쓰기 속도가 HDD보다 느리다.

## Optical Disk(OD) | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/%EA%B4%91_%EB%94%94%EC%8A%A4%ED%81%AC)
Optical disk(OD, 광 디스크)는 빛의 반사를 이용하여 자료를 읽어내는 저장 매체이다. OD의 효시로는 디지털 방식으로는 음반인 CD가 있고 아날로그 방식으로는 비디오 디스크인 레이저 데스크가 1980년대 초에 개발 완료되어 발매되기 시작하였다. 재기록 가능한 OD로는 자기 방식과 광 방식을 혼합한 광자기 디스크가 1980년대 말에 개발되었고 실용적으로는 1회 기록형 유기광 디스크가 1990년대 초에 개발되었다.

## Hard Disk Drive(HDD) | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/%ED%95%98%EB%93%9C_%EB%94%94%EC%8A%A4%ED%81%AC_%EB%93%9C%EB%9D%BC%EC%9D%B4%EB%B8%8C)
Hard disk drive(HDD, 하드 디스크 드라이브/hard disk/hard drive/fixed disk)는 비휘발성, 순차 접근이 가능한 컴퓨터의 보조 기억 장치이다. 보호 케이스 안에 있는 platter를 회전시켜 이것에 자기 패턴으로 정보를 기록한다. 이 platter를 구동시키는 장치는 스팬들 모터로 이루어져있다. 데이터는 platter 표면의 코팅된 자성체에 기록되며 회전하는 platter 위에 부상하는 입출력 헤드에 의해 자기적으로 데이터를 쓰고 읽을 수 있다. HDD는 floppy disk와 같은 자기 기록 매체이나, floppy disk와 다르게 금속 재질의 platter에 데이터를 기록하기 때문에 구분짓기 위해 재질적으로 단단하다는 뜻으로 hard라는 이름이 붙었다. 일반적으로 아직까지는 personal computer의 OS를 담는 용도로 없어서는 안 되는 저장 매체로 많이 쓰이고 있다.

### Platter | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/%ED%95%98%EB%93%9C_%EB%94%94%EC%8A%A4%ED%81%AC_%ED%94%8C%EB%9E%98%ED%84%B0)
Platter는 HDD에서 데이터가 저장되는 원판을 말한다. Platter의 장당 용량은 기록 밀도가 높아질수록 커질 뿐만 아니라, 같은 용량의 데이터를 입출력 하더라도 head가 적게 움직이므로 HDD의 입출력 속도에도 영향을 미친다. 또한 platter의 회전 속도는 HDD의 반응 속도에 영향을 미친다. 대용량의 HDD의 경우 여러 장의 platter를 사용하기도 한다. 하지만 너무 많은 장수의 platter를 장착하면 발열, 소음, 전력 소모, 오작동 등의 문제가 발생하므로 여러 장의 platter를 사용해 고용량을 만드는 방법도 한계가 있다. HDD의 bad sector 등 오류는 흔히 platter에 발생한 물리적 흠집(스크래치)에 의해 발생한다.

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

## Solid State Drive(SSD)

### Single Level Cell(SLC)

### Multi Level Cell(MLC)

### Triple Level Cell(TLC)

### Quad Level Cell(QLC)

## CPU Cache | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/CPU_%EC%BA%90%EC%8B%9C)
CPU cache(캐시)는 CPU 구조에 메모리로 사용하도록 구성된 하드웨어 캐시다. CPU cache는 메인 메모리에서 가장 자주 사용되는 위치의 데이터를 갖고 있는, 크기는 작지만 빠른 메모리이다. 대부분의 메모리 접근은 특정한 위치의 근방에서 자주 일어나는 경향이 있기 때문에, 데이터를 크기는 작지만 속도가 빠른 cache memory에 복사해 두면 평균 메모리 접근 시간을 아낄 수 있다. 프로세서가 메인 메모리를 읽거나 쓰고자 할 때는, 먼저 그 주소에 해당하는 데이터가 cache에 존재하는지를 살핀다. 만약 그 주소의 데이터가 cache에 있으면 데이터를 cache에서 직접 읽고, 그렇지 않으면 메인 메모리에 직접 접근한다. 이때 대부분의 프로세서는 메인 메모리에 직접 접근해서 전송된 데이터를 cache에 복사해 넣음으로써 다음에 같은 주소에 프로세서가 접근할 때 cache에서 직접 읽고 쓸 수 있도록 한다.

#### Reference
- ECC blog KO-KR, https://m.blog.naver.com/PostView.nhn?blogId=jamiet1&logNo=221557521166&proxyReferer=https%3A%2F%2Fwww.google.com%2F, 2020-10-19-Mon.
- SDRAM, DDR1, DDR2, DDR3, DDR4 blog KO-KR, https://kr.transcend-info.com/Support/FAQ-296, 2020-10-19-Mon.
- DDR, GDDR, https://m.post.naver.com/viewer/postView.nhn?volumeNo=7144098&memberNo=5148059, 2020-10-19-Mon.
- ROM Wiki KR-KO, https://ko.wikipedia.org/wiki/%EA%B3%A0%EC%A0%95_%EA%B8%B0%EC%96%B5_%EC%9E%A5%EC%B9%98, 2020-11-07-Sat.
- Flash Memory Wiki KR-KO, https://ko.wikipedia.org/wiki/%ED%94%8C%EB%9E%98%EC%8B%9C_%EB%A9%94%EB%AA%A8%EB%A6%AC, 2020-11-07-Sat.
- EPROM Wiki KR-KO, https://ko.wikipedia.org/wiki/EPROM, 2020-11-08-Sun.
- RAM Wiki KR-KO, https://ko.wikipedia.org/wiki/%EB%9E%9C%EB%8D%A4_%EC%95%A1%EC%84%B8%EC%8A%A4_%EB%A9%94%EB%AA%A8%EB%A6%AC, 2020-11-09-Mon.
- DRAM Wiki KR-KO, https://ko.wikipedia.org/wiki/%EB%8F%99%EC%A0%81_%EB%9E%A8, 2020-11-09-Mon.
- SRAM Wiki KR-KO, https://ko.wikipedia.org/wiki/%EC%A0%95%EC%A0%81_%EB%9E%A8, 2020-11-09-Mon.
- SDRAM Wiki KR-KO, https://ko.wikipedia.org/wiki/SDRAM, 2020-11-09-Mon.
- DDR SDRAM Wiki KR-KO, https://ko.wikipedia.org/wiki/DDR_SDRAM, 2020-11-09-Mon.
- GDDR SDRAM Wiki KR-KO, https://ko.wikipedia.org/wiki/GDDR_SDRAM, 2020-11-09-Mon.
- Multi Channel Memory Architecture Wiki KR-KO, https://ko.wikipedia.org/wiki/%EB%8B%A4%EC%A4%91_%EC%B1%84%EB%84%90_%EB%A9%94%EB%AA%A8%EB%A6%AC_%EA%B5%AC%EC%A1%B0, 2020-11-09-Mon.
- Parity Bit Wiki KR-KO, https://ko.wikipedia.org/wiki/%ED%8C%A8%EB%A6%AC%ED%8B%B0_%EB%B9%84%ED%8A%B8, 2020-11-09-Mon.
- ECC emory Wiki KR-KO, https://ko.wikipedia.org/wiki/ECC_%EB%A9%94%EB%AA%A8%EB%A6%AC, 2020-11-09-Mon.
- Hamming Code Wiki KR-KO, https://ko.wikipedia.org/wiki/%ED%95%B4%EB%B0%8D_%EB%B6%80%ED%98%B8, 2020-11-10-Tue.
- CPU Cache Wiki KR-KO, https://ko.wikipedia.org/wiki/CPU_%EC%BA%90%EC%8B%9C, 2020-11-11-Wed.
- NVM Wiki KR-KO, https://ko.wikipedia.org/wiki/%EB%B9%84%ED%9C%98%EB%B0%9C%EC%84%B1_%EB%A9%94%EB%AA%A8%EB%A6%AC, 2020-11-13-Fri.
- MRAM Wiki KR-KO, https://ko.wikipedia.org/wiki/%EC%9E%90%EA%B8%B0_%EC%A0%80%ED%95%AD_%EB%A9%94%EB%AA%A8%EB%A6%AC, 2020-11-13-Fri.
- PRAM Wiki KR-KO, https://ko.wikipedia.org/wiki/PRAM, 2020-11-13-Fri.
- HDD Wiki KR-KO, https://ko.wikipedia.org/wiki/%ED%95%98%EB%93%9C_%EB%94%94%EC%8A%A4%ED%81%AC_%EB%93%9C%EB%9D%BC%EC%9D%B4%EB%B8%8C, 2020-11-11-Wed.
- HDD Platter Wiki KR-KO, https://ko.wikipedia.org/wiki/%ED%95%98%EB%93%9C_%EB%94%94%EC%8A%A4%ED%81%AC_%ED%94%8C%EB%9E%98%ED%84%B0, 2020-11-11-Wed.
- Floppy disk Wiki KR-KO, https://ko.wikipedia.org/wiki/%ED%94%8C%EB%A1%9C%ED%94%BC_%EB%94%94%EC%8A%A4%ED%81%AC, 2020-11-11-Wed.
- OD Wiki KR-KO, https://ko.wikipedia.org/wiki/%EA%B4%91_%EB%94%94%EC%8A%A4%ED%81%AC, 2020-11-13-Fri.
