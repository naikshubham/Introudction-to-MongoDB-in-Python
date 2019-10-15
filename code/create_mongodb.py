import requests # gets the data from API
from pymongo import MongoClient # pymongo is the official python driver for MongoDB

client = MongoClient()  # client connects to localhost by default

db = client['nobel'] # create local nobel database on the fly

for collection_name in ['prizes', 'laureates']:
	# collect the data from API
	response = requests.get("http://api.nobleprize.org/v1/{}.json".format(collection_name[:-1]))
	# print('response->',response)
	# response = str(response).strip("'<>() ").replace('\'', '\"')
	# print('response->',response)
	# convert the data to json
	documents = response.json()[collection_name]
	# create collections on the fly
	db[collection_name].insert_many(documents)

# Accessing databases and collections
# client is a dictionary of databases
db = client['nobel']

# database is the dict of collections
prizes_collection = db['prizes']

# count documents in a collection
filter = {}

n_prizes = db.prizes.count_documents(filter)
n_laureates = db.laureates.count_documents(filter)
doc = db.prizes.find_one(filter)

# save a list of names of the databases managed b client
db_names = client.list_database_names()
print(db_names)

# save a list of names of the collections managed by the 'nobel' database
nobel_coll_names = client['nobel'].list_collection_names()
print(nobel_coll_names)
