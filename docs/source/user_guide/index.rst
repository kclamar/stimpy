:orphan:

.. _user:

#################
StimPy user guide
#################

This guide is an overview and explains the important features.

Quickstart
========================

Import StimPy:

.. code-block:: python

    import stimpy as sp

Instantiate a circle that moves in a rectangular trajectory:

.. code-block:: python

    circle = sp.visual.Circle(
        size=(2, 2), fillColor=(1, 1, 1),
        pos=sp.Animate([(-40, -20), (-40, 20), (40, 20), (40, -20)], [1, 1, 1, 1])
    )

Add the circle to a scene:

.. code-block:: python

    scene = sp.Scene(color=(-1, -1, -1), units="deg")
    scene.add(circle, begin=0, dur=4)

Create a window and display the stimulus:

.. code-block:: python

    win = sp.Window(distance=13, width=26)
    trial = sp.Trial(scene, win=win)
    trial.start()

(Optional) Save the stimulus as a movie:

.. code-block:: python

    trial.save_movie("example.mp4", fps=60)

.. image:: ../_static/example.gif
