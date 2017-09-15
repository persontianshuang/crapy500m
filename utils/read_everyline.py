from openpyxl import load_workbook


def txt(path):
    try:
        with open(path,'r',encoding='utf_8') as f:
            lines = f.readlines()
            return [x.split('\t') for x in lines if x.strip()!='']
    except:
        with open(path,'r',encoding='gbk') as f:
            lines = f.readlines()
            return [x.split('\t') for x in lines if x.strip()!='']

# def excel_xlsx(path):
#     f = open(path, 'rb')
#     lines = f.readlines()
#     try:
#         return [x.decode('gbk').split('\t') for x in lines]
#     except:
#         return [x.decode('utf_8').split('\t') for x in lines]


# 可笑 有时候 利用第三方库反而是累赘 误导

def excel_xlsx(path):
    # 打开一个workbook
    wb = load_workbook(filename=path)
    # 获取当前活跃的worksheet,默认就是第一个worksheet
    ws = wb.active
    # 获取表格所有行和列，两者都是可迭代的
    rows = ws.rows
    # columns = ws.columns
    # 迭代所有的行
    all_line = []
    for row in rows:
        # print(row)
        line = [str(col.value) for col in row]
        all_line.append(line)
    return all_line
