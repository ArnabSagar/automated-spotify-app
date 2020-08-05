from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://open.spotify.com")
print(driver.title)


log_in = driver.find_element_by_css_selector("#main > div > div.Root__top-container > div.Root__top-bar > header > div:nth-child(4) > button._2221af4e93029bedeab751d04fab4b8b-scss._1edf52628d509e6baded2387f6267588-scss")
log_in.click()
