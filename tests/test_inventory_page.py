"""test_inventory_page
    validate title
    validate visible products
    validate name and price of first product"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.conftest import driver
from utils.helpers import login, wait_for_inventory_page

def test_inventory_page(driver):
    
    login(driver)
    wait_for_inventory_page(driver)
    
    #Validate URL contains /inventory.html
    assert "/inventory.html" in driver.current_url

    #Validate title of inventory page
    title = driver.find_element(By.CLASS_NAME, "title").text
    assert title == "Products"

    #Validate products are visible
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(products) > 0

    #Validate name and price of first product
    first_product_name = products[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    first_product_price = products[0].find_element(By.CLASS_NAME, "inventory_item_price").text
 