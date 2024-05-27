#!/usr/bin/env python3
'''
module of auth
'''
from typing import List, TypeVar
from flask import request
from os import getenv


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
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        return not(path in excluded_paths or f'{path}/' in excluded_paths)

    def authorization_header(self, request=None) -> str:
        '''
        public method
        args requst type
        returns str request object
        '''
        if request:
            return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        '''
        current users method
        '''
        return None

    def session_cookie(self, request=None):
        '''
        session cookie
        args request
        '''
        if not request:
            return None
        return request.cookies.get(getenv('SESSION_NAME'))\
            if getenv('SESSION_NAME') else None
