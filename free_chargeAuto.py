
from selenium import webdriver
from selenium.webdriver.support import wait
from selenium.webdriver.support import select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time

name_number="number"


driver=webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.freecharge.in")

driver.find_element_by_name(name_number).send_keys("8421835355")
time.sleep(10)

