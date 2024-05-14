#Log-Residential request with the following issues:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize Chrome webdriver
driver = webdriver.Chrome()

# Open the website
driver.get("https://redrabbit.rebaseventures.com/qa-automation/maintenance")
driver.maximize_window()

#wait
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "firstName")))

# Fill in the maintenance request form
driver.find_element_by_id("description").send_keys("Plumbing – Blocked Drain")
driver.find_element_by_id("description").send_keys("\n")  # Press Enter
driver.find_element_by_id("description").send_keys("Structural – Window")

# Upload photos for each issue
plumbing_photo_input = driver.find_element_by_xpath("//input[@name='photo']")
plumbing_photo_input.send_keys("/path/to/plumbing_photo.jpg")

structural_photo_input = driver.find_element_by_xpath("//input[@name='photo']")
structural_photo_input.send_keys("/path/to/structural_photo.jpg")

# Fill in contact details
driver.find_element_by_id("firstName").send_keys("Your First Name")
driver.find_element_by_id("lastName").send_keys("Your Last Name")
driver.find_element_by_id("email").send_keys("your@email.com")

# Submit the request
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()

# Wait for the success message
wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Thank you for logging your request. We will respond to your request within 24hrs.')]")))

# Close the browser after a brief delay
time.sleep(2)
driver.quit()
