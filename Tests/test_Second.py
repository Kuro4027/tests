import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from Pages.test_sbis_page import test_SbisPage
from Pages.test_tensor_page import test_TensorPage
from Utility.Utility import Utility

def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.close()
    driver.quit()
    
try:
    driver_instance = next(driver())
    
    sbis_page = test_SbisPage(driver_instance)
    sbis_page.test_open()
    
    Utility.wait_until_page_loaded(driver_instance)
    sbis_page.test_click_contact()
    
    Utility.wait_until_page_loaded(driver_instance)
    sbis_page.test_contacts_list_exists()
    
    
    sbis_page.test_region_check()
    Utility.wait_until_page_loaded(driver_instance)
    sbis_page.test_swap_region()
    
    
    Utility.wait_until_page_loaded(driver_instance)
    sbis_page.test_second_region_check()
    
    Utility.wait_until_page_loaded(driver_instance)
    sbis_page.test_contact_name()
    
    
    
except Exception as ex:
    print('Miss')
    
