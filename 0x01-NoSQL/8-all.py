#!/usr/bin/env python3
""" pymongo project task """


def list_all(mongo_collection):
    """ returns all documents in a collection """
    docs = mongo_collection.find()
    return docs if docs.count() > 0 else []
