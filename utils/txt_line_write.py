
def write_lines(write_path,lines,header):
    with open(write_path,'a',encoding='utf_8') as wf:
        wf.writelines(header)
        [wf.writelines(x) for x in lines]
    # return 0
