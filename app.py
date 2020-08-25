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
sleep(2)    

# Login screen
email_entry = driver.find_element_by_xpath("//*[@id='login-username']")
email_entry.click()
email_entry.send_keys(Keys.HOME)
email_entry.send_keys(USERNAME)

email_entry.send_keys(Keys.TAB)
sleep(2)

password_entry = driver.find_element_by_xpath("//*[@id='login-password']")
password_entry.click()
password_entry.send_keys(Keys.HOME)
password_entry.send_keys(PASSWORD)

login_button = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/form/div[3]/div[2]/button")
login_button.click()

# Cue music
sleep(5)
playlist_name = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/nav/div[2]/div/div/div[3]/div[2]/div/div/ul/div[1]/li/div/div/div/a/div')
playlist_name.click()

sleep(2)
play_button = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[4]/div[1]/div/div[2]/div/div/div[2]/section/div[3]/div/button')
play_button.click()

sleep(5)
device_picker = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[3]/footer/div/div[3]/div/div/div[2]')
device_picker.click()

sleep(2)
speaker = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[3]/footer/div/div[3]/div/div/div[2]/span/div/div/ul/button[2]/div[2]/div')
speaker.click()


