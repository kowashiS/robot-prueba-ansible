import os
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def main():
    screenshot_path = './/results//screenshot.png'

    screenshot_dir = os.path.dirname(screenshot_path)

    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    # Configuración automática del WebDriver usando webdriver-manager
    service = Service(EdgeChromiumDriverManager().install())
    options = webdriver.EdgeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Inicializa el navegador
    driver = webdriver.Edge(service=service, options=options)
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.implicitly_wait(10)

    try:
        # Navega a una página web
        driver.get("https://www.saucedemo.com/")

        # Login
        driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        driver.find_element(By.ID, 'login-button').click()

        # Screenshot
        driver.save_screenshot('.//results//screenshot.png')

    finally:
        # Cierra el navegador
        driver.quit()

if __name__ == "__main__":
    main()
