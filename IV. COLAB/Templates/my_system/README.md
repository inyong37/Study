# Templete of My System

```Bash
my_auto_tool_project/
├── config/                     # 설정 파일 저장
│   ├── config.yaml             # 메인 설정 파일
│   ├── logging_config.yaml     # 로깅 설정 파일
│   └── paths.json              # 경로 설정 파일 (데이터/모델 저장 위치 등)
│
├── data/                       # 데이터 관련 파일 및 디렉토리
│   ├── raw/                    # 원본 데이터
│   ├── processed/              # 전처리된 데이터
│   └── output/                 # 모델 예측 결과 저장
│
├── docs/                       # 프로젝트 문서
│   ├── README.md               # 프로젝트 설명서
│   ├── INSTALL.md              # 설치 방법
│   └── USAGE.md                # 사용 방법
│
├── models/                     # 파인 튜닝된 모델과 관련된 파일
│   ├── base_model/             # 사전 학습된 베이스 모델 저장
│   ├── fine_tuned/             # 파인 튜닝된 모델 저장
│   └── checkpoints/            # 모델 체크포인트
│
├── notebooks/                  # 실험 및 시각화 노트북
│   ├── eda.ipynb               # 데이터 탐색 분석
│   ├── training_experiment.ipynb # 모델 학습 실험
│   └── inference_demo.ipynb    # 모델 추론 데모
│
├── scripts/                    # 다양한 자동화 스크립트
│   ├── data_preprocessing.py   # 데이터 전처리 스크립트
│   ├── train_model.py          # 모델 학습 스크립트
│   ├── evaluate_model.py       # 모델 평가 스크립트
│   └── generate_image.py       # 이미지 생성 스크립트
│
├── src/                        # 주요 코드 소스
│   ├── __init__.py             # 패키지 초기화
│   ├── data_loader.py          # 데이터 로딩 모듈
│   ├── model.py                # 모델 정의 모듈
│   ├── trainer.py              # 학습 관리 모듈
│   ├── inferencer.py           # 추론 모듈
│   ├── utils/                  # 유틸리티 함수 모음
│   │   ├── __init__.py
│   │   ├── image_utils.py      # 이미지 처리 유틸리티
│   │   └── log_utils.py        # 로깅 관련 유틸리티
│   └── pipelines/              # 자동화된 파이프라인 모듈
│       ├── __init__.py
│       ├── train_pipeline.py   # 학습 파이프라인
│       └── inference_pipeline.py # 추론 파이프라인
│
├── tests/                      # 테스트 코드
│   ├── test_data_loader.py     # 데이터 로더 테스트
│   ├── test_model.py           # 모델 테스트
│   └── test_inferencer.py      # 추론 모듈 테스트
│
├── .gitignore                  # Git에 포함하지 않을 파일 목록
├── requirements.txt            # 의존성 목록
├── setup.py                    # 패키지 설정 파일
└── README.md                   # 프로젝트 개요
```
