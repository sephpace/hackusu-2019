
from . import GameObject


class Planet(GameObject):
    def __init__(self, pos, color=(255, 255, 255), scale=15.0, rotation=0.0):
        super(Planet, self).__init__(pos, color=color, scale=scale, rotation=rotation)
        self.load_model('raw_models/planet.yml')

    def update(self):
        pass
