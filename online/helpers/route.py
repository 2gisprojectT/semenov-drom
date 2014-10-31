from helpers.base_component import BaseComponent


class Route(BaseComponent):

    selectors = {
        'self': '.online__searchBar',
        'router': '#module-1-1 > div.searchBar__tabs > div.searchBar__tab.searchBar__rsTab',
        'inputFrom': '.searchBar__form .searchBar__textfield._from .suggest__input',
        'inputTo': '.searchBar__form .searchBar__textfield._to .suggest__input',
        'metro': 'div.searchBar__transportButton.searchBar__transportSubway',
        'submit': '.searchBar__submit._rs',
        'result': 'header.routeResults__header'
    }

    def input(self, query, query1):
        self.driver.find_element_by_css_selector(self.selectors['inputFrom']).send_keys(query)
        self.driver.find_element_by_css_selector(self.selectors['inputTo']).send_keys(query1)

    def finder(self):
        self.driver.find_element_by_css_selector(self.selectors['submit']).submit()

    def rtr(self):
        self.driver.find_element_by_css_selector(self.selectors['router']).click()

    def result(self):
        self.driver.find_element_by_css_selector(self.selectors['result']).get_attribute('value')

    def metro(self):
        self.driver.find_element_by_css_selector(self.selectors['metro']).click()


