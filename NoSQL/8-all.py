#!/usr/bin/env python3
'''
mongo collection
pymongo
'''
def list_all(mongo_collection: object) -> list:
    '''
    listing all docs in collection
    args 
    mongo collection object
    pymongo collection object
    '''
    return mongo_collection.find({}) if mongo_collection.find({}) else []
