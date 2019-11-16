
from . import GameObject


class City(GameObject):
    def __init__(self, pos, color=(255, 255, 255), scale=5.0, rotation=0.0):
        super(City, self).__init__(pos, color=color, scale=scale, rotation=rotation)
        self.load_model('raw_models/city.yml')

    def update(self):
        pass
