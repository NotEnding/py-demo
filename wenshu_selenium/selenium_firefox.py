"""程序说明"""
# -*-  coding: utf-8 -*-
# Author: cao wang
# Datetime : 2020
# software: PyCharm
# 收获:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import math
import time
import logging
from selenium.webdriver.firefox.options import Options
import os
from crawler_tools import user_agent as u
from datetime import datetime
from selenium.common.exceptions import *
import pyautogui
import random
from selenium.webdriver import ActionChains
from retrying import retry

logging.disable(logging.INFO)
def start_logger():
    path = os.path.dirname(__file__)+"\\log"
    if not os.path.exists(path):
        os.makedirs(path)
    """日志初始化设置、文件名（时间）、DEBUG为调试级别(级别导致输出内容的不同）、日志的记录格式、日期格式"""
    logging.basicConfig(filename=path+'//daily_report_%s.log' %datetime.strftime(datetime.now(), '%m%d%Y_%H%M%S'),
        level=logging.WARNING,
        format='%(asctime)s %(message)s',
        datefmt='%m-%d %H:%M:%S')
start_logger()


class Selenium_firefox():
    def __init__(self):
        # 设置输出内容目录
        # 下载无弹窗
        path = "E:\Firefox\Download"
        if not os.path.exists(path):
            os.makedirs(path)
        profile = webdriver.FirefoxProfile()
        # profile.set_preference('browser.download.folderList', 2)
        # logging.info('运行支持')

        profile.set_preference('browser.download.dir', path.strip('\u202a'))
        profile.set_preference('browser.download.folderList', 2)
        profile.set_preference('browser.download.manager.showWhenStarting', False)
        profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip,application/octet-stream')
        # 无图
        profile.set_preference('browser.migration.version', 9001)
        profile.set_preference('permissions.default.image', 2)
        profile.set_preference('user-agent', u()['User-Agent'])
        ops = Options()
        ops.add_argument('--headless')
        ops.add_argument('disable-infobars')
        """网页获取"""
        self.browser = webdriver.Firefox(profile,options=ops)
        self.wait = WebDriverWait(self.browser, 20)
        self.browser.get('https://wenshu.court.gov.cn/website/wenshu/181217BMTKHNT2W0/index.html?pageId=d176b4c9586ed2bea95d1fbab98bdd9d&s8=02')
    @retry
    def login(self):
        """登录"""
        # 切换框架
        wait = self.wait
        self.browser.refresh()
        frame = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="contentIframe"]')))
        self.browser.switch_to.frame(frame)


        click = wait.until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/app-root/div/app-login/div/div/form/div/div[1]/input')))
        # actions.move_to_element(click).click().perform()
        # click.click()
        click.send_keys("自己的手机号")
        time.sleep(1)
        click1 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.ng-invalid')))
        # click1.clear()
        click1.send_keys("密码")
        time.sleep(1)#等一秒是最优选择，短了网络错误
        button1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.custom-button')))
        button1.click()
        # 必须加上表单退出，否者就是死元素无法定位
        self.browser.switch_to.default_content()

        # 新版改变，导致无法直接进入刑事
        click = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="_view_1540966819000"]/div/ul/li[2]/a')))

        click.click()



        #self.browser.refresh()

    def content_change(self,country, index_, keyword):

        wait =self.wait

        self.login()


        """优化为发送country：高级检索 """

        #self.browser.switch_to.window(self.browser.window_handles[1])
        self.browser.refresh()
        click1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.advenced-search')))#/html/body/div/div[3]/diy:lawyee/div/div[1]/div[1]
        click1.click()
        # 判决结果检索
        #keyword_select = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="qbType"]')))
        #keyword_select.click()
        #select = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="qwTypeUl"]/li[7]')))
        #select.click()
        send_ = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="qbValue"]')))
        send_.clear()
        send_.send_keys(keyword)
        # country限定
        send1 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="s2"]')))  # //div[@class ="search-wrapper clearfix"]/div[@class =
        # "search-middle"]/input全文输入
        send1.send_keys(country)
        button_1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchBtn"]')))
        button_1.click()
        # logging.info('运行至发送country处。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。')
        time.sleep(0.3)
        #self.browser.refresh()
        """文书数量：15"""

        button_ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.pageSizeSelect')))
        button_.click()
        # time.sleep(1)
        button_ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.pageSizeSelect > option:nth-child(3)')))
        button_.click()
        time.sleep(1)
        # 刷新一下
        #self.browser.refresh()

        #except TimeoutException as e:
            #print("没有检索到裁判文书而导致元素找不到")
        """目的：减少遍历次数，进行页数遍历"""

        condition = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="_view_1545184311000"]/div[1]/div[2]/span')))
        #print(condition.text)  # 不能直接//text()原因不明
        conditions = math.ceil(int(condition.text) / 15)  # 最长12，最短6
        # print(conditions)
        if int(condition.text) == 0:
            # with open(path + '/没有文书的城市.txt', 'a+', encoding='utf-8')as file:
            # file.write("{}没有检索到文书\n".format(str(country)))
            pass
        elif int(conditions) > 40:  # condition本身已经除了15
            with open(path + '/第三次超过600页.txt', 'a+', encoding='utf-8')as file:
                file.write(
                    '出现超过600条的裁判文书,其所在区域为：' + str(country) + '，其数量为：' + str(condition.text) + str(keyword) + '\n')
            # logging.warning('出现超过600条的裁判文书,其所在区域为：' + str(country) + '，其数量为：' + str(condition.text) + str(keyword) + '\n')
            # 超过600的另作处理
        else:
            for index in range(conditions):
                # browser.execute_script('document.documentElement.scrollTop = 100000')
                try:
                    '''全选的点击'''
                    time.sleep(1)
                    click_1 = wait.until(EC.element_to_be_clickable( (By.XPATH, '//div[@class="LM_tool clearfix"]/div[4]/a[1]/label')))
                    click_1.click()
                    '''批量下载的点击'''
                    click_2 = wait.until(EC.presence_of_element_located( (By.XPATH, '//html/body/div/div[4]/div[2]//div[@class="LM_tool clearfix"]/div[4]/a[3]')))
                    click_2.click()
                    print('第%d页下载成功============================================' % index)
                    """下一页的点击"""
                    button_ = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="left_7_3"]/a[last()]')))
                    button_.click()
                except:
                    logging.warning('第%d页出现缺失' % index + str(country))

    def start_crawl(self,content):  # keyword):
        """主函数遍历页数"""
        # 当前目录下的城市限制调件
        index_ = 0

        i, keyword = content.strip().split(",")[1], content.strip().split(",")[0]
        try:
            self.content_change(i.strip(), index_, keyword)
            with open(path + "/已经爬取的.txt", 'a', encoding='utf-8')as f:
                f.write(content)
            #self.browser.close()
            self.browser.quit()
        except Exception as e:
            self.browser.quit()
            logging.info(e)





if __name__ =="__main__":
    # 读取限定词目录
    path = os.path.dirname(__file__)
    print(path)
    file = r"J:\PyCharm项目\项目\中国裁判文书网\selenium路线\文书爬取模块\crime_and_city.txt"
    with open(file, 'r', encoding='utf-8')as f:
        contents = f.readlines()
    print("原contens", len(contents))
    file = r"J:\PyCharm项目\项目\中国裁判文书网\selenium路线\文书爬取模块\已经爬取的.txt"
    with open(file, 'r', encoding='utf-8')as f:
        del_contents = f.readlines()

    # 实现中断继续的功能
    contents = [i for i in contents if i not in del_contents]
    print("现在的contents", len(contents))

    for q in range(len(contents)):
        i = random.choice(contents)
        #print(i)
        Selenium_firefox().start_crawl(i)



