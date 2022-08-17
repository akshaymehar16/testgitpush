import pymongo

client = pymongo.MongoClient("mongodb+srv://akshay:99999999@cluster0.tv8iqgg.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name": "akshay",
    "email": "akshay@gmail.com",
    "surname": "mehar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)