#!/usr/bin/env python3
'''module 2
'''
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''list of 10 nums'''
    return [num async for num in async_generator()]
