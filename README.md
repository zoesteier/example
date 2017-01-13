# example

[![Build
Status](https://travis-ci.org/zoesteier/example.svg?branch=master)](https://travis-ci.org/zoesteier/example)

Example python project with testing.

## usage

To use the package, first run

```
conda install --yes --file requirements.txt
```

to install all the dependencies in `requirements.txt`. Then the package's
main function (located in `example/__main__.py`) can be run as follows

```
python -m example
```

## testing

Testing is as simple as running

```
python -m pytest
```

from the root directory of this project.
