from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chromeoptions=webdriver.ChromeOptions()
chromeoptions.add_argument("start-maximized")
#chromeoptions.add_argument("--ignore-cetrificate-errors")
chromeoptions.add_argument("disable-notifications")
chromeoptions.add_argument("--disable-infobars")
chromeoptions.add_argument("--disable-extensions")
driver=webdriver.Chrome(executable_path='./drivers/chromedriver.exe',options=chromeoptions)


#driver.maximize_window()
driver.get('http://google.com')
print(driver.name)
print(driver.title)
print(driver.current_url)


element=driver.find_element_by_name("q")
element.send_keys("ajanta caves Aurangabad maharashtra")
#element=driver.find_element(By.NAME,"btnK")
element.submit()
element=driver.find_elements_by_class_name("LC20lb")
print("elements on webpage",len(element))
time.sleep(30)
driver.close()
