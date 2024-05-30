#!/usr/bin/env python3
'''
testing client module
'''
import unittest
from unittest.mock import PropertyMock, patch
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    '''
    githubOrg ckient tests class
    '''
    @parameterized.expand(
        [('google'), ('abc')]
    )
    @patch('client.get_json')
    def test_org(self, input, mock):
        '''
        testing github clients returns correctly
        '''
        test_class = GithubOrgClient(input)
        test_class.org()
        mock.assert_called_once_with(f'https://api.github.com/orgs/{input}')
