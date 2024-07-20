#!/usr/bin/env python3
""" pymongo project task 9 """


def insert_school(mongo_collection, **kwargs):
    """ inserts a new doc to a collection """
    return mongo_collection.insert_one(kwargs).inserted_id
