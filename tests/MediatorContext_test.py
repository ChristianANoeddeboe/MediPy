# import asyncio
# import sys, inspect
# import os

# PROJECT_ROOT = os.path.abspath(os.path.join(
#                   os.path.dirname(__file__), 
#                   os.pardir)
# )

# # print(sys.path)
# sys.path.append(PROJECT_ROOT)

from tests.mediator.BasicContext import BasicContext
from Medipy import Mediator
from tests.mediator.TestCommand import TestCommand
from unittest import IsolatedAsyncioTestCase

class MediatorContextTest(IsolatedAsyncioTestCase):
    
    def setUp(self):
        context = BasicContext()
        services = [context]
        self.mediator = Mediator.Mediator(services)
        
    async def test(self):
        test = TestCommand()
        test.id = 1
        test.title = "Test"
        res: TestCommand = await self.mediator.send(test)
        assert res == 2
