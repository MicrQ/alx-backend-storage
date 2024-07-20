#!/usr/bin/env python3
""" pymongo project task """
from pymongo import MongoClient


def list_all(mongo_collection):
    """ returns all documents in a collection """
    return mongo_collection.find()
