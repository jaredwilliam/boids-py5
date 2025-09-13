# Setting this amoeba file up so that it can be plugged
# in to a different files, as a module
from py5 import *

cs = get_current_sketch()


class Amoeba:
    def __init__(self, x, y, diameter) -> None:
        self.x = x
        self.y = y
        self.diameter = diameter
        self.nuclues = {
            "fill": ["#FF0000", "#FF9900", "#FFFF00", "#00FF00", "#0099FF"][
                int(random(5))
            ],
            "x": self.diameter * random(-0.15, 0.15),
            "y": self.diameter * random(-0.15, 0.15),
            "diameter": self.diameter / random(2.5, 4),
        }
        print("Amboeba initialized!")
