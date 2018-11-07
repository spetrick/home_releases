import pymongo
#So we can select by ObjectId
from bson import ObjectId
class MongoCon:
    #Initialize variables
    mongoClient = None
    #Name of the database
    dbname = None
    #db connection
    mydb = None
    #collection object
    collection = None

    def __init__(self, host, dbname, col):
        ###Initialize a wrapper for pymongo for this use###
        self.mongoClient = pymongo.MongoClient(host)
        self.dbname = dbname
        self.mydb = self.mongoClient[dbname]
        self.collection = self.mydb[col]

    def insert(self, record):
        ###Insert a record into the db###
        ret = self.collection.insert_one(record)
        return ret.inserted_id

    def selectRecord(self, name):
        ###Select all records from the database with the same title###
        ret = []
        for x in self.collection.find({}, {"title": name}):
            ret.append(self.collection.find_one(x))
        return ret

    def deleteRecord(self, uid):
        ###Delete a single record from the DB###
        self.collection.delete_one({"_id": ObjectId(uid)})

    def selectAll(self):
        ###Return a single array containing all titles in the database
        ret = []
        for x in self.collection.find({}):
            ret.append(self.collection.find_one(x))
        return ret