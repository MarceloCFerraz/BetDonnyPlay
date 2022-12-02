from PIL import ImageGrab


def printWholeScreen(x, y):
    # ImageGrab-To capture the screen image in a loop.
    # Bbox used to capture a specific area.
    return ImageGrab.grab(bbox=(0, 0, x, y))


def printScreen(x1, y1, x2, y2):
    # ImageGrab-To capture the screen image in a loop.
    # Bbox used to capture a specific area.
    return ImageGrab.grab(bbox=(x1, y1, x2, y2))
