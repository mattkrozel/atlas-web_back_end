#!/usr/bin/env python3
'''
multiple coroutines at thesime time of async
'''
from typing import List
import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    async routine
    args n int, max_delay
    returns list/float
    '''

    delay_list = [asyncio.create_task(
        wait_random(max_delay)) for _ in range(n)]
    return [await delay_list for delay_list in asyncio.as_completed(delay_list)]
