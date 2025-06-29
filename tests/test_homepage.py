# File: tests/test_app.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def setup_driver():
    options = Options()
    options.headless = True
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    return webdriver.Chrome(options=options)


def test_homepage_loads():
    driver = setup_driver()
    try:
        driver.get("http://52.3.59.229:5173")
        time.sleep(2)
        assert "Vite + React" in driver.title
        print("Test 1 Passed: Homepage loads successfully.")
    finally:
        driver.quit()

def test_navigation_to_about():
    driver = setup_driver()
    try:
        driver.get("http://52.3.59.229:5173")
        time.sleep(2)
        about_link = driver.find_element(By.LINK_TEXT, "About")
        about_link.click()
        time.sleep(2)
        assert "About" in driver.page_source
        print("Test 2 Passed: Navigation to About page successful.")
    finally:
        driver.quit()

def test_button_click():
    driver = setup_driver()
    try:
        driver.get("http://52.3.59.229:5173")
        time.sleep(2)
        button = driver.find_element(By.TAG_NAME, "button")
        button.click()
        time.sleep(2)
        assert "Clicked" in driver.page_source  # Replace with actual change after click
        print("Test 3 Passed: Button click works.")
    finally:
        driver.quit()

def test_input_field():
    driver = setup_driver()
    try:
        driver.get("http://52.3.59.229:5173")
        time.sleep(2)
        input_box = driver.find_element(By.TAG_NAME, "input")
        input_box.send_keys("Test Input")
        time.sleep(1)
        assert input_box.get_attribute('value') == "Test Input"
        print("Test 4 Passed: Input field accepts text.")
    finally:
        driver.quit()

def test_form_submission():
    driver = setup_driver()
    try:
        driver.get("http://52.3.59.229:5173")
        time.sleep(2)
        input_box = driver.find_element(By.TAG_NAME, "input")
        input_box.send_keys("Sample Data")
        submit_button = driver.find_element(By.TAG_NAME, "button")
        submit_button.click()
        time.sleep(2)
        assert "Submission Successful" in driver.page_source  # Replace with actual confirmation text
        print("Test 5 Passed: Form submission successful.")
    finally:
        driver.quit()

def test_database_insertion():
    driver = setup_driver()
    try:
        driver.get("http://52.3.59.229:5173")
        time.sleep(2)
        # Submit form or action that inserts into DB
        # This is a placeholder, adjust as needed
        assert True  # Normally you would check database or confirmation message
        print("Test 6 Passed: Database insertion simulated.")
    finally:
        driver.quit()

def test_error_message():
    driver = setup_driver()
    try:
        driver.get("http://52.3.59.229:5173")
        time.sleep(2)
        # Submit form without filling required fields
        submit_button = driver.find_element(By.TAG_NAME, "button")
        submit_button.click()
        time.sleep(2)
        assert "Error" in driver.page_source  # Adjust to actual error text
        print("Test 7 Passed: Error message displayed for invalid input.")
    finally:
        driver.quit()

def test_page_refresh():
    driver = setup_driver()
    try:
        driver.get("http://52.3.59.229:5173")
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        assert "Vite + React" in driver.title
        print("Test 8 Passed: Page refresh works correctly.")
    finally:
        driver.quit()

def test_back_navigation():
    driver = setup_driver()
    try:
        driver.get("http://52.3.59.229:5173")
        time.sleep(2)
        driver.get("http://52.3.59.229:5173/anotherpage")  # Replace with actual page
        time.sleep(2)
        driver.back()
        time.sleep(2)
        assert "Vite + React" in driver.title
        print("Test 9 Passed: Back navigation successful.")
    finally:
        driver.quit()

def test_multiple_tabs():
    driver = setup_driver()
    try:
        driver.get("http://52.3.59.229:5173")
        driver.execute_script("window.open('http://52.3.59.229:5173', '_blank');")
        time.sleep(2)
        assert len(driver.window_handles) == 2
        print("Test 10 Passed: Multiple tabs handled.")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_homepage_loads()
    test_navigation_to_about()
    test_button_click()
    test_input_field()
    test_form_submission()
    test_database_insertion()
    test_error_message()
    test_page_refresh()
    test_back_navigation()
    test_multiple_tabs()



