from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(r"C:\Drivers\chromedriver.exe"))
driver.get("https://store.epicgames.com/en-US/")

search_field = driver.find_element(By.CLASS_NAME, "css-w7sedp")
search_field.click()
search_field.send_keys("Son") #Automation works until this step.

#Due to Captcha, suggested results did not appear. Therefore, I could not complete the following automated step.
#driver.find_element(By.CLASS_NAME, "css-z3vg5b").click()

