#!/usr/bin/env python3

'''
type annotated function sum_mixed_list
'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    type annotated function sum mixed list
    
    args: mxd_lst (List[Float]): lost of ints and floats
    
    returns: float: sum as a float
    '''
    return sum(mxd_lst)
