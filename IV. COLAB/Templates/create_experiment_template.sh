#!/bin/bash

# 프로젝트 이름 입력 받기
if [ -z "$1" ]; then
  echo "프로젝트 이름을 입력하세요. 예: ./create_structure.sh my_project_name"
  exit 1
fi

PROJECT_NAME=$1

# 프로젝트 루트 디렉토리 생성
mkdir -p "$PROJECT_NAME"

# 하위 디렉토리 및 파일 생성
mkdir -p "$PROJECT_NAME/config"
touch "$PROJECT_NAME/config/experiment_config.yaml"

mkdir -p "$PROJECT_NAME/data/raw"
mkdir -p "$PROJECT_NAME/data/processed"

mkdir -p "$PROJECT_NAME/experiments/exp1/logs"
mkdir -p "$PROJECT_NAME/experiments/exp1/models"
mkdir -p "$PROJECT_NAME/experiments/exp1/results"
mkdir -p "$PROJECT_NAME/experiments/exp2/logs"
mkdir -p "$PROJECT_NAME/experiments/exp2/models"
mkdir -p "$PROJECT_NAME/experiments/exp2/results"

mkdir -p "$PROJECT_NAME/notebooks"
touch "$PROJECT_NAME/notebooks/experiment_analysis.ipynb"

mkdir -p "$PROJECT_NAME/src"
touch "$PROJECT_NAME/src/data_loader.py"
touch "$PROJECT_NAME/src/model.py"
touch "$PROJECT_NAME/src/train.py"
touch "$PROJECT_NAME/src/evaluate.py"

mkdir -p "$PROJECT_NAME/tests"
touch "$PROJECT_NAME/tests/test_model.py"

touch "$PROJECT_NAME/requirements.txt"
touch "$PROJECT_NAME/README.md"

echo "Directory structure for project '$PROJECT_NAME' created successfully."

