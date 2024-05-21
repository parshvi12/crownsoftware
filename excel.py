import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Read Excel sheet
sheet = pd.read_excel("excelsheet.xlsx")

# Initialize webdriver
driver = webdriver.Chrome()

try:
    # Navigate to the first URL
    driver.get(sheet.iloc[0][3])
    time.sleep(10)  

    # Fill in username
    driver.find_element(By.XPATH, sheet.iloc[1][3]).send_keys(sheet.iloc[1][4])
    time.sleep(2)

    # Fill in password
    driver.find_element(By.XPATH, sheet.iloc[2][3]).send_keys(sheet.iloc[2][4])
    time.sleep(2)
    # Click on login button
    driver.find_element(By.XPATH, sheet.iloc[3][3]).click()
    time.sleep(20)

    # Navigate to the leave application page
    driver.find_element(By.XPATH, sheet.iloc[4][3]).click()
    time.sleep(10)


    # Click on add button
    driver.find_element(By.XPATH, sheet.iloc[5][3]).click()
    time.sleep(2)
    
        #select leave type
    driver.find_element(By.XPATH, sheet.iloc[6][3]).send_keys(sheet.iloc[6][4])
    time.sleep(2) 
    
        #select place
    driver.find_element(By.XPATH, sheet.iloc[7][3]).send_keys(sheet.iloc[7][4])
    time.sleep(2)
    
    # Fill in reason for leave
    driver.find_element(By.XPATH, sheet.iloc[8][3]).send_keys(sheet.iloc[8][4])
    time.sleep(2)
    
    # Fill in leave start date
    driver.find_element(By.XPATH, sheet.iloc[9][3]).send_keys(sheet.iloc[9][4])
    time.sleep(2)

    # Fill in leave end date
    driver.find_element(By.XPATH, sheet.iloc[10][3]).send_keys(sheet.iloc[10][4])
    time.sleep(2)
    
    
    # Fill in leave start date
    driver.find_element(By.XPATH, sheet.iloc[11][3]).send_keys(sheet.iloc[11][4])
    time.sleep(2)

   
    # Fill in leave end time
    driver.find_element(By.XPATH, sheet.iloc[12][3]).send_keys(sheet.iloc[12][4])
    time.sleep(2)

    # Click on submit button
    driver.find_element(By.XPATH, sheet.iloc[13][3]).click()
    time.sleep(10)
    
    

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the webdriver
    driver.quit()