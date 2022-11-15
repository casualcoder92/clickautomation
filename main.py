from selenium import webdriver
import time
from selenium.webdriver.common.by import By

username = "business@lead-academy.org"
password = "LeadAcademy1234@@!"
url = "https://account.shareasale.com/m-login.cfm?invalid=1&reason=10"


driver = webdriver.Chrome(executable_path="C:\\Users\\User\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get(url)

driver.find_element(By.ID,"username").send_keys(username)
driver.find_element(By.ID,"password").send_keys(password)
driver.find_element(By.XPATH,'//*[@id="form2"]/div/div[3]/button').click()
driver.find_element(By.XPATH,'//*[@id="merchantToolMenuListItem"]').click()
driver.find_element(By.XPATH,'//*[@id="merchantToolMenu"]/div/ul/li[1]/a/span').click()
driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/a[1]').click()
