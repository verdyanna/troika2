# -*- coding: utf-8 -*-
__author__ = 'Irsen'
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.platform_helper import PlatformHelper

class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        # дополнительное ожидание необходимо в случае динамического обновления страницы
        # self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.platform_helper = PlatformHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd

# if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_id("maintable")) > 0):
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
