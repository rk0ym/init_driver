from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class InitDriver():
    def __init__(self, browser="chrome"):
        if browser == "chrome":
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        elif browser == "firefox":
            self.driver = webdriver.Firefox(GeckoDriverManager().install())
