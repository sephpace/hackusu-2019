
from numpy import array

from . import GameObject


class Projectile(GameObject):
    def __init__(self, pos, color=(255, 255, 255)):
        vertices = array([])
        super(Projectile, self).__init__(pos, vertices, color=color)

    def update(self):
        pass
