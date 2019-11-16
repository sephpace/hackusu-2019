
from numpy import array

from . import GameObject


class TestObj(GameObject):
    def __init__(self, pos, color=(255, 255, 255)):
        vertices = array([[-2.5, -2.5], [2.5, -2.5], [2.5, 2.5], [-2.5, 2.5]])
        super(TestObj, self).__init__(pos, vertices, color=color)

    def update(self):
        pass
