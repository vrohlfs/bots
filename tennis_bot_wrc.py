## Import packages
from os import times
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

import time
from datetime import date, timedelta


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
actions = ActionChains(driver)

driver.get("https://wtc.clubautomation.com/")
wait = WebDriverWait(driver, 10)

########### INPUT PARAMETERS ###################
## Login
try:
    from dev_settings import *
except:
    pass

## Details
guest_name = "Anderson Perilla"
game_date = date.today() + timedelta(days=3)
game_date = game_date.strftime("%m/%d/%Y") 
playing_time = "07:00 AM"
t = " 7:00am " #confirm time

# if playing_time == "07:00 AM":
#     time_index = "8"

# Website Login
login_form = driver.find_element_by_id("signin_login_form")
un = driver.find_element_by_name("login")
un.send_keys(username)

actions.send_keys(Keys.TAB).perform()
pw = wait.until(EC.visibility_of_element_located((By.NAME,"pass")))
pw.send_keys(password)

login_form.submit()

########### MAKE A NEW RESERVATION ###################
driver.get("https://wtc.clubautomation.com/event/reserve-court-new")

# wHO WILL HOST? -> Add guest
wait.until(EC.element_to_be_clickable((By.ID,"addParticipant"))).click()
guest = wait.until(EC.visibility_of_element_located((By.ID,"guest_1")))
guest.send_keys(guest_name)
wait.until(EC.element_to_be_clickable((By.ID,"ui-id-3"))).click()

# When ? 
reservation_date = wait.until(EC.visibility_of_element_located((By.ID,"date")))
reservation_date.clear()
reservation_date.send_keys(game_date)
wait.until(EC.element_to_be_clickable((By.ID,"interval-90"))).click()


# Search for available times
# From: option[8] = 7:00AM
selection_From_time = driver.find_element_by_xpath('//*[@id="timeFrom"]/option[8]')
driver.execute_script("arguments[0].setAttribute('selected', 'selected')", selection_From_time)
# To: option[24] = 11:00PM
selection_To_time = driver.find_element_by_xpath('//*[@id="timeTo"]/option[24]')
driver.execute_script("arguments[0].setAttribute('selected', 'selected')", selection_To_time)

## Click Search
search = wait.until(EC.visibility_of_element_located((By.ID,"reserve-court-search")))
actions.click(search).perform()

# Choose Time'
# wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="times-to-reserve"]/tbody/tr/td[1]/a[1]'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="times-to-reserve"]/tbody/tr/td[1]/a[text()[contains(.,"' + t +'" )]]'))).click()

# Confirm
# wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="confirm"]'))).click()

# close entire browser
#driver.quit()