
from abc import ABC, abstractmethod
import math

import numpy as np
import yaml


class GameObject(ABC):
    def __init__(self, pos, vertices=np.array([]), color=(255, 255, 255), scale=1.0, rotation=0.0):
        if type(pos) == np.ndarray:
            self.pos = pos
        else:
            self.pos = np.array(pos)
        self.__vertices = vertices
        self.color = color
        self.scale = scale
        self.rotation = rotation

    def __str__(self): return f'x={self.pos[0]} y={self.pos[1]} color={self.color}'

    def get_vertices(self):
        v = np.copy(self.__vertices)
        rotation_matrix = np.array([[math.cos(self.rotation), -math.sin(self.rotation)],
                                   [math.sin(self.rotation), math.cos(self.rotation)]])
        v = np.transpose(np.matmul(rotation_matrix, np.transpose(v)))
        v *= self.scale
        v += self.pos
        return v

    def load_model(self, file_path):
        with open(file_path, 'r') as file:
            self.__vertices = np.array(yaml.full_load(file))

    @abstractmethod
    def update(self):
        pass
