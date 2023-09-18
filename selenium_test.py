from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://aws.amazon.com/")
time.sleep(5)
driver.quit()