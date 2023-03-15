from selenium.webdriver.common.by import By

aboutlocs = dict()

aboutlocs['Play_btn'] = (By.CSS_SELECTOR, "#example-video > button > span.vjs-control-text")
aboutlocs['X_btn'] = (By.CSS_SELECTOR, "#videoModal > div > div > div.modal-header > button > span")
aboutlocs['Close_btn'] = (By.CSS_SELECTOR, "#videoModal > div > div > div.modal-footer > button")