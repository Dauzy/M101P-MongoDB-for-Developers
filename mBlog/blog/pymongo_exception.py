#!/usr/bin/env python
import pymongo

# Do not need to import sys

connection = pymongo.MongoClient("mongodb://172.17.0.2")

db = connection.test
users = db.users

doc = {'firstname':'Andrew', 'lastname':'Erlichson'}
print(doc)
print("about to insert the document")

try:
    users.insert_one(doc)
except Exception as e:
    print("insert failed:", e)

print (doc)
print ("inserting again")

try:
    users.insert_one(doc)
except Exception as e:
    print("second insert failed:", e)

print(doc)

