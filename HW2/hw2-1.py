import pymongo
import sys

# connnecto to the db on standard port
connection = pymongo.MongoClient("mongodb://localhost")

db = connection.students                 # attach to db
collection = db.grades         # specify the colllection
query = {"type": "exam", "score": {"$gt": 65}}

try:
    cursor = collection.find(query, {"student_id": True}).sort(
        "score", pymongo.ASCENDING).limit(1)

except Exception as e:
    print "Error trying to read collection:", type(e), e

for every in cursor:
    print(every)
