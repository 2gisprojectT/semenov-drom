class Page():
    def __init__(self, driver):

        self.driver = driver
        self._search_bar = None
        self._search_result = None
        self._link = None
        self._route = None

    @property
    def search_bar(self):
        from helpers.search_bar import SearchBar

        if self._search_bar is None:
            self._search_bar = SearchBar(self.driver, self.driver.find_element_by_css_selector(SearchBar.selectors['self']))
        return self._search_bar

    @property
    def search_result(self):
        from helpers.search_result import SearchResult

        if self._search_result is None:
            self._search_result = SearchResult(self.driver, self.driver.find_element_by_css_selector(SearchResult.selectors['self']))
        return self._search_result

    def link(self):
        from helpers.link import Link

        if self._link is None:
            self._link = Link(self.driver, self.driver.find_element_by_css_selector(Link.selectors['self']))
        return self._link

    @property
    def route(self):
        from helpers.route import Route

        if self._route is None:
            self._route = Route(self.driver, self.driver.find_element_by_css_selector(Route.selectors['self']))
        return self._route

    def open(self, url):
        self.driver.get(url)

