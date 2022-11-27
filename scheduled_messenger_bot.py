from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import schedule
import time
import sys
import json

def send_and_quit():
    # press send button
    send_button.click()

    # exit the browser
    time.sleep(7)
    driver.quit()

    return schedule.CancelJob

# read config
with open(sys.argv[1]) as fp:
    config = json.load(fp)

# driver initialization
# block the pop up notification when login (type 1 to accept type 2 to block the pop up)
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options = chrome_options)

# open chat window
contact = config["contact"]
driver.get('https://www.facebook.com/messages/t/' + contact)

# enter email + password
email_input = driver.find_element_by_id("email")
pasword_input = driver.find_element_by_id("pass")
login_button = driver.find_element_by_id("loginbutton")

email = config["email"]
password = config["password"]

email_input.send_keys(email)
pasword_input.send_keys(password)
login_button.click()

# enter message
time.sleep(3)

while True:
    try:
        message_text_box = driver.find_element_by_css_selector(".notranslate")
        if message_text_box != None:
            break
    except:
        pass

    time.sleep(1)

messages = config["messages"]

for message in messages:
    message_text_box.send_keys(message)
    ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()

# find send button
send_button = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/span[2]/div")

# set up daily schedule at config["send_time"]
schedule.every().day.at(config["send_time"]).do(send_and_quit)

while True:
    schedule.run_pending()
    time.sleep(1)
