#!/usr/bin/env python3
'''
encrypting password
'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''
    encrypts password
    '''
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''
    encrypts password
    '''
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
