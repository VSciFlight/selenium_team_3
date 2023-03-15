from selenium.webdriver.common.by import By

signuplocs = dict()

signuplocs['Username'] = (By.CSS_SELECTOR, "#sign-username")
signuplocs['Password'] = (By.CSS_SELECTOR, "#sign-username")
signuplocs['X_btn'] = (By.CSS_SELECTOR, "#signInModal > div > div > div.modal-header > button > span")
signuplocs['Close_btn'] = (By.CSS_SELECTOR, "#signInModal > div > div > div.modal-footer > button.btn.btn-secondary")
signuplocs['SignUp_btn'] = (By.CSS_SELECTOR, "#signInModal > div > div > div.modal-footer > button.btn.btn-primary")