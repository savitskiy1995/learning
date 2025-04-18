# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import pytest
from application import Application


@pytest.fixture
def app(request):
    fixture = Applicatiom()
    request.addfinalizer(fixture.destroy)
    return fixture
  class test_add_group(unittest.Testcase):
    def create_group(self, wd):
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("testname")
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_link_text("Logout").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

