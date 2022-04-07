from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from time import sleep
from selenium.webdriver.firefox.service import Service
url = "https://books.toscrape.com"


def get_connected(link):
    options = Options()
    options.add_argument('-headless')
    options.add_argument('-incognito')
    s = Service(GeckoDriverManager().install())
    browser = webdriver.Firefox(service=s, options=options)
    sleep(5)
    browser.get(link)
    sleep(5)

    return browser


if __name__ == "__main__":
    driver = get_connected(url)
    sleep(5)
    driver.close()
