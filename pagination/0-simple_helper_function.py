#!/usr/bin/env python3
'''
helper func index_range
'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    args page int and page_size int
    returns Tuple int,int
    '''
    start_index = page_size * (page - 1)
    page_range = start_index + page_size
    return (start_index, page_range)
