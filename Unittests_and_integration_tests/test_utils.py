#!/usr/bin/env python3

'''
test utils
'''
from unittest import TestCase
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(TestCase):
    '''
    inheirts from unittest.TestCase
    arguments TestCase type
    '''
    @parameterized.expand(
        [({'a': 1}, ('a'), 1),
         ({'a': {'b': 2}}, ('a',), {'b': 2}),
         ({'a': {'b': 2}}, ('a', 'b'), 2)]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        '''
        testing method returns correctly
        '''
        self.assertEqual(access_nested_map(nested_map, path), expected)
