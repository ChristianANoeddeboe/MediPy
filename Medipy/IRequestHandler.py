from abc import ABC, abstractmethod
from typing import TypeVar, Generic

K = TypeVar("K")
V = TypeVar("V")

class IRequestHandler(ABC, Generic[K, V]):

    @abstractmethod
    async def handle(self, request: K, cancellation_token) -> V:
        pass