from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize Chrome webdriver
driver = webdriver.Chrome()

# Open the website
driver.get("https://redrabbit.rebaseventures.com/qa-automation/maintenance")

# Wait for the page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "firstName")))

# Log first issue: Doors and lock – Garage door faulty
driver.find_element_by_id("description").send_keys("Doors and lock – Garage door faulty")
driver.find_element_by_id("add").click()

# Log second issue: Appliances – Oven Faulty
driver.find_element_by_id("description").send_keys("Appliances – Oven Faulty")
driver.find_element_by_id("add").click()

# Log third issue: Garden and yard – Tap leaking
driver.find_element_by_id("description").send_keys("Garden and yard – Tap leaking")
driver.find_element_by_id("add").click()

# Scroll to the top of the page
driver.execute_script("window.scrollTo(0, 0);")

# Click on Roof Leaking (under Structural)
driver.find_element_by_xpath("//label[contains(text(),'Structural')]/following-sibling::div//label[contains(text(),'Roof Leaking')]").click()

# Wait for the toast message
toast_message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "Toastify__toast-body")))

# Print the toast message text
print(toast_message.text)

# Close the browser after a brief delay
time.sleep(2)
driver.quit()
