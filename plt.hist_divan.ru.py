import time
import pandas as pd
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

driver = webdriver.Firefox()

def fetch_page(driver, url):
    driver.get(url)
    time.sleep(3)  # Ожидание загрузки страницы

def parse_page(driver):
    products = []
    product_elements = driver.find_elements(By.CSS_SELECTOR, '.styles_item__FxNqc')
    for product in product_elements:
        try:
            title = product.find_element(By.CSS_SELECTOR, '.productName').text
            price = product.find_element(By.CSS_SELECTOR, '.price').text
            price = int(price.replace(' ', '').replace('₽', ''))
            products.append({'title': title, 'price': price})
        except Exception as e:
            print(f'Error parsing product: {e}')
    return products


base_url = 'https://www.divan.ru/category/divany-i-kresla'
all_products = []

for page in range(1, 4):
    url = base_url + str(page)
    fetch_page(driver, url)
    products = parse_page(driver)
    all_products.extend(products)

driver.quit()

df = pd.DataFrame(all_products)
df.to_csv('divan_prices.csv', index=False)
