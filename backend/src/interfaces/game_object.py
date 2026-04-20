# 1. Base ABC
from abc import ABC, abstractmethod

from nanoid import generate

from src.interfaces.placeable import Placeable


class GameObject(Placeable, ABC):
    def __init__(self):
        # Generate 10-character ID
        self.id = generate(size=10) 

    @abstractmethod
    def get_info(self):
        pass
        