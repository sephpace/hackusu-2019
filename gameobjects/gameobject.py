
from abc import ABC, abstractmethod

from numpy import array


class GameObject(ABC):
    def __init__(self, x, y, width, height, vertices, color=(255, 255, 255)):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.__vertices = vertices

    def get_vertices(self):
        return self.__vertices + array([self.x, self.y])

    @abstractmethod
    def update(self):
        pass
