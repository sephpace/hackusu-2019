
from gameobjects import Camera


class Scene:
    def __init__(self, screen):
        self.screen = screen
        self.camera = Camera()
        self.game_objects = []

    def add(self, game_object): self.game_objects.append(game_object)

    def update(self):
        for g in self.game_objects:
            g.update()
            g.draw(self.screen)
