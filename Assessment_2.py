#Log a Commercial request with the following issue:
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

# Choose Commercial request
driver.find_element_by_xpath("//label[contains(text(),'Commercial')]").click()

# Fill in the maintenance request form
driver.find_element_by_id("description").send_keys("Other – My problem is not listed")
driver.find_element_by_id("location").send_keys("Location of the problem")
driver.find_element_by_id("item").send_keys("Item having issues")

# Fill in a comment with over 200 characters
comment = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
driver.find_element_by_id("comment").send_keys(comment)

# Fill in contact details
driver.find_element_by_id("firstName").send_keys("Your First Name")
driver.find_element_by_id("lastName").send_keys("Your Last Name")
driver.find_element_by_id("email").send_keys("your@email.com")

# Submit the request
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()

# Wait for the validation message
validation_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'The description must not be greater than 200 characters')]")))

# Print the validation message text
print(validation_message.text)

# Close the browser
driver.quit()

