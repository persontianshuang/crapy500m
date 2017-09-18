# 2.各个客户端取任务
from db import RedisClient

def get_task(funcc):
    coll = RedisClient()
    task = 'None'
    r_len = coll.queue_len
    print(r_len)
    if r_len==0:
        print('you have aready crawl all urls')
    else:
        try:
            task = coll.rpop()
            # print(task)
            funcc(task)

        except:
            coll.lpush(task)



