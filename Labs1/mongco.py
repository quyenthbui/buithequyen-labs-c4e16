from pymongo import MongoClient

mongo_uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'

client = MongoClient(mongo_uri)

db = client.get_default_database()

posts = db['posts']

title = ['không làm kịp bài rồi']

author = ['ẩn danh']

content = ['ngã cũng phải ngã về phía trước']

new_post = {
    'title':title,
    'author':author,
    'content':content
}

posts.insert_one(new_post)
