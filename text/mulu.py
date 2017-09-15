import os

all_img = set()
def visitDir(path):
    li = os.listdir(path)
    for p in li:
        pathname = os.path.join(path,p)
        if not os.path.isfile(pathname):    #判断路径是否为文件，如果不是继续遍历
            visitDir(pathname)
        else:
            all_img.add(os.path.split(pathname)[1].split('.')[0])


visitDir("C:\\Users\Administrator\Desktop\恐龙玩具")
print(all_img)
everyline = []
from utils.amazon import every_line

with open("F:\采集\恐龙\亚马逊采集器生成的txt文件\恐龙_不侵权.txt",'r',encoding='utf_8') as f:
    all = f.readlines()

    for x in all_img:
        for xx in all:
            # print(xx.split('\t'))
            st = xx.split('\t')
            if x==st[3]:

                if st[1].lower() not in st[2].lower():
                    everyline.append(st)
                    break
from utils.txt_line_write import write_lines
from utils import const
lines = [every_line(x) for x in everyline]
write_lines("F:\采集\恐龙\亚马逊采集器生成的txt文件\w1.txt",lines,const.header)
