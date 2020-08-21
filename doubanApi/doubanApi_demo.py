#-*- coding:utf-8 _*- 
""" 
@file: move_detail.py 
@time: 2020/08/20
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
import random

api_key_list = ['0b2bdeda43b5688921839c8ecb20399b','0df993c66c0c636e29ecbb5344252a4a']
api_key = random.choice(api_key_list)

'''
正在热映
接口示例：/v2/movie/in_theaters?apikey=0b2bdeda43b5688921839c8ecb20399b
参数
start : 数据的开始项
count：单页条数
city：城市
'''
# url = f'http://api.douban.com/v2/movie/in_theaters?apikey={api_key}&city=武汉' # {'msg': 'invalid_credencial2', 'code': 109, 'request': 'GET /v2/movie/coming_soon'}
url = f'http://t.yushu.im/v2/movie/in_theaters?apikey={api_key}&city=武汉'     #2020.08.20 可用，正常返回数据
response = requests.get(url)
print(response.json())



'''
#获取电影top250
# 接口：https://api.douban.com/v2/movie/top250?apikey=0b2bdeda43b5688921839c8ecb20399b
#
# 访问参数：
#
# start : 数据的开始项
# count：单页条数
'''
# url = f"https://api.douban.com/v2/movie/top250?apikey={api_key}"  #不可用，返回{'msg': 'invalid_credencial2', 'code': 109, 'request': 'GET /v2/movie/coming_soon'}
url = f"http://t.yushu.im/v2/movie/top250?apikey={api_key}"         #2020.8.20 可用，正常返回数据
response = requests.get(url)
print(response.json())




'''
# 获取即将上映电影：
# 接口：https://api.douban.com/v2/movie/coming_soon?apikey=0b2bdeda43b5688921839c8ecb20399b
# 访问参数：
# start : 数据的开始项
# count：单页条数
'''
# url = f"https://api.douban.com/v2/movie/coming_soon?apikey={api_key}"  #不可用，返回{'msg': 'invalid_credencial2', 'code': 109, 'request': 'GET /v2/movie/coming_soon'}
url = f"http://t.yushu.im/v2/movie/coming_soon?apikey={api_key}"         #2020.8.20 可用
response = requests.get(url)
print(response.json())


'''
# 电影搜索
# 接口：https://api.douban.com/v2/movie/search?apikey=0b2bdeda43b5688921839c8ecb20399b
# 访问参数：
# start : 数据的开始项
# count：单页条数
# q：要搜索的电影关键字
# tag：要搜索的电影的标签
'''
# url = f"https://api.douban.com/v2/movie/search?apikey={api_key}&q=教父"  #不可用，返回{'msg': 'invalid_credencial2', 'code': 109, 'request': 'GET /v2/movie/search'}
url = f"http://t.yushu.im/v2/movie/search?apikey={api_key}&q=教父"  #可用
response = requests.get(url)
print(response.json())


'''
# 电影详情
# 接口：https://api.douban.com/v2/movie/subject/:id?apikey=0b2bdeda43b5688921839c8ecb20399b
# 访问参数：
# 电影id
'''
# url = f"https://api.douban.com/v2/movie/subject/1291841?apikey={api_key}"  #不可用，返回{'msg': 'invalid_credencial2', 'code': 109, 'request': 'GET /v2/movie/subject/1291841'}
# url = f"http://t.yushu.im/v2/movie/subject/1291841?apikey={api_key}"   #返回 {}
url = f"http://t.yushu.im/v2/movie/subject/326"  #可行，但是这个为电影id，不是subject_id
# url = f"http://t.yushu.im/v2/movie/subject/26754233"
print(url)
response = requests.get(url)
print(response.json())