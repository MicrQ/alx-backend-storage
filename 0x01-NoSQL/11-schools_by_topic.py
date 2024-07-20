#!/usr/bin/env python3
""" pymongo project task 11 """


def schools_by_topic(mongo_collection, topic):
    """ returns list of schools that a given topic """
    return mongo_collection.find({'topics': topic})
