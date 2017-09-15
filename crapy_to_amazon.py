import os

from utils import read_everyline
from utils.txt_line_write import write_lines
from utils import amazon
from utils import const

path = "C:\\Users\Administrator\Desktop\啊阿飞的"
# 文件夹

# 单文件  文件后缀 if os.path.isfile(path):


def a_file_extrat(path,write_path=None):
    s_path = os.path.split(path)
    if write_path==None:
        write_path = s_path[0]+'\\'+'_amazon.'.join([s_path[1].split('.')[0],'txt'])
    if os.path.splitext(path)[1]=='.xlsx':
        everyline = read_everyline.excel_xlsx(path)
    else:
        everyline = read_everyline.txt(path)
    lines = [amazon.every_line(x) for x in everyline[1:]]
    write_lines(write_path,lines,const.header)


if os.path.isfile(path):
    a_file_extrat(path)
else:
    new_path = os.path.join(path,'可上传文件')
    os.makedirs(new_path)
    for x in os.listdir(path):
        this_path = os.path.join(path,x)
        if os.path.isfile(this_path):
            a_file_extrat(this_path,write_path=os.path.join(new_path,x.split('.')[0]+'.txt'))
