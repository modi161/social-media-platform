import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestTestlogin:
    def setup_method(self, method):
        options = Options()
        options.add_argument("--headless")  # Runs Chrome in headless mode.
        options.add_argument("--no-sandbox")  # Bypass OS security model.
        options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems.
        options.add_argument('--disable-gpu')  # Applicable to windows os only.
        options.add_argument('start-maximized')  # Start maximized.
        options.add_argument('disable-infobars')
        options.add_argument('--disable-extensions')
        self.driver = webdriver.Chrome(options=options)
        self.vars = {}
  
    def teardown_method(self, method):
        self.driver.quit()
  
    def test_testlogin(self):
        self.driver.get("https://reunion.azurewebsites.net/")
        self.driver.set_window_size(1524, 822)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "email_login"))).click()
        self.driver.find_element(By.ID, "email_login").send_keys("testuser123@gmail.com")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "password_login"))).click()
        self.driver.find_element(By.ID, "password_login").send_keys("123")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "log"))).click()
        elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.ID, "create-post")))
        assert len(elements) > 0
