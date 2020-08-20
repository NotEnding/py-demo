

## 豆瓣API 说明

#### 正在热映

接口示例

```python
#老版
http://api.douban.com/v2/movie/in_theaters?apikey=0b2bdeda43b5688921839c8ecb20399b
#新版
http://t.yushu.im/v2/movie/in_theaters?apikey=0b2bdeda43b5688921839c8ecb20399b
```

接口参数

```
start : 数据的开始项
count：单页条数
city：城市
```

示例

```python
url = f'http://api.douban.com/v2/movie/in_theaters?apikey={api_key}&city=武汉' 
#{'msg': 'invalid_credencial2', 'code': 109, 'request': 'GET/v2/movie/coming_soon'}   #老版接口已不可用

url = f'http://t.yushu.im/v2/movie/in_theaters?apikey={api_key}&city=武汉'     
response = requests.get(url)
print(response.json())     #2020.08.20 亲测可用，正常返回数据
```

#### 电影top250

接口示例

```
#老版
https://api.douban.com/v2/movie/top250?apikey=0b2bdeda43b5688921839c8ecb20399b
#新版
http://t.yushu.im/v2/movie/top250?apikey=0b2bdeda43b5688921839c8ecb20399b
```

接口参数

```
# start : 数据的开始项
# count：单页条数
```

示例

```python
url = f"https://api.douban.com/v2/movie/top250?apikey={api_key}"  
#{'msg': 'invalid_credencial2', 'code': 109, 'request': 'GET /v2/movie/coming_soon'}   老版本接口已不可用

url = f"http://t.yushu.im/v2/movie/top250?apikey={api_key}"
response = requests.get(url)
print(response.json())     #2020.8.20 亲测可用，正常返回数据
```

#### 即将上映电影

接口示例

```
#老版
https://api.douban.com/v2/movie/coming_soon?apikey=0b2bdeda43b5688921839c8ecb20399b
#新版
http://t.yushu.im/v2/movie/coming_soon?apikey=0b2bdeda43b5688921839c8ecb20399b
```

接口参数

```
# start : 数据的开始项
# count：单页条数
```

示例

```python
url = f"https://api.douban.com/v2/movie/coming_soon?apikey={api_key}"  
#{'msg': 'invalid_credencial2', 'code': 109, 'request': 'GET /v2/movie/coming_soon'}  老版本接口已不可用

url = f"http://t.yushu.im/v2/movie/coming_soon?apikey={api_key}"         
response = requests.get(url)
print(response.json())   #2020.8.20 亲测可用
```

#### 搜索电影

接口示例

```
#老版
https://api.douban.com/v2/movie/search?apikey=0b2bdeda43b5688921839c8ecb20399b
#新版
http://t.yushu.im/v2/movie/search?apikey=0b2bdeda43b5688921839c8ecb20399b
```

接口参数

```
# start : 数据的开始项
# count：单页条数
# q：要搜索的电影关键字
# tag：要搜索的电影的标签
```

示例

```python
url = f"https://api.douban.com/v2/movie/search?apikey={api_key}&q=教父"  
#{'msg': 'invalid_credencial2', 'code': 109, 'request': 'GET /v2/movie/search'}  老版本测试已不可用

url = f"http://t.yushu.im/v2/movie/search?apikey={api_key}&q=教父"  
response = requests.get(url)
print(response.json())    #2020.8.20 亲测可用
```

#### 电影详情

接口示例

```
#老版
https://api.douban.com/v2/movie/subject/:id?apikey=0b2bdeda43b5688921839c8ecb20399b
#新版
http://t.yushu.im/v2/movie/subject/326
```

参数

```
#电影id
```

示例

```python
url = f"https://api.douban.com/v2/movie/subject/1291841?apikey={api_key}"  
# {'msg': 'invalid_credencial2', 'code': 109, 'request': 'GET /v2/movie/subject/1291841'}  老版测试已不可用

url = f"http://t.yushu.im/v2/movie/subject/1291841?apikey={api_key}"   
#{}  测试不可用，返回空字典

url = f"http://t.yushu.im/v2/movie/subject/26683723"
response = requests.get(url)
print(response.json())
# 这样请求返回是 {}
```

```python
url = f"http://t.yushu.im/v2/movie/subject/326"
response = requests.get(url)
print(response.json())
# 这样可以拿到结果，但是发现这个 “326”并非我们看到的 https://movie.douban.com/subject/26683723/  这串数字，326暂时不知从哪里获取
```

```json
# http://t.yushu.im/v2/movie/subject/326 返回结果示例
{
    "casts": [
        {
            "avatars": {
                "large": "https://img3.doubanio.com/view/celebrity/s_ratio_celebrity/public/p44501.jpg"
            },
            "name": "刘若英"
        },
        {
            "avatars": {
                "large": "https://img3.doubanio.com/view/celebrity/s_ratio_celebrity/public/p1452260519.76.jpg"
            },
            "name": "井柏然"
        },
        {
            "avatars": {
                "large": "https://img1.doubanio.com/view/celebrity/s_ratio_celebrity/public/p36798.jpg"
            },
            "name": "周冬雨"
        }
    ],
    "comments_count": 642,
    "countries": [
        "中国大陆"
    ],
    "directors": [
        {
            "avatars": {
                "large": null
            },
            "name": "刘若英"
        }
    ],
    "genres": [
        "剧情",
        "爱情"
    ],
    "id": 326,
    "images": {
        "large": "https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2519994468.jpg"
    },
    "original_title": "后来的我们",
    "rating": {
        "average": 7,
        "max": 10,
        "min": 0,
        "stars": "35"
    },
    "reviews_count": 119,
    "summary": "这是一个爱情故事，关于一对异乡漂泊的年轻人。\\n十年前，见清和小晓偶然地相识在归乡过年的火车上。两人怀揣着共同的梦想，一起在北京打拼，并开始了一段相聚相离的情感之路。\\n十年后，见清和小晓在飞机上再次偶然重逢……\\n命运似乎是一个轮回。在一次次的偶然下，平行线交叉，再平行，故事始终有“然后”。可后来的他们，学会如何去爱了吗？",
    "title": "后来的我们",
    "warning": "数据来源于网络整理，仅供学习，禁止他用。如有侵权请联系公众号：小楼昨夜又秋风。我将及时删除。",
    "wish_count": 26250,
    "year": 2018
}
```

