"""test_inventory_page
    open SauceDemo
    login with valid user
    validate URL contains /inventory.html
    validate title
    validate visible products
    validate name and price of first product"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.conftest import driver

def test_inventory_page(driver):
    #Open SauceDemo
    driver.get("https://www.saucedemo.com")

    #Login with valid user
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    #Click on login button
    driver.find_element(By.ID, "login-button").click()
    print('login OK') 

    #Wait for the page load and validate URL
    WebDriverWait(driver, 5).until(
    EC.url_contains("/inventory.html")
    )

    #Validate URL contains /inventory.html
    assert "/inventory.html" in driver.current_url

    #Validate title of inventory page
    title = driver.find_element(By.CLASS_NAME, "title").text
    assert title == "Products"
    print('Title of section OK →', title) 

    #Validate products are visible
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(products) > 0

    #Validate name and price of first product
    first_product_name = products[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    first_product_price = products[0].find_element(By.CLASS_NAME, "inventory_item_price").text
    print("Product:", first_product_name) 
    print("Price:", first_product_price)