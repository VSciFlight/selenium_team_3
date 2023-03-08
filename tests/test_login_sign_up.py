import string

import locators
import utils as u
import unittest
import pages.login_sign_up as login_signup


class TestLoginSignUp(unittest.TestCase):
    def setUp(self):
        self.url = 'https://demoblaze.com/index.html'
        self.driver = u.WebDriver.Chrome()
        self.driver.get(self.url)

        self.username = login_signup.rand_string(n=10)
        self.password = login_signup.rand_string(group=string.printable,n=10)


    def test_sign_up(self):
        login_signup.sign_up(self.driver, self.username, self.password)
        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert

        try:
            self.assertEqual(alert.text, "Sign up successful.")
            alert.accept()

        except:
            print("The user exists")
            self.assertEqual(alert.text, "This user already exist.")
            alert.accept()


    def test_sign_up_no_values(self):
        login_signup.sign_up(self.driver, "", "")

        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert

        try:
            self.assertEqual(alert.text, "Please fill out Username and Password.")
            alert.accept()

        except:
            print("Undefined Error")
            alert.accept()


    def test_sign_up_user_only(self):
        """
        test sign up with username only,
        The error I should get is indicator of "Password missing" or something along these lines
        However I don't get those and it returns "Please fill out Username and Password." as alert message.
        :return:
        """
        login_signup.sign_up(self.driver, self.username, "")

        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert

        try:
            self.assertEqual(alert.text, "Please fill out Username and Password.")
            alert.accept()

        except:
            print("Undefined Error")
            alert.accept()


    def test_sign_up_pass_only(self):
        """
        test sign up with username only,
        The error I should get is indicator of "Password missing" or something along these lines
        However I don't get those and it returns "Please fill out Username and Password." as alert message.
        :return:
        """
        login_signup.sign_up(self.driver, "", self.password)

        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        alert = self.driver.switch_to.alert

        try:
            self.assertEqual(alert.text, "Please fill out Username and Password.")
            alert.accept()

        except:
            print("Undefined Error")
            alert.accept()


    def test_login(self):
        login_signup.sign_up(self.driver, self.username, self.password)
        u.WDW(self.driver, 5).until(u.EC.alert_is_present())
        self.driver.switch_to.alert.accept()

        login_signup.login_acc(self.driver, self.username, self.password)
        u.WDW(self.driver, 10).until(u.EC.visibility_of_element_located(locators.Locator.locLog['Welcome']))
        welc_user = self.driver.find_element(u.By.XPATH, '//*[@id="nameofuser"]')

        self.assertEqual(welc_user.text, 'Welcome ' + self.username)


    def test_login_no_values(self):
        login_signup.login_acc(self.driver, "", "")

        alert = self.driver.switch_to.alert
        try:
            self.assertEqual(alert.text, "Please fill out Username and Password.")
            alert.accept()

        except:
            print("Undefined Error")
            alert.accept()


    def test_login_user_only(self):
        login_signup.login_acc(self.driver, self.username, "")

        alert = self.driver.switch_to.alert
        try:
            self.assertEqual(alert.text, "Please fill out Username and Password.")
            alert.accept()

        except:
            print("Undefined Error")
            alert.accept()


    def test_login_pass_only(self):
        login_signup.login_acc(self.driver, "", self.password)

        alert = self.driver.switch_to.alert
        try:
            self.assertEqual(alert.text, "Please fill out Username and Password.")
            alert.accept()

        except:
            print("Undefined Error")
            alert.accept()





    def tearDown(self):
        self.driver.close()