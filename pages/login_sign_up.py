import string
import random

import utils as u
from time import sleep


def sign_up(driver):

    u.WDW(driver, 5).until(u.EC.visibility_of_element_located(u.loca.Locator.locHome['Head_Signup']))
    driver.find_element(u.By.XPATH, '//a[text()="Sign up"]').click()

    u.WDW(driver, 5).until(u.EC.visibility_of_element_located(u.loca.Locator.locLog['Signup_Username']))
    signup_username_field = driver.find_element(u.loca.Locator.locLog['Signup_Username'])
    signup_username_field.send_keys(rand_string(n=))

def rand_string(group = string.ascii_letters, n = 10):
    """
    this fuction is taking a group of letters and then takes a number.
    it returns a string with random chars from the group in the length of the number  we provided
    :param group:
    :param n:
    :return:
    """
    return ''.join(random.choice(group) for i in range(n))

# sign_up()
print(rand_string(n=10))