
from . import GameObject


class Projectile(GameObject):
    def __init__(self, pos, color=(255, 255, 255), scale=0.5, rotation=0.0):
        super(Projectile, self).__init__(pos, color=color, scale=scale, rotation=rotation)
        self.load_model('raw_models/projectile.yml')

    def update(self):
        pass
