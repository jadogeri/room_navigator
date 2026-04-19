# 1. Base ABC
from abc import ABC, abstractmethod

from nanoid import generate


class GameObject(ABC):
    def __init__(self):
        # Generate 10-character ID
        self.id = generate(size=10) 

    @abstractmethod
    def get_info(self):
        pass
        