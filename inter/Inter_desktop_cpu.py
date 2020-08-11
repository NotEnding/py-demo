# -*- coding:utf-8 _*-
""" 
@file: Inter_desktop_cpu.py 
@time: 2020/08/07
@site:  
@software: PyCharm 

# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛ 
"""

import requests
import chardet
from lxml import etree

import xlrd
import xlwt
from xlutils.copy import copy


def write_excel_xls(path, sheet_name, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet(sheet_name)  # 在工作簿中新建一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])  # 像表格中写入数据（对应的行和列）
    workbook.save(path)  # 保存工作簿
    print("xls格式表格写入数据成功！")


def write_excel_xls_append(path, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            new_worksheet.write(i + rows_old, j, value[i][j])  # 追加写入数据，注意是从i+rows_old行开始写入
    new_workbook.save(path)  # 保存工作簿
    print("xls格式表格【追加】写入数据成功！")


def read_excel_xls(path):
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    for i in range(0, worksheet.nrows):
        for j in range(0, worksheet.ncols):
            print(worksheet.cell_value(i, j), "\t", end="")  # 逐行逐列读取数据
        print()



url = 'http://www.mydrivers.com/zhuanti/tianti/cpu/index_intel.html'

heraders = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Host": "www.mydrivers.com",
    "If-None-Match": "efab9a1e550d61:0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
}


if __name__ == '__main__':
    book_name_xls = 'intel桌面处理器规格表.xls'
    sheet_name_xls = 'sheet1'

    value_title = [['处理器型号', '核心架构', '制造工艺(nm)', '核心/线程', '核心频率（GHz）', '加速频率（GHz）', '三级缓存（MB）', '核显', '热设计功耗（W）', '插槽'], ]

    response = requests.get(url,heraders)
    if response.status_code == 200:
        # 解码
        data = response.text.encode("latin1").decode("gbk")
        html = etree.HTML(data)

        write_excel_xls(book_name_xls, sheet_name_xls, value_title)

        result_list = html.xpath('//div[@class="main"]/table')
        for result in result_list:
            res = result.xpath('./tr')
            for re in res:
                a = re.xpath('./td/text()')
                if not a:
                    pass
                elif a == ['\xa0']:
                    pass
                elif a == [' 驱动之家·版权所有']:
                    pass
                elif a == ['处理器型号', '核心架构', '制造工艺(nm)', '核心/线程', '核心频率（GHz）', '加速频率（GHz）', '三级缓存（MB）', '核显', '热设计功耗（W）', '插槽']:
                    pass
                else:
                    value = [a]
                    # print(value)
                    write_excel_xls_append(book_name_xls, value)