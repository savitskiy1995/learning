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
        wd.get("http://msk-srv-elma04/Security/Account/LogOn?ReturnUrl=%2f")
        wd.find_element_by_id("password").click()
        wd.close()
        wd.get("http://msk-srv-testit01/auth")
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='LOCAL'])[1]/following::button[1]").click()
        wd.find_element_by_id("username").clear()
        wd.find_element_by_id("username").send_keys("testrole")
        wd.find_element_by_name("null").click()
        wd.find_element_by_name("null").clear()
        wd.find_element_by_name("null").send_keys("Testrole12")
        wd.find_element_by_xpath("//button[@type='submit']").click()
        wd.get("http://msk-srv-testit01/projects")
        wd.find_element_by_id("9").click()
        wd.find_element_by_xpath("//div[@id='cdk-overlay-0']/ui-drawer-container/tms-projects-filters/form/section/ui-key-value-grid/nz-form-item[2]/nz-form-control/div/div/nz-select/nz-select-top-control/nz-select-item").click()
        wd.find_element_by_xpath("//div[@id='cdk-overlay-1']/nz-option-container/div/cdk-virtual-scroll-viewport/div/nz-option-item[2]/div").click()
        wd.find_element_by_xpath("//button[@type='submit']").click()
        wd.find_element_by_xpath("//tms-user-avatar[@id='8']/span").click()
        wd.find_element_by_xpath("//div[@id='cdk-overlay-3']/div/ul/li[5]/span").click()
    
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
