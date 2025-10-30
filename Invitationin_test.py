from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Open the website
driver = webdriver.Chrome()
driver.get("https://invu.ge")
wait = WebDriverWait(driver, 10)
print("Opened website https://invu.ge")
time.sleep(2)

#  Click the “Login” button
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='secondary-button']")))
login_button.click()
print("Clicked 'Login' button")
time.sleep(2)

# Enter email address
email_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='email']")))
email_field.send_keys("salamashvilisopho@gmail.com")
print("Entered Email: salamashvilisopho@gmail.com")
time.sleep(1)

#  Enter password
password_field = driver.find_element(By.XPATH, "//input[@id='password']")
password_field.send_keys("Sopho12@")
print("Entered Password")
time.sleep(1)

# Click the "Sign In" button
sign_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Sign In']")))
sign_in_button.click()
print("Clicked 'Sign In' button")
time.sleep(2)

# Click “My Invitations”
my_invitations = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'ჩემი მოსაწვევები')]")))
my_invitations.click()
print("Clicked 'My Invitations'")
time.sleep(2)

#  Select “Browse Templates”
browse_templates = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'შაბლონების ნახვა')]")))
browse_templates.click()
print("Selected 'Browse Templates'")
time.sleep(2)

#  Choose the card “Simple Wedding”
simple_wedding_card = wait.until(EC.element_to_be_clickable((By.XPATH, "//h3[normalize-space()='Simple Wedding']")))
simple_wedding_card.click()
print("Chosen card 'Simple Wedding'")
time.sleep(2)

# 8️⃣ Fill the Event Title field “Ema and Noah”
event_title_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='Wedding Celebration']")))
event_title_field.send_keys("Ema and Noah")
print("Filled Event Title: Ema and Noah")
time.sleep(1)

# 9️⃣ Fill Location field “Central Park, New York”
location_field = driver.find_element(By.XPATH, "//input[@value='The Grand Ballroom']")
location_field.send_keys("Central Park, New York")
print("Filled Location: Central Park, New York")
time.sleep(1)

# 🔟 Enter the Date “22/10/2025”
date_field = driver.find_element(By.XPATH, "//input[@value='2024-06-15']")
date_field.send_keys("22/10/2025")
print("Entered Date: 22/10/2025")
time.sleep(1)

# 1️⃣1️⃣ Enter the Time “18:00”
time_field = driver.find_element(By.XPATH, "//input[@value='16:00']")
time_field.send_keys("18:00")
print("Entered Time: 18:00")
time.sleep(1)

# 1️⃣2️⃣ Click the “Create Invitation” button
create_invitation_button = driver.find_element(By.XPATH, "//button[normalize-space()='Create Invitation']")
create_invitation_button.click()
print("Clicked 'Create Invitation' button")
time.sleep(3)

print("✅ Invitation creation test completed successfully")
driver.quit()