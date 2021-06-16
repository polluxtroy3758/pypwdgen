# pypwdgen

![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/polluxtroy3758/pypwdgen/Build%20Python%20Package/main?label=main%20build&logo=githubactions&style=flat-square)
![PyPI](https://img.shields.io/pypi/v/pypwdgen?logo=pypi&style=flat-square)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pypwdgen?logo=python&style=flat-square)

Complex pasword generator

## Prerequisites
Python 3.6 minimum is required to use the `secrets` module (which is recomended instead of the `random` module to manipulate sensitive data).

## Installation
```shell
pip install pypwdgen
```

## Using the cli
```shell
python3 -m pypwdgen 
```

### Optional arguments
```text
-l, --length:
    Length of the password (default: 9)
-n, --number:
    Number of passwords to generate (default: 1)
-c, --complexity:
    Minimum number of character classes to use (default: 3)
```

### Example
```shell
# generates 20 passwords of 10 characters
python3 -m pypwdgen -l 10 -n 20
```

## Using in a script
You can easily use `pypwdgen` to generate password inside your scripts.

### Get only the password itself
```python
from pypwdgen.core import Password

passwd_string = str(Password(20, 4))  # Please note the usage of str()

# Print password
print(f"My password is: {passwd_string}")
```

### Get a Password object and use its properties
```python
from pypwdgen.core import Password

passwd_object = Password(20, 4)

# Print password complexity score from object attribute
print(f"My password complexity score is: {passwd_object.complexity}")

# Print password string from object attribute
print(f"My password is: {passwd_object.password}")
```