# AI Experiment

This is a simple directory structure for machine learning experiments, suitable for organizing and managing various experiments efficiently.

## Directory Structure

```plaintext
ml_experiment_project/
├── config/                     # Configuration files
│   └── experiment_config.yaml  # Experiment configuration file
│
├── data/                       # Data-related files
│   ├── raw/                    # Raw data
│   └── processed/              # Processed data
│
├── experiments/                # Experiment results
│   ├── exp1/                   # First experiment
│   │   ├── logs/               # Experiment logs
│   │   ├── models/             # Trained models
│   │   └── results/            # Experiment results (predictions, visualizations, etc.)
│   └── exp2/                   # Second experiment
│       ├── logs/
│       ├── models/
│       └── results/
│
├── notebooks/                  # Jupyter notebooks for experiments
│   └── experiment_analysis.ipynb  # Analysis notebook
│
├── src/                        # Main source code
│   ├── data_loader.py          # Data loading module
│   ├── model.py                # Model definition module
│   ├── train.py                # Training script
│   └── evaluate.py             # Evaluation script
│
├── tests/                      # Test files
│   └── test_model.py           # Model-related tests
│
├── requirements.txt            # Dependency list
└── README.md                   # Project overview
```
