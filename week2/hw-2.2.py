import pymongo
import sys

# establish a connection to the database
client = pymongo.MongoClient('mongodb://localhost:27017/')
# get a handle to the students database
db=client.students
grades = db.grades

def find():

    print "mongo db course hw 2.2 students' grades"

    query = {'type': 'homework'}
    sort  = [('student_id', pymongo.ASCENDING), ('score', pymongo.ASCENDING)];

    try:
        cursor = grades.find(query).sort(sort)
    except:
        print "Unexpected error:", sys.exc_info()[0]

    sid = None
    for doc in cursor:
        if doc['student_id'] != sid:
            sid = doc['student_id']
            try:
                grades.remove({'_id': doc['_id']})
            except:
			    print "error during remove:", sys.exc_info()[0]

find()
