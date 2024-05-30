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

    def test_public_repos_url(self):
        '''
        testing result from pulic repos is expected
        based on payload
        '''
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            payload = {'repos_url': 'World'}
            mock.return_value = payload
            test_class = GithubOrgClient('test')
            result = test_class._public_repos_url
            self.assertEqual(result, payload['repos_url'])

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        '''
        testing listing of repos is expected from chosen payload
        testing mocked proprty
        '''
        json_payload = [{'name': 'Google'}, {'name': 'Twitter'}]
        mock_json.return_value = json_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public:
            mock_public.return_value = 'hello/world'
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()
            check = [i['name'] for i in json_payload]
            self.assertEqual(result, check)
            mock_public.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand(
        [({'license': {'key': 'my_license'}}, 'my_license', True),
         ({'license': {'key': 'other_license'}}, 'my_license', False)]
    )
    def test_has_license(self, repo, license_key, expected):
        '''
        unittesting githuborg for license
        '''
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)
