import utils as u
from locators import locators

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def click_home_btn(self):
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(locators.Locator.locHome['Head_Home'])).click()