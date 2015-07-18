import pymongo
import sys

# connnecto to the db on standard port
connection = pymongo.MongoClient("mongodb://localhost")

db = connection.students                 # attach to db
collection = db.grades         # specify the colllection
query = {"type": "homework"}

try:
    cursor = collection.find(query).sort(
        [("student_id", pymongo.ASCENDING), ("score", pymongo.ASCENDING)])

except Exception as e:
    print "Error trying to read collection:", type(e), e

first_student_id = -1.0

for every in cursor:
    if every:
        if every["student_id"] == first_student_id:
            print every
        else:
            first_student_id = float(every["student_id"])
            result = collection.delete_one(
                {"student_id": first_student_id, "type": "homework", "score": every["score"]})
