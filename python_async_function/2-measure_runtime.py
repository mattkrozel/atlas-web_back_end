#!/usr/bin/env python3
'''
measures runtime
'''

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    measures total execution time
    
    args n int, max_delay int
    returns float total_time
    '''
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    time_process = time.perf_counter() - start_time
    return time_process / n
