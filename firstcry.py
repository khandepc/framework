

from selenium import webdriver
from selenium.webdriver.support import wait
from selenium.webdriver.support import select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

import time

id_fname="u_0_j"
id_lname="u_0_l"
id_mob_email="u_0_o"
id_pass="u_0_v"
id_day="day"
id_month="month"
id_year="year"
xpath_gender="//*[@id='u_0_z']/span[2]/label"
xpath_sign_up_button="//button[@name='websubmit']"

driver=webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.facebook.com")
driver.implicitly_wait(10)
assert driver.title=="Facebook – log in or sign up"
driver.find_element_by_id(id_fname).send_keys("prashant")
time.sleep(2)
driver.find_element_by_id(id_lname).send_keys("khande")
time.sleep(2)
driver.find_element_by_id(id_mob_email).send_keys("1234567890")
time.sleep(2)
driver.find_element_by_id(id_pass).send_keys("khande123")
time.sleep(2)

element=driver.find_element_by_id(id_day)
sel=select.Select(element)
sel.select_by_visible_text("14")
time.sleep(2)
element=driver.find_element_by_id(id_month)
sel=select.Select(element)
sel.select_by_visible_text("Sept")
time.sleep(2)
element=driver.find_element_by_id(id_year)
sel=select.Select(element)
sel.select_by_visible_text("1996")
time.sleep(2)
driver.find_element_by_xpath(xpath_gender).click()
time.sleep(2)
driver.find_element_by_xpath(xpath_sign_up_button).click()

time.sleep(30)
driver.close()