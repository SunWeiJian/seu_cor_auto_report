from selenium import webdriver
import time


opt = webdriver.ChromeOptions()  # 创建浏览器
opt.headless = True  # 无窗口模式
driver = webdriver.Chrome(options=opt)  # 创建浏览器对象
driver.get('https://xgbxscwx.seu.edu.cn/#/')  # 打开网页
time.sleep(3)

driver.find_element_by_xpath("//input[@id='username']").send_keys("学号")
driver.find_element_by_xpath("//input[@id='password']").send_keys("密码")
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(2)

print(driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/h2").text)
driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div/div[1]").click()
# todo: clike()
print('上报成功！')