#!/usr/bin/env python3
'''
filtered_logger
'''
import re
from typing import List
import logging
import mysql.connector
from os import getenv

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        '''
        format method
        args record
        returns str
        '''
        msg = filter_datum(self.fields, self.REDACTION,
                           super().format(record), self.SEPARATOR)
        return msg


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    '''
    func filter_datum
    args filds list, redaction str, message str, seperator str
    '''
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}',
                         message)
    return message


def get_logger() -> logging.Logger:
    '''
    get_logger functiinon
    returns logging.logger
    '''
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    '''
    returns connector to database
    '''
    db = mysql.connector.connection.MySQLConnection(
        user=getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
        password=getenv('PERSONAL_DATA_DB_PASSWORD', ''),
        host=getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
        database=getenv('PERSONAL_DATA_DB_NAME')
    )
    return db


def main():
    '''
    obtain databse connection using get_db
    '''
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM users;')
    result = cursor.fetchall()
    for data in result:
        message = f'name={data[0]}; ' + \
                  f'email={data[1]}; ' + \
                  f'phone={data[2]}; ' + \
                  f'ssn={data[3]}; ' + \
                  f'password={data[4]}; ' + \
                  f'ip={data[5]}; ' + \
                  f'last_login={data[6]}; ' + \
                  f'user_agent={data[7]};'
        print(message)
        log_record = logging.LogRecord('my_logger', logging.INFO,
                                       None, None, message, None, None)
        formatter = RedactingFormatter(PII_FIELDS)
        formatter.format(log_record)
    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
