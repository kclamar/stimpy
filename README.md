[![PyPI version](https://badge.fury.io/py/stimpy.svg)](https://pypi.python.org/pypi/stimpy)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/stimpy.svg)](https://pypi.python.org/pypi/stimpy)
[![Documentation Status](https://readthedocs.org/projects/stimpy/badge/?version=latest)](https://stimpy.readthedocs.io/en/latest/?badge=latest)
# StimPy

[StimPy](https://github.com/kclamar/stimpy) is a thin [PsychoPy](https://www.psychopy.org/) wrapper to simplify the creation of visual stimuli.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install StimPy.

```bash
pip install stimpy
```

## Usage

```python
import stimpy as sp

circle = sp.visual.Circle(
    size=(2, 2), fillColor=(1, 1, 1),
    pos=sp.Animate([(-45, 0), (45, 0)], [2, 2])
)

stimuli = sp.Scene(color=(-1, -1, -1), units="degFlat")
stimuli.add(circle, begin=0, dur=10)

win = sp.Window(distance=13, width=26)
trial = sp.Trial(stimuli, win=win)
trial.start()
```
