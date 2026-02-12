# My ML Project

A machine learning project with automated CI/CD pipeline and virtual environment setup.

## Project Structure

```
my-ml-project/
├── .github/
│   └── workflows/
│       └── ci-cd.yml        # CI/CD pipeline configuration
├── train_model.py           # Model training script
├── test_model.py            # Unit tests
├── requirements.txt         # Python dependencies
├── README.md               # This file
└── .gitignore              # Git ignore rules
```

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Train the model:

```bash
python train_model.py
```

3. Run tests:

```bash
python test_model.py
```

## CI/CD

The project uses GitHub Actions for automated testing on push and pull requests.
