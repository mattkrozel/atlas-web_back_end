#!/usr/bin/env python3
'''
basics of async
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
    ansyncrhonoys courotine
    args max_delay
    returns float
    '''

    actual_delay = random.uniform(0, max_delay)
    await asyncio.sleep(actual_delay)
    return actual_delay
