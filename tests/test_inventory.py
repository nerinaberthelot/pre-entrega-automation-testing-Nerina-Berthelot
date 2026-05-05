"""Test 2: Inventory
validar título
validar productos visibles
extraer nombre + precio primer item"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.conftest import driver

def test_inventory_page(driver):
    #Abrir SauceDemo
    driver.get("https://www.saucedemo.com")

    #Login con usuario válido
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    #Click en boton de login
    driver.find_element(By.ID, "login-button").click()

    #wait para que la página cargue 
    WebDriverWait(driver, 5).until(
    EC.url_contains("/inventory.html")
    )

    #Validar url contiene /inventory.html
    assert "/inventory.html" in driver.current_url

    #Validar título
    title = driver.find_element(By.CLASS_NAME, "title").text
    assert title == "Products" 

    #Validar que existan productos
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(products) > 0

    #Validar nombre y precio del primer producto
    first_product_name = products[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    first_product_price = products[0].find_element(By.CLASS_NAME, "inventory_item_price").text