import datetime
import pprint
from pymongo import MongoClient
from bson.objectid import ObjectId

MONGODB_URI = "mongodb+srv://pablocalderon9408:junio806P-1.@platzi-course.hdhuyrb.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGODB_URI)

# Get reference to 'bank' database
db = client.bank

# Get reference to 'accounts' collection
accounts_collection = db.accounts

# Query by ObjectId
document_to_find = {"_id": ObjectId("62d6e04ecab6d8e1304974ae")}


# Filter
document_to_update = {"_id": ObjectId("62d6e04ecab6d8e130497482")}

# Get a reference to the 'accounts' collection
accounts_collection = db.accounts

# Filter by ObjectId
document_to_delete = {"_id": ObjectId("62d6e04ecab6d8e130497485")}

# Search for document before delete
print("Searching for target document before delete: ")
pprint.pprint(accounts_collection.find_one(document_to_delete))

# Write an expression that deletes the target account.
result = accounts_collection.delete_one(document_to_delete)

# Search for document after delete
print("Searching for target document after delete: ")
pprint.pprint(accounts_collection.find_one(document_to_delete))

print("Documents deleted: " + str(result.deleted_count))

# Filter for accounts with balance less than $2000
documents_to_delete = {"balance": {"$lt": 2000}}

# Search for sample document before delete
print("Searching for sample target document before delete: ")
pprint.pprint(accounts_collection.find_one(documents_to_delete))

# Write an expression that deletes the target accounts.
result = accounts_collection.delete_many(documents_to_delete)

# Search for sample document after delete
print("Searching for sample target document after delete: ")
pprint.pprint(accounts_collection.find_one(documents_to_delete))

print("Documents deleted: " + str(result.deleted_count))

client.close()