from typing import cast
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
import json
import html_to_json
from bs4 import BeautifulSoup
import asyncio

loop = asyncio.get_event_loop()

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



# Login Page
browser.get(
    'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')

# input Gmail
print(browser.find_element_by_id("identifierId"))
browser.find_element_by_id("identifierId").send_keys("meeting.recorder.revanth@gmail.com")
browser.find_element_by_id("identifierNext").click()
browser.implicitly_wait(10)

# input Password
browser.find_element_by_xpath(
    '//*[@id="password"]/div[1]/div/div[1]/input').send_keys("Bharathi@123")
browser.implicitly_wait(10)
browser.find_element_by_id("passwordNext").click()
browser.implicitly_wait(1000)

# go to google home page
browser.get('https://google.com/')
browser.implicitly_wait(10)
time.sleep(5)
#yDmH0d > c-wiz > div > div > div:nth-child(9) > div.crqnQb > div > div > div.QkY02 > div:nth-child(2) > div



browser.get('https://meet.google.com/jsd-zbbr-eou')

browser.implicitly_wait(10)
time.sleep(4)

browser.find_element_by_css_selector( # mic off
        'div.U26fgb.JRY2Pb.mUbCce.kpROve.yBiuPb.y1zVCf.HNeRed.M9Bg4d').click()

browser.find_element_by_css_selector( # mic off
        'div.U26fgb.JRY2Pb.mUbCce.kpROve.yBiuPb.y1zVCf.HNeRed.M9Bg4d').click()

time.sleep(5)
browser.implicitly_wait(10)
browser.find_element_by_css_selector(
        'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()


def open_chat():
    try:
        time.sleep(4)
        browser.implicitly_wait(10)
        browser.find_element_by_xpath(
                '//button[@aria-label="Chat with everyone"]').click()
        return True
    except:
        print("Failed to open Chat")
        time.sleep(10)
        return open_chat()



async def save_chat_conversation(browser):        
    for i in range(0,3600):
        messages=[]
        print(f"increment : {i}")
        chat_convarsation = browser.find_elements_by_xpath('//div[@class="GDhqjd"]')
        for each_user_chat in chat_convarsation:
            
            temp = {}
            try:
                name = each_user_chat.find_element_by_xpath('div[1]/div[1]').get_attribute('innerHTML')
                mesage_time = each_user_chat.find_element_by_xpath('div[1]/div[2]').get_attribute('innerHTML')
                temp['name'] = str(name)
                temp['mesage_time'] = str(mesage_time)
                temp['messages'] = []

            except:
                print("Unable to read messages")

            try:    
                for each_message in each_user_chat.find_elements_by_xpath('div[2]/div[@class="oIy2qc"]'):
                    time_in_utc = datetime.utcnow()
                    formatted_time_in_utc = time_in_utc.strftime("%Y-%m-%dT%H:%M:%S")
                    temp['messages'].append({
                    str(formatted_time_in_utc) : str(each_message.get_attribute('innerHTML'))
                    })

            except:
                print("unable to read {name} messages".format(**temp))

            messages.append(temp)
        time.sleep(10)


        with open("messages.json",'w+') as f:
            json.dump(messages,f)


async def get_peoples_list(browser):
    for i in range(0,2000):
        time.sleep(2)
        print(f"get_peoples_list {i}")

if open_chat():
    save_chat_conversation(browser)
    asyncio.gather(save_chat_conversation(browser),get_peoples_list(browser))
   

loop.run_forever()