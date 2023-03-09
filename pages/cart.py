import utils as u


def add_to_cart_button():
    driver = u.WebDriver.Chrome()
    driver.get("https://demoblaze.com/index.html")
    u.sleep(5)
    driver.find_element(u.By.XPATH, '//*[@id="tbodyid"]/div[1]/div/div/h4/a').click()
    u.sleep(4)
    add_cart = driver.find_element(u.By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a')
    add_cart.click()
    u.sleep(4)
    u.WDW(driver, 5).until(u.EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
    driver.find_element(u.By.XPATH, '//*[@id="cartur"]').click()
    u.sleep(4)

########################################################################################################
import utils as u
import unittest


class Test_Cart_Page(unittest.TestCase):

    def setUp(self):
        self.driver = u.WebDriver.Chrome()

    def test_add_to_cart_button(self):
        self.driver.get("https://demoblaze.com/index.html")
        u.sleep(3)
        self.driver.find_element(u.By.XPATH, '//*[@id="tbodyid"]/div[1]/div/div/h4/a').click()
        u.sleep(3)
        self.add_cart = self.driver.find_element(u.By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a')
        self.add_cart.click()
        u.sleep(3)
        u.WDW(self.driver, 3).until(u.EC.alert_is_present())
        self.alert = self.driver.switch_to.alert
        self.alert.accept()
        self.driver.find_element(u.By.XPATH, '//*[@id="cartur"]').click()
        u.sleep(3)
        self.assertTrue(True)

    def tearDown(self):
        self.driver.quit()