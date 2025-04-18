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
        self.driver = webdriver.Chrome(executable_path=r'')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self, username, password):
        driver = self.driver
        driver.get("http://msk-srv-elma04/Security/Account/LogOn?ReturnUrl=%2f")
        driver.find_element_by_id("password").click()
        driver.close()
        driver.get("http://msk-srv-testit01/auth")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='LOCAL'])[1]/following::button[1]").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(username)
        driver.find_element_by_name("null").click()
        driver.find_element_by_name("null").clear()
        driver.find_element_by_name("null").send_keys(password)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.get("http://msk-srv-testit01/projects")
        driver.find_element_by_id("9").click()
        driver.find_element_by_xpath(
            "//div[@id='cdk-overlay-0']/ui-drawer-container/tms-projects-filters/form/section/ui-key-value-grid/nz-form-item[2]/nz-form-control/div/div/nz-select/nz-select-top-control/nz-select-item").click()
        driver.find_element_by_xpath(
            "//div[@id='cdk-overlay-1']/nz-option-container/div/cdk-virtual-scroll-viewport/div/nz-option-item[2]/div").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//tms-user-avatar[@id='8']/span").click()
        driver.find_element_by_xpath("//div[@id='cdk-overlay-3']/div/ul/li[5]/span").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()