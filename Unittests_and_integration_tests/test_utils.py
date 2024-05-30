#!/usr/bin/env python3

'''
test utils
'''
from unittest import TestCase
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch


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

    @parameterized.expand(
        [({}, ('a',), 'a'),
         ({'a': 1}, ('a', 'b'), 'b')]
    )
    def test_access_nested_map_exception(self, nested_map, path, expected):
        '''
        testing keyerror raises
        '''
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(f'KeyError("{expected}")', repr(e.exception))

class TestGetJson(TestCase):
    '''
    class for getting json tests
    '''
    @parameterized.expand(
            [('http://example.com', {'payload': True}),
             ('http://holberton.io', {'payload': False})]
    )
    def test_get_json(self, test_url, test_payload):
        '''
        testing get_json to get expected return
        '''
        config = {'return_value.json.return_value': test_payload}
        patcher = patch('requests.get', **config)
        mock = patcher.start()
        self.assertEqual(get_json(test_url), test_payload)
        mock.assert_called_once()
        patcher.stop()
