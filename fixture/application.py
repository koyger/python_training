# -*- coding: utf-8 -*-
from selenium import webdriver
from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        print("APP INITIALIZED")

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_xpath(
                "//a[contains(text(),'Last name')]")) > 0):
            self.wd.get("http://localhost/addressbook/index.php")

    def destroy(self):
        self.wd.quit()
