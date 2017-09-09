import time,random
from concurrent import futures

import requests
from lxml import html

from mongosdb.db import coll

class Bianti:
    def __init__(self,asin):
        self.asin = asin
        self.url = 'https://www.amazon.com/dp/' + self.asin

    def make_req(self,url):
        header = {}
        header['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
        li = random.choice(eval(requests.get('http://localhost:5000/').text))
        proxies = {"http": "http://"+li}
        print(proxies)
        the_html = requests.get(url,headers=header,proxies=proxies).text
        # the_html = requests.get(url,headers=header).text
        response = html.fromstring(the_html)
        return response
    def parse(self, response):
        # img = response.xpath('//div[contains(@id, "imgTagWrapperId")]//img/@src')[0]
        # img = img.strip().replace('data:image/jpeg;base64,','')

        title = response.xpath('//*[@id="productTitle"]/text()')[0].strip()
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
        if brand.lower() not in title.lower():
            isbrand = False
        return {'asin': self.asin,'title': title,'brand':brand,'price':price,'isbrand':isbrand}

    def single(self):
        return self.parse(self.make_req(self.url))


def single(asin):
    data = Bianti(asin).single()
    print(data)
    coll.insert(data)
    # time.sleep(random.randint(1,3))

from redisdb import task
from redisdb.db import RedisClient

queue_len = int(RedisClient().queue_len)




def download_many(cc_list):
    print('download_many')
    workers = min(10, len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        executor.map(task.get_task, cc_list)


download_many([single for x in range(queue_len)])