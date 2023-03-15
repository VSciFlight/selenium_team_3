import time
from src.utils.chromeDriverSetUp import ChromeDriverSetUp
from src.pages.HomePage import HomePage
from selenium.webdriver.common.by import By

hp = HomePage
class TestHomePage(ChromeDriverSetUp):

    def test_home_btn(self):
        hp.home_btn_click(self)
        self.assertTrue("https://www.demoblaze.com/index.html")
    def test_contact_btn(self):
        hp.contact_btn_click(self)
        time.sleep(1)
        self.assertEqual(self.driver.find_element(By.XPATH, "/html/body/div[1]").get_attribute("class"), "modal fade show")
    def test_about_us_btn(self):
        hp.about_us_btn_click(self)
        self.assertEqual(self.driver.find_element(By.XPATH, '//*[@id="videoModal"]').get_attribute("id"), "videoModal")
    def test_cart_btn(self):
        hp.cart_btn_click(self)
        self.assertTrue("https://www.demoblaze.com/cart.html")
    def test_login_btn(self):
        hp.login_btn_click(self)
        time.sleep(1)
        self.assertEqual(self.driver.find_element(By.XPATH, '//*[@id="logInModal"]').get_attribute("class"), "modal fade show")
    def test_logout_btn(self):
        hp.logout_btn_click(self, 'User30', 'user123')
        self.assertTrue("https://www.demoblaze.com/index.html")
    def test_logo_btn(self):
        hp.logo_btn_click(self)
        self.assertTrue("https://www.demoblaze.com/index.html")