#!/usr/bin/env python3
'''
async comprehensions
'''
import asyncio
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    '''
    coroutine will collect 10 random nums
    returns list float
    '''
    return [number async for number in async_generator()]

