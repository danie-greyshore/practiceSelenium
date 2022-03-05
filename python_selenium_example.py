from selenium import webdriver
from selenium.webdriver.common.by import By

# this is a version of the chrome browser that we will use to test
driver = webdriver.Chrome()

# this step goes to a URL provided
driver.get('https://demoqa.com/text-box')

#this step tests the title element of the page
assert "ToolsQA" in driver.title

#get the element with this id, clear the field then enter text
full_name_form_element = driver.find_element(By.ID, "userName")
full_name_form_element.clear()
full_name_form_element.send_keys("Test Python")

#find the submit button and click
submit_button = driver.find_element(By.ID, "submit")
submit_button.click()

#find the output element and test the text
name_display_element = driver.find_element(By.ID, "output")
assert "Test Python" in name_display_element.text

driver.close()