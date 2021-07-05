from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

class InitDriver():
    def __init__(self, browser="chrome", options=[]):
        driver_options = Options()
        for opt in options:
            driver_options.add_argument(opt)
        if browser == "chrome":
            self.driver = webdriver.Chrome(
                ChromeDriverManager().install(),
                options=driver_options
            )
        elif browser == "firefox":
            self.driver = webdriver.Firefox(
                GeckoDriverManager().install(),
                options=driver_options
            )
        return self.driver