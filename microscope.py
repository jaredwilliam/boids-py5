import py5
from amoeba import Amoeba

jerry = Amoeba(400, 400, 50)


def setup():
    py5.size(800, 800)


def draw():
    py5.background("#004477")
    # nucleus
    py5.fill(jerry.nuclues["fill"])
    py5.no_stroke()
    py5.circle(
        jerry.x + jerry.nuclues["x"],
        jerry.y + jerry.nuclues["y"],
        jerry.nuclues["diameter"],
    )

    # cell membrane
    py5.fill(0x880099FF)
    py5.stroke("#FFFFFF")
    py5.stroke_weight(3)
    py5.circle(jerry.x, jerry.y, jerry.diameter)


py5.run_sketch()
