# -*- coding:utf-8 _*-
""" 
@file: pdf_file.py 
@time: 2020/09/17
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
'''
将PDF 格式文件中提取出TXT
'''


import pathlib
import pdfplumber

with pdfplumber.open('./2018璧山年鉴_董奕锋_主编_璧山概况_璧山概况.pdf') as pdf, open('./out_txt.txt', 'a', encoding='utf-8') as txt:
    for page in pdf.pages:
        textdata = page.extract_text()
        txt.write(textdata)
