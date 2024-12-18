
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Setup WebDriver
service = Service("path/to/chromedriver")
driver = webdriver.Chrome(service=service)

try:
    # Open the web application
    driver.get("http://localhost:3000")

    # Login first
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-btn")

    username_field.send_keys("testuser")
    password_field.send_keys("password")
    login_button.click()

    # Logout
    logout_button = driver.find_element(By.ID, "logout-btn")
    logout_button.click()

    # Validate redirection to login
    assert "Login" in driver.title, "Logout failed, user not redirected"
    print("Logout test passed")

finally:
    # Close the browser
    driver.quit()
