import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json

driver = webdriver.Chrome()


def get_list_elements(class_name):
    driver.get("https://www.tunisianet.com.tn/702-ordinateur-portable")
    elemnets = driver.find_elements(By.CLASS_NAME, class_name)
    return elemnets


def get_products():
    titels = get_list_elements("product-title")
    reference = get_list_elements("product-reference")
    disponabilite = get_list_elements("in-stock")
    prices = get_list_elements("price")
    all_products = []
    for i in range(len(titels)):
        details = {
            "title": titels[i].text,
            "price": str(prices[i]),
            "reference": str(reference[i]),
            "disponabilite": str(disponabilite[i]),
        }
        all_products.append(details)
        print(all_products)
        json_object = json.dumps(all_products, indent=4)
    with open("products.json", "a+") as products:
        products.write(json_object)


get_products()
