
from numpy import array

from . import GameObject


class Projectile(GameObject):
    def __init__(self, x, y, width, height, color=(255, 255, 255)):
        vertices = array([])
        super(Projectile, self).__init__(x, y, width, height, vertices, color=color)

    def update(self):
        pass
