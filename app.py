from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://open.spotify.com")
print(driver.title)


log_in = driver.find_element_by_class_name(_2221af4e93029bedeab751d04fab4b8b-scss _1edf52628d509e6baded2387f6267588-scss)