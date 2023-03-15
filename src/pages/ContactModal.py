from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from src.locators.ContactLocators import contactlocs

class ContactModal:
    def __init__(self, driver):
        self.driver = driver

    def wdw_locator(self, locator):
        return WDW(self.driver, 5).until(EC.visibility_of_element_located(locator))

    def set_email(self, email):
        ContactModal.wdw_locator(self, contactlocs['Email_fld']).send_keys(email)
    def set_name(self, name):
        ContactModal.wdw_locator(self, contactlocs['Name_fld']).send_keys(name)
    def set_message(self, message):
        ContactModal.wdw_locator(self, contactlocs['Message_fld']).send_keys(message)
    def x_btn_click(self):
        ContactModal.wdw_locator(self, contactlocs['X_btn']).click()
    def close_btn_click(self):
        ContactModal.wdw_locator(self, contactlocs['Close_btn']).click()
    def send_message_click(self):
        ContactModal.wdw_locator(self, contactlocs['Send_msg_btn']).click()