#!/usr/bin/env python3

'''
iterable objec
'''

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    telement length function
    
    args: 
        lst iterable
    
    returns: list tuple
    '''
    return [(i, len(i)) for i in lst]

