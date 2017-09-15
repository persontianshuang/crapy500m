from qn.simple import QiniuUp
import random
import os


def new_sku(num):
    az_strs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'
    def rannum(num):
        rand_str = ''
        for x in range(num):
            rand_str += random.choice(az_strs)
        return rand_str
    sku = rannum(num)
    return sku

z_path = r"F:\png\长"

q = QiniuUp('gongsi')
yun_path = 'http://ovvv2q5lc.bkt.clouddn.com/'


def single_dir(this_path):
    for this_file in os.listdir(this_path):
        # try:
        #     os.remove(os.path.join(this_path,"图片链接.txt"))
        # except:
        #     pass
        if this_file[-3:] == 'jpg' or this_file[-3:] == 'png' or this_file[-3:] == 'PNG' or this_file[-3:] == 'JPG':
            this_img_path = os.path.join(this_path,this_file)
            print(this_img_path)
            write_txt = os.path.join(this_path,"图片链接.txt")
            yun_img_name = new_sku(15) + '.jpg'
            yun_img_path = yun_path + yun_img_name
            q.upqiniu(yun_img_name,this_img_path)
            with open(write_txt,'a',encoding="utf_8") as f:
                f.writelines(this_file+'\t => \t'+ yun_img_path+'\n')


for z in os.listdir(z_path):
    path = os.path.join(z_path,z)
    if not os.path.isfile(path):    
        try:
            for x in os.listdir(path):
                this_path = os.path.join(path,x)
                print(this_path)
                single_dir(this_path)
        except:
            single_dir(path)


# QiniuUp('kindle').upqiniu(new_sku(12)+'.jpg',"C:\\Users\Administrator\Desktop\92create1\\1\\1 (1).jpg")