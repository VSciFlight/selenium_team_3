from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from src.utils.edgeDriverSetUp import EdgeDriverSetUp
from src.pages.HomePage import HomePage
from src.pages.ContactModal import ContactModal
from selenium.webdriver.common.by import By


hp = HomePage
cm = ContactModal

class TestContactModal(EdgeDriverSetUp):
    def test_sending_valid_message(self):
        hp.contact_btn_click(self)
        cm.set_email(self, "jhon34567@mail.com")
        cm.set_name(self, "Jhon")
        cm.set_message(self, "Hello world!")
        cm.send_message_click(self)
        WDW(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        self.assertEqual(alert.text, "Thanks for the message!!")
        alert.accept()

    def test_sending_invalid_email_message(self):
        hp.contact_btn_click(self)
        cm.set_email(self, "b!fg")
        cm.set_name(self, "Jhon")
        cm.set_message(self, "Hello world!")
        cm.send_message_click(self)
        WDW(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        self.assertNotEqual(alert.text, "Thanks for the message!!", msg="The message should not be sent")
        alert.accept()

    def test_sending_invalid_name_message(self):
        hp.contact_btn_click(self)
        cm.set_email(self, "jhon34567@mail.com")
        cm.set_name(self, 24324)
        cm.set_message(self, "Hello world!")
        cm.send_message_click(self)
        WDW(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        self.assertNotEqual(alert.text, "Thanks for the message!!", msg="The message should not be sent")
        alert.accept()

    def test_sending_invalid_message_without_char(self):
        hp.contact_btn_click(self)
        cm.send_message_click(self)
        WDW(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        self.assertNotEqual(alert.text, "Thanks for the message!!", msg="The message should not be sent")
        alert.accept()

    def test_name_length_more_than_10_char(self):
        hp.contact_btn_click(self)
        cm.set_email(self, "jhon34567@mail.com")
        cm.set_name(self, "Jhon" * 10)
        cm.set_message(self, "Hello world!")
        cm.send_message_click(self)
        WDW(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        self.assertNotEqual(alert.text, "Thanks for the message!!", msg="The message should not be sent")
        alert.accept()

    def test_message_length_more_than_256_char(self):
        hp.contact_btn_click(self)
        cm.set_email(self, "jhon34567@mail.com")
        cm.set_name(self, "Jhon")
        cm.set_message(self, "Hello world!" * 256)
        cm.send_message_click(self)
        WDW(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        self.assertNotEqual(alert.text, "Thanks for the message!!", msg="The message should not be sent")
        alert.accept()

    def test_X_btn(self):
        hp.contact_btn_click(self)
        cm.x_btn_click(self)
        self.assertEqual(self.driver.find_element(By.XPATH, "/html/body/div[1]").get_attribute("class"), "modal fade")

    def test_close_btn(self):
        hp.contact_btn_click(self)
        cm.close_btn_click(self)
        self.assertEqual(self.driver.find_element(By.XPATH, "/html/body/div[1]").get_attribute("class"), "modal fade")
