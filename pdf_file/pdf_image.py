# -*- coding:utf-8 _*-
""" 
@file: pdf_image.py 
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
提取PDF中的图片
'''

import pathlib
import pdfplumber
from PIL import Image


pdf_path = './2018璧山年鉴_董奕锋_主编_璧山概况_璧山概况.pdf'

path = list(pathlib.Path.cwd().parents)[1].joinpath('./')
out_path = path.joinpath('002pdf_figures.png')
with pdfplumber.open(pdf_path) as pdf, open(out_path, 'wb') as fout:
    page = pdf.pages[7]
    im = page.to_image()
    im.save(out_path, format='PNG')
    figures = page.figures
    for i, fig in enumerate(figures):
        size = fig['width'], fig['height']
        crop = page.crop((fig['x0'], fig['top'], fig['x1'], fig['bottom']))
        img_crop = crop.to_image()
        out_path = path.joinpath(f'002pdf_figures_{i}.png')
        img_crop.save(out_path, format='png')
    im.draw_rects(page.extract_words(), stroke='yellow')
    im.draw_rects(page.images, stroke='blue')
    im.draw_rects(page.figures)
