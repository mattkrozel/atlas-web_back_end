#!/usr/bin/env python3
'''
session auth module
'''
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    '''
    SessionAuth
    args auth type
    '''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        '''
        creates session methoid
        args user_id str
        returns str
        '''
        
