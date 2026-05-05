"""test_login_valid
    open SauceDemo
    login with valid user
    validate URL contains /inventory.html"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_valid(driver):
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



