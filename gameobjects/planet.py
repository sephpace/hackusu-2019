
from numpy import array

from . import GameObject


class Planet(GameObject):
    def __init__(self, pos, color=(255, 255, 255)):
        vertices = array([])
        super(Planet, self).__init__(pos, vertices, color=color)

    def update(self):
        pass
