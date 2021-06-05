from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import schedule
import time

# uncomment the function  and  schedule line down bellow if u dont want to use cron jobs for  scheduling execution of the script and also  make a one  space indentation after declaring the function to all of the code bellow
#↓↓↓↓↓↓↓↓↓↓↓↓↓
# def remind():
    
# This blocks the pop up notification when u login  type 1 to acept type 2 to block the pop up
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

driver=webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://www.facebook.com/messages/t/')

# email pasword and login elements stored in a variable
email_input = driver.find_element_by_id("email")
pasword_input = driver.find_element_by_id("pass")
login_button = driver.find_element_by_id("loginbutton")

# ENTER YOUR EMAIL AND PASSWORD HERE
      #↓↓↓↓↓
email = ""
         #↓↓↓↓↓
password = ""

email_input.send_keys(email)
pasword_input.send_keys(password)
login_button.click()

# Selecting and inputing person u want to message
time.sleep(10)
#  enter a persons facebook name one line below
        #↓↓↓↓↓↓↓
contacts= [""]      
search_input = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div/div/div/label/input")
search_input.send_keys(contacts[0])

#Choosing firs account that pops up after searching the input
time.sleep(3)
first_account = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/ul/li[1]/ul/li[2]/div/a/div/div[2]/div/div/span/span/span")
first_account.click()

##writing  a message 
time.sleep(3)
#THE MESSAGE GOES HERE 
     #↓↓↓↓↓
message = ""
message_text_box = driver.find_element_by_css_selector(".notranslate")
message_text_box.send_keys(message)

##pressing send
time.sleep(1)
send_button = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div")
send_button.click()

#exits the browser 
time.sleep(7)
driver.quit()
#information about schedule https://pypi.org/project/schedule/
# I USE SCHEDULE TO SEND OUT A MESSAGE AT 15:00 PM
# choose to your liking

# uncomment if u dont use cron jobs ↓↓↓↓

# schedule.every().day.at("15:00").do(remind)
# while True:
#     schedule.run_pending()
#     time.sleep(1)