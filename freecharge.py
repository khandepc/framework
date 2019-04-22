from selenium import webdriver
from selenium.webdriver.support import select
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time


name_number="number"
xpath_datacard_type_radio="//span[contains(text(),'%s')]"
name_operat_type="dataCardType"
xpath_select_op="//*[@id='wrapper']/div/div/div/div[1]/div[2]/form/div[1]/div[3]/select/option[2]"
name_sel_op="operator"
class_name_proceed="_2eaVn"
xpath_enter_amount="//input[@name='amount']"
xpath_button_pay="//button[@class='btn _24xNn']"
xpath_close_new_frame="//span[@class='QBTfm']"
class_log_in_register="_3mvx0"

chromeoptions=webdriver.ChromeOptions()
chromeoptions.add_argument("start-maximized")
chromeoptions.add_argument("disable-notifications")
chromeoptions.add_argument("--disable-infobars")
chromeoptions.add_argument("--disable-extensions")

driver=webdriver.Chrome(executable_path="./drivers/chromedriver.exe",options=chromeoptions)
driver.implicitly_wait(10)

driver.get("http://freecharge.com")
actual_title=driver.title
assert actual_title=="Online Recharge on FreeCharge | Fast & Easy Recharge for Prepaid Mobile, Postpaid Mobile, Datacard & DTH."
driver.find_element_by_name(name_number).send_keys("8421835355")
time.sleep(5)
xpath_datacard_type_radio=xpath_datacard_type_radio%("Postpaid")
driver.find_element_by_xpath(xpath_datacard_type_radio).click()
element=driver.find_element_by_xpath("//option[contains(text(),'Airtel Postpaid')]")
element.click()
time.sleep(5)
element=driver.find_element_by_class_name("_2eaVn")
element.click()
element=driver.find_element_by_xpath(xpath_enter_amount).send_keys("399")
time.sleep(5)
element=driver.find_element_by_xpath(xpath_button_pay).click()
time.sleep(5)
element=driver.find_element_by_xpath(xpath_close_new_frame).click()
time.sleep(5)

element=driver.find_element_by_class_name(class_log_in_register).click()