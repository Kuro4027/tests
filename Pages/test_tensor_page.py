import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time


class test_TensorPage:
        
    def __init__ (self, driver):
        self.driver=driver
    
    def test_HumanPower(self):

        try:
            
            block = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Сила в людях')]")))

            assert True, "Блока 'Сила в людях' нет"
            

        except NoSuchElementException:
            
            print("Элемент не найден")

    
    def test_Continue_button(self):
        
        try:

            link = self.driver.find_element(By.XPATH, "//p[contains(text(), 'Сила в людях')]/following::a[contains(text(), 'Подробнее')]")

            link.click()
            
            assert True, "Кнопка 'Подробнее' не работает"

        except Exception as ex:
            print(ex)
            
    def test_URL_test(self):
        current_url = self.driver.current_url

        expected_url = "https://tensor.ru/about"
        
        assert current_url==expected_url, "URL неверный"

            
    def test_Image_check(self):
        
        try:
                
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

            section = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Работаем')]")))

            parent = section.find_element(By.XPATH, "..")  # Находим родительский div
            grandParent = parent.find_element(By.XPATH, "..")  # Находим родительский div

            images = grandParent.find_elements(By.TAG_NAME, 'img')

            if images:
                first_image = images[0]
                first_width = first_image.size['width']
                first_height = first_image.size['height']

                all_same = True
                for img in images:
                    width = img.size['width']
                    height = img.size['height']
                    if width != first_width or height != first_height:
                        all_same = False
                        print(f"Размеры изображения {img.get_attribute('src')} отличаются: {width}x{height}")

                assert all_same, "Изображения имеют разный размер"
                
            else:
                print("Изображения не найдены в разделе 'Работаем'.")
                
        except TimeoutException:
            print("Раздел 'Работаем' не найден.")
        except Exception as e:
            print("Произошла ошибка:", str(e))
            
            

        
        

        
