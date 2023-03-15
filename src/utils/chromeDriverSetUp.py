import unittest
from src.utils.drivers import Drivers as D

class ChromeDriverSetUp(unittest.TestCase):
    def setUp(self):
        try:
            self.driver = D.get_chrome_driver(self)
            self.driver.maximize_window()
            self.driver.get("https://www.demoblaze.com/")
        except AssertionError:
            self.driver.quit()


    def tearDown(self):
        self.driver.quit()

#



