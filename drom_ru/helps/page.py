class Page():
    def __init__(self, driver):

        self.driver = driver
        self._login = None
        self._search = None
        self._rega = None

    @property
    def login(self):
        from login import Login

        if self._login is None:
            self._login = Login(self.driver, self.driver.find_element_by_css_selector(Login.selectors['self']))
        return self._login


    @property
    def search(self):
        from search import Search

        if self._search is None:
            self._search = Search(self.driver, self.driver.find_element_by_css_selector(Search.selectors['self']))
        return self._search

    def open(self, url):
        self.driver.get(url)

    @property
    def rega(self):
        from rega import Rega

        if self._rega is None:
            self._rega = Rega(self.driver, self.driver.find_element_by_css_selector(Rega.selectors['self']))
        return self._rega
