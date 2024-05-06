#!/usr/bin/env python3
'''
coroutine called async gen no args
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
    coroutine will loop 10 times
    each time delay 1 sec
    yield random number betwen 0-10
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
