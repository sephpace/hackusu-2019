
from abc import ABC, abstractmethod


class GameObject(ABC):
    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass
