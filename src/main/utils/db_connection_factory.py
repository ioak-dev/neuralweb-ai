from pymongo import MongoClient
from bson.objectid import ObjectId
import os

DATABASE_URI = os.environ.get('DATABASE_URI')
if DATABASE_URI is None:
    DATABASE_URI = 'mongodb://localhost:27017'

__connection_map = {}


def get_collection(space, collection):
    _db_name = 'neuralweb_' + space
    if _db_name not in __connection_map.keys():
        __connection_map[_db_name] = MongoClient(DATABASE_URI)[_db_name]
    return __connection_map.get(_db_name)[collection]

def clean_object(data):
    if data is not None and data.get('_id') is not None and type(data.get('_id')) == ObjectId:
        data['_id'] = str(data.get('_id'))
    return data

def clean_array(data):
    if data is not None and type(data) == list:
        for item in data:
            item = clean_object(item)
    return data
