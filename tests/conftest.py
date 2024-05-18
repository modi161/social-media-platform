from selenium import webdriver

import pytest

@pytest.fixture
def browser(scope="module"):
    # intializing the chrome driver
    chrom_driver = webdriver.Chrome()
    
    #make the driver wait untill response
    chrom_driver.implicitly_wait(10)
    
    #return the webdriver
    yield chrom_driver
    
    #quit from the webdriver
    chrom_driver.quit()