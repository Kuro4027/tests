from selenium import webdriver

class Utility:

    def wait_until_page_loaded(driver):
        while True:
            # Проверяем состояние страницы через execute_script
            page_state = driver.execute_script("return document.readyState")
            if page_state == "complete":
                break