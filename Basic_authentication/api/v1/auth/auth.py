#!/usr/bin/env python3
'''
module of auth
'''
from typing import List, TypeVar
from flask import request


class Auth():
    '''
    manages api authetnication
    '''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''
        public method requiring auth
        arguments oath str and excluded_paths list str
        returns boolean
        '''
        return False

    def authorization_header(self, request=None) -> str:
        '''
        public method
        args requst type
        returns str request object
        '''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''
        current users method
        '''
        return None
