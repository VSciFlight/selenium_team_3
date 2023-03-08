import unittest
import utils as u
from pages.home import HomePage

class TestHomePage(unittest.TestCase):
    def setUp(self):
        try:
            options = u.WebDriver.ChromeOptions()
            options.add_argument("--disable-extensions")
            self.driver = u.WebDriver.Chrome(options=options)
        except AssertionError:
            self.driver.quit()

    def tearDown(self):
        self.driver.quit()


    def test_home_btn(self):
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")
        hp = HomePage
        hp.click_home_btn(self)
        assert self.driver.current_url == "https://www.demoblaze.com/index.html"