#!/usr/bin/env python3
'''module Task 7.
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''tuple of kwy and their value square.
    '''
    return (k, float(v**2))
