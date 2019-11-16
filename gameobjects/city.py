
from numpy import array

from . import GameObject


class City(GameObject):
    def __init__(self, x, y, width, height, color=(255, 255, 255)):
        vertices = array([])
        super(City, self).__init__(x, y, width, height, vertices, color=color)

    def update(self):
        pass
