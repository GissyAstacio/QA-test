
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Setup WebDriver
service = Service("path/to/chromedriver")
driver = webdriver.Chrome(service=service)

try:
    # Open the web application
    driver.get("http://localhost:3000")

    # Locate and interact with elements
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-btn")

    # Input credentials and log in
    username_field.send_keys("testuser")
    password_field.send_keys("password")
    login_button.click()

    # Validate login
    assert "Dashboard" in driver.title, "Login failed, dashboard not loaded"
    print("Login test passed")

finally:
    # Close the browser
    driver.quit()
