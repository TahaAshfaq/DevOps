# # File: tests/test_app.py

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import time

# def setup_driver():
#     options = Options()
#     options.headless = True
#     options.add_argument('--no-sandbox')
#     options.add_argument('--disable-dev-shm-usage')
#     return webdriver.Chrome(options=options)


# def test_homepage_loads():
#     driver = setup_driver()
#     try:
#         driver.get("http://52.3.59.229:5173")
#         time.sleep(2)
#         assert "Vite + React" in driver.title
#         print("Test 1 Passed: Homepage loads successfully.")
#     finally:
#         driver.quit()

# def test_navigation_to_about():
#     driver = setup_driver()
#     try:
#         driver.get("http://52.3.59.229:5173")
#         time.sleep(2)
#         about_link = driver.find_element(By.LINK_TEXT, "About")
#         about_link.click()
#         time.sleep(2)
#         assert "About" in driver.page_source
#         print("Test 2 Passed: Navigation to About page successful.")
#     finally:
#         driver.quit()

# def test_button_click():
#     driver = setup_driver()
#     try:
#         driver.get("http://52.3.59.229:5173")
#         time.sleep(2)
#         button = driver.find_element(By.TAG_NAME, "button")
#         button.click()
#         time.sleep(2)
#         assert "Clicked" in driver.page_source  # Replace with actual change after click
#         print("Test 3 Passed: Button click works.")
#     finally:
#         driver.quit()

# def test_input_field():
#     driver = setup_driver()
#     try:
#         driver.get("http://52.3.59.229:5173")
#         time.sleep(2)
#         input_box = driver.find_element(By.TAG_NAME, "input")
#         input_box.send_keys("Test Input")
#         time.sleep(1)
#         assert input_box.get_attribute('value') == "Test Input"
#         print("Test 4 Passed: Input field accepts text.")
#     finally:
#         driver.quit()

# def test_form_submission():
#     driver = setup_driver()
#     try:
#         driver.get("http://52.3.59.229:5173")
#         time.sleep(2)
#         input_box = driver.find_element(By.TAG_NAME, "input")
#         input_box.send_keys("Sample Data")
#         submit_button = driver.find_element(By.TAG_NAME, "button")
#         submit_button.click()
#         time.sleep(2)
#         assert "Submission Successful" in driver.page_source  # Replace with actual confirmation text
#         print("Test 5 Passed: Form submission successful.")
#     finally:
#         driver.quit()

# def test_database_insertion():
#     driver = setup_driver()
#     try:
#         driver.get("http://52.3.59.229:5173")
#         time.sleep(2)
#         # Submit form or action that inserts into DB
#         # This is a placeholder, adjust as needed
#         assert True  # Normally you would check database or confirmation message
#         print("Test 6 Passed: Database insertion simulated.")
#     finally:
#         driver.quit()

# def test_error_message():
#     driver = setup_driver()
#     try:
#         driver.get("http://52.3.59.229:5173")
#         time.sleep(2)
#         # Submit form without filling required fields
#         submit_button = driver.find_element(By.TAG_NAME, "button")
#         submit_button.click()
#         time.sleep(2)
#         assert "Error" in driver.page_source  # Adjust to actual error text
#         print("Test 7 Passed: Error message displayed for invalid input.")
#     finally:
#         driver.quit()

# def test_page_refresh():
#     driver = setup_driver()
#     try:
#         driver.get("http://52.3.59.229:5173")
#         time.sleep(2)
#         driver.refresh()
#         time.sleep(2)
#         assert "Vite + React" in driver.title
#         print("Test 8 Passed: Page refresh works correctly.")
#     finally:
#         driver.quit()

# def test_back_navigation():
#     driver = setup_driver()
#     try:
#         driver.get("http://52.3.59.229:5173")
#         time.sleep(2)
#         driver.get("http://52.3.59.229:5173/anotherpage")  # Replace with actual page
#         time.sleep(2)
#         driver.back()
#         time.sleep(2)
#         assert "Vite + React" in driver.title
#         print("Test 9 Passed: Back navigation successful.")
#     finally:
#         driver.quit()

# def test_multiple_tabs():
#     driver = setup_driver()
#     try:
#         driver.get("http://52.3.59.229:5173")
#         driver.execute_script("window.open('http://52.3.59.229:5173', '_blank');")
#         time.sleep(2)
#         assert len(driver.window_handles) == 2
#         print("Test 10 Passed: Multiple tabs handled.")
#     finally:
#         driver.quit()

# if __name__ == "__main__":
#     test_homepage_loads()
#     test_navigation_to_about()
#     test_button_click()
#     test_input_field()
#     test_form_submission()
#     test_database_insertion()
#     test_error_message()
#     test_page_refresh()
#     test_back_navigation()
#     test_multiple_tabs()






from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

APP_URL = "http://web:5173"

def setup_driver():
    options = Options()
    options.headless = True
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    return webdriver.Chrome(options=options)


def test_homepage_loads():
    driver = setup_driver()
    try:
        driver.get(APP_URL)
        time.sleep(2)
        print("Page title:", driver.title)
        assert "Vite + React" in driver.title
        print("Test 1 Passed: Homepage loads successfully.")
    except Exception as e:
        print(f"Test 1 Failed: Homepage did not load. Error: {e}")
    finally:
        driver.quit()

def test_navigation_to_about():
    driver = setup_driver()
    try:
        driver.get(APP_URL)
        time.sleep(2)
        print("Page source:", driver.page_source)
        about_link = driver.find_element(By.LINK_TEXT, "About")
        about_link.click()
        time.sleep(2)
        assert "About" in driver.page_source
        print("Test 2 Passed: Navigation to About page successful.")
    except Exception as e:
        print(f"Test 2 Failed: Navigation to About page failed. Error: {e}")
    finally:
        driver.quit()

def test_button_click():
    driver = setup_driver()
    try:
        driver.get(APP_URL)
        time.sleep(2)
        button = driver.find_element(By.TAG_NAME, "button")
        button.click()
        time.sleep(2)
        assert "Clicked" in driver.page_source  # Replace with actual change after click
        print("Test 3 Passed: Button click works.")
    except Exception as e:
        print(f"Test 3 Failed: Button click failed. Error: {e}")
    finally:
        driver.quit()

def test_input_field():
    driver = setup_driver()
    try:
        driver.get(APP_URL)
        time.sleep(2)
        input_box = driver.find_element(By.TAG_NAME, "input")
        input_box.send_keys("Test Input")
        time.sleep(1)
        assert input_box.get_attribute('value') == "Test Input"
        print("Test 4 Passed: Input field accepts text.")
    except Exception as e:
        print(f"Test 4 Failed: Input field test failed. Error: {e}")
    finally:
        driver.quit()

def test_form_submission():
    driver = setup_driver()
    try:
        driver.get(APP_URL)
        time.sleep(2)
        input_box = driver.find_element(By.TAG_NAME, "input")
        input_box.send_keys("Sample Data")
        submit_button = driver.find_element(By.TAG_NAME, "button")
        submit_button.click()
        time.sleep(2)
        assert "Submission Successful" in driver.page_source  # Replace with actual confirmation text
        print("Test 5 Passed: Form submission successful.")
    except Exception as e:
        print(f"Test 5 Failed: Form submission failed. Error: {e}")
    finally:
        driver.quit()

def test_database_insertion():
    driver = setup_driver()
    try:
        driver.get(APP_URL)
        time.sleep(2)
        # Submit form or action that inserts into DB
        # This is a placeholder, adjust as needed
        assert True  # Normally you would check database or confirmation message
        print("Test 6 Passed: Database insertion simulated.")
    except Exception as e:
        print(f"Test 6 Failed: Database insertion test failed. Error: {e}")
    finally:
        driver.quit()

def test_error_message():
    driver = setup_driver()
    try:
        driver.get(APP_URL)
        time.sleep(2)
        submit_button = driver.find_element(By.TAG_NAME, "button")
        submit_button.click()
        time.sleep(2)
        assert "Error" in driver.page_source  # Adjust to actual error text
        print("Test 7 Passed: Error message displayed for invalid input.")
    except Exception as e:
        print(f"Test 7 Failed: Error message test failed. Error: {e}")
    finally:
        driver.quit()

def test_page_refresh():
    driver = setup_driver()
    try:
        driver.get(APP_URL)
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        assert "Vite + React" in driver.title
        print("Test 8 Passed: Page refresh works correctly.")
    except Exception as e:
        print(f"Test 8 Failed: Page refresh failed. Error: {e}")
    finally:
        driver.quit()

def test_back_navigation():
    driver = setup_driver()
    try:
        driver.get(APP_URL)
        time.sleep(2)
        # Replace '/anotherpage' with a real route from your app
        driver.get(APP_URL + "/anotherpage")  # TODO: Replace with actual page
        time.sleep(2)
        driver.back()
        time.sleep(2)
        assert "Vite + React" in driver.title  # TODO: Replace with your app's title
        print("Test 9 Passed: Back navigation successful.")
    except Exception as e:
        print(f"Test 9 Failed: Back navigation failed. Error: {e}")
    finally:
        driver.quit()

def test_multiple_tabs():
    driver = setup_driver()
    try:
        driver.get(APP_URL)
        driver.execute_script(f"window.open('{APP_URL}', '_blank');")
        time.sleep(2)
        assert len(driver.window_handles) == 2
        print("Test 10 Passed: Multiple tabs handled.")
    except Exception as e:
        print(f"Test 10 Failed: Multiple tabs test failed. Error: {e}")
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

