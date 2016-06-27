# -*- coding: utf-8 -*-

class SessionHelper():

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_id("id_username").click()
        wd.find_element_by_id("id_username").clear()
        wd.find_element_by_id("id_username").send_keys(username)
        wd.find_element_by_id("id_password").click()
        wd.find_element_by_id("id_password").clear()
        wd.find_element_by_id("id_password").send_keys(password)
        wd.find_element_by_xpath("//div[@class='login-window']//button[.='Войти']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("a.exit").click()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_element_by_css_selector("a.exit")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        # получаем имя текущего пользователя из окна браузера
        # и избавляемся от обрамляющих его круглых скобок - (username)
        return wd.find_element_by_css_selector("div.username.ico").text

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)