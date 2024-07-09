#!/usr/bin/env python3
'''module 1
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    ''' sequences of 10numbers.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
