# 1. Base ABC
from abc import ABC, abstractmethod

from src.interfaces.placeable import Placeable


class GameObject(Placeable, ABC):
    def __init__(self, id: str | None = None):
        self.id: str = id

    @abstractmethod
    def get_info(self):
        pass
        