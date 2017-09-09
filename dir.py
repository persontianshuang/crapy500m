import os
n = 0
def dirlist(path):
    filelist =  os.listdir(path)

    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            dirlist(filepath)
        else:
            print(filepath)
            global n
            n = n + 1

dirlist("C:\\Users\Administrator\Desktop\德比帽，T恤")
print(n)
