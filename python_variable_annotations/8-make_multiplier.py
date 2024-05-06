#!/usr/bin/env python3

'''
type annotated function make_multiplier
'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    type annotated function make_multiplier
    
    args: 
        multiplier float
    
    returns: Callable Float
    '''
    return lambda x: x * multiplier
