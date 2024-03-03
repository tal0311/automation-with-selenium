from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException

class SeleniumHandler:
    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.browser = None

    def start_driver(self):
        try:
            self.browser = webdriver.Chrome(service=Service(self.driver_path))
            print("Browser started successfully.")
        except WebDriverException as e:
            print(f"Failed to start browser: {e}")

    def stop_driver(self):
        if self.browser:
            self.browser.quit()
            print("Browser stopped.")
        else:
            print("Browser is not running.")

    def navigate_to_url(self, url):
        if not self.browser:
            print("Browser is not running.")
            return
        try:
            self.browser.get(url)
            print(f"Browser navigated to URL: {url}")
        except Exception as e:
            print(f"An error occurred while navigating to URL: {e}")

    def fill_form_field(self, field_type, field_name, value):
        if not self.browser:
            print("Browser is not running.")
            return
        try:
            if field_type == "name":
                field = self.browser.find_element(By.NAME, field_name)
            elif field_type == "id":
                field = self.browser.find_element(By.ID, field_name)
            else:
                print("Invalid field type.")
                return
            field.send_keys(value)
            print(f"Filled {field_type} field '{field_name}' with value '{value}'.")
        except Exception as e:
            print(f"An error occurred while filling form field: {e}")
            
    def find_element(self, locator_type, locator_value, timeout=10):
        if not self.browser:
            print("Browser is not running.")
            return None

        try:
            wait = WebDriverWait(self.browser, timeout)
            if locator_type == 'id':
                return wait.until(EC.presence_of_element_located((By.ID, locator_value)))
            elif locator_type == 'class_name':
                return wait.until(EC.presence_of_element_located((By.CLASS_NAME, locator_value)))
            elif locator_type == 'xpath':
                return wait.until(EC.presence_of_element_located((By.XPATH, locator_value)))
            elif locator_type == 'css_selector':
                return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_value)))
            elif locator_type == 'name':
                return wait.until(EC.presence_of_element_located((By.NAME, locator_value)))
            elif locator_type == 'tag_name':
                return wait.until(EC.presence_of_element_located((By.TAG_NAME, locator_value)))
            else:
                print("Invalid locator type.")
                return None
        except Exception as e:
            print(f"An error occurred while locating the element: {e}")
            return None
    
    def scrape_page_content(self):
        if not self.browser:
            print("Browser is not running.")
            return None

        try:
            return self.find_element("tag_name","body").text
        except Exception as e:
            print(f"An error occurred while scraping page content: {e}")
            return None
    
    def collect_all_links(self, timeout=10):
        links = []
        if not self.browser:
            print("Browser is not running.")
            return None

        try:
            wait = WebDriverWait(self.browser, timeout)
            elements = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "a")))
            
            for element in elements:
                href = element.get_attribute('href')
                if href and 'http' in href:
                    links.append(href)
            print(links)
            print(f"Found {len(elements)} links.")
            return links
        except Exception as e:
            print(f"An error occurred while collecting links: {e}")
            return None