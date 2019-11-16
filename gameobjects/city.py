
import numpy as np

from . import GameObject
from .projectile import Projectile


class City(GameObject):
    def __init__(self, pos, color=(255, 255, 255), scale=5.0, rotation=0.0):
        super(City, self).__init__(pos, color=color, scale=scale, rotation=rotation)
        self.load_model('raw_models/city.yml')

    def shoot(self, scene, point):
        """
        Shoots in the direction of the given point.
        """
        direction = point - self.pos
        direction = direction / np.linalg.norm(direction)
        bullet = Projectile(np.copy(self.pos), velocity=direction)
        scene.add(bullet)

    def update(self):
        pass
