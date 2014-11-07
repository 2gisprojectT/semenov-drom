#-*- coding:UTF-8 -*-
from unittest import TestCase
import unittest
from helps.page import Page
from selenium import webdriver


class SeleniumTest_aregistration_neg(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.page = Page(cls.driver)
        cls.page.open("http://drom.ru")
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_rega(self):
        self.page.rega.registr(u'1234567891')
        self.assertEqual(self.page.rega.result_sms(), u'Не удалось отправить SMS')
        self.page.rega.force()
        self.assertEqual(self.page.rega.result_phone(), u'Невозможно нормализовать номер '
                                                        u'(номер не в федеральном формате?)')


class SeleniumTest_search(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.page = Page(cls.driver)
        cls.page.open("http://drom.ru")
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_search_neg(self):
        self.page.search.finder(u'1234')
        self.page.search.finder_neg()
        self.assertEqual(self.page.search.finder_neg(), u'Поиск на Drom.ru')

    def test_search_pos(self):
        self.page.open("http://drom.ru")
        self.page.search.finder(u'ниссан')
        self.page.search.go()
        self.assertEqual(self.page.search.result(), u'Продажа Nissan Skyline GT-R в Новосибирске')


class SeleniumTest_login(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.page = Page(cls.driver)
        cls.page.open("http://drom.ru")
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_login_neg(self):
        self.page.login.log()
        self.page.login.submit('89639440258', '123456')
        self.assertEqual(self.page.login.neg_log_res(), u'К сожалению, нам не удалось вас авторизовать - '
                                                        u'неверный логин или пароль')

    def test_login_pos(self):
        self.page.login.log()
        self.page.login.submit('89639440258', '******')
        self.assertEqual(self.page.login.result(), '123, id: 18220755')
        self.page.login.settings()
        self.page.login.change_name('Alex')
        self.assertEqual(self.page.login.result(), 'Alex, id: 18220755')
        self.page.login.change_name('123')
        self.assertEqual(self.page.login.result(), '123, id: 18220755')
        self.page.login.logout()


if __name__ == '__main__':
    unittest.main()


'''
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.page = Page(self.driver)
        self.page.open("http://drom.ru")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.close()
'''