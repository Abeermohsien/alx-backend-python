#!/usr/bin/env python3
'''module Task 8.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''multiplier.
    '''
    return lambda x: x * multiplier
