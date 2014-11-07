__author__ = 'sasha'
#-*- coding:UTF-8 -*-
from base_component import BaseComponent


class Login(BaseComponent):

    selectors = {
        'self': '.authorisation',
        'login': '.authLinks > a',
        'input_login': '.auth-block .login-form .f .inp',
        'input_pass': '.auth-block .login-form .f-pass .inp',
        'submit': '.auth-block .login-form .f-btn .inp-b',
        'profile': '//td[2]/div/div/a',
        'settings': '.settings-ico',
        'rename': '//td[2]/input',
        'save_name': '//div/input',
        'notification': '//div[2]/span',
        'logout': '.logout-ico'

    }

    def log(self):
        self.driver.find_element_by_css_selector(self.selectors['login']).click()

    def submit(self, query, query1):
        self.driver.find_element_by_css_selector(self.selectors['input_login']).send_keys(query)
        self.driver.find_element_by_css_selector(self.selectors['input_pass']).send_keys(query1)
        self.driver.find_element_by_css_selector(self.selectors['submit']).click()

    def result(self):
        return self.driver.find_element_by_xpath(self.selectors['profile']).text

    def logout(self):
        self.driver.find_element_by_css_selector(self.selectors['logout']).click()

    def settings(self):
        self.driver.find_element_by_css_selector(self.selectors['settings']).click()

    def change_name(self, text):
        self.driver.find_element_by_xpath(self.selectors['rename']).clear()
        self.driver.find_element_by_xpath(self.selectors['rename']).send_keys(text)
        self.driver.find_element_by_xpath(self.selectors['save_name']).click()

    def neg_log_res(self):
        return self.driver.find_element_by_xpath(self.selectors['notification']).text




