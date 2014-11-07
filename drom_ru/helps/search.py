__author__ = 'sasha'
#-*- coding:UTF-8 -*-
from base_component import BaseComponent


class Search(BaseComponent):

    selectors = {
        'self': '.smallSearch',
        'string': 'q',
        'find': 'sa',
        'find1': '//td[2]/input',
        'link': 'Продажа Nissan в Новосибирске',
        'link1': '//td[3]/h3[12]/a',
        'h1': '//h1'

    }

    def finder(self, info):
        self.driver.find_element_by_id(self.selectors['string']).send_keys(info)
        self.driver.find_element_by_name(self.selectors['find']).click()

    def go(self):
        self.driver.find_element_by_link_text(self.selectors['link']).click()
        self.driver.find_element_by_xpath(self.selectors['link1']).click()

    def result(self):
        return self.driver.find_element_by_xpath(self.selectors['h1']).text

    def finder_neg(self):
        self.driver.find_element_by_xpath(self.selectors['find1']).click()
        return self.driver.find_element_by_xpath(self.selectors['h1']).text