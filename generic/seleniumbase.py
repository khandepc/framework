from selenium import webdriver
from selenium.webdriver.support import select

#creare class for seleniumbase
class seleniumBase:
    driver=None
    #to launch app
    def launch_app(self,browser_name,url):

        if browser_name=="chrome":

            chromeoptions = webdriver.ChromeOptions()
            chromeoptions.add_argument("start-maximized")
            chromeoptions.add_argument("--ignore-cetrificate-errors")
            chromeoptions.add_argument("disable-notifications")
            chromeoptions.add_argument("--disable-infobars")
            chromeoptions.add_argument("--disable-extensions")
            self.driver = webdriver.Chrome(executable_path='./drivers/chromedriver.exe', options=chromeoptions)
        elif browser_name=="firefox":
            pass
        elif browser_name=="ie":
            pass

        else:
            print("incorrect browser name")
        #to get url
        self.driver.get(url)

    #to close the browser
    def close_app(self):

        self.driver.close()

    #to find element

    def get_element(self,locater_type,locater):
        element=None
        if locater_type=="id":
            return self.driver.find_element_by_id(locater)
        elif locater_type=="name":
            return self.driver.find_element_by_name(locater)
        elif locater_type=="classname":
            return self.driver.find_element_by_class_name(locater)
        elif locater_type=="tagname":
            return self.driver.find_element_by_tag_name(locater)
        elif locater_type=="css":
            return self.driver.find_element_by_css_selector(locater)
        elif locater_type=="xpath":
            return self.driver.find_element_by_xpath(locater)
        elif locater_type=="linktext":
            return self.driver.find_element_by_link_text(locater)
        elif locater_type=="partiallinktext":
            return self.driver.find_element_by_partial_link_text(locater)
        else:
            print("invalid locater type")


    def identify_elements(self,locater_type,locater):
        elements=None
        if locater_type=="id":
            return self.driver.find_elements_by_id(locater)
        elif locater_type=="name":
            return self.driver.find_elements_by_name(locater)
        elif locater_type=="classname":
            return self.driver.find_elements_by_class_name(locater)
        elif locater_type=="tagname":
            return self.driver.find_elements_by_tag_name(locater)
        elif locater_type=="css":
            return self.driver.find_elements_by_css_selector(locater)
        elif locater_type=="xpath":
            return self.driver.find_elements_by_xpath(locater)
        elif locater_type=="linktext":
            return self.driver.find_elements_by_link_text(locater)
        elif locater_type=="partiallinktext":
            return self.driver.find_elements_by_partial_link_text(locater)
        else:
            print("invalid locater type")



    def get_page_details(type):
        driver=None
        if type=="title":
            return driver.title


    def perform_action(self,element,action_type,value=None):
        if action_type=="click":
            element.click(value)

        elif action_type=="send_keys":
            element.send_keys(value)

        elif action_type=="submit":
            element.submit(value)

        elif action_type=="select":
            element=select.Select(element)
            element.select_by_visible_text(value)
        else:
            print("action_type is unknown")