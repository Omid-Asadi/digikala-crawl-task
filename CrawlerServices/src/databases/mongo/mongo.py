from pymongo import MongoClient


client = MongoClient()
db = client['torob']
links_collection = db.storage_list


def save_link_to_mongo(data):
    return links_collection.insert_many(data)


def get_link_from_mongo():
    return links_collection.find({'flag': False})


def set_crawled_flag(link_id):
    links_collection.find_one_and_update(
        {'_id': link_id}, {'$set': {'flag': True}}
    )


def get_collection(db, collection):
    return db.collection
