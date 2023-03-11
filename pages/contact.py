import utils as u
import locators

class ContactModal:

    def __init__(self, driver):
        self.driver = driver

    def set_contact_email(self, email):
        """
        set the given email in the Contact modal email field
        :param email:
        :return:
        """
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(locators.Locator.locContact['Contact_Email_fld'])).send_keys(email)
    def set_contact_name(self, name):
        """
        set the given name in the Contact modal name field
        :param name:
        :return:
        """
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(locators.Locator.locContact['Contact_Name_fld'])).send_keys(name)
    def set_message(self, message):
        """
        set the given name in the Contact modal message field
        :param message:
        :return:
        """
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(locators.Locator.locContact['Message_fld'])).send_keys(message)
    def click_X_btn(self):
        """
        performs click on X button of Contact modal
        :return:
        """
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(locators.Locator.locContact['X_btn'])).click()
    def click_close_btn(self):
        """
        performs click on Close button of Contact modal
        :return:
        """
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(locators.Locator.locContact['Close_btn'])).click()
    def click_send_message_btn(self):
        """
        performs click on Send message button of Contact modal
        :return:
        """
        u.WDW(self.driver, 5).until(u.EC.visibility_of_element_located(locators.Locator.locContact['Send_Message_btn'])).click()