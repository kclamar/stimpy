from stimpy import Animate, Scene, Trial, Window, animate, visual

color = (1, 1, 1)
dur = 2.0

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

scene = Scene(color=(-1, -1, -1), units="deg")
scene.add(sweeping, begin=0, dur=dur)
scene.add(circulating, begin=2, dur=dur)
scene.add(spiraling, begin=4, dur=dur)
scene.add(looming, begin=6, dur=dur)
scene.add(flashing, begin=8, dur=dur)
scene.add(dimming, begin=10, dur=dur)
scene.add(grating, begin=12, dur=dur)

win = Window(distance=1, width=26)
trial = Trial(scene, win=win, dur=40)
trial.start()
