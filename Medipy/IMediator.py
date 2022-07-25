from abc import ABC, abstractmethod

from Medipy.IBroadcaster import IBroadcaster
from Medipy.ISender import ISender

class IMediator(ISender, IBroadcaster):

    def __init__(self):
        pass