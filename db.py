from datetime import datetime
from datetime import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb+srv://mongo_practicing:YSAZE9fx2W1ztrWr@cluster0.2ad7r7v.mongodb.net/?retryWrites=true&w=majority")

# print(client.list_database_names())

example_db = client.example
my_collection = example_db.my_collection

# result = my_collection.insert_one({'name': 'emad', 'age': 24, 'city': 'Amman'})
# print(my_collection.delete_one({'_id': ObjectId('63343cea0ca00dc8f93b748e')}))
# my_collection.update_one({'name': 'emad'}, {'$set': {'age': 25}})
my_collection.update_one({'name': 'emad'}, {'$inc': {'age': 1}})
my_collection.update_one({'name': 'emad'}, {'$inc': {'age': -1}})
my_collection.update_one({'name': 'emad'}, {'$set': {'modifying_date': datetime.now()}})  # search for $currentDate



print(example_db.list_collection_names())

print( my_collection.find_one())

print(list(my_collection.find()))

results = my_collection.find()

for result in results:
    print (result)

print(my_collection.count_documents({'name':'emad'}))



sample_airbnb_db = client.sample_airbnb
listingsAndReviews = sample_airbnb_db.listingsAndReviews

print(listingsAndReviews.count_documents({'beds':{'$gt':4}}))

d = datetime(2019,2,1)
print(d)
print(listingsAndReviews.find_one({'last_scraped':{'$gte':d}}))

# print(listingsAndReviews
#     .find(
#         {'$and': [
#                 {'bed_type': 'Real Bed'},
#                 {'accommodates': 8},
#                 {'maximum_nights': 30}
#                 ]
#         }
#         )
#         .sort('name').limit(2)
#     )


