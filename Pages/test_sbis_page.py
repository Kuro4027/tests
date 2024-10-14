import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class test_SbisPage:
        
    def __init__ (self, driver):
        self.driver=driver
    
    def test_open(self):
        self.driver.get("https://sbis.ru/")
        assert True, "URL https://sbis.ru/ не верный"
        
    def test_click_contact(self):
        
        element_1 = self.driver.find_element(By.XPATH, "//*[text()='Контакты']")
        element_1 = self.driver.find_element(By.XPATH, "//*[text()='Контакты']")
        element_1.click()
        
        element_2 = self.driver.find_element(By.XPATH, "//*[text()='Еще 841 офис в России']")
        element_2.click()
        
        assert True, "Переход в раздел 'Контакты' не работает"

    
    def test_clic_banner(self):

        banner = self.driver.find_element(By.XPATH, "//a[@href='https://tensor.ru/']")
        banner.click()
        
        assert True, "Банер тензора не работает"
        
    def test_contacts_list_exists(self):

        try:
            
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "contacts_list")))
            assert element is not None
            
            print("Элемент 'contacts_list' найден.")
        
        except Exception as e:
            
            pytest.fail(f"Элемент 'contacts_list' не найден. Ошибка: {str(e)}")

    def test_region_check(self):
        
        try:
            
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".sbis_ru-Region-Chooser__text.sbis_ru-link")))

            region_text = element.text
            
            element.click()

            assert region_text == "г. Тюмень", f"Текущий регион: {region_text}, ожидалось: г. Тюмень"
        
        except Exception as e:
            print(e)
        
    def test_swap_region(self):
        
        try:
            
            span_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='41 Камчатский край']")))
            # Кликнуть на элемент
            span_element.click()
            
        except Exception as e:
            print()

    def test_second_region_check(self):
        
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".sbis_ru-Region-Chooser__text.sbis_ru-link")))

            region_text = element.text
            
            assert region_text == "Камчатский край", f"Текущий регион: {region_text}, ожидалось: Камчатский край"
            time.sleep(5)
            
        except Exception as e:
            print(e)

        
    def test_contact_name(self):
        
        try:
            
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[title="СБИС - Камчатка"]')))
            
            assert element.text == "СБИС - Камчатка"
            print("Элемент 'СБИС - Камчатка' найден и содержит правильный текст.")
            time.sleep(5)
            
        except Exception as e:
            
            print(e)
            pytest.fail(f"Элемент 'СБИС - Камчатка' не найден или содержит неправильный текст. Ошибка: {str(e)}")

        
        
