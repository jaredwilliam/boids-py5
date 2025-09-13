import py5


def setup():
    py5.size(500, 500)
    py5.no_fill()
    py5.stroke("#FFFFFF")
    py5.stroke_weight(3)
    py5.frame_rate(2.5)


def draw():
    py5.background("#004477")

    if py5.frame_count % 2 == 0:
        py5.ellipse(250, 140, 47, 47)
    else:
        py5.ellipse(250, py5.height - 140, 47, 47)


py5.run_sketch()
