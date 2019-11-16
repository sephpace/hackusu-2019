
import numpy as np

from . import GameObject


class Planet(GameObject):
    def __init__(self, pos, color=(255, 255, 255), scale=15.0, rotation=0.0, gravity=1.0):
        super(Planet, self).__init__(pos, color=color, scale=scale, rotation=rotation)
        self.load_model('raw_models/planet.yml')
        self.gravity = gravity

    def gravitate(self, obj):
        direction = self.pos - obj.pos
        direction = direction / np.linalg.norm(direction)
        force = direction * self.gravity / self.distance(obj.pos)
        obj.pos += force

    def distance(self, point):
        return np.linalg.norm(point - self.pos) - self.scale

    def update(self):
        pass
