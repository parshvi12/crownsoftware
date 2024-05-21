from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome driver
driver = webdriver.Chrome()

# Navigate to facebook
driver.get("https://www.facebook.com/")

# Wait for the email input field to be visible
email_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "email"))
)

# Enter the email address
email_input.send_keys("parshvipatel4@gmail.com")

# Wait for the password input field to be visible
password_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "pass"))
)

# Enter the password
password_input.send_keys("Parshvi@5555!")

# Click the login button
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "loginbutton"))
)
login_button.click()

# Wait for the login to complete
WebDriverWait(driver, 10).until(
    EC.title_contains("Facebook")
)

print("Logged in successfully!")

# You can now access Facebook's features
#...

# Close the browser
driver.quit()