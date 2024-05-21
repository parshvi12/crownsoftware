from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace these with your Facebook credentials
username = "parshvipatel4@gmail.com"
password = "Parshvi@5555!"

# Start a Selenium WebDriver session
driver = webdriver.Chrome()  # You need to have Chrome WebDriver installed, or use another browser

# Navigate to Facebook login page
driver.get("https://www.facebook.com/")

# Find the username and password fields and fill them in
username_field = driver.find_element(By.ID, "email")
password_field = driver.find_element(By.ID, "pass")
login_button = driver.find_element(By.NAME, "login")

username_field.send_keys(username)
password_field.send_keys(password)

# Click on the login button
login_button.click()

# Wait for the login process to complete
WebDriverWait(driver, 10).until(EC.url_matches("https://www.facebook.com/"))

# Once logged in, you can perform further actions
# For example, you can navigate to the user's profile page
# driver.get("https://www.facebook.com/your_profile")

# Remember to close the WebDriver session when finished
driver.quit()
