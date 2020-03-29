#coding=utf-8
import time

from selenium import webdriver
import selenium
import os
import requests

try:
    user = os.environ["username"]
    pwd = os.environ["password"]
    sckey = os.environ["sckey"]
except:
    print("参数不完整或错误，请检查用户名、密码、key是否正确填写")
    exit(1)

options = webdriver.ChromeOptions()
options.add_argument('--disable-infobars')
options.add_argument("--disable-extensions");
options.add_argument("--disable-gpu");
options.add_argument("--disable-dev-shm-usage");
options.add_argument("--no-sandbox");
options.add_argument("--headless");
browser = webdriver.Chrome(options=options)
browser.set_window_size(1200, 2000)

browser.get('https://newids.seu.edu.cn/authserver/login?service=http://ehall.seu.edu.cn/qljfwapp2/sys/lwReportEpidemicSeu/*default/index.do')  # 打开网页
time.sleep(3)
print("1")
browser.find_element_by_xpath('//*[@id="username"]').send_keys(user)  # 填入你的一卡通号
browser.find_element_by_xpath('//*[@id="password"]').send_keys(pwd)  # 填入你的密码
browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div/div[3]/div/form/p[4]/button').click()
time.sleep(10)

print("3")
try:
    browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/button[1]').click()
except selenium.common.exceptions.NoSuchElementException:
    api = 'https://sc.ftqq.com/' + sckey + '.send'
    title = "今日已经上报过了"
    content = "今日已经上报过了！"
    data = {
        "text" : title,
        "desp" : content
            }
    req = requests.post(api, data = data)
    print("推送成功，假如没有收到推送，请检查key是否正确")
    exit(0)
else:
    time.sleep(7)
    browser.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/button').click()
    time.sleep(5)
    browser.find_element_by_xpath('/html/body/div[3]/div/div[3]/button[2]').click()
    api = 'https://sc.ftqq.com/' + sckey + '.send'
    title = "上报成功"
    content = "今日上报成功！"
    data = {
        "text" : title,
        "desp" : content
            }
    req = requests.post(api, data = data)
    print("推送成功，假如没有收到推送，请检查key是否正确")
    exit(0)
