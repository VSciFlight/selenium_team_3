import utils as u
import unittest
import pages.login_sign_up as abc
class TestLoginSignUp(unittest.TestCase):
    def setUp(self):
        self.url = 'https://demoblaze.com/index.html'
        self.driver = u.WebDriver.Chrome()
        self.driver.get(self.url)

    def test_sign_up(self):
        abc.sign_up()

    def tearDown(self):
        self.driver.close()