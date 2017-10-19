import redis
# from redisdb.setting import HOST, PORT, PASSWORD,COLL
HOST = '45.32.173.22'
# HOST = 'localhost'
PORT = 6379
# PASSWORD = None
PASSWORD = 'helloredis'
COLL = '1019'

class RedisClient(object):
    def __init__(self, host=HOST, port=PORT,coll=COLL):
        if PASSWORD:
            self._db = redis.Redis(host=host, port=port, password=PASSWORD)
        else:
            self._db = redis.Redis(host=host, port=port)
        self.coll = COLL


    # 1.添加爬取任务
    def add_crawl_tasks(self,tasks):
        if type(tasks)==list:
            tasks = list(set(tasks))
            for x in tasks:
                self._db.rpush(self.coll,x)
        else:
            self._db.rpush(self.coll,tasks)


    def lpush(self,task):
        self._db.lpush(self.coll,task)


    def rpop(self):
        try:
            return self._db.rpop(self.coll).decode('utf-8')
        except:
            print('get from redis failed')

    @property
    def queue_len(self):
        return self._db.llen(self.coll)


    def flush(self):
        self._db.flushall()


if __name__ == '__main__':
    conn = RedisClient()
    rp = conn.rpop()
    print(rp)
    # print(conn.queue_all)
