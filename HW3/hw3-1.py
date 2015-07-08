import pymongo
import sys

# connnecto to the db on standard port
connection = pymongo.MongoClient("mongodb://localhost")

db = connection.school                 # attach to db
collection = db.students         # specify the colllection
query = {"type" : "homework"}

try:
    cursor = collection.find()

except Exception as e:
    print "Error trying to read collection:", type(e), e

for every in cursor:
	if every:
		if every["student_id"] == first_student_id:
			print every
		else:
			first_student_id = float(every["student_id"])
			result = collection.delete_one({"student_id": first_student_id, "type" : "homework", "score" : every["score"]})



#for student_id in range(0,199):
#	new_cursor = collection.find({"type" : "homework", "student_id" : student_id}).sort("score", pymongo.ASCENDING)



