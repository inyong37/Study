# Change Python Version of Virtual Environment

### Date

2025-01-09-Thu.

### Environment

Ubuntu 20.04.6 LTS

## Change Python Version of Virtual Environment

### 0. Install Python Version

```Bash
sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.10 python3.10-venv python3.10-distutils
```

Verify:

```Bash
python3.10 --version
```

### 1. Replace venv/python

Deactivate vevn:

```Bash
deactivate
```

Remove and link:

```Bash
rm -rf {venv}/bin/python
rm -rf {venv}/bin/python3
ln -s /usr/bin/python3.10 {venv}/bin/python
ln -s /usr/bin/python3.10 {venv}/bin/python3
```

Update packages:

```Bash
source {venv}/bin/activate
python -m ensurepip --upgrade
python -m pip install --upgarde pip setuptools wheel
```

### Appendix

Make a new venv:

```Bash
rm -rf {venv}
python3.10 -m venv {venv}
source {venv}/bin/activate
```

Alias and use!
