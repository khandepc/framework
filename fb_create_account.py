
from generic.seleniumbase import seleniumBase
sb=seleniumBase()
sb.launch_app("chrome","https://www.facebook.com/")

element=sb.get_element("id","u_0_j")
sb.perform_action(element,"send_keys","prashant")

element=sb.get_element("id","u_0_l")
sb.perform_action(element,"send_keys","khande")

element=sb.get_element("id","u_0_o")
sb.perform_action(element,"send_keys","8421835355")

element=sb.get_element("id","u_0_v")
sb.perform_action(element,"send_keys","khande123")

element=sb.get_element("id","day")
sb.perform_action(element,"select",'14')

element=sb.get_element("id","month")
sb.perform_action(element,"select","Sept")

element=sb.get_element("id","year")
sb.perform_action(element,"select",'1996')

element=sb.get_element("xpath","//*[@id='u_0_z']/span[2]/label")
sb.perform_action(element,"click")
# from selenium import webdriver
# from selenium.webdriver.support import select
#
# import time
#
# id_fname="u_0_j"
# id_lname="u_0_l"
# id_mobile_email="u_0_o"
# id_password="u_0_v"
# id_bday_day="day"
# id_bday_month="month"
# id_bday_year="year"
# xpath_gender="//label[contains(text(),'%s')]/preceding-sibling::input"
# name_sign_up="websubmit"
#
# chromeoptions=webdriver.ChromeOptions()
# chromeoptions.add_argument("start-maximized")
# #chromeoptions.add_argument("--ignore-cetrificate-errors")
# chromeoptions.add_argument("disable-notifications")
# chromeoptions.add_argument("--disable-infobars")
# chromeoptions.add_argument("--disable-extensions")
# driver=webdriver.Chrome(executable_path='./drivers/chromedriver.exe',options=chromeoptions)
#
# driver.get('http://fb.com')
# # actual_title=driver.title
# # assert actual_title=="Facebook - log in or sign up"
#
# element=driver.find_element_by_id(id_fname)
# element.send_keys("prashant")
#
# element=driver.find_element_by_id(id_lname)
# element.send_keys("khande")
#
# element=driver.find_element_by_id(id_mobile_email)
# element.send_keys("1234567890")
#
# element=driver.find_element_by_id(id_password)
# element.send_keys("khande123")
#
# element=driver.find_element_by_id(id_bday_day)
# sel=select.Select(element)
# sel.select_by_index(14)
#
# element=driver.find_element_by_id(id_bday_month)
# sel=select.Select(element)
# sel.select_by_value("9")
#
# element=driver.find_element_by_id(id_bday_year)
# sel=select.Select(element)
# sel.select_by_visible_text("1996")
#
# xpath_gender=xpath_gender%("Male")
# element=driver.find_element_by_xpath(xpath_gender)
# element.click()
#
#
# element=driver.find_element_by_name(name_sign_up)
# element.click()
#
# time.sleep(30)
# driver.close()
