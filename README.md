# Pre-Entrega QA Automation 
# Nerina Berthelot
# SauceDemo

## Propósito del proyecto

El objetivo de este proyecto es automatizar flujos básicos de navegación en el sitio https://www.saucedemo.com utilizando Selenium WebDriver y Python.

Se desarrollan pruebas automatizadas para validar funcionalidades clave como:
-Login de usuario
-Visualización del catálogo de productos
-Interacción con el carrito de compras

## Tecnologías utilizadas

-Python
-Pytest
-Selenium WebDriver
-Git y GitHub

## Casos de prueba implementados

### Login
-Login con credenciales válidas
-Validación de redirección a `/inventory.html`

### Inventory
-Validación del título "Products"
-Verificación de presencia de productos
-Obtención de nombre y precio del primer producto

### Cart
-Agregado de producto al carrito
-Validación del contador del carrito
-Verificación del producto en el carrito

