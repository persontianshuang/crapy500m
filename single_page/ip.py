import requests

import random

# li = random.choice(eval (requests.get('http://localhost:5000/').text))

# proxies = {
#     "http": "socks5://us2.fly6fish.rocks:14640",
#     "https": "socks5://us2.fly6fish.rocks:14640",
# }
# url = "http://www.httpbin.org/ip"
#
# html = requests.get(url,proxies=proxies).text
# print(html)

r = requests.get('http://baidu.com/')
cookie = r.cookies.get_dict()
print(cookie)
