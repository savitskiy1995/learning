# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome(executable_path=r'')
        self.wd.implicitly_wait(30)

    def test_untitled_test_case(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.open_project_name(wd)

    def open_project_name(self, wd):
        self.go_to_projects(wd)

    def go_to_projects(self, wd):
        self.check_project_filter(wd)


    def open_home_page(self, wd):
        wd.get("http://msk-srv-elma04/Security/Account/LogOn?ReturnUrl=%2f")

    def login(self, wd):
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_id("password").click()
        wd.close()
        wd.get("http://msk-srv-testit01/auth")
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='LOCAL'])[1]/following::button[1]").click()
        wd.find_element_by_id("username").clear()
        wd.find_element_by_id("username").send_keys("testrole")
        wd.find_element_by_name("null").click()
        wd.find_element_by_name("null").clear()
        wd.find_element_by_name("null").send_keys("Testrole12")
        wd.find_element_by_xpath("//button[@type='submit']").click()

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
