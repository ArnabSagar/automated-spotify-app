from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get("https://open.spotify.com")

log_in = driver.find_element_by_css_selector("#main > div > div.Root__top-container > div.Root__top-bar > header > div:nth-child(4) > button._2221af4e93029bedeab751d04fab4b8b-scss._1edf52628d509e6baded2387f6267588-scss")
log_in.click()
sleep(3)
#**************************************


email_entry = driver.find_element_by_xpath("//*[@id='login-username']")
email_entry.send_keys("chuckycheese99")

password_entry = driver.find_element_by_css_selector("#login-password")


#**************************************
login_button = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/form/div[3]/div[2]/button")
login_button.click()