from log_helper import logger
from selenium_helper import get_connected
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as ec
from time import sleep

logger.info("logger started")

def clean_title(str):
    return str.replace(',', '-')


def print_to_file(dict_):
    with open('results.csv', 'a') as f:
        f.write(str(dict_)+'\n')


url = "https://books.toscrape.com"

driver = get_connected(url)
sleep(5)

books = driver.find_elements(by=By.TAG_NAME, value='article')
for book in books:
    title = book.find_element(by=By.TAG_NAME, value='h3').\
        find_element(by=By.TAG_NAME, value='a').get_property('title')
    link = book.find_element(by=By.TAG_NAME, value="h3").\
        find_element(by=By.TAG_NAME, value='a').get_property('href')
    price = book.find_element(by=By.CLASS_NAME, value='price_color').text
    result = {
        'title': clean_title(title),
        'price': price[1:],
        'link': link
    }
    print_to_file(result)

driver.close()
