# _Video Graphics Array (VGA)_ | [WiKi (KR)](https://ko.wikipedia.org/wiki/%EB%B9%84%EB%94%94%EC%98%A4_%EA%B7%B8%EB%9E%98%ED%94%BD%EC%8A%A4_%EC%96%B4%EB%A0%88%EC%9D%B4)

비디오 그래픽스 어레이는 IBM이 1987년에 제정한 아날로그 방식의 컴퓨터 디스플레이 표준이다.

VGA가 표준으로 자리잡고 있는 포켓 PC 시장을 제외하고 오늘날 VGA는 일반적인 목적으로 사용되지는 않지만, 대부분의 컴퓨터 제조사가 기본적으로 지원하는 마지막 표준으로써, 많은 PC 디스플레이 장치에서 장치 드라이버를 올리기 이전에 화면 표시를 위해 VGA 방식이 쓰이고 있다. 예를 들어, 마이크로소프트 윈도의 일부 버전의 로딩 화면이나 안전모드에서는 VGA 모드로 동작한다.

VGA라는 용어는 하드웨어와 관계 없이 영상의 640x480 해상도를 나타낸다. 모든 해상도의 아날로그 영상 신호 전송에서 아직까지도 쓰이느느 15핀 D-sub VGA 커넥터가 VGA로 불리기도 한다.

VGA는 공식적으로 IBM의 XGA 표준으로 대체되었지만, 실제로는 VGA를 개선해 여러 호환 하드웨어 제조사에서 제조하던 SVGA로 대체되었다.

# _Graphics Processing Unit (GPU)_ | [WiKi (KR)](https://ko.wikipedia.org/wiki/%EA%B7%B8%EB%9E%98%ED%94%BD_%EC%B2%98%EB%A6%AC_%EC%9E%A5%EC%B9%98)

그래픽 처리 장치는 메모리를 빠르게 처리하고 바꾸어 화면으로 출력할 프레임 버터 안의 영상 생성을 가속하도록 설계된, 전문화된 전자 회로이다. VPU(Visual Processing Unit)이라고 하기도 한다.

GPU는 임베디드 시스템, 휴대 전화, 개인용 컴퓨터, 워크스테이션, 비디오 게임 콘솔, 인공지능, 무인 자동차, 클라우드 컴퓨팅 등에 사용된다. 현대의 GPU는 컴퓨터 그래픽과 영상 처리를 매우 효과적으로 처리하며, 고도의 병행 구조는 큰 덩어리의 영상 데이터가 병행 처리되는 알고리즘에 다용도 CPU보다 능률적이라다. 개인 컴퓨터에서 GPU는 그래픽 카드에 부착되고, 메인보드나 CPU에 따라서는 다이에 포함되기도 한다.

GPU라는 용어는 1999년 엔비디아에서 지포스 256을 세계 최초의 GPU로 판매하면서 널리 알려졌다. 지포스 256은 단일 칩 프로세서와 통합된 TCL(Transform, clipping, and lighting) 초당 1천만개 이상의 폴리곤(다각형)을 처리할 수 있는 렌더링 엔진을 갖추고 있었다. 라이벌인 ATI 테크놀로지스는 2002년 라데온 9700을 발매하면서 VPU(영상 처리 장치)라는 용어를 사용하였다.

GPU는 그래픽과 관련된 연산을 할 때에 CPU의 부담을 크게 줄일 수 있다. macOS는 10.6부터 최초로 운영 체제 수준에서 GPU를 사용하기 시작했다.

### Comparison

|GPU|VRAM|ARCHITECTURE|COMMENT|% w/ V100|MSRP|
|:-:|:---|:-----------|:------|--------:|---:|
|T4|16GB GDDR6|Turing|에너지 효율이 높아 추론 작업에 적합하며, 데이터센터에서 널리 사용됨|52%||
|K80|24GB GDDR5|Kepler|구형 아키텍처로 현재 AI 작업에는 성능이 제한적이며, 최신 모델로의 업그레이드가 필요|40%||
|V100 32GB|32GB HBM2|Volta|딥러닝 트레이닝과 추론 모두에 최적화된 고성능 GPU로, 연구 및 산업 분야에서 널리 사용됨|100%||
|GTX 1060 6GB|6GB GDDR5|Pascal|게임용으로 설계되어 AI 작업에는 제한적이지만, 소규모 프로젝트나 학습용으로 사용 가능|30%||
|GTX 1080 Ti|11GB GDDR5X|Pascal|게임 및 그래픽 작업에 최적화되어 있으며, AI 작업에는 제한적이지만 중간 수준의 성능 제공|45%||
|RTX 2080Ti|11GB GDDR6|Turing|Tensor 코어를 탑재하여 AI 추론 작업에 효율적이며, 트레이닝에도 활용 가능|70%||
|RTX 3060 12GB|12GB GDDR6|Ampere|최신 아키텍처로 향상된 성능을 제공하며, AI 작업에 효율적이나 고급 작업에는 한계가 있음|60%||
|RTX 3090|24GB GDDR6X|Ampere|대용량 메모리와 높은 연산 성능으로 AI 트레이닝과 추론 모두에 적합하며, 고해상도 작업에 최적|90%||
|RTX 4060 Ti 16GB|16GB GDDR6|Ada Lovelace|최신 아키텍처로 에너지 효율이 향상되었으며, 중간 수준의 AI 작업에 적합|65%||
|RTX 4090|24GB GDDR6X|Ada Lovelace|최고 수준의 연산 성능과 대용량 메모리로 대규모 AI 트레이닝 및 추론 작업에 최적화됨|120%||
|RTX 5090|32GB GDDR7|Blackwell|DLSS 4 및 최신 AI 가속 기능을 통해 프레임 속도를 대폭 향상시키며, AI 기반 연산에 강력한 성능 제공|150%|| 

---

### Reference
- VGA and GPU blog KR-KO, https://intel-ryzen.tistory.com/20, 2020-10-21-Wed.
- VGA Wiki KR-KO, https://ko.wikipedia.org/wiki/%EB%B9%84%EB%94%94%EC%98%A4_%EA%B7%B8%EB%9E%98%ED%94%BD%EC%8A%A4_%EC%96%B4%EB%A0%88%EC%9D%B4, 2020-10-21-Wed.
- GPU Wiki KR-KO, https://ko.wikipedia.org/wiki/%EA%B7%B8%EB%9E%98%ED%94%BD_%EC%B2%98%EB%A6%AC_%EC%9E%A5%EC%B9%98, 2020-10-21-Wed.
- AMD Radeon, https://www.amd.com/en/graphics/radeon-rx-graphics, 2020-11-07-Sat.
