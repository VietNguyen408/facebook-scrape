#use command "python instagram.py" to scrape and then download all image in instagram
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
import wget

#You should put the driver in Program Files (x86) because it is easier to monitor your program
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.instagram.com/")

accept_first_cookies = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Accept All')]"))).click()
click_facebook = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='button']"))).click()
accept_fb_cookies = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Hyväksy kaikki')]"))).click()

#log in to instagram by facebook
username = driver.find_element_by_id("email")
password = driver.find_element_by_id("pass")
submit = driver.find_element_by_id("loginbutton")
username.clear()
password.clear()
#Enter your username and password between quote to log in (remember the country code)
username.send_keys("")
password.send_keys("")
submit.click()

not_now = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Not Now')]"))).click()

#searchbox instagram
searchbox = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchbox.clear()
keyword = "amee" #enter the name of instagram account that you want to scrape (eg.amee)
searchbox.send_keys(keyword)
time.sleep(2)
searchbox.send_keys(Keys.ENTER)
searchbox.send_keys(Keys.ENTER)

time.sleep(3)
driver.execute_script("window.scrollTo(0,2500);")
time.sleep(3)
images = driver.find_elements_by_tag_name('img')
images = [image.get_attribute('src') for image in images]

#save path
path = os.getcwd()
path = os.path.join(path, keyword + "s")

os.mkdir(path)
print(path)

#download the image with wget
counter = 0
for image in images:
    save_as = os.path.join(path, keyword + str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1