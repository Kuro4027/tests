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
    sbis_page.test_clic_banner()
    
    original_window = driver_instance.current_window_handle
    new_window = [window for window in driver_instance.window_handles if window != original_window][0]

    # Переключаемся на новое окно
    driver_instance.switch_to.window(new_window)
    
    tensor_page = test_TensorPage(driver_instance)
    
    Utility.wait_until_page_loaded(driver_instance)
    tensor_page.test_HumanPower()
    tensor_page.test_Continue_button()    
    
    Utility.wait_until_page_loaded(driver_instance)
    tensor_page.test_URL_test()    
    
    tensor_page.test_Image_check()    
    
except Exception as ex:
    print('Miss')

    
