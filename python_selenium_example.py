from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://demoqa.com/text-box')

assert "ToolsQA" in driver.title

full_name_form_element = driver.find_element(By.ID, "userName")
full_name_form_element.clear()
full_name_form_element.send_keys("Test Python")

submit_button = driver.find_element(By.ID, "submit")
submit_button.click()

name_display_element = driver.find_element(By.ID, "output")
assert "Test Python" in name_display_element.text

driver.close()