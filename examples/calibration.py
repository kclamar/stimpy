from stimpy import Scene, Trial, Window, visual

screen_distance = 1
screen_width = 34.5

bkg_color = (1, 1, 1)
bkg_width_cm = 5
bkg_height_cm = .6

dot_color = (-1, -1, 1)
dot_size = (5, 5)
dot_altitude = 0
dot_azimuths = (-60, -45, 0, 45, 60)

bright_rect = visual.Rect(
    fillColor=bkg_color,
    width=bkg_width_cm,
    height=bkg_height_cm,
    units="cm",
    lineWidth=0,
)

dots = [
    visual.Circle(
        fillColor=dot_color,
        size=dot_size,
        pos=(az, dot_altitude),
        units="degFlatPos",
    )
    for az in dot_azimuths
]

scene = Scene(color=(-1, -1, -1), units="deg")
scene.add(dots, begin=0, dur=1e7)
scene.add(bright_rect, begin=0, dur=1e7)

win = Window(distance=screen_distance, width=screen_width)
trial = Trial(scene=scene, win=win)
trial.start()
