from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
import wget

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH,chrome_options=chrome_options)

driver.get("https://www.facebook.com/")

accept_fb_cookies = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Hyväksy kaikki')]"))).click()
username = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='email']")))
password = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='pass']")))
username.clear()
username.send_keys("yourusername/phonenumber")  #Enter your username
password.clear()
password.send_keys("your_password")  #Enter your password
button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type='submit']"))).click()

time.sleep(15)
images = []

for i in ['photos_by','photos_albums']:
    driver.get("https://www.facebook.com/the_profile_you_want_to_scrape/" + i + "/")
    time.sleep(5)

    n_scrolls = 2
    for j in range(1, n_scrolls):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

        anchors = driver.find_elements_by_tag_name('a')
        anchors = [a.get_attribute('href') for a in anchors]
        anchors = [a for a in anchors if str(a).startswith("https://www.facebook.com/photo")]

        for a in anchors:
            driver.get(a)
            time.sleep(2)
            img = driver.find_elements_by_tag_name("img")
            images.append(img[0].get_attribute("src"))

path = os.getcwd()
path = os.path.join(path, "Scrapped_FB")

os.mkdir(path)
print(path)

counter = 0
for image in images:
    save_as = os.path.join(path, str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1
