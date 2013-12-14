__author__ = 'janusz.rybski'

import pymongo
import sys

# establish a connection to the database
client = pymongo.MongoClient('mongodb://localhost:27017/')
# get a handle to the school database
db = client.school
# assign students collection
students = db.students

def remove_homework_lowest_scored():

    print "mongo db course home work 3.1"

    query = {'scores.type': 'homework'}

    try:
        cursor = students.find(query)
    except:
        print "Unexpected error:", sys.exc_info()[0]

    for student in cursor:
        minScore = 100;
        for score in student['scores']:
            if score['type'] == 'homework' and score['score'] < minScore:
                minScore = score['score'];

        student['scores'].remove({'score': minScore, 'type': 'homework'})
        try:
            students.update({'_id': student['_id']}, {'$set': {'scores': student['scores']}});
        except:
            print "error during removing lowest homework:", sys.exc_info()[0]

remove_homework_lowest_scored()