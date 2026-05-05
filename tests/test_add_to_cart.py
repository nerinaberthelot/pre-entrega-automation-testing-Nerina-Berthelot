"""test_add_to_cart
    open SauceDemo
    login with valid user
    navigate to inventory page
    add product to cart
    validate badge = 1
    go to cart page
    validate product visible"""    

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_to_cart(driver):
     #Open SauceDemo
    driver.get("https://www.saucedemo.com")
    
    #Login with valid user
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    #Click on login button
    driver.find_element(By.ID, "login-button").click()

    #wait for the page to load and validate URL
    WebDriverWait(driver, 5).until(
    EC.url_contains("/inventory.html")
    )

    #Validate URL contains /inventory.html
    assert "/inventory.html" in driver.current_url

    #Add first product to cart
    add_button = driver.find_element(By.CLASS_NAME, "btn_inventory")
    add_button.click()

    #Verify badge shows 1
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "1"

    #Go to cart page
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    WebDriverWait(driver, 5).until(
        EC.url_contains("/cart.html")
    )

    # 4. Verify that the product is in the cart
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) > 0