"""test_login
abrir login
login correcto
assert URL contiene /inventory.html"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_valid(driver):
    #Abrir SauceDemo
    driver.get("https://www.saucedemo.com")
    
    #Login con usuario válido
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    #Click en boton de login
    driver.find_element(By.ID, "login-button").click()

    #wait para que la página cargue y validar URL
    WebDriverWait(driver, 5).until(
    EC.url_contains("/inventory.html")
    )

    #Validar URL contiene /inventory.html
    assert "/inventory.html" in driver.current_url, "URL no contiene /inventory.html"



