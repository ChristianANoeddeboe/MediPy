
from abc import ABC, abstractmethod

class IRequest(ABC):

    @abstractmethod
    async def handle(self, request, cancellation_token):
        pass