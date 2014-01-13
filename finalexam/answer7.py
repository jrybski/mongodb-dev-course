__author__ = 'janusz.rybski'

import sys
import pymongo

# establish a connection to the database
client = pymongo.MongoClient('mongodb://localhost:27017/')
# get a handle to the school database
db = client.final7
# assign images collection
images = db.images
# assign albums collection
albums = db.albums

def remove_orphan_images():

    try:
        cursor = images.find({}, {'_id': 1})
    except:
        print "Unexpected error:", sys.exc_info()[0]

    for image in cursor:
        albums_num = albums.find({'images': image['_id']}).count()
        if albums_num == 0:
             try:
                db.images.remove({'_id': image['_id']})
                print "removing image ", image['_id']
             except:
                print "error during removing image", sys.exc_info()[0]
    return 0


remove_orphan_images()