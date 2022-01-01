from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json
import html_to_json
from bs4 import BeautifulSoup

opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--start-maximized')
opt.add_experimental_option("prefs", {
  
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 0,
    "profile.default_content_setting_values.notifications": 1
})
browser = webdriver.Chrome(executable_path='./chromedriver',options=opt)


browser.get('http://localhost')
chat_convarsation = browser.find_elements_by_xpath('/html/body/div')

print(chat_convarsation)
print(type(chat_convarsation))
print(chat_convarsation.get_attribute('innerHTML'))
print("--------------------------")

for each_recod in chat_convarsation:

    # test = each_recod.find_elements_by_xpath('/div[1]/div[1]')

    print(each_recod.get_attribute('innerHTML'))
    print("--------------------------")



