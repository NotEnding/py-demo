# coding: utf-8
#
import json
import os
import re
import time
import urllib.parse

import bs4
import httpx
import requests
import yaml

if not os.path.exists('cache.json'):
    with open('cache.json', 'wb') as f:
        f.write(b"{}")


def read_cache():
    with open('cache.json', 'rb') as f:
        try:
            return json.loads(f.read())
        except json.JSONDecodeError:
            return {}


def write_cache(data: dict):
    with open('cache.json', 'wb') as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=4).encode('utf-8'))


def movie_name2douban_link(name: str):
    cache = read_cache()
    if name in cache.keys():
        return cache[name]
    time.sleep(1.5)
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    headers = {'User-Agent': user_agent}
    html = requests.get("https://www.douban.com/search", params={
        "q": name}, headers=headers).text
    soup = bs4.BeautifulSoup(html, 'lxml')
    href = soup.find("div", "result").find_all("a")[1].attrs['href']
    u = urllib.parse.urlparse(href)
    qs = urllib.parse.parse_qs(u.query)
    assert qs.get('url'), 'missing url part'
    douban_link = qs['url'][0]
    cache[name] = douban_link
    write_cache(cache)
    return douban_link


def douban_link2mdtext(douban_link: str) -> str:
    """ 将豆瓣链接转化Markdown文本
    Eg: https://movie.douban.com/subject/1301419/
    """
    pattern = re.compile(r"subject/(.+?)/?$")
    m = pattern.search(douban_link)
    assert m
    sub_id = m.group(1)
    r = httpx.get(
        f"http://t.yushu.im/v2/movie/subject/{sub_id}?apikey=0df993c66c0c636e29ecbb5344252a4a")
    assert r.status_code == 200, r.text

    data = r.json()
    average_score = data['rating']['average']
    title = data['title']
    summary = data['summary']
    lines = []
    lines.append(f"### [{title}]({douban_link})")
    lines.append(f"豆瓣评分: {average_score}\n")
    lines.append(f">{summary}")
    lines.append("")

    if data['has_video']:
        for v in data['videos']:
            lines.append(f"- [{v['source']['name']}]({v['sample_link']})")

    return "\n".join(lines)




if __name__ == "__main__":
    dblink = movie_name2douban_link('我是传奇')
    mktext = douban_link2mdtext(dblink)
    with open('movies.yml', 'rb') as f:
        movies = yaml.load(f, Loader=yaml.SafeLoader)

    results = []
    for name in movies:
        print("Query movie:", name)
        dblink = movie_name2douban_link(name)
        print("Douban link:", dblink)
        mdtext = douban_link2mdtext(dblink)
        results.append(mdtext)

    with open("README.md", 'w', encoding='utf-8') as f:
        f.write("## 以下内容由代码自动生成\n生成方法: `python3 main.py`\n")
        f.write('\n\n'.join(results))
