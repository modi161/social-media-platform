import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestDeletepost():
    def setup_method(self, method):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument('--disable-gpu')
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        options.add_argument('--disable-extensions')
        self.driver = webdriver.Chrome(options=options)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_deletepost(self):
        self.driver.get("https://reunion.azurewebsites.net/")
        self.driver.set_window_size(1524, 822)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "email_login"))).click()
        self.driver.find_element(By.ID, "email_login").send_keys("testuser123@gmail.com")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "password_login"))).click()
        self.driver.find_element(By.ID, "password_login").send_keys("123")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "log"))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".menu-item:nth-child(3) > h3"))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".feed:nth-child(1) h3"))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".feed:nth-child(1) > .head"))).click()
        self.vars["posttimestamp"] = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".feed:nth-child(1) small"))).text
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".feed:nth-child(1) .delete-post path"))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "confirm-delete"))).click()
        
        # Wait and refresh to ensure deletion using XPath to check for element invisibility
        xpath_expression = f"//*[contains(@class, 'feed')][1]//small[contains(text(), '{self.vars["posttimestamp"]}')]"

        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH, xpath_expression)))

        # Refresh and check that the timestamp is no longer present
        self.driver.refresh()
        posts = self.driver.find_elements(By.CSS_SELECTOR, ".feed .info small")
        timestamps = [post.text for post in posts]
        assert self.vars["posttimestamp"] not in timestamps, "Timestamp still present on the page after deletion."
