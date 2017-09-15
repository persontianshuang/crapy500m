import os


def dirlist(path):
    filelist = os.listdir(path)
    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            dirlist(filepath)
        else:
            ol = os.path.split(filepath)[1].split('.')[0]
            all_img.add(ol)
            # print(ol)

all_img = set()
dirlist("C:\\Users\Administrator\Desktop\德比帽，T恤")
# print(all_img)
def a_file_extrat(path,write_path=None):
    s_path = os.path.split(path)
    if write_path==None:
        write_path = s_path[0]+'\\'+'_amazon.'.join([s_path[1].split('.')[0],'txt'])
    with open(path,'r',encoding='utf_8') as f:
        have_img = list(all_img).copy()
        for x in f.readlines()[1:]:
            # print(x.split('\t')[1])
            asin = x.split('\t')[1]
            try:
                if asin in list(all_img):
                    if len(have_img)>0:
                        have_img.remove(asin)
                        print(x.strip('\n'))
            except:
                pass

a_file_extrat("F:\采集\德比帽子\帽子\德比帽子_不侵权_amazon.txt")
