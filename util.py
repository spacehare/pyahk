from main import a


def click(coords):
    orig = a.get_mouse_position()
    a.mouse_move(*coords)
    a.click()
    a.mouse_move(*orig)
