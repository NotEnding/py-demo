#-*- coding:utf-8 _*- 
""" 
@file: douyin.py 
@time: 2020/08/21
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
import random
import time

import requests
import re
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# file dir
video_path = os.path.join(BASE_DIR, "video")  # 存储配置信息
if not os.path.exists(video_path):
    os.mkdir(video_path)


def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").json()



def Ip_proxy():
    """
    :return: 获取的代理IP：port
    """

    proxies = None
    url = 'http://api.ip.data5u.com/dynamic/get.html'
    params = {
        'order': 'de15a979c3c4c0ab0de6e89f6a37924d',
        'random': 1,
        'json': 1
    }
    while not proxies:
        try:
            res = requests.get(url, params=params, verify=False)
            if res.ok and res.json()['success']:
                proxies = {"proxies": "http://{}:{}".format(res.json()['data'][0]['ip'], res.json()['data'][0]['port'])}
            else:
                time.sleep(.2)
        except:
            time.sleep(.2)
    return proxies



class DY():  # 抖音
    headers = {  # 模拟手机端
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Mobile Safari/537.36'
    }

    def __init__(self, s_url):
        '''
        :param s_url: 客户端分享，复制链接
        '''
        self.url = re.findall('(https?://[^\s]+)', s_url)[0]  # 正则提取字符串中的链接

    def dy_download(self):
        proxy = Ip_proxy()
        proxies = {
            "http": proxy['proxies'],
            "https": proxy['proxies']
        }
        rel_url = str(requests.get(self.url, proxies=proxies, headers=self.headers).url)
        print(f"复制链接在网页版打开后的url：{rel_url}")
        if 'video' == rel_url.split('/')[4]:
            URL = 'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=' + rel_url.split('/')[5] + '&dytk='
            r = requests.get(URL, proxies=proxies, headers=self.headers)
            video_url = r.json()['item_list'][0]['video']['play_addr']['url_list'][0].replace('/playwm/', '/play/')
            print(video_url)
            video_name = r.json()['item_list'][0]['share_info']['share_title'].split('#')[0].split('@')[0].replace(' ','')
            if video_name == '':
                video_name = int(random.random() * 2 * 1000)
            if len(str(video_name)) > 20:
                video_name = video_name[:20]
            video = requests.get(video_url, proxies=proxies, headers=self.headers).content
            with open(os.path.join(video_path,f'{str(video_name)}.mp4'),'wb') as f:
                f.write(video)
            if 'www.iesdouyin.com' in self.url:
                print("【抖音短视频】: {}.mp4 无水印视频下载完成！".format(video_name))
            if 'v.douyin.com' in self.url:
                print("【抖音短视频/抖音极速版】: {}.mp4 无水印视频下载完成！".format(video_name))


if __name__ == '__main__':
    s_url = 'https://v.douyin.com/JMKHkqt/' #客户端分享链接
    DY(s_url).dy_download()

    # proxy = get_proxy().get("proxy")
    # proxies = {"http": "http://{}".format(proxy)}
    # print(proxies)
    #
    # response = requests.get('http://www.baidu.com',proxies=proxies)
    # print(response.text)