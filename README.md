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

## Notes from 1/24/17 (HW1 submission)

Implemented bubblesort and quicksort functions in algs.py.
Counted conditionals and assignments.
Plotted results in run_stuff.py.
Tested edge cases in test_algs.py.
Other scripts were for learning how to plot, run from modules, and try counting.
