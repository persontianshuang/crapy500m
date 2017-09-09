
from utils.amazon import real_need
from mongosdb.db import coll1

lines = []
for x in coll1.find({'isbrand': False}):
    try:
        lines.append(real_need(x['asin'],x['price'].strip('$')))
    except:
        print('fail')


from utils.txt_line_write import write_lines
from utils import const

write_lines("F:\采集\恐龙\亚马逊采集器生成的txt文件\w5.txt",lines,const.header)
