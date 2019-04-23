# coding=utf-8
from selenium.webdriver import Firefox
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
import selenium
# class MyListener(AbstractEventListener):
#     def before_navigate_to(self, url, driver):
#         print("Before navigate to %s" % url)
#     def after_navigate_to(self, url, driver):
#         print("After navigate to %s" % url)

driver = Firefox()

driver.get("http://ivt.hschefu.com:88/user/login")
driver.find_element_by_name('username').send_keys('18583287560')
driver.find_element_by_name('password').send_keys('12345678')
driver.find_element_by_class_name('loginButton___1nomS').submit()
