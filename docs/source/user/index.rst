:orphan:

.. _user:

#################
StimPy user guide
#################

This guide is an overview and explains the important features.

A simple visual stimulus
========================

.. code-block:: python

    import stimpy as sp

    circle = sp.visual.Circle(
        size=(2, 2), fillColor=(1, 1, 1),
        pos=sp.Animate([(-45, 0), (45, 0)], [2, 2])
    )

    stimuli = sp.Stimuli()
    stimuli.append(circle, begin=0, dur=10)

    win = sp.Window(distance=13, width=26, units="degFlat")
    trial = sp.Trial(stimuli, win=win)
    trial.run()

