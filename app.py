from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from decouple import config


USERNAME = config('SPOTIFY_USERNAME')
PASSWORD = config('SPOTIFY_PASSWORD')
 
# webdriver setup and accessing website 

driver = webdriver.Chrome()
driver.get("https://open.spotify.com")
log_in = driver.find_element_by_xpath("//*[@id='main']/div/div[2]/div[1]/header/div[4]/button[2]")
log_in.click()
sleep(5)

# Login screen

email_entry = driver.find_element_by_xpath("//*[@id='login-username']").click()
email_entry.send_keys(Keys.HOME)
email_entry.send_keys(USERNAME)
print("yes1")

email_entry.send_keys(Keys.TAB)
sleep(2)

password_entry = driver.find_element_by_xpath("//*[@id='login-password']").click()
password_entry.send_keys(Keys.HOME)
password_entry.send_keys(PASSWORD)
print("yes2")

login_button = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/form/div[3]/div[2]/button")
login_button.click()
