import requests
import getdata
import pymongo 


# mongodb_url = "mongodb+srv://weekenddiscoveries6:V62ejRjlVilThUGv@cluster0.dhpp5yh.mongodb.net/"
# database_name = "test"
# collection_name = "collections"

# client = pymongo.MongoClient(mongodb_url)
# db = client[database_name]
# collection = db[collection_name]

# user_interests = collection.find()
# for x in user_interests:



# interests = getdata.interests
data = getdata.interests
names = []
interests = []
already = []

for x in data:
     names.append(x['name'])
     interests.append(x['interests'])
     already.append(x['already'])


print(names)