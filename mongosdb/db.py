import pymongo
MONGO_URI = '108.61.203.110'
PORT = 29999
def pymg(highest,collections,uri=MONGO_URI,port=PORT):
    client = pymongo.MongoClient(uri,port)
    zhihu = client[highest]
    collections = zhihu[collections]
    return collections

coll = pymg('goods','short30')
# coll1 = pymg('goods','konglong')
