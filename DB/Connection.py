import pymongo
client = pymongo.MongoClient(
    "mongodb+srv://iot:1234560@mongodbproject.spgbw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

dbITI = client["ITI"]
