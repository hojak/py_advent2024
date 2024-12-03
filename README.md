# py_advent2024
My humble attempts around the advent of code 2024. This time in python.


## Getting Started
First you need a running Python 3 envidonment.
On Windows Powershell, you can install it e.g. via

```shell
winget install python3
```

Create / activate virtual python environment

```shell
python -m venv venvsource venv/bin/activate
```

Install the required python packages:

```shell
pip install -r requirements.txt
```

Install modules

```shell
pip install --editable .
```

### Execute all tests Once

```shell
python -m pytest
```

### Launch the Test Runner in Watch Mode

```shell
ptw . --now --last-failed --new-first
```