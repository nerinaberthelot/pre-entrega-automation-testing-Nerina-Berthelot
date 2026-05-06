"""Helper functions for tests"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver):
    #Login to SauceDemo with given username and password
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()


def wait_for_inventory_page(driver):
    #Wait for the inventory page to load and validate URL
    WebDriverWait(driver, 5).until(
        EC.url_contains("/inventory.html")
    )