#-*- coding:UTF-8 -*-
from unittest import TestCase
import unittest
from selenium import webdriver
from helpers.page import Page


class SeleniumTest(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.page = Page(self.driver)
        self.page.open("http://2gis.ru")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.close()

    def test_share_link(self):
        self.page.search_bar.search(u'полет')
        self.assertTrue(self.page.search_result.count > 0, 'Wrong count of firms')
        b = self.page.search_result.count
        self.page.link().click_link()
        a = self.page.link().get_link()
        self.page.open(a)
        self.assertEqual(self.page.search_result.count, b, 'error')

    def test_route(self):
        self.page.route.rtr()
        self.page.route.input(u'Площадь Ленина', u'метро студенческая')
        self.page.route.metro()
        self.page.route.finder()
        self.driver.implicitly_wait(30)
        result = self.page.route.result()
        assert (result, 'Метрополитен')


if __name__ == '__main__':
    unittest.main()
