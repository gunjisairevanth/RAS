from typing import cast
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
import json
import html_to_json
from bs4 import BeautifulSoup
import asyncio


opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--start-maximized')
opt.add_experimental_option("prefs", {
  
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 0,
    "profile.default_content_setting_values.notifications": 1
})


class Meets():

    def __init__(self, meet_link, start_time, end_time) -> None:

        self.browser = webdriver.Chrome(executable_path='./chromedriver',options=opt)
        # Login Page
        self.browser.get(
            'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')

        # input Gmail
        # print(self.browser.find_element_by_id("identifierId"))
        self.browser.find_element_by_id("identifierId").send_keys("meeting.recorder.revanth@gmail.com")
        self.browser.find_element_by_id("identifierNext").click()
        self.browser.implicitly_wait(10)

        # input Password
        self.browser.find_element_by_xpath(
            '//*[@id="password"]/div[1]/div/div[1]/input').send_keys("Bharathi@123")
        self.browser.implicitly_wait(10)
        self.browser.find_element_by_id("passwordNext").click()
        self.browser.implicitly_wait(1000)

        # go to google home page
        self.browser.get('https://google.com/')
        self.browser.implicitly_wait(10)
        time.sleep(5)

        self.browser.get(meet_link)

        self.browser.implicitly_wait(10)
        time.sleep(4)

        self.browser.find_element_by_css_selector( # mic off
                'div.U26fgb.JRY2Pb.mUbCce.kpROve.yBiuPb.y1zVCf.HNeRed.M9Bg4d').click()

        self.browser.find_element_by_css_selector( # mic off
                'div.U26fgb.JRY2Pb.mUbCce.kpROve.yBiuPb.y1zVCf.HNeRed.M9Bg4d').click()

        time.sleep(5)
        self.browser.implicitly_wait(10)
        self.browser.find_element_by_css_selector(
                'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()

        self.participants_data = {}
        self.participants_count = 1

        self.meet_duration = self.get_meet_duration( # return meet duration in mintutes
            start_time=start_time,
            end_time=end_time
        )


        if self.open_chat():
            for i in range(0,self.meet_duration):
                self.get_participants_list()
                self.save_chat_conversation()
                time.sleep(60)

        self.left_from_call()


    def left_from_call(self):
        # if self.participants_count == 1:
        self.browser.find_element_by_xpath('//button[@aria-label="Leave call"]').click()
        print("Left from call")
        



    def get_meet_duration(self,start_time,end_time):
        start_time = datetime.strptime(start_time,"%Y-%m-%dT%H:%M:%S")
        end_time = datetime.strptime(end_time,"%Y-%m-%dT%H:%M:%S")
        minutes_difference = (end_time-start_time).total_seconds()/60
        return int(minutes_difference)



    def open_chat(self):
        try:
            time.sleep(4)
            self.browser.implicitly_wait(10)
            self.browser.find_element_by_xpath(
                    '//button[@aria-label="Chat with everyone"]').click()
            time.sleep(2)
            self.browser.find_element_by_xpath(
                    '//button[@aria-label="Chat with everyone"]').click()
            time.sleep(2)
            self.browser.find_element_by_xpath(
                    '//button[@aria-label="Show everyone"]').click()
            time.sleep(2)
            self.browser.find_element_by_xpath(
                    '//button[@aria-label="Show everyone"]').click()
            return True
        except:
            print("Failed to open Chat")
            time.sleep(10)
            return self.open_chat()



    def save_chat_conversation(self):

        messages=[]
        chat_convarsation = self.browser.find_elements_by_xpath('//div[@class="GDhqjd"]')
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
                print("unable to read messages".format(**temp))

            messages.append(temp)

        with open("messages.json",'w+') as f:
            json.dump(messages,f)


    def get_participants_list(self):

        participants_list = self.browser.find_elements_by_xpath('//div[@aria-label="Participants"]//div[@class="kvLJWc"]//span[@class="ZjFb7c"]')
        time_date = str(datetime.now().strftime("%Y-%m-%dT%H:%M:%S"))
        temp = []
        for each_participants in participants_list:
            temp.append(each_participants.get_attribute('innerHTML'))
        self.participants_data[time_date] = temp

        with open("participants_data.json",'w+') as f:
            json.dump(self.participants_data,f)


# meets = Meets()
Meets(
    meet_link='https://meet.google.com/xfn-mdpt-bfa', 
    start_time='2021-11-21T10:30:00',
    end_time='2021-11-21T10:31:00'
)
