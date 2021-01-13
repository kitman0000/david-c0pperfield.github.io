﻿#!usr/bin/env python3

import xlrd
import json
import re
import os
import subprocess

excel_name = r'闪击战ID情报.xlsx'
def xlsxRead():
    while os.path.exists(excel_name) == False:
        data = input('找不到“{}”，请寻找相关文件后键入路径或放入同一文件夹后回车。\n\
                     寻找文件：'.format(excel_name))

    data = xlrd.open_workbook(excel_name)
    table = data.sheet_by_name(r'军团列表')
    data_list = []
    for i in range(1,table.nrows):
        title_data =['ID','Tag','Full','Desc','Estbl','MID']
        row_content = []
        row_data = {}
        
        for j in range (table.ncols):
            ctype = table.cell(i,j).ctype
            cell = table.cell_value(i,j)
            if ctype == 2 and cell % 1 == 0:
                cell = int(cell)
            if j == 3:
                cell = cell.replace('\n','<br>')
            row_content.append(cell)
            
        for k in range(len(title_data)):
            row_data[title_data[k]]=row_content[k]
        data_list.append(row_data)
        
    print('共{}条数据'.format(i))
    processed_json=json.dumps(data_list,sort_keys=False,separators=(',',':'),ensure_ascii=False)

    f = open('../js/clan.json','w+')
    f.write(processed_json)
    f.close()
    print('json建立成功！')

if __name__ == '__main__':
    xlsxRead()
