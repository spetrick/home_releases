import pymongo
class MongoCon:
    mongoClient = None
    dbname = None
    mydb = None
    collection = None
    def __init__(self, host, dbname, col):
        self.mongoClient = pymongo.MongoClient(host)
        self.dbname = dbname
        self.mydb = self.mongoClient[dbname]
        self.collection = self.mydb[col]

    def insert(self, record):
        ret = self.collection.insert_one(record)
        return ret.inserted_id

    def selectRecord(self, name):
        ret = []
        for x in self.collection.find({}, {"name": name}):
            ret.append(self.collection.find_one(x))
        return ret

    def deleteRecord(self, uid):
        self.collection.delete_one({"_id": "ObjectId(\"" + uid + "\")"})