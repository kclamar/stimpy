from stimpy import Animate, Stimuli, Trial, Window, animate, visual

color = (1, 1, 1)
dur = 2.0

win = Window(
    monitor="testMonitor",
    distance=10,
    width=35,
    units="deg",
    color=(-1, -1, -1),
    fullscr=True,
)

sweep = Animate([(-90, 0), (90, 0), (0, 0)], [dur / 2, dur / 2, 0])
sweeping = visual.Circle(
    size=(2, 8), fillColor=color, pos=sweep, ori=animate.ori.Tangential(sweep)
)

circulation = animate.pos.Circulating(
    center=(0, 0), size=(10, 10), period=dur, init_angle=90, clockwise=True
)
circulating = visual.Circle(
    size=(2, 8),
    fillColor=color,
    pos=circulation,
    ori=animate.ori.Tangential(circulation),
)

spiral = animate.pos.Circulating(
    center=(0, 0),
    period=1,
    clockwise=True,
    init_angle=0,
    size=Animate([(0, 0), (60, 30)], [dur, 0]),
)

spiraling = visual.Circle(
    fillColor=color,
    pos=circulation,
    size=Animate([(0, 0), (2, 10)], [dur, 0]),
    ori=animate.ori.Tangential(circulation),
)

looming = visual.Circle(
    fillColor=color, pos=(0, 0), size=Animate([(0, 0), (90, 90)], [dur, 0])
)

flashing = visual.Rect(
    size=(180, 90),
    fillColor=color,
    opacity=Animate([1, 0], [1, 1], calc_mode="discrete"),
)

dimming = visual.Rect(
    fillColor=color,
    pos=(0, 0),
    size=(180, 90),
    opacity=Animate([1, 0], [dur, 0]),
)

grating = visual.GratingStim(
    size=(180, 90), sf=0.1, phase=Animate([0, 1], [1, 0])
)

stimuli = Stimuli()
stimuli.append(sweeping, 0, dur)
stimuli.append(circulating, 2, dur)
stimuli.append(spiraling, 4, dur)
stimuli.append(looming, 6, dur)
stimuli.append(flashing, 8, dur)
stimuli.append(dimming, 10, dur)
stimuli.append(grating, 12, dur)

trial = Trial(stimuli, win=win)
trial.run()
