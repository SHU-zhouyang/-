
## Issues: Can only be used at night (for the sake of searching method)


import time
import json
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
end_time="10-20晨报" #补报结束日期

class TestDailyReport():
  def setup_method(self):

    # 我的默认路径是这个C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe
    self.driver = webdriver.Chrome(executable_path="chromedriver") #如果报错可以修改为自己chromedriver.exe存储路径
    # chrome_driver = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
    # self.driver = webdriver.Chrome(executable_path=chrome_driver)
    vars = {}
  def teardown_method(self):
    quit()
  
  def login(self):
    zh=[""]
    mm=[""]
    self.driver.get("https://selfreport.shu.edu.cn/XueSFX/HalfdayReport_History.aspx")
    self.driver.find_element(By.ID, "username").click()
    ## ID and Password
    self.driver.find_element(By.ID, "username").send_keys(zh[0]) # 账号
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys(mm[0])# 密码
    self.driver.find_element(By.ID, "submit").click()
  def close(self):
    self.driver.quit()
    # pass
  def tes_dailyReport(self):
    global flag
    n = 0.5
    #timeset, depends on your Internet Situation
    while True:
        text=""
        try:
          text=self.driver.find_element(By.PARTIAL_LINK_TEXT, "未填报").text
          print(text)
        except:
          flag = 1
          break
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "未填报").click()
        time.sleep(n)
        self.driver.find_element(By.CSS_SELECTOR, "#p1_ChengNuo .f-field-body-checkboxlabel").click()
        time.sleep(n)
        self.driver.find_element(By.ID, "p1_TiWen-inputEl").click()
        time.sleep(n)
        temperature = random.randint(1, 6)/10
        t = str(36+temperature)
        self.driver.find_element(By.ID, "p1_TiWen-inputEl").send_keys(t)
        time.sleep(n)
        self.driver.find_element(By.CSS_SELECTOR, "#fineui_7 .f-field-body-checkboxlabel").click()
        time.sleep(n)
        self.driver.find_element(By.ID, "p1_ctl00_btnSubmit").click()
        time.sleep(n)
        self.driver.find_element(By.ID, "fineui_14").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "fineui_19").click()
        time.sleep(n)
        self.driver.find_element(By.ID, "lbReportHistory").click()

        if text[5:12] == end_time:

          flag=1
          break
flag=0
def main():
  while True:

    if flag==1:
      break
    TD = TestDailyReport()
    try:

      TD.setup_method()
      TD.login()
      TD.tes_dailyReport()
    except:
      TD.close()

if __name__ == "__main__":
  main()