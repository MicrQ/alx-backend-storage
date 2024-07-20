#!/usr/bin/env python3
""" pymongo project task """


def top_students(mongo_collection):
    """ returns all students sorted by average score """
    return mongo_collection.find().sort([("name", 1), ("averageScore", -1)])