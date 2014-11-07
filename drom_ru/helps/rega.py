__author__ = 'sasha'
#-*- coding:UTF-8 -*-
from base_component import BaseComponent


class Rega(BaseComponent):

    selectors = {
        'self': '.authorisation',
        'click': '//td[2]/div/div/a[2]',
        'reg': 'phone_id',
        'submit': '.inp-b',
        'sms': '//div[3]/span',
        'force_click': '//div[3]/input',
        'phone': '//div[2]/span'

    }

    def registr(self, info):
        self.driver.find_element_by_xpath(self.selectors['click']).click()
        self.driver.find_element_by_id(self.selectors['reg']).send_keys(info)
        self.driver.find_element_by_css_selector(self.selectors['submit']).submit()

    def result_sms(self):
        return self.driver.find_element_by_xpath(self.selectors['sms']).text

    def result_phone(self):
        return self.driver.find_element_by_xpath(self.selectors['phone']).text

    def force(self):
        self.driver.find_element_by_xpath(self.selectors['force_click']).click()
