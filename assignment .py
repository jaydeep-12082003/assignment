import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_successful(browser):
    # Navigate to the login page
    browser.get("https://example.com/login")
    
    # Find the username and password input fields
    username_field = browser.find_element(By.NAME, "username")
    password_field = browser.find_element(By.NAME, "password")
    
    # Enter your username and password
    username_field.send_keys("your_username")
    password_field.send_keys("your_password")
    
    # Submit the login form
    login_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    
    # Add an assertion to check if the login was successful.
    # Here, we check for the presence of a success message element.
    success_message = browser.find_element(By.ID, "success-message")
    assert success_message.text == "Login Successful"
    
    # You can also add additional checks for elements on the user dashboard page
    # "Welcome, User!" message is displayed.
    welcome_message = browser.find_element(By.XPATH, "//h1[contains(text(), 'Welcome, User!')]")
    assert welcome_message.is_displayed()

# To run the test, use pytest in your terminal:
# pytest your_test_script.py