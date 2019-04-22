from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions

chromeoptions=webdriver.ChromeOptions()
chromeoptions.add_argument("start-maximized")
chromeoptions.add_argument("disable-notifications")
chromeoptions.add_argument("--disable-infobars")
chromeoptions.add_argument("--disable-extensions")

driver=webdriver.Chrome(executable_path='./drivers/chromedriver.exe',options=chromeoptions)

driver.implicitly_wait(10)

driver.get("https://the-internet.herokuapp.com/")

actual_title=driver.title
assert actual_title=="The Internet"



xpath_dyna="//li//a[contains(text(),'Dynamic Loading')]"
driver.find_element_by_xpath(xpath_dyna).click()

xpath_example_1="//a[contains(text(),'Example 1: Element on page that is hidden')]"
driver.find_element_by_xpath(xpath_example_1).click()

xpath_start="//div//button"
driver.find_element_by_xpath(xpath_start).click()

xpath_hello_world="//div/h4[contains(text(),'Hello World!')]"
wait=wait.WebDriverWait(driver,30)
element=expected_conditions.visibility_of_element_located((By.XPATH,xpath_hello_world))
wait.until(element)

assert "Hello World!"==driver.find_element_by_id("finish").text

driver.close()