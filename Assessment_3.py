#Log a Body Corporate request with the following issue:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome webdriver
driver = webdriver.Chrome()

# Open the website
driver.get("https://redrabbit.rebaseventures.com/qa-automation/maintenance")

# Wait for the page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "firstName")))

# Choose Body Corporate request
driver.find_element_by_xpath("//label[contains(text(),'Body Corporate')]").click()

# Fill in the maintenance request form
driver.find_element_by_id("description").send_keys("Garden and pool – Irrigation system")
description_field = driver.find_element_by_id("description")
description_field.clear()
description_field.send_keys("Garden and pool – Irrigation system is faulty")

# Fill in contact details with an invalid email address
driver.find_element_by_id("firstName").send_keys("Your First Name")
driver.find_element_by_id("lastName").send_keys("Your Last Name")
driver.find_element_by_id("email").send_keys("123")

# Submit the request
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()

# Wait for the validation message
validation_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'The email must be a valid email address')]")))

# Print the validation message text
print(validation_message.text)

# Close the browser
driver.quit()
