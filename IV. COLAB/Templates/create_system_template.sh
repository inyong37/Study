#!/bin/bash

# 프로젝트 이름 입력 받기
if [ -z "$1" ]; then
  echo "프로젝트 이름을 입력하세요. 예: ./create_auto_tool_structure.sh my_project_name"
  exit 1
fi

PROJECT_NAME=$1

# 프로젝트 루트 디렉토리 생성
mkdir -p "$PROJECT_NAME"

# 하위 디렉토리 및 파일 생성
mkdir -p "$PROJECT_NAME/config"
touch "$PROJECT_NAME/config/config.yaml"
touch "$PROJECT_NAME/config/logging_config.yaml"
touch "$PROJECT_NAME/config/paths.json"

mkdir -p "$PROJECT_NAME/data/raw"
mkdir -p "$PROJECT_NAME/data/processed"
mkdir -p "$PROJECT_NAME/data/output"

mkdir -p "$PROJECT_NAME/docs"
touch "$PROJECT_NAME/docs/README.md"
touch "$PROJECT_NAME/docs/INSTALL.md"
touch "$PROJECT_NAME/docs/USAGE.md"

mkdir -p "$PROJECT_NAME/models/base_model"
mkdir -p "$PROJECT_NAME/models/fine_tuned"
mkdir -p "$PROJECT_NAME/models/checkpoints"

mkdir -p "$PROJECT_NAME/notebooks"
touch "$PROJECT_NAME/notebooks/eda.ipynb"
touch "$PROJECT_NAME/notebooks/training_experiment.ipynb"
touch "$PROJECT_NAME/notebooks/inference_demo.ipynb"

mkdir -p "$PROJECT_NAME/scripts"
touch "$PROJECT_NAME/scripts/data_preprocessing.py"
touch "$PROJECT_NAME/scripts/train_model.py"
touch "$PROJECT_NAME/scripts/evaluate_model.py"
touch "$PROJECT_NAME/scripts/generate_image.py"

mkdir -p "$PROJECT_NAME/src/utils"
touch "$PROJECT_NAME/src/__init__.py"
touch "$PROJECT_NAME/src/data_loader.py"
touch "$PROJECT_NAME/src/model.py"
touch "$PROJECT_NAME/src/trainer.py"
touch "$PROJECT_NAME/src/inferencer.py"
touch "$PROJECT_NAME/src/utils/__init__.py"
touch "$PROJECT_NAME/src/utils/image_utils.py"
touch "$PROJECT_NAME/src/utils/log_utils.py"
mkdir -p "$PROJECT_NAME/src/pipelines"
touch "$PROJECT_NAME/src/pipelines/__init__.py"
touch "$PROJECT_NAME/src/pipelines/train_pipeline.py"
touch "$PROJECT_NAME/src/pipelines/inference_pipeline.py"

mkdir -p "$PROJECT_NAME/tests"
touch "$PROJECT_NAME/tests/test_data_loader.py"
touch "$PROJECT_NAME/tests/test_model.py"
touch "$PROJECT_NAME/tests/test_inferencer.py"

touch "$PROJECT_NAME/.gitignore"
touch "$PROJECT_NAME/requirements.txt"
touch "$PROJECT_NAME/setup.py"
touch "$PROJECT_NAME/README.md"

echo "Directory structure for project '$PROJECT_NAME' created successfully."

