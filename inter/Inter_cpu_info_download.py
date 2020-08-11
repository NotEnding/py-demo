import asyncio
import pyppeteer
import pymongo
import redis
import time
import random
import requests
from lxml import etree

client = pymongo.MongoClient(host='localhost', port=27017)
db = client['Inter']
collection = db['cpu']

redis_config = {
    "host": "localhost",
    "port": 6379,
    "password": '',
    "db": 1,
    "decode_responses": True,
    "max_connections": 100,
    "encoding": 'utf-8',
}
# 创建redis连接池
redis_pool = redis.ConnectionPool(**redis_config)
redis_conn = redis.Redis(connection_pool=redis_pool)


# 获取product URL
def get_product_url():
    # init  url
    url = 'https://ark.intel.com/content/www/cn/zh/ark.html#@Processors'

    headers = {
        "authority": "ark.intel.com",
        "path": "/content/www/cn/zh/ark.html",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "referer": "https://ark.intel.com/content/www/cn/zh/ark.html",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    }

    # 首先获取处理器下的全部 子品类
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        ele = etree.HTML(response.text)
        PanelLabel_list = ele.xpath('//div[@data-parent-panel-key="Processors"]/div/div/@data-panel-key')
        category_name_list = ele.xpath('//div[@data-parent-panel-key="Processors"]/div/div/span')
        for index in range(len(PanelLabel_list)):
            category_url = 'https://ark.intel.com/content/www/cn/zh/ark.html#@' + PanelLabel_list[index].strip()
            category_name = category_name_list[index].xpath('./text()')[0].strip()
            print(f"category_name:{category_name},PanelLabel:{PanelLabel_list[index]}")

            sub_url_path = f'//div[@data-parent-panel-key="{PanelLabel_list[index].strip()}"]/div/div//a/@href'
            sub_name_path = f'//div[@data-parent-panel-key="{PanelLabel_list[index].strip()}"]/div/div//a/text()'
            sub_href_list = ele.xpath(sub_url_path)
            sub_name_list = ele.xpath(sub_name_path)
            sub_category_info = []
            for i in range(len(sub_href_list)):
                sub_category_url = "https://ark.intel.com" + sub_href_list[i].strip()
                sub_category_name = sub_name_list[i].strip()
                print(f"当前请求子类：{sub_category_name},URL:{sub_category_url}")
                resp = requests.get(sub_category_url, headers=headers)
                if resp.status_code == 200:
                    html = etree.HTML(resp.text)
                    tr_list = html.xpath('//table[@id="product-table"]/tbody/tr')
                    product_url_list = []
                    for tr in tr_list:
                        product_url = tr.xpath('.//a/@href')[0]
                        # 加入到队列
                        redis_conn.lpush('product', product_url)
                        product_url_list.append("https://ark.intel.com" + product_url)
                    print(f"获取到product list,长度：{len(product_url_list)}")
                    sub_category_info.append(
                        {
                            "sub_category_name": sub_category_name,
                            "sub_category_url": sub_category_url,
                            "product_list": product_url_list
                        }
                    )
            # 添加到MongoDB
            result = {
                "category_name": category_name,
                "category_url": category_url,
                "PanelLabel": PanelLabel_list[index],
                "sub_category": sub_category_info
            }
            collection.insert(result)


# 下载详细文件
async def download_cpu_info(url):
    browser = await pyppeteer.launch(
        {
            'headless': False,
            'ignoreDefaultArgs': ['--enable-automation'],
            # 'devtools': True
            'args': [
                # proxy
                # f"--proxy-server={Ip_proxy()['proxies']}",
                # 最大化窗口
                "--start-maximized",
                '--disable-extensions',
                '--hide-scrollbars',
                '--disable-bundled-ppapi-flash',
                '--mute-audio',
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-gpu',
            ],
            'dumpio': True,
        }
    )
    page = await browser.newPage()
    # set headers
    await page.setExtraHTTPHeaders(
        {
            "authority": "ark.intel.com",
            "path": "/content/www/cn/zh/ark.html",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "referer": "https://ark.intel.com/content/www/cn/zh/ark.html",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
        }
    )

    await page.setUserAgent(
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36")
    await page.setViewport({'width': 1920, 'height': 1080})

    # 是否启用JS，enabled设为False，则无渲染效果
    await page.setJavaScriptEnabled(enabled=True)
    # 超时间见 1000 毫秒
    await page.goto(url, options={'timeout': 1000000})

    try:
        await page.click('#exportSpecification')
        await page.waitForNavigation({"timeout": 5000})
    except pyppeteer.errors.TimeoutError:
        print(f"download {url} success,close browser")

    await browser.close()


if __name__ == '__main__':
    # get_product_url()

    # init 处理
    # datas = collection.find()
    # for data in datas:
    #     sub_category_list = data['sub_category']
    #     for sub_category in sub_category_list:
    #         product_list = sub_category['product_list']
    #         for product in product_list:
    #             redis_conn.lpush('product',product)
    count = 0
    while True:
        length = redis_conn.llen("product")
        if length == 0 or count == 100:
            break
        else:
            # 单轮请求10次
            url = redis_conn.lpop("product")
            print(f"请求{url}")
            # print(url,type(url))
            asyncio.get_event_loop().run_until_complete(download_cpu_info(url))
            count += 1
            time.sleep(random.random() * 3)  # 每轮10次请求完成,随机进行延时
    print(f"获取全部的CPU info 完成，退出！！！")
