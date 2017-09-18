#!/usr/bin/env python3

import time,random
from concurrent import futures

import requests
from lxml import html

import pymongo
MONGO_URI = '108.61.203.110'
PORT = 29999
def pymg(highest,collections,uri=MONGO_URI,port=PORT):
    client = pymongo.MongoClient(uri,port)
    zhihu = client[highest]
    collections = zhihu[collections]
    return collections

coll = pymg('goods','918_no2')

class Bianti:
    def __init__(self,asin):
        self.asin = asin
        self.url = 'https://www.amazon.com/dp/' + self.asin

    def make_req(self,url):
        header = {}
        header['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
        # li = random.choice(eval(requests.get('http://localhost:5000/').text))

        # li = requests.get('http://localhost:5000/get').text


        # proxies = {"http": "http://"+li}
        # print(proxies)

        # the_html = requests.get(url,headers=header,proxies=proxies).text

        # proxies = {'http': 'socks5://127.0.0.1:1080',
        #            'https': 'socks5://127.0.0.1:1080'}
        #
        # rg = requests.get(url,headers=header,proxies=proxies)
        rg = requests.get(url,headers=header)
        if rg.status_code != 404:
            the_html = rg.text
            response = the_html
            return response
        else:
            return None
    def parse(self, response):
        # img = response.xpath('//div[contains(@id, "imgTagWrapperId")]//img/@src')[0]
        # img = img.strip().replace('data:image/jpeg;base64,','')
        if response!=None:
            response = html.fromstring(response)

            title = response.xpath('//*[@id="productTitle"]/text()')[0].strip()
            # print(title)
            try:
                try:
                    brand = response.xpath('//*[@id="brand"]/text()')[0].strip()
                except:
                    brand = response.xpath('//*[@id="bylineInfo"]/text()')[0].strip()
            except:
                brand = 'cannotcrawlbrand'
            try:
                try:
                    price = response.xpath('//*[@id="priceblock_ourprice"]/text()')[0]
                except:
                    price = response.xpath('//*[@id="priceblock_saleprice"]/text()')[0]
            except:
                price = '0'
            isbrand = True
            # if brand.lower() not in title.lower():
            #     isbrand = False


            img = response.xpath('//div[contains(@id, "imgTagWrapperId")]//img/@data-a-dynamic-image')[0]
            # img = re.sub(r'\.\_UX.+\_', '', list(eval(img).keys())[0])
            img = list(eval(img).keys())[0]

            return {'asin': self.asin,'title': title,'brand':brand,
                    'price':price,'isbrand':isbrand,'img':img}
        else:
            return None

    def single(self):
        time.sleep(random.randint(1,56))
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
from db import RedisClient

queue_len = int(RedisClient().queue_len)




def download_many(cc_list):
    print('download_many')
    workers = min(50, len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        executor.map(get_task, cc_list)


download_many([single for x in range(queue_len)])
