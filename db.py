from pymongo import MongoClient

client = MongoClient("mongodb+srv://mongo_practicing:YSAZE9fx2W1ztrWr@cluster0.2ad7r7v.mongodb.net/?retryWrites=true&w=majority")

print(client.list_database_names)