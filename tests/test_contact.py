import unittest
import utils as u
from pages.home import HomePage
from pages.contact import ContactModal

class TestContactModal(unittest.TestCase):
    def setUp(self):
        try:
            options = u.WebDriver.ChromeOptions()
            options.add_argument("--disable-extensions")
            self.driver = u.WebDriver.Chrome(options=options)
            self.driver.maximize_window()
            self.driver.get("https://www.demoblaze.com/index.html")
            hp = HomePage
            hp.click_contact_btn(self)


        except AssertionError:
            self.driver.quit()

    def tearDown(self):
        self.driver.quit()


    def test_valid_message_send(self):
        """
        test that verify user can send a message with valid data
        :return:
        """
        cm = ContactModal
        cm.set_contact_email(self, "Jhon237@gmail.com")
        cm.set_contact_name(self, "Jhon")
        cm.set_message(self, "Hello everyone! \nYou have to many bugs")
        cm.click_send_message_btn(self)
        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert
        self.assertEqual(alert.text, "Thanks for the message!!")
        alert.accept()

    def test_invalid_email_message_send(self):
        """
        test that verify user can't send a message with invalid data
        when he puts some invalid email to the email field
        :return:
        """
        cm = ContactModal
        cm.set_contact_email(self, "b!fg")
        cm.set_contact_name(self, "Jhon")
        cm.set_message(self, "Hello everyone! \nYou have to many bugs")
        cm.click_send_message_btn(self)
        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert
        self.assertNotEqual(alert.text, "Thanks for the message!!", msg="The message should not be sent")
        alert.accept()

    def test_invalid_name_message_send(self):
        """
        test that verify user can't send a message with invalid data
        when he puts some invalid email to the email field
        :return:
        """
        cm = ContactModal
        cm.set_contact_email(self, "Jhon237@gmail.com")
        cm.set_contact_name(self, 24324)
        cm.set_message(self, "Hello everyone! \nYou have to many bugs")
        cm.click_send_message_btn(self)
        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert
        self.assertNotEqual(alert.text, "Thanks for the message!!", msg="The message should not be sent")
        alert.accept()

    def test_invalid_message_without_char(self):
        """
        test that verify user can't send a message with invalid data
        when he inserts into fields nothing
        :return:
        """
        cm = ContactModal
        cm.click_send_message_btn(self)
        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert
        self.assertNotEqual(alert.text, "Thanks for the message!!", msg="The message should not be sent")
        alert.accept()

    def test_name_length_more_than_10_char(self):
        """
        test that verify user can't send a message with invalid data
        when he inserts into name field a name that greater than 10 characters
        :return:
        """
        cm = ContactModal
        cm.set_contact_email(self, "Jhon237@gmail.com")
        cm.set_contact_name(self, "asd"*4)
        cm.set_message(self, "Hello everyone! \nYou have to many bugs")
        cm.click_send_message_btn(self)
        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert
        self.assertNotEqual(alert.text, "Thanks for the message!!", msg="The message should not be sent")
        alert.accept()

    def test_message_length_more_than_256_char(self):
        """
        test that verify user can't send a message with invalid data
        when he inserts into message field a message that greater than 256 characters
        :return:
        """
        cm = ContactModal
        cm.set_contact_email(self, "Jhon237@gmail.com")
        cm.set_contact_name(self, "Jhon")
        cm.set_message(self, "Hello everyone!" * 257)
        cm.click_send_message_btn(self)
        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert
        self.assertEqual(alert.text, "Thanks for the message!!", msg="The message should not be sent")
        alert.accept()

    def test_X_btn(self):
        """
        test that verify if user can close the Contact modal
        :return:
        """
        cm = ContactModal
        cm.click_X_btn(self)
        self.assertEqual(self.driver.find_element(u.By.XPATH, "/html/body/div[1]").get_attribute("class"), "modal fade")

    def test_close_btn(self):
        """
        test that verify if user can close the Contact modal
        :return:
        """
        cm = ContactModal
        cm.click_close_btn(self)
        self.assertEqual(self.driver.find_element(u.By.XPATH, "/html/body/div[1]").get_attribute("class"), "modal fade")

    def test_send_message_btn(self):
        """
        test that verify if user can send a message
        :return:
        """
        cm = ContactModal
        cm.set_contact_email(self, "Jhon237@gmail.com")
        cm.set_contact_name(self, "Jhon")
        cm.set_message(self, "Hello everyone! \nYou have to many bugs")
        cm.click_send_message_btn(self)
        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert
        self.assertEqual(alert.text, "Thanks for the message!!")
        alert.accept()
