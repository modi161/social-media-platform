from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(browser , email , password):
    browser.get('http://127.0.0.1:5000')
    
    email_field = browser.find_element(By.ID,"email_login")
    password_field = browser.find_element(By.ID, "password_login")
   
   # Enter the username and password
    email_field.send_keys(email)
    password_field.send_keys(password)

    # Locate and click the login button
    login_button = browser.find_element(By.ID, 'log')
    login_button.click()
    
    # Wait for the homepage to load after login
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'create-post'))  # Assuming 'homepage_text' is the ID of the text you want to verify
    )
    
    