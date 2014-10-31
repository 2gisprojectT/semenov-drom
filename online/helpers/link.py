from helpers.base_component import BaseComponent


class Link(BaseComponent):

    selectors = {
        'self': '.extras__group',
        'input': '.share__popupUrlInput',
        'submit': '.extras__btn.extras__share'
    }

    def click_link(self):
        self.driver.find_element_by_css_selector(self.selectors['submit']).click()

    def get_link(self):
        return self.driver.find_element_by_css_selector(self.selectors['input']).get_attribute('value')




