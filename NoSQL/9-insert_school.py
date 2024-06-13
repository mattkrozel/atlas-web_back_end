#!/usr/bin/env python3
'''
mongo collection
pymongo
'''
def insert_school(mongo_collection: object, **kwargs):
    '''
    func inserts new document in colleection
    args 
    mongo collection object
    '''
    data = mongo_collection.insert_one({**kwargs})
    return data.inserted_id
