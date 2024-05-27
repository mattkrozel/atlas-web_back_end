#!/usr/bin/env python3
'''
module of bbasic auth
'''
from api.v1.auth.auth import Auth
import re
import base64
from typing import TypeVar
from models.user import User


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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        '''
        arguments str
        returns decoded value base64 str
        '''
        if (not base64_authorization_header or
                type(base64_authorization_header) != str):
            return None
        try:
            msg = base64.b64decode(base64_authorization_header.encode('utf-8'))
            return msg.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        '''
        args self type
        returns str type
        '''
        if (not decoded_base64_authorization_header
                or type(decoded_base64_authorization_header) != str):
            return (None, None)
        credentials = decoded_base64_authorization_header.split(':', 1)
        return (credentials[0], credentials[1]) if ':' in\
            decoded_base64_authorization_header else (None, None)

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        '''
        args self type
        '''
        if not user_email or type(user_email) != str:
            return None
        if not user_pwd or type(user_pwd) != str:
            return None
        try:
            users = User.search({'email': user_email})
            if not users:
                return None
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''
        protected api with basic auth
        '''
        try:
            header = self.authorization_header(request)
            base64header = self.extract_base64_authorization_header(header)
            decodebase64header = self.decode_base64_authorization_header(
                base64header)
            user_email, user_pwd = self.extract_user_credentials(
                decodebase64header)
            return self.user_object_from_credentials(user_email, user_pwd)
        except Exception:
            return None
