
from redisdb.db import RedisClient
from concurrent import futures

coll = RedisClient()
path = "F:\采集\old\采集器\\todo\我\\30.txt"

# raw
# with open(path,'r') as f:
#     tasks = [x.split('\t')[1] for x in f.readlines()[1:]]
# print(tasks)

# only asin
with open(path,'r') as f:
    the_tasks = [x.strip() for x in f.readlines()[1:]]
print(the_tasks)

# def add_task(tasks):
#
#     coll.add_crawl_tasks(tasks)
#
# # add_task(tasks)
#
def download_many(cc_list):
    print('download_many')
    workers = min(20,len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        executor.map(coll.add_crawl_tasks,cc_list)

download_many(the_tasks)
