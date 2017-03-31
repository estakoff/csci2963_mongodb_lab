from pymongo import MongoClient
from bson.objectid import ObjectId
import json

client = MongoClient()
db = client.csci2963.definitions
post = db.find({})
#fetch all
##for document in post:
##	print(document)
#fetch a single post
##postIndiv = db.find_one({})
##print postIndiv
#fetch a spec record
##postSpec = db.find_one({"word": "Ethan Stakoff"})
##print postSpec
#find a post by id
postId = db.find_one({ "_id": ObjectId("56fe9e22bad6b23cde07b8c9") })
print postId
#insert a record
#db.insert({"word": "anotherInsertByMe", "definition":"the def of course duh!"})

print post
