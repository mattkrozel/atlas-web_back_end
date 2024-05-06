#!/usr/bin/env python3

'''
type annotated function sum_list
'''

from typing import List


def sum_list(input_list: List[float]) -> float:
    '''
    type annotated function sumlist

    args: input_list (List[Float]): lost of floats

    returns: float: sum as a float
    '''
    return sum(input_list)
