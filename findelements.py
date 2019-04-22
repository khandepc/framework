from selenium import webdriver
from selenium.webdriver.common.by import By

chromeoptions=webdriver.ChromeOptions()
chromeoptions.add_argument("start-maximized")
chromeoptions.add_argument("disable-notifications")
chromeoptions.add_argument("--disable-infobars")
chromeoptions.add_argument("--disable-extensions")

driver=webdriver.Chrome(executable_path='./drivers/chromedriver.exe',options=chromeoptions)

driver.get("http://google.com")

element=driver.find_element_by_name("q")
element.send_keys("Dr.br.Ambedkar")
element=driver.find_element_by_name("btnK")
element.submit()
element=driver.find_elements_by_class_name("LC20lb")
print(len(element),": links are available on this webpage")