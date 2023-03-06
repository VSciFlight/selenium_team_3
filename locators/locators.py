import utils as u

class Locator:
    loc = dict()

    # Header
    loc['Head_Home'] = (u.By.XPATH, '//a[text()="Home "]')
    loc['Head_Contact'] = (u.By.XPATH, '//a[text()="Contact"]')
    loc['Head_About_Us'] = (u.By.XPATH, '//a[text()="About us"]')
    loc['Head_Cart'] = (u.By.XPATH, '//a[text()="Cart"]')
    loc['Head_Login'] = (u.By.XPATH, '//a[text()="Log in"]')
    loc['Head_Logout'] = (u.By.XPATH, '//a[text()="Log out"]')
    loc['Head_Signup'] = (u.By.XPATH, '//a[text()="Sign up"]')


    # Home
    # Categories
    loc['Home_Phones'] = (u.By.XPATH, '//a[text()="Phones"]')
    loc['Home_Laptops'] = (u.By.XPATH, '//a[text()="Laptops"]')
    loc['Home_Monitors'] = (u.By.XPATH, '//a[text()="Monitors"]')


    # Home
    # Items

    loc['Items_Collection'] = (u.By.CSS_SELECTOR, '#tbodyid > div')
