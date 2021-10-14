# Chapter 05 딥러닝의 한계를 뛰어넘는 최신 기술
## 01 메타 학습(Meta-Learning)
### 메타 학습의 개념

### 메타 최적화 학습(Meta Optimizer Learning)

### 모델에 자유로운 메타 학습(Model-Agnostic Meta Learning, MAML)
Meta Congnition, Learning to Learn, Meta Optimizer Learning, Meta Loss, Model-Agnostic Meta Learning(MAML), Model-Agnostic, MAML

## 02 원샷 학습(One-Shot Leanring) :star:
Way, Shot, Few-Shot Learning, Pre-Trained Network, Feature, Zero-Shot, Similarity Function, Clustering Algorithm

### 원샷 학습의 개념
원샷 학습은 대표적인 메타 학습의 방법론으로 소량의 데이터를 이용하여 학습 방법을 수행한다. 보통 딥러닝은 분류별로 수백 개 이상의 데이터를 학습해야 성공적으로 학습을 실행할 수 있지만 사람은 딥러닝에 비해 적은 데이터를 가지고도 쉽게 지식을 학습할 수 있다. 원샷 학습의 기술은 아직 초기 단계에 있지만 이미지 인식 분야에서 조금씩 성과가 나오고 있다.

### 원샷 학습의 기본 '웨이(Way)와 샷(Shot)'
원샷 학습에서 샷은 분류별로 학습에 활용되는 데이터의 수를 의마하는 것으로 5 샷은 분류별로 5 개의 데이터를 활용하여 학습하는 것이다. 웨이는 분류의 개수를 의미하는 것인데 예를 들어 5 웨이-3 샷은 5 가지 뷴루에서 3 개의 데이터를 활용하여 학습하는 것이다. 샷은 낮을수록, 웨이는 높을수록 학습이 어렵기 때문에 원샷 학습은 매우 도전적인 과제에 해당한다. 학계에서는 퓨샷 학습 (Few-Shot Learning)이라는 주제로 10~20개의 데이터를 활용한 접근을 중시하는데, 원샷 학습 역시 다양한 활용 방안이 제시되고 있다. 

### 원샷 학습의 과정
원샷 학습은 한 개의 데이터로 학습을 하기 때문에 인공신경망의 입력과 출력에서는 한 쌍이 존재한다. 여기에서 인공신경망은 일반적으로 이미 학습된 신경망(Pre-Trained Network)을 활용한다. 인공신경망에서 원샷에 해당하는 데이터가 입력에 들어가면 출력에서는 특성(Feature)이 추출된다. 이러한 특성은 일종의 벡터로 데이터의 특징을 표현한다. 추출된 특성은 유사도 함수나 군집 알고리즘을 활용하여 구별하고, 결과 값을 통해 신경망의 가중치를 변경하거나 군집 알고리즘의 모수를 변경한다. 이것이 바로 원샷 학습의 과정이다.

### 원샷 학습의 한계와 전망
원샷 학습에서 이미 학습된 인공신경망이 필요하다는 것은 그것을 학습시키기 위해 여전히 많은 데이터가 필요하다는 점이 한계로 보인다. 이러한 원샷 학습에서는 학습된 신경망이 많이 공개되어 있는 이미지 인식 분야에서 중요한 결과가 나오고 있다. 원샷 학습을 넘어 제로샷 학습이라는 개념도 등장하고 있는데 이는 한 개의 데이터도 학습하지 않고 분류한다는 것이다. 원샷 학습이 딥러닝의 고질적인 데이터 수급 문제에 대해 원척적인 해결책을 주는 것은 아니지만 이러한 접근이 고도화되는 과정에서 많은 대안이 나올 것이라 기대된다.

### 원샷 학습의 과정(이미지 인식 4웨이-1샷)
1. 학습된 신경망에서 특성을 추출하고, 마지막 FC 층의 벡터를 활용한다.
2. 특성으로 손실 함수를 정의하고, 이를 통해 신경망을 학습한다.

유사도 함수(Similarity Function)을 이용해 두 특성이 얼마나 비슷한 지를 측정하거나 군집 알고리즘(Clustering Algorithm)을 이용해 손실 함수를 정의하여 학습된 신경망을 원샷 데이터로 재학습된 신경망으로 학습한다.

## 03 지속적인 학습(Continual Learning)
### 지속적인 학습의 의미

### 인공신경망과 치명적 망각

### 생성 모델을 활용하 지속적인 학습

### 동적으로 확자 가능한 인공신경망(Dynamically Expandable Network, DEN)
Catastrophic Forgetting, Elastic Weight Consolidation (EWC), Dynamically Expandable Network (DEN)

## 04 신경망 구조 탐색(Neural Architecture Search)
### 신경망 구조 탐색의 개념

### 신경망 구조 탐색의 과정

### 신경망 구조 탐색의 응용(AutoML)
Hyper-Parameter, AutoML

## 05 스파이킹 신경망(Spiking Neural Network)
### 스파이킹 신경망의 개념

### 스파이크와 스파이크 트레인

### 스파이킹 신경망의 비지도 학습

### 스파이킹 신경망의 지도 학습
Neuron, Spike, Spike Train, Layer-Wise, Synaptic Timing Dependent Plasticity (STDP), Gradient-Descent Method, Firing, Fire

## 06 활성 학습(Active Learning)
### 활성 학습의 개념

### 활성 학습과 불확실성
Uncertainty, 활성 학습은 이러한 문제를 해결하기 위해 라벨이 주어지지 않은 데이터에 자동으로 라벨을 붙일 수 있도록 고안된 방법이다.

## 07 그래프 신경망 (Graph Neural Network)
### 그래프의 기본 개념

### 그래프 신경망의 개념

### 그래프 신경망의 연구 동향
Vertex, Edge, Attribute, Node, Invariance, 인공신경망으 입력 값을 선정함에 있어 그 순서에도 영향을 받는다.

## 08 메모리 네트워크(Memory Network)
### 메모리 네트워크의 개념

### 메모리 네트워크의 구조

### 종단간(End-to-End) 메모리 네트워크
Long-Term Dependency, Question & Answer, Input Feature Map, Generalization, Output, Response, Supporting Fact, Embedding, IGOR

## 09 뉴럴 튜링 머신(Neural Turing Machine)
### 뉴럴 튜링 머신의 개념

### 뉴럴 튜링 머신의 제어기

### 주소 지정 메커니즘
Alan Turing, Controller, Read Head, Write Head, Addressable Memory, Turing-Complete, Differentiable Neural Computer, Content Addressing, Interpolation, Convolutional Shift, Sharpening

## 10 BERT 모델
### 자연어 처리 알고리즘의 성능

### BERT 구조의 개념적 이해

### BERT의 학습 방법과 결과
Bidrectional Encoder Representations from Transformer, BERT, Fine-Tuning, Masked Language Model, Pre-Trained, korBERT, MNLI, QQP. QNLI, SST-2, CoLA, STS-B, MRPC, RTE, SQuAD v1.1, SQuAD v2.0, SWAG, Google

## 11 생성적 사전 학습 모델
### GPT의 개념

### GPT-2(재학습 과정이 없는 언어 모델)

### GPT-3(퓨삿 학습을 통한 성능 향상)
OpenAI, Generative Pre-Training, GPT, Semi-Supervised Learning, Fine-Tuning, 10, Zero-shot, 100, Few-shot, Language Model, Scale-up

## 12 캡슐 네트워크(Capsule Network)
### 캡슐 네트워크의 개념

### 캡슐 네트워크의 구조
Entity, Property, Primary Capsule, Dynamic Routing, Reconstruction

## :bulb: 인공지능의 미중 기술 패권
### 미국과 중국의 기술 패권 경쟁

### 인공지능의 다크호스 - 중국

### 인공지능의 전통적인 강자 - 미국
