#!/usr/bin/env python3
'''
module of bbasic auth
'''
from api.v1.auth.auth import Auth
import re


class BasicAuth(Auth):
    '''
    basic auth
    arguments auth type
    '''
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        '''
        arguments authorization_header
        returns str base of auth
        '''
        if not authorization_header or type(authorization_header) is not str:
            return None
        header = authorization_header.split(' ')
        return (None if not bool(re.search('^Basic ', authorization_header))
                else header[1])
