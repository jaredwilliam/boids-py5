import py5


def setup():
    py5.size(1200, 1200)

    # dark blue background
    py5.background("#004477")
    py5.no_fill()
    py5.stroke("#FFFFFF")
    py5.stroke_weight(3)

    for column in range(24):
        for row in range(24):
            if int(py5.random(2)) == 1:
                py5.arc(column * 50, row * 50, 50, 50, 0, py5.PI / 2)
                py5.arc(
                    column * 50 + 50, row * 50 + 50, 50, 50, py5.PI, py5.PI + py5.PI / 2
                )
            else:
                py5.arc(column * 50 + 50, row * 50, 50, 50, py5.PI / 2, py5.PI)
                py5.arc(
                    column * 50, row * 50 + 50, 50, 50, py5.PI + py5.PI / 2, 2 * py5.PI
                )


# def draw():
#     py5.rect(py5.mouse_x, py5.mouse_y, 10, 10)


py5.run_sketch()
