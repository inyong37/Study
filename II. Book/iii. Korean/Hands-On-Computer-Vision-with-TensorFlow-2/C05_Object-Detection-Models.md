# 05 객체 탐지 모델
최신 기법 중 가장 일반적으로 사용되는 두 모델인 YOLO(You Only Look Once)와 R-CNN(Regions with Convolutional Neural Networks) 아키텍처를 설명한다.

- 객체 탐지 기법의 역사
- 주요 객체 탐지 방법
- YOLO 아키텍처를 사용해 빠른 객체 탐지 구현하기
- Faster R-CNN 아키텍처를 사용해 객체 탐지 성능 개선하기
- 텐서플로 객체 탐지 API로 Faster R-CNN 사용하기

## 기술 요구사항

## 객체 탐지 소개

### 배경
객체 탐지(Object Detection) 또는 객체 위치 특정(Object Localization)이라고도 하는 이 프로세스는 한 이미지에서 객체와 그 경계 상자를 탐지한다. 경계 상자(Bounding Box)는 이미지에서 하나의 객체 전체를 포함하는 가장 작은 직사각형이다.

객체 탐지 알고리즘에서는 일반적으로 이미지를 입력으로 받고 경계 상자와 객체 클래스 리스트를 출력한다. 모델은 각 경계 상자에 대해 그에 대응하는 예측 클래스와 해당 클래스의 신뢰도(Confidence)를 출력한다. 

#### 애플리케이션

#### 약력
객체 탐지는 전통적인 컴퓨터 비전 기법인 이미지 설명자(Image Descriptors)를 기반으로 한다. 예를 들어 자전거 같은 객체를 탐지하려면 이 객체가 포함된 몇 장의 사진으로 시작한다. 자전거에 해당하는 설명자는 이미지로부터 추출된다. 그 설명자는 이미지로부터 추출된다. 그 설명자는 자전거의 특정 부분을 나타낸다. 알고리즘이 이 객체를 찾을 때 목표 이미지에서 다시 설명자를 찾으려고 할 것이다.

이미지에서 자전거를 찾기 위해 가장 일반적으로 사용되는 기법은 플로팅 윈도우(Floating Window)다. 이미지의 작은 직사각형 영역이 차례로 검사된다. 가장 일치하는 설명자를 가진 부분이 해당 객체를 포함하는 것으로 간주된다.

이 기법은 이미지를 회정하거나 색이 바뀌더라도 성능에 영향을 주지 않고 훈련 데이터가 많이 필요하지 않으며 대부분의 객체에 동작한다. 하지만 정확도는 만족스럽지 않다.

성능은 알고리즘이 다음 항목에서 얼마나 우수한지를 나타낸다.

- 경계 상자 정밀도(Bounding Box Precision): 정확한 경계 상자(너무 크지도, 너무 작지도 않은)를 제공하는가?
- 재현율(Recall): 모든 객체를 찾았는가? (어떤 객체도 놓치지 않았는가?)
- 클래스 정밀도(Class Precision): 객체마다 정확한 클래스를 출력했는가? (고양이를 개로 착각하지 않았는가?)

성능 개선은 모델이 결과를 계산하는 속도가 빨라졌음(특정 입력 이미지에 대해 특정 컴퓨팅 파워로)을 뜻하기도 한다. 초기 모델은 객체를 탐지하는 데 상당한 시간(몇 초보다 오랜 시간)이 걸렸지만, 지금은 실시간으로 사용될 수 있다. 컴퓨터 비전에서 실시간이란 일반적으로 1초에 5개 이상 탐지하는 속도를 뜻한다.

### 모델 성능 평가

#### 정밀도와 재현율
일반적으로 정밀도와 재현율은 객체 탐지 모델 평가에 사용되지 않지만, 다른 지표를 계샇나는 기본 지표 역할을 한다.

정밀도와 재현율을 측정하기 위해서는 먼저 각 이미지에 대해 다음을 계산해야 한다.

- 참긍정 수: 참긍정(True Positive, TP)은 얼마나 많은 예측이 동일 클래스의 실제 상자와 일치하는지 측정한다.
- 거짓긍정 수: 거짓긍정(False Positive, FP)은 얼마나 많은 예측이 동일 클래스의 실제 상자와 일치하지 않는지 측정한다.
- 거짓부성 수: 거짓부정(False Negative, FN)은 얼마나 많은 실제 분류 값이 그와 일치하는 예측을 갖지 못하는지 측정한다.

정밀도(Precision)와 재현율(Recall)은 다음과 같이 정의된다.

precision = TP / (TP + FP)

recall = TP / (TP + FN)

예측이 실제 분류와 정확히 일치하면 거짓긍정이나 거짓부정이 없을 것이다. 따라서 정밀도와 재현율에서 만점은 1이다. 대체로 모델이 안정적이지 않은 특징을 기반으로 객체 존재를 예측하면 거짓긍정이 많아져 정밀도가 낮아진다. 반대로 모델이 너무 엄격해서 정확한 조건을 만족할 때만 객체가 탐지된 것으로 간주한다면 거짓부정이 많아져서 재현율이 낮아질 것이다.

#### 정밀도-재현율 곡선
정밀도-재현율 곡선(Precision-Recall Curve)은 수많은 머신러닝 모델에서 사용된다. 일반적인 개념은 신뢰도 임곗값마다 모델의 정밀도와 재현율을 시각화하는 것이다. 모델은 모든 경계 상자와 함께 모델이 예측의 정확성을 얼마나 확신하는지를 0과 1 사이의 숫자로 나타내는 신뢰도(Confidence)를 출력한다.

신뢰도가 낮은 예측은 유지할 필요가 없으므로 일반적으로 특정 임곗값 T 이하의 예측은 제거한다. 예를 들어 T=0.4라면 이 숫자 이하의 신뢰도를 갖는 예측은 고려 대상에서 제외한다.

임곗값을 바꾸면 정밀도와 재현율도 달라진다.

- T가 1에 가까우면: 정밀도는 높지만 재현율은 낮다. 객체를 많이 걸러내기 때문에 놓치는 객체가 많아져 재현율이 낮아진다. 신뢰도가 높은 예측만 유지하므로 거짓긍정 수가 많지 않아 정밀도는 높아진다.
- T가 0에 가까우면: 정밀도는 낮지만 재현율은 높다. 대부분의 예측을 유지하므로 거짓부정이 없어져 재현율이 높아진다. 모델이 자신의 예측에 대한 확신이 낮기 때문에 거짓긍정이 많아져 정밀도가 낮아진다.

:bulb: 임곗값은 정확도(Accuracy)와 재현율 사이의 트레이드오프를 고려해 정해야 한다. 모델이 보행자를 탐지하고 있다면 때때로 마땅한 이유 없이 차를 세우더라도 어떤 보행자도 놓치지 않도록 재현율을 높여야 한다. 모델이 투자 기회를 탐지하고 있다면 일부 기회를 놓치게 되더라도 잘못된 기회에 돈을 거는 일을 피하기 위해 정밀도를 높여야 한다.

#### AP와 mAP
정밀도-재현 곡선이 모델에 대해 많은 것을 말해줄 수 있지만, 대체로 하나의 숫자로 이해하는 것이 더 편리하다. AP(Average Precision, 평균 정밀도)는 곡선의 아래 영역에 해당한다. 이 영역은 항상 1 * 1 정사각형으로 구성되므로 AP는 항상 0에서 1 사이의 값을 갖는다.

AP는 단일 클래스에 대한 모델 성능 정보를 제공한다. 전역 점수를 얻기 위해 mAP(Mean Average Precision)를 사용한다. 이는 각 클래스에 대한 AP의 평균에 해당한다. 데이터셋이 10개의 클래스로 구성된다면 각 클래스에 대한 AP를 계산하고 다시 그 숫자의 평균을 구한다.

:bulb: mAP는 최소 2개 이상의 객체를 탐지하는 대회인 PASCAL Visual Object Classes(일반적으로 Pascal VOC라고도 함)와 Common Objects in Context(일반적으로 COCO라고 함)에서 사용된다. COCO 데이터셋이 더 크고 많은 클래스를 포함하고 있으므로 여기에서 얻는 점수는 Pascal VOC보다 더 낮다.

#### AP 임곗값
TP과 FP가 실제 상자와 일치하거나 일치하지 않는 예측 개수에 의해 정의된다고 설명했다. 그렇지만 예측과 실제가 언제 일치하는지 어떻게 결정할까? 일반적으로 두 집합(여기에서는 상자로 표현되는 픽셀 집합)이 얼마나 겹치는지 측정하는 자카드 지표(Jaccard Index)를 메트릭으로 사용한다. IoT(Intersection over Union)라고도 알려진 이 지표는 다음과 같이 정의된다.

IoU(A, B) = | intersection(A, B) | / | union(A, B) | = | intersection(A, B) | / (|A| +|B| - | intersection(A, B)|)

|A|와 |B|는 각 집합의 카디널리티(Cardinality)로, 각 집합이 포함한 요소의 개수를 말한다. intersection(A, B)는 두 집합의 교집합으로 분자 |intersection(A, B)|는 두 집합이 공통으로 갖고 있는 요소 개수를 나타낸다. 마찬가지로 union(A, B)는 두 집합의 합집합으로 분모 |union(A, B)|는 두 집합이 함께 가지고 있는 전체 요소 개수를 나타낸다.

교집합은 두 집합/상자가 얼마나 겹치는지를 보기에는 좋은 지표지만, 이 값은 절대적인 수치일 뿐 상대적이지 않다. 따라서 두 개의 큰 상자가 아마 두 개의 작은 상자보다 훨씬 많은 픽셀이 겹칠 것이다. 그렇기 때문에 이 비율을 사용한다. 이 비율은 항상 0(두 상자가 전혀 겹치지 않는 경우)과 1(두 상자가 완전히 겹치는 경우) 사이의 값을 갖는다.

AP를 계산할 때 IoU가 특정 임곗값을 넘으면 두 상자가 겹친다고 말한다. 일반적으로 이 임곗값은 0.5로 정한다.

:bulb: Pascal VOC 대회에서도 0.5를 사용하며 mAP@0.5라고 부른다. COCO 대회에서는 약간 다른 지표로 mAP@[0.5:0.95]를 사용한다. 이는 mAP@0.5, mAP@0.95를 계산해 평균을 구한다는 뜻이다. IoU를 평균하면 모델의 위치 측정 성능이 좋아진다.

## 빠른 객체 탐지 알고리즘 - YOLO
최신 버전은 YOLOv3은 크기가 256x256인 이미지에 대해 최신 GPU에서 초당 170프레임(170FPS, frames per second)의 속도로 실행될 수 있다.

### YOLO 소개
2015년에 최초로 공개된 YOLO는 속도와 정확도 측면 모두에서 거의 모든 객체 탐지 아키텍처를 능가했다. 그 이후로 이 아키텍처는 몇 차례 개선됐다.

- You Only Look Once: Unified, real-time object detection (2015), Joseph Redmon, Santosh Divvala, Ross Girshick, Ali Farhad
- YOLO9000: Better, Faster, Stronger (2016), Joseph Redmon, Ali Farhadi
- YOLOv3: An Incremental Improvement (2018), Joseph Redmon, Ali Farhadi

:bulb: YOLO 논문의 1저자는 다크넷(Darknet)이라는 딥러닝 프레임워크를 관리한다. 이 프레임워크는 YOLO의 공식 구현을 제공하고 있어 논문의 결과를 재현하는 데 사용될 수 있다. 이 코드는 C++로 구현됐으며 텐서플로를 기반으로 하지 않는다.

#### YOLO의 강점과 한계
YOLO는 속도가 빠른 것으로 유명하다. 하지만 Faster R-CNN이 정확도 측면에서 YOLO를 능가했다. 게다가 YOLO는 객체를 탐지하는 방식 때문에 작은 크기의 물건을 탐지하는 데 어려움을 겪는다. 예를 들어 새 무리에서 개별 새를 탐지하는 데 문제가 있을 수 있다. 대부분의 딥러닝 모델과 마찬가지로 훈련 세트에서 너무 많이 벗어난 객체(모양이나 가로/세로 비율이 이례적인 경우)를 적절히 탐지하는 일에도 어려움을 겪는다. 그럼에도 불구하고 이 아키텍처는 꾸준히 진화하고 있으며 이러한 문제들을 해결하고 있다.

#### YOLO의 주요 개념
YOLO의 핵심 아이디어는 객체 탐지를 단일 회귀 문제로 다시 구성하는 것이다. 슬라이딩 윈도우나 다른 복잡한 기법을 사용하는 대신 입력을 w * h로 나눈다. 그리드의 각 부분에 대해 B개의 경계 상자를 정의한다. 그런 다음 각 경계 상자에 대해 다음을 예측하기만 하면 된다.

- 상자의 중심
- 상자의 너비와 높이
- 이 상자가 객체를 포함하고 있을 확률
- 앞서 말한 객체의 클래스

이 모든 예측은 숫자이므로 객체 탐지 문제를 회귀 문제로 변환했다. 실제로 YOLO에서 사용하는 개념은 이보다 좀 더 복잡하다.

### YOLO로 추론하기
추론(Inference)은 이미지 입력을 받아 결과를 계산하는 절차다. 훈련은 모델의 가중치를 학습하는 절차다. 모델을 처음부터 구현할 때는 모델이 훈련되기 전에는 추론을 사용할 수 없다. 그렇지만 설명을 단순화하기 위해 추론부터 알아본다.

#### YOLO 백본
대부분의 이미지 탐지 모델처럼 YOLO는 백본 모델(Backbone Model)을 기반으로 한다. 이 모델의 역할은 마지막 계층에서 사용될 의미 있는 특징을 이미지로부터 추출하는 것이다. 이 때문에 백본 모델을 특징 추출기(Feature Extractor)라고도 부른다. 특징 추출기로 어떤 아키텍처도 사용할 수 있지만 YOLO 논문에서는 맞춤 아키텍처를 사용했다. 최종 모델의 성능은 특징 추출기 아키텍처로 무엇을 사용했는지에 따라 크게 달라진다.

백본의 마지막 계층은 크기가 w * h * D인 특징 볼륨을 출력하는데, 여기에서 w * h는 그리드의 크기이고 D는 특징 볼륨의 깊이다. 예를 들어, VGG-16의 경우 D=512다.

그리드 크기인 w * h는 다음 2 요인에 따라 달라진다.

- 전체 특징 추출기의 보폭: VGG-16의 보폭은 16으로, 출력된 특징 볼륨이 입력 이미지보다 16배 작다는 뜻이다.
- 입력 이미지 크기: 특징 볼륨 크기는 이미지 크기에 비례하므로 입력 크기가 작을수록 그리드 크기가 작아진다.

YOLO의 마지막 계층은 입력으로 특징 볼륨을 받는다. 이 마지막 계층은 크기가 1 * 1인 합성곱 필터로 구성된다. 크기가 1 * 1인 합성곱 계층은 특징 볼륨의 공간 구조에 영향을 주지 않고 깊이를 바꾸는 데 사용될 수 있다.

#### YOLO의 계층 출력
YOLO의 마지막 출력은 w * h * M 행렬로, 여기에서 w * h는 그리드 크기이며 M은 공식 B * (C + 5)에 해당한다. B와 C는 각각 다음과 같이 정의할 수 있다.

- B는 그리드 셀당 경계 상자 개수이다.
- C는 클래스 개수다.

클래스 개수에 5를 더했다는 점에 유념하자. 이는 경계 상자마다 (C + 5)개의 숫자를 예측해야 하기 때문이다.

- t_x와 t_y는 경계 상자의 중심 좌표를 계산하기 위해 사용된다.
- t_w와 t_h는 경계 상자의 너비와 높이를 계산하기 위해 사용된다.
- c는 객체가 경계 상자 안에 있다고 확신하는 신뢰도다.
- p1, p2, ..., p_C는 경계 상자 클래스 1, 2, ..., C의 객체를 포함할 확률이다.

#### 앵커 박스 소개
t_x, t_y, t_w, t_h가 경계 상자의 좌표를 계산하는 데 사용된다고 설명했다. 왜 네트워크 좌표(x, y, w, h)를 직접 출력할 것을 요청하지 않을까? 실제로 YOLOv1에서는 그 방식을 사용했다. 유감스럽게도 이 방법은 객체 크기가 다양하기 때문에 수많은 오차가 발생한다.

사실 훈련 데이터셋의 객체 대부분이 크면 네트워크 w와 h가 매우 크다고 예측할 것이다. 그리고 작은 객체에서 훈련된 모델을 사용할 때 이 네트워크는 대체로 실패할 것이다. 이 문제를 해결하기 위해 YOLOv2에서는 앵커 박스(Anchor Box)를 도입했다.

앵커 박스(사전 정의된 상자, Prior Box)는 네트워크를 훈련시키기 전에 결정되는 일련의 경계 상자 크기다. 예를 들어 보행자를 탐지하기 위해 신경망을 훈련시킬 때 크고 가는 앵커 박스를 선택한다. 경계 상자에 따른 보정은 신경망에 의해 계산된다.

앵커 박스의 집합은 일반적으로 작으며 실제로 3~25 사이의 다양한 크기를 갖는다. 그러한 상자가 모든 객체와 정확하게 일치할 수는 없으므로 네트워크는 가장 근접한 앵커 박스를 개선하는 데 사용된다. 예제에서는 이미지의 보행자를 가장 근접한 앵커 박스와 맞추고 신경망을 사용해 앵커 박스의 높이를 보정한다. 이것이 t_x, t_y, t_w, t_h가 필요한 이유로, 앵커 박스 보정에 해당한다.

최초로 논문에서 앵커 박스를 소개했을 때는 수작업으로 앵커 박스를 선택했다. 일반적으로 9개의 상자 크기가 사용됐다.

- 3개의 정사각형(작은 크기, 중간 크기, 큰 크기)
- 3개의 가로로 긴 직사각형(작은 크기, 중간 크기, 큰 크기)
- 3개의 세로로 긴 직사각형(작은 크기, 중간 크기, 큰 크기)

하지만 YOLOv2 논문에서 저자들은 앵커 박스의 크기가 데이터셋마다 다르다는 점을 인정했다. 따라서 모델을 훈련시키기 전에 데이터를 분석해 앵커 박스의 크기를 선택할 것을 권고하고 있다. 예를 들어, 보행자를 탐지하기 위해서라면 세로로 긴 직사각형을 사용할 것이고, 사과를 탐지하는 데는 정사각형 앵커 박스가 사용될 것이다.

#### YOLO가 앵커 박스를 개선하는 방법
YOLOv2는 다음 공식을 사용해 최종 경계 상자 좌표를 각각 계산한다.

b_x = sigmoid(t_x) + c_x

b_y = sigmoid(t_y) + c_y

b_w = p_w * exp(t_w)

b_h = p_h * exp(t_h)

t_x, t_y, t_w, t_h는 마지막 계층의 출력이다. b_x, b_y, b_w, b_h는 각각 예측된 경계 상자의 위치와 크기다. p_w, p_h는 앵커 박스의 원래 크기를 나타낸다. c_x, c_y는 현재 그리드 셀의 좌표다(상단 왼쪽 상자는 (0, 0), 상단 오른쪽 상자는 (w-1, 0), 하단 왼쪽 상자는 (0, h-1) 등으로 한다). 신경망의 출력은 원시 숫자로 이뤄진 행렬로 경계 상자 목록으로 변환돼야 한다.

#### 상자를 사후 처리하기
필터링 연산을 그래드 내 모든 경계 상자에 적용하면 결국 예측을 그리기 위해 필요한 모든 정보를 얻게 된다. 수많은 경계 상자가 겹쳐 있다. 객체가 여러 그리드 셀에 걸쳐 있으므로 한 번 이상 탐지된다. 이를 보정하기 위해 사후 처리 파이프라인의 마지막 단계로 비최댓값 억제(non-maximum suppression, NMS)가 필요하다. 

#### NMS
NMS의 기본 생각은 확률이 가장 높은 상자와 겹치는 상자들을 제거하는 것이다. 따라서 최댓값을 갖지 않는 상자들을 제거한다. 그러기 위해서는 확률 기준으로 모든 상자를 정렬하고 먼저 가장 확률이 높은 상자를 취한다. 그런 다음 각 상자에 대해 다른 모든 상자와의 IoU를 계산한다.

하나의 상자와 그 밖의 상자 사이의 IoU를 계산한 다음, 특정 임곗값(이 임곗값은 일반적으로 0.5 ~ 0.9 사이의 값을 갖는다)을 넘는 상자를 제거한다.

:bulb: 실제로 텐서플로는 자체적으로 구현한 NMS, tf.image.non_max_suppression(boxes, ...)를 제공하며 이 책에서도 이 함수를 사용할 것을 추천한다(이 함수는 최적화가 잘 돼 있으며 유용한 옵션을 제공한다). 또한 NMS는 대부분의 객체 탐지 모델의 사후 처리 파이프라인에서 사용된다.

#### YOLO 추론 요약
YOLO 추론 단계는 다음과 같이 요약할 수 있다.

1. 입력 이미지를 받아 CNN 백본을 사용해 특징 볼륨을 계산한다.
2. 합성곱 계층을 사용해 앵커 박스 보정, 객체성 점수, 클래스 확률을 계산한다.
3. 이 출력을 사용해 경계 상자의 좌표를 계산한다.
4. 임곗값보다 낮은 상자는 걸러내고 남은 상자는 비최댓값 억제 기법을 사용해 사후 처리한다.

### YOLO 훈련시키기

#### YOLO 백본 훈련 방법
YOLO 논문에서 InceptionV3 아케텍처를 사용해 구현한다. 이 아키텍처가 가장 좋은 결과를 낸다. 그렇지만 모바일 환경에서 모델을 실행하려면 더 작은 모델을 사용해야 할 것이다.

#### YOLO 손실
마지막 계층의 출력이 상당히 일반적이지 않아서 그에 대응하는 손실 또한 그렇다. 실제로 YOLO 손실은 복잡하기로 악명이 높다. 이를 설명하기 위해 여기서는 손실을 여러 부분으로 나누는데, 각각은 마지막 계층에서 반환되는 출력의 한 종류에 해당한다. 이 네트워크는 다음처럼 여러 종류의 정보를 예측한다.

- 경계 상자 좌표와 크기
- 객체가 경계 상자 안에 있을 신뢰도
- 클래스에 대한 점수

이 손실에 대한 기본 개념은 오차가 높을 때 손실도 높아야 한다는 것이다. 그래야 손실이 부정확한 값에 페널티를 부과할 것이다. 그렇지만 그렇게 하는 것이 타당할 때만 패널티를 부과해야 한다. 만약 경계 상자에 아무 객체도 포함돼 있지 않으면 어차피 사용하지 않기 때문에 해당 좌표에 페널티를 부과해서는 안 된다.

##### 경계 상자 손실
네트워크가 경계 상자 좌표와 크기를 예측하기 위해 가중치를 학습하는 데 가이드를 제공한다. 핵심은 지시 함수(Indicator Function)다. 해당 상자가 객체를 탐지할 때만 좌표가 정확하다. 여기에서 이미지 내의 객체마다 어느 경계 상자가 탐지하는 지를 결정하는 일이 어려운 부분이다. YOLOv2에서는 탐지된 객체를 포함하면서 IoU가 가장 높은 앵커 박스가 해당 객체를 탐지한 것으로 간주한다. 여기서의 이론적 근거는 각 앵커 박스를 한 가지 유형의 객체에 특화시키는 것이다.

##### 객체 신뢰도 손실
경계 상자가 객체를 포함하는지 여부를 예측하기 위해 가중치를 학습하도록 네트워크를 가르친다. 

##### 분류 손실
분류 손실은 네트워크가 각 경계 상자에 대해 적절한 클래스를 예측하게 해준다. YOLO 논문에서는 L2 손실을 사용하지만 교차-엔트로피(Cross-Entropy)를 사용하는 구현도 많다. 이 부분의 손실은 올바른 객체 클래스가 예측되도록 한다.

##### 전체 YOLO 손실
전체 YOLO 손실은 3개 손실의 합이다. 이 세항을 결합함으로써 전체 손실은 경계 상자 좌표 개선, 객체성 점수, 클래스 예측에 대한 오차에 페널티를 부과한다. 이 오차를 역전파함으로써 정확한 경계 상자를 예측하도록 YOLO 네트워크를 훈련시킬 수 있다.

#### 훈련 기법
손실이 발산되는 것을 막고 우수한 성능을 얻기 위한 몇 가지 훈련 기법이 있다.

- 데이터 보강과 드롭아웃을 사용한다. 이 두 기법이 없다면 네트워크는 훈련 데이터에서 과적합되어 일반화될 수 없게 된다.
- 또 다른 기법으로는 다중-척도 훈련(Multi-Scale Training)이 있다. n개의 분기마다 네트워크 입력이 다른 크기로 바뀐다. 이렇게 함으로써 네트워크는 다양한 입력 차원에서 정확하게 예측하는 법을 학습한다.
- 대부분의 탐지 네트워크처럼 YOLO는 이미지 분류 작업에 대해 사전 훈련돼 있다.
- 이 논문에서 언급하지는 않지만, 공식 YOLO 구현에는 번-인(Burn-In)을 사용한다. 이 기법은 손실 폭발을 피하기 위해 훈련 초기에 학습률을 감소히킨다.

## Faster R-CNN - 강력한 객체 탐지 모델
YOLO의 주요 이점은 속도에 있다. 하지만 더 복잡한 네트워크의 성능이 더 뛰어나다. 이 Faster R-CNN 모델은 상당히 빨라서 현재 GPU에서 4 ~ 5 FPS에 도달했다. Faster R-CNN은 R-CNN과 Fast R-CNN의 두 아키텍처를 거쳐 점진적으로 구축됐다. 

### Faster R-CNN의 일반 아키텍처
YOLO는 SSD(Single Shot Detector)로 간주되는데, 그 이름에서도 알 수 있듯이 이미지의 각 픽셀을 한 번에 분석한다. 이 덕분에 속도가 매우 빠르다. Faster R-CNN은 두 단계로 작동한다.

1. 첫 단계는 관심 영역(Region of Interset, RoI)을 추출하는 것이다. RoI는 이미지에서 객체를 포함할 수 있는 영역을 말한다. 각 이미지에 대해 첫 번째 단계에서 약 2000개의 RoI를 생성한다.
2. 두 번째 단계는 분류 단계(때로는 탐지 단계라고도 함)다. 2000개의 RoI 각각에 대해 합성곱 네트워크의 입력에 맞춰 정사각형으로 크기를 조정한다. 그런 다음 CNN을 사용해 RoI를 분류한다.

:bulb: R-CN과 Fast R-CNN에서 관심 영역은 선택적 탐색(Selective Search)이라고 하는 기법을 사용해 생성된다. 이 기법은 속도가 느려 Faster R-CNN 논문에서 제거됐다. 또한 선택적 탐색은 딥러닝 기법과 관련 없다.

#### 1단계 - 영역 제안
관심 영역은 영역 제안 네트워크(region proposal network, RPN)를 사용해 생성된다. RoI를 생성하기 위해 영역 제안 네트워크는 합성곱 계층을 사용한다. RPN 아키텍처는 YOLO 아키텍처와 상당히 많은 유사점을 공유한다.

- 이 아키텍처도 앵커 박스를 사용한다. Faster R-CNN 논문에서 9개 크기의 앵커 박스(3개의 세로로 긴 직사각형, 3개의 가로로 긴 직사각형, 3개의 정사각형)를 사용했다.
- 특징 볼륨을 생성하기 위해 어떤 백본이라도 사용할 수 있다.
- 그리드를 사용하며 그리드 크기는 특징 볼륨의 크기에 따라 달라진다.
- 마지막 계층은 숫자를 출력하는데, 이 숫자를 사용해서 앵커 박스를 객체에 맞는 적절한 경계 상자로 정교화할 수 있다.

그렇지만 이 아키텍처가 YOLO와 완전히 동일하지는 않다. RPN은 입력으로 이미지를 받고 관심 영역을 출력한다. 각 관심 영역은 경계 상자와 객체성 확률로 구성된다. 그 숫자를 생성하기 위해 CNN을 사용해 특징 볼륨을 추출한다. 그런 다음 특징 볼륨을 사용해 영역, 좌표, 확률을 생성한다.

1. 네트워크는 입력으로 이미지를 받아들이고 여러 합성곱 계층을 적용한다.
2. 특징 볼륨을 출력한다. 합성곱 필터가 특징 볼륨에 적용된다. 필터 크기는 3 * 3 * D이며 여기에서 D는 특징 볼륨의 깊이(예제에서는 D=512)다.
3. 특징 볼륨의 각 위치에서 이 필터는 중간 단계로 1 * D 벡터를 생성한다.
4. 두 형제 1 * 1 합성곱 계층은 객체성 점수와 경계 상자 좌표를 계산한다. k개의 경계 상자마다 두 개의 객체성 점수가 있다. 또한 앵커 박스의 좌표를 개선하기 위해 사용될 4개의 부동소수점 수도 있다.

사후 처리 단계 이후 최종 출력은 RoI 리스트다. 이 단계에서는 객체의 클래스에 대한 어떤 정보도 생성되지 않고 그 위치에 대한 정보만 생성된다.

#### 2단계 - 분류
Faster R-CNN의 두 번째 부분은 분류다. 이 단계에서는 최종 경계 상자를 출력하고, 이전 단계(RPN)의 RoI 리스트와 입력 이미지에서 계산된 특징 볼륨을 두 개의 입력으로 받는다.

:bulb: 대부분의 분류 단계 아키텍처는 이전 논문 Fast R-CNN에서 비롯됐기 때문에 동일한 이름으로 불리기도 한다. 따라서 Faster R-CNN은 RPN과 Fast R-CNN의 조합으로 볼 수 있다.

분류 부분은 입력 이미지에 대응하는 어떤 특징 볼륨과도 동작할 수 있다. 그렇지만 이전 영역-제안 단계에서 특징 맵을 이미 계산했기 때문에 여기서는 간단히 재사용하면 된다.

- 가중치를 공유한다: 다른 CNN을 사용하려면 두 개의 백본(하나는 RPN, 다른 하나는 분류 부분)에 대한 가중치를 저장해야 한다.
- 계산을 공유한다: 하나의 입력 이미지에 대해 두 개 대신 한 개의 특징 볼륨만 계산한다. 이 연산이 전체 네트워크에서 가장 비용이 많이 들기 때문에 두 번 실행하지 않아도 된다는 점에서 계산 성능이 향상된다.

##### Fast R-CNN 아키텍처
Faster R-CNN의 두 번째 단계는 첫 번째 단계에서 특징 맵과 함께 RoI 리스트를 받는다. 각 RoI에 대해 합성곱 계층이 적용돼 클래스 예측과 경계 상자 개선 정보를 얻는다.

1. RPN 단계로부터 특징 맵과 RoI를 받는다. 원본 이미지 좌표계로 생성된 RoI는 특징 맵 좌표계로 전환된다. 예제에서 CNN의 보폭은 16이다. 따라서 좌표는 16으로 나눠진다.
2. 각 RoI 크기를 조정해 완전 연결 계층의 입력과 맞춘다.
3. 완전 연결 계층을 적용한다. 모든 합성곱 네트워크의 마지막 계층과 매우 유사하다. 여기에서 특징 벡터를 얻는다.
4. 두 개의 서로 다른 합성곱 계층을 적용한다. 하나는 분류(cls라고도 함)를 처리하고 다른 하나는 RoI 개선(rgs라고도 함)을 처리한다.

최종 결과는 클래스 점수와 경계 상자 개선을 위한 부동소수점 숫자이며 이 결과를 사후 처리해서 모델의 최종 출력을 생성할 수 있다.

:bulb: 특징 볼륨의 크기는 입력 크기와 CNN 아키텍처에 따라 달라진다. 예를 들어 VGG16의 경우 특징 볼륨 크기가 w * h * 512이면 여기에서 w = input_width / 16 이고 h = input_height / 16 이다. VGG16의 경우 특징 맵의 픽셀 하나가 입력 이미지의 16개 픽셀과 동일하므로 보폭은 16이다.

합성곱 네트워크기 모든 크기의 입력을 받을 수 있지만(이미지 위에 슬라이딩 윈도우를 사용하기 때문에), 마지막의 완전 연결 계층(단계 2와 3 사이)은 입력으로 고정된 크기의 특징 볼륨을 받는다. 영역 제안의 크기가 다르기 때문에(사람이면 세로로 긴 직사각형, 사과라면 정사각형 등) 마지막 계층을 그대로 사용할 수 없다.

이 문제를 피하기 위해 Fast R-CNN에 관심 영역 풀링(RoI Pooling)이라는 기법을 도입했다. 이 기법은 다양한 크기의 특징 맵 영역을 고정된 크기의 영역으로 전환한다. 그러면 크기가 조정된 특징 영역이 마지막 분류 계층에 전달될 수 있다.

##### RoI 풀링
RoI 풀링 계층의 목표는 다양한 크기의 활성화 맵의 일부를 취하고 이를 고정된 크기로 변환하는 것으로 단순하다. 입력 활성화 맵 하부 윈도우의 크기는 h * w 이다. 목표 활성화 맵의 크기는 H * W 이다. RoI 풀링은 입력을 각 셀의 크기가 h / H * w / W 인 그리드로 나눔으로써 동작한다. 

예를 들어, 입력 크기가 h * w = 5 * 4이고 목표 활성화 맵 크기가 H * W = 2 * 2라면 각 셀의 크기는 2.5 * 2가 된다. 정수만 사용할 수 있으므로 일부 셀의 크기는 3 * 2로, 다른 셀의 크기는 2 * 2로 만든다. 그런 다음 각 셀의 최댓값을 취한다.

:bulb: RoI 풀링 계층은 최대-풀링 계층과 매우 유사하다. 차이점이라면 RoI 풀링은 다양한 크기의 입력에 동작하지만, 최대-풀링은 고정된 크기에서만 동작한다. RoI 풀링은 경우에 따라 RoI 최대-풀링(RoI max-pooling)으로 부르기도 한다.

R-CNN 원본 논문에서는 아직 RoI 풀링을 도입하지 않았다. 따라서 각 RoI는 원본 이미지에서 추출돼 크기를 조정하고 바로 합성곱 네트워크에 전달된다. 이 경우 RoI가 약 2000개가 되므로 이 아키텍처는 극도로 느리다. Fast R-CNN에서 Fast는 RoI 풀링 계층이 불러온 엄청난 속도 향상에서 비롯한다. 

### Faster R-CNN 훈련
어떤 입력 크기에서도 동작할 수 있다. Faster R-CNN은 독특한 아키텍처를 가지고 있기 때문에 일반적인 CNN처럼 훈련될 수 없다. 이 네트워크의 두 부분이 각각 별도로 훈련되며 각 부분의 특징 추출기는 동일한 가중치를 공유하지 않는다. 

#### RPN 훈련시키기
RPN의 입력은 이미지이고 출력은 RoI 리스트다. 각 이미지에는 H * W * k개의 제안 영역이 있다(여기에서 H와 W는 특징 맵의 크기를 나타내고 k는 앵커 박스의 개수다). 이 단계에서는 아직 객체의 클래스를 고려하지 않는다. 모든 제안 영역을 한 번에 훈련시키기는 어렵다. 이미지의 대부분은 배경이기 때문에 대부분의 제안 영역은 '배경'을 예측하도록 훈련된다. 그 결과 이 네트워크는 항상 배경을 예측하도록 학습한다. 대신 샘플링 기법을 선호한다. 256개의 실제 앵커 박스의 미니 배치가 구성되며 이 중 128개는 양성(positive, 객체를 포함함)이고 다른 128개는 음성(negative, 배경만 포함)이다. 이미지에서 음성 샘플이 128개보다 적으면 가능한 양성 샘플이 모두 사용되며 배치는 음성 샘플로 채워진다.

#### RPN 손실
RPN 손실은 YOLO 손실보다 단순하다. 이 손실은 두 개의 항으로 구성된다.

L({p_i}, {t_i}) = 1/N_cls * sum(L_cls (p_i, p_i')) + lambda * 1/N_reg * sum(pi' * L_reg(t_i, t_i'))

- i는 훈련 배치의 앵커 박스의 인덱스이다.
- p_i는 해당 앵커 박스가 객체일 확률이다. p_i'는 실제 확률로 앵커 박스가 '양성'이면 1이고 그렇지 않으면 0의 값을 갖는다.
- t_i는 좌표 개선을 나타내는 벡터이며, t_i'는 실제 좌표다.
- N_cls는 훈련 미니 배치에서 실제 앵커 상자의 개수다.
- N_reg는 가능한 앵커 위치 개수다.
- L_cls는 두 클래스(객체와 배경)에 대한 로그 손실이다.
- lambda는 이 손실의 두 부분의 균형을 맞추기 위한 밸런싱 매개변수다.

마지막으로 이 손실은 L_reg(t_i, t_i') = R(t_i - t_i')로 구성되며, 여기에서 R은 다음과 같이 정의되는 '평활' L1 손실 함수다.

smooth L_1(x) = { 0.5 * x^2 if |x| < 1 else |x| - 0.5}

smooth L_1 함수는 앞에서 사용했던 L2 손실을 대체할 함수로 도입됐다. 오차가 너무 중요한 경우 L2 손실이 너무 커져서 훈련이 불안정해진다. YOLO와 마찬가지로 p_i'항 덕분에 객체를 포함한 앵커 박스에 대해서만 회귀 손실이 사용된다. 이 손실은 N_cls와 N_reg의 두 부분으로 나뉜다. 이 두 값을 정규화 항이라고 하며, 미니 배치 크기를 바꾸더라도 이 손실은 균형을 잃지 않을 것이다. 마지막으로 lambda는 밸런싱 매개변수이다. 논문에서는 N_cls ~= 256, N_reg ~= 2400으로 설정했다. 논문 저자는 lambda를 10으로 설정해 두 항의 전체 가중치를 동일하게 만든다.

요약하면 YOLO와 유사하게 손실은 다음의 페널티를 부과한다.

- 첫 번째 항으로 객체성 분류에서의 오차
- 두 번째 항으로 경계 상자 개선에서의 오차

그러나 YOLO 손실과 반대로 RPN은 관심 영역만 예측하기 때문에 객체 클래스를 다루지 않는다. 손실과 미니 배치를 구성하는 방식을 제외하면 RPN은 여느 네트워크와 마찬가지로 역전파를 사용해 훈련된다.

#### Fast R-CNN 손실
R-CNN의 두 번째 단계를 Fast R-CNN이라고도 한다. 따라서 그 손실은 종종 Fast R-CNN 손실이라고 한다. Fast R-CNN 손실의 공식이 RPN 손실과 다르지만, 근본적으로는 매우 비슷하다.

L(p, u, t^u, v) = L_cls(p, u) + lambda[u >= 1] * L_Loc(t^u, v)

- L_cls(p, u)는 실제 클래스 u와 클래스 확률 p 사이의 로그 손실이다.
- L_Loc(t^u, v)는 RPN 손실의 L_reg와 동일한 손실이다.
- lambda[u >= 1]는 u >= 1일 때 1이고 그 외의 경우는 0이다.

Fast R-CNN을 훈련하는 동안 id=0으로 설정해 항상 배경 클래스를 사용한다. 실제로 ROI가 배경 영역을 포함할 수 있고 이를 배경으로 분류하는 일은 중요하다. lambda[u >= 1] 항은 배경 상자에 대해 경계 상자 오차에 페널티를 부과하는 것을 피한다. 그 외 모든 클래스에 대해 u는 0 이상의 값을 가지므로 그 오차에 페널티를 부과한다. 

#### 훈련 계획
네트워크의 두 부분 사이에 가중치를 공유해 모델이 빨라지고(CNN이 한 번만 적용되기 때문에) 가벼워진다. Faster R-CNN 논문에서 추천하는 훈련 절차는 4 단계 교대 훈련(4-step alternating training)이라고 한다.

1. RPN을 훈련해 허용할 만한 RoI를 예측한다.
2. 훈련된 RPN의 출력을 사용해 분류 파트를 훈련시킨다. RPN과 분류 부분이 별도로 훈련됐기 때문에 훈련이 끝나면 두 부분이 서로 다른 합성곱 가중치를 갖게 된다.
3. RPN의 CNN을 분류 부분의 CNN으로 교체해 합성곱 가중치를 공유하게 만든다. 공유된 CNN의 가중치를 고정시킨다. RPN의 마지막 계층을 다시 훈련시킨다.
4. 분류 부분의 마지막 계층을 RPN의 출력을 사용해 다시 훈련한다.

이 절차가 끝나면 합성곱 가중치를 공유하는 두 부분으로 이루어진 훈련된 네트워크를 얻게 된다.

### 텐서플로 객체 탐지 API
이 API는 사전에 훈련된 모델과 사용자만의 모델을 훈련하기 위한 코드를 제공한다. 객체 탐지 API는 텐서플로 핵심 라이브러리에 포함되지는 않지만 별도 저장소에서 내려받을 수 있다.

#### 사전 훈련된 모델 사용하기
COCO 데이터셋에서 훈련된 몇 가지 사전 훈련된 모델이 포함돼 있다. 이 모델들은 아키텍처에 따라 다양하다. 이들은 모두 Faster R-CNN을 기반으로 하지만 서로 다른 매개변수와 백본을 사용한다. 이 차이가 추론 속도와 성능에 영향을 미친다. 추론 시간은 mAP에 따라 길어진다.

#### 맞춤 데이터셋에서 훈련하기
COCO 데이터셋에 포함되지 않는 객체를 탐지하기 위해 모델을 훈련시킬 수 있다. 그러려면 대량의 데이터가 필요하다. 일반적으로 객체 클래스당 최소 1000개의 샘플을 확보할 것을 추천한다. 또한 훈련 데이터셋을 생성하기 위해 훈련 이미지 주위에 경계 상자를 그리고 직접 주석을 달아야 한다.

API는 객체 탐지를 사용하므로 파이썬 코드 작성을 포함하지 않는다. 대신 설정 파일을 사용해 아키텍처를 정의한다. 우수한 성능을 얻으려면 기존 설정에서 시작하는 것이 좋다.

## 요약
두 객체 탐지 모델의 아키텍처를 다뤘다. 첫 번째 아키텍처는 추론 속도가 우수한 YOLO다. 일반 아키텍처를 살펴봤으며 추론이 작동하는 방법과 함께 훈련 절차를 알아봤다. 두 번째 아키텍처인 Faster R-CNN은 최신의 탁월한 성능을 보여주는 것으로 유명하다. 이 네트워크를 구성하는 두 단계와 함께 이를 훈련시키는 방법을 분석했다. 또한 텐서플로 객체 탐지 API를 통해 Faster R-CNN을 사용하는 방법을 설명했다.

## 질문

## 참고 문헌