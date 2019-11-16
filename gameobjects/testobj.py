
from numpy import array

from . import GameObject


class TestObj(GameObject):
    def __init__(self, x, y, width, height, color=(255, 255, 255)):
        vertices = array([[0, 0], [10, 0], [10, 10], [0, 10]])
        super(TestObj, self).__init__(x, y, width, height, vertices, color=color)

    def update(self):
        pass
