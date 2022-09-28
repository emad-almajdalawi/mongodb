from pymongo import MongoClient

# cluster = 'mongodb+srv://mongo_practicing:r8eMIeQo6wTzqZZa@cluster0.2ad7r7v.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient("mongodb+srv://mongo_practicing:YSAZE9fx2W1ztrWr@cluster0.2ad7r7v.mongodb.net/?retryWrites=true&w=majority")

# client = MongoClient(cluster)

print(client.list_database_names)