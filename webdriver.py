from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Path to your Chrome WebDriver executable
webdriver_path = "C:\\Users\\HP\\Downloads\\newdriver\\chromedriver.exe"

driver = webdriver.Chrome(executable_path = "C:\\Users\\HP\\Downloads\\newdriver\\chromedriver.exe")
# Path to the photo you want to upload
photo_path = "D:\\visuals\\a.jpeg"

# Instagram username and password
username = "Angle_bot22"
password = "Angle_bot22@2023"

# Start the Chrome browser
driver = webdriver.Chrome(webdriver_path)

# Open Instagram
driver.get("https://www.instagram.com/")

# Wait for the page to load
time.sleep(3)

# Find the username field, enter the username, and press Enter
username_field = driver.find_element_by_name("username")
username_field.send_keys(username)
username_field.send_keys(Keys.RETURN)

# Find the password field, enter the password, and press Enter
password_field = driver.find_element_by_name("password")
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)

# Wait for the page to load
time.sleep(4)

# Find the "Not Now" button for saving login info and click on it
"""not_now_button = driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
not_now_button.click()


# Wait for the page to load
time.sleep(2)

# Find the "Not Now" button for turning on notifications and click on it
not_now_button = driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
not_now_button.click()
"""
# Find the "New Post" button and click on it
new_post_button = driver.find_element_by_xpath("//div[contains(@aria-label, 'New Post')]")
new_post_button.click()

# Wait for the file input element to load
time.sleep(2)

# Find the file input element and send the path of the photo you want to upload
file_input = driver.find_element_by_xpath("//input[@type='file']")
file_input.send_keys(photo_path)

# Wait for the photo to upload
time.sleep(4)

# Find the "Next" button and click on it
next_button = driver.find_element_by_xpath("//button[contains(text(), 'Next')]")
next_button.click()

# Wait for the page to load
time.sleep(12)

# Find the "Share" button and click on it
share_button = driver.find_element_by_xpath("//button[contains(text(), 'Share')]")
share_button.click()

# Wait for the photo to be uploaded
time.sleep(40)
# Close the browser
#driver.quit(10)

