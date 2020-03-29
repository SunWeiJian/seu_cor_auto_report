#coding=utf-8
import time

from selenium import webdriver
import selenium
import os

try:
    sckey = os.environ(sckey)
try:
    user = os.environ(username)
    pwd = os.environ(password)
except:
    print("参数不完整或错误，请检查用户名、密码是否正确填写")
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

browser.get('https://xgbxscwx.seu.edu.cn/#/')  # 打开网页
time.sleep(3)

browser.find_element_by_xpath("//input[@id='username']").send_keys(user)  # 填入你的一卡通号
browser.find_element_by_xpath("//input[@id='password']").send_keys(pwd)  # 填入你的密码
browser.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(2)

print(driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/h2").text)
driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div[1]").click()
time.sleep(2)

try:
    driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div/form/div[9]/div/button").click()
except selenium.common.exceptions.NoSuchElementException:
    api = 'https://sc.ftqq.com/' + sckey + '.send'
    title = "上报成功"
    content = "今日已经上报过了！"
    data = {
        "text" : title,
        "desp" : content
            }
    req = requests.post(api, data = data)
    print("推送成功，假如没有收到推送，请检查key是否正确")
    exit(0)
else:
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