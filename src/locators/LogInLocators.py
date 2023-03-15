from selenium.webdriver.common.by import By

loginlocs = dict()

loginlocs['Username'] = (By.CSS_SELECTOR, "#loginusername")
loginlocs['Password'] = (By.CSS_SELECTOR, "#loginpassword")
loginlocs['X_btn'] = (By.CSS_SELECTOR, "#logInModal > div > div > div.modal-header > button > span")
loginlocs['Close_btn'] = (By.CSS_SELECTOR, "#logInModal > div > div > div.modal-header > button > span")
loginlocs['LogIn_btn'] = (By.CSS_SELECTOR, "#logInModal > div > div > div.modal-footer > button.btn.btn-primary")