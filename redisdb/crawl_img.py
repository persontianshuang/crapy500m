#!/usr/bin/env python3

import time,random
from concurrent import futures

import requests
from lxml import html

import gevent
from gevent import monkey,pool
monkey.patch_all()


import pymongo
MONGO_URI = '108.61.203.110'
PORT = 29999
def pymg(highest,collections,uri=MONGO_URI,port=PORT):
    client = pymongo.MongoClient(uri,port)
    zhihu = client[highest]
    collections = zhihu[collections]
    return collections

coll = pymg('goods','920_yantai2')



links = []
p = pool.Pool(35)

class Bianti:
    def __init__(self,asin):
        self.asin = asin
        self.url = 'https://www.amazon.com/dp/' + self.asin

    def make_req(self,url):
        header = {}
        header['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'

        rg = requests.get(url,headers=header)
        if rg.status_code != 404:
            the_html = rg.text
            response = the_html
            return response
        else:
            return None
    def parse(self, response):
        if response!=None:
            response = html.fromstring(response)

            title = response.xpath('//*[@id="productTitle"]/text()')[0].strip()

            try:
                try:
                    img = response.xpath('//div[contains(@id, "imgTagWrapperId")]//img/@data-a-dynamic-image')[0]
                    # img = re.sub(r'\.\_UX.+\_', '', list(eval(img).keys())[0])
                    img = list(eval(img).keys())[0]
                except:
                    img = response.xpath('//div[contains(@id, "imgTagWrapperId")]//img/@src')[0]
                    img = img.strip().replace('data:image/jpeg;base64,','')
            except:
                img = ''


            return {'asin': self.asin,
                    'img':img}
        else:
            return None

    def single(self):
        time.sleep(random.randint(1,40))
        print(self.asin)
        return self.parse(self.make_req(self.url))


def single(asin):
    data = Bianti(asin).single()
    if data!=None:
        print(data)
        coll.insert(data)
    else:
        print(asin,':可能该商品已经不存在了')
        # time.sleep(random.randint(1,3))

from task import get_task



jobs = [p.spawn(get_task, single) for x in range(30000)]
gevent.joinall(jobs)

