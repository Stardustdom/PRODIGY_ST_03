from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

URL = "https://www.saucedemo.com/"
PASSWORD = "secret_sauce"
USERNAMES = {
    "standard_user": True,
    "locked_out_user": False,
    "problem_user": True,
    "performance_glitch_user": True,
    "error_user": True,
    "visual_user": True,
    "invalid_user": False
}

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(URL)
        self.driver.maximize_window()

    def test_login_users(self):
        for user, expected_success in USERNAMES.items():
            self.driver.get(URL)  # reload before each test
            self.driver.find_element(By.ID, "user-name").send_keys(user)
            self.driver.find_element(By.ID, "password").send_keys(PASSWORD)
            self.driver.find_element(By.ID, "login-button").click()
            time.sleep(1)
            if expected_success:
                self.assertIn("inventory", self.driver.current_url, f"{user} should log in successfully")
            else:
                error_present = self.driver.find_element(By.CLASS_NAME, "error-message-container").is_displayed()
                self.assertTrue(error_present, f"{user} should see an error")

    def test_empty_fields(self):
        self.driver.find_element(By.ID, "login-button").click()
        error_present = self.driver.find_element(By.CLASS_NAME, "error-message-container").is_displayed()
        self.assertTrue(error_present, "Empty fields should show an error")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
