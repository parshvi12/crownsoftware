from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the Chrome driver
driver = webdriver.Chrome()

# Navigate to the hostel application login page
driver.get("https://glexas.com/hostel/login")

time.sleep(10)
# Wait for the username input field to be visible

EC.visibility_of_element_located((By.XPATH, "//input[@class='form-control']"))


# Enter your username
email_input.send_keys("studenttest")

# Wait for the password input field to be visible
password_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//input[@class='form-control'])[2]"))
)

# Enter your password 
password_input.send_keys("studenttest")

# Click the submit button
submit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "submit-button"))
)
submit_button.click()

# Wait for the submit to complete
WebDriverWait(driver, 10).until(
    EC.title_contains("Hostel Application")
)

print("Logged in successfully!")

# You can now access the hostel application's features
#...

# Close the browser
driver.quit()