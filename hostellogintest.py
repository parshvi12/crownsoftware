from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Replace with actual hostel application URL
url = "https://glexas.com/hostel/login"

# Replace with your browser driver path (e.g., ChromeDriver)
driver = webdriver.Chrome()


# Open the application URL 

driver.get(url)
time.sleep(20)


# Wait for the username input field to be visible

driver.find_element((By.XPATH, "//input[@class='form-control']"))

# Enter your username
email_input.send_keys("studenttest")

# Wait for the password input field to be visible
password_input = WebDriverWait(driver, 10).until(

driver.find_element((By.XPATH, "(//input[@class='form-control'])[2]"))
)


# Enter your password
password_input.send_keys("studenttest")

# Click the submit button
 #submit_button = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.XPATH, "(//div[@class='visually-hidden']/following-sibling::div)[2]"))
submit_button.click()

time.sleep(10)

# Wait for the submit to complete
#WebDriverWait(driver, 10).until(
EC.title_contains("Hostel Application")





# Wait for the page to load (adjust timeout as needed)
#wait = WebDriverWait(driver, 10)

# Identify and fill in the application form elements (replace with actual IDs/names)
Place_field = wait.until(EC.presence_of_element_located((By.ID, "Place")))
Place_field.send_keys("Gandhinagar")

reason_field = wait.until(EC.presence_of_element_located((By.ID, "Reason")))
reason_field.send_keys("Reason")

from_date_field = wait.until(EC.presence_of_element_located((By.ID, "from_date")))
from_date_field.send_keys("2024-05-14")  # Replace with your departure date

to_date_field = wait.until(EC.presence_of_element_located((By.ID, "to_date")))
to_date_field.send_keys("2024-05-27")  # Replace with your return date


from_time_field = wait.until(EC.presence_of_element_located((By.ID, "from_time")))
from_time_field.send_keys("9:00 AM")  # Replace with your departure time


to_time_field = wait.until(EC.presence_of_element_located((By.ID, "to_time")))
to_time_field.send_keys("9:00 PM")  # Replace with your return time

# Submit the application (replace with actual submit button ID/name)
submit_button = wait.until(EC.element_to_be_clickable((By.ID, "submit_button")))
submit_button.click()

# Optional: Wait for confirmation message or perform further actions
confirmation_message = wait.until(EC.presence_of_element_located((By.ID, "confirmation_message")))
print(confirmation_message.text)

# Close the browser
driver.quit()