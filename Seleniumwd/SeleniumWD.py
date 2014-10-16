#-*-coding:utf8-*-
from unittest import TestCase
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SeleniumTest(TestCase):

    def test_search(self):
        driver = webdriver.Firefox()
        driver.get("http://www.drom.ru")
        elem = driver.find_element_by_name("q")
        elem.send_keys(u"ниссан")
        elem.send_keys(Keys.RETURN)
        assert "Nissan" in driver.page_source
        ##xpath:href
        elem = driver.find_element_by_xpath("//a[contains(text(),'Посмотреть все модели Nissan')]").click()
        elem = driver.find_element_by_xpath("//a[contains(text(),'370Z')]").click()
        assert "car-photo" in driver.page_source
        ##xpath:position
        elem = driver.find_element_by_xpath("//div/div/a").click()
        driver.close()

if __name__ == '__main__':
    unittest.main()
