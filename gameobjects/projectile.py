
from numpy import array

from . import GameObject


class Projectile(GameObject):
    def __init__(self, pos, color=(255, 255, 255), scale=0.5, rotation=0.0, velocity=array([0., 0.])):
        super(Projectile, self).__init__(pos, color=color, scale=scale, rotation=rotation)
        self.load_model('raw_models/projectile.yml')
        self.velocity = velocity

    def update(self):
        self.pos += self.velocity
