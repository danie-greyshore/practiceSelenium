import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class InputFormsCheck(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_single_input_field(self):
        page_url = 'https://demoqa.com/text-box'
        driver = self.driver
        driver.get(page_url)

        full_name_form_element = driver.find_element(By.ID, "userName")
        full_name_form_element.clear()
        full_name_form_element.send_keys("Test Python")

        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        name_display_element = driver.find_element(By.ID, "output")
        assert "Test Python" in name_display_element.text

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
