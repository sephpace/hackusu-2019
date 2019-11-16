
from abc import ABC, abstractmethod

from numpy import array, ndarray


class GameObject(ABC):
    def __init__(self, pos, vertices, color=(255, 255, 255)):
        if type(pos) == ndarray:
            self.pos = pos
        else:
            self.pos = array(pos)
        self.__vertices = vertices
        self.color = color

    def __str__(self): return f'x={self.pos[0]} y={self.pos[1]} color={self.color}'

    def get_vertices(self):
        return self.__vertices + self.pos

    @abstractmethod
    def update(self):
        pass
