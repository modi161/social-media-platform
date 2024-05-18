# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture(scope="session")
def driver():
    """Create a WebDriver with a logged-in session that can be used across different tests."""
    driver = webdriver.Chrome()
    driver.get("https://reunion.azurewebsites.net/")
    driver.set_window_size(1524, 822)
    driver.find_element(By.ID, "email_login").click()
    driver.find_element(By.ID, "email_login").send_keys("super@gmail.com")
    driver.find_element(By.ID, "password_login").click()
    driver.find_element(By.ID, "password_login").send_keys("123")
    driver.find_element(By.ID, "log").click()
    yield driver
    driver.quit()
