
from redisdb.db import RedisClient
coll = RedisClient()
path = "F:\采集\old\采集器\\todo\我\\30.txt"


# raw
# with open(path,'r') as f:
#     tasks = [x.split('\t')[1] for x in f.readlines()[1:]]
# print(tasks)

# only asin
with open(path,'r') as f:
    tasks = [x.strip() for x in f.readlines()[1:]]
print(tasks)


def add_task(tasks):
    coll.add_crawl_tasks(tasks)

add_task(tasks)

