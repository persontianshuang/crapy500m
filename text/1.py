import os

file="C:\\Users\Administrator\Desktop\不侵权\沙拉盘不侵权-38.xls"

with open(file, 'r',encoding='gbk') as f:
    lines = f.readlines()
    for line in lines:
        line = line
        print(line)
