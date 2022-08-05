
from abc import ABC, abstractmethod


class IContext(ABC):

    @abstractmethod
    def call(self, val: int):
        pass