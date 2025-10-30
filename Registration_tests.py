from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1️⃣ Open website
driver = webdriver.Chrome()
driver.get("https://invu.ge")
wait = WebDriverWait(driver, 10)
print("Opened website https://invu.ge")
time.sleep(2)

# 2️⃣ Click on “Sign In”
sign_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='secondary-button']")))
sign_in_button.click()
print("Clicked 'Sign In'")
time.sleep(2)

# 3️⃣ Click on "Sign Up Here"
sign_up_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Sign up here']")))
sign_up_link.click()
print("Clicked 'Sign Up Here'")
time.sleep(2)

# 4️⃣ Enter valid name "Sopho"
name_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='firstName']")))
name_field.send_keys("Sopho")
print("Entered Name: Sopho")
time.sleep(1)

# 5️⃣ Enter valid surname "Salamashvili"
surname_field = driver.find_element(By.XPATH, "//input[@id='lastName']")
surname_field.send_keys("Salamashvili")
print("Entered Surname: Salamashvili")
time.sleep(1)

# 6️⃣ Enter valid email "sophosalamashvili2@gmail.com"
email_field = driver.find_element(By.XPATH, "//input[@id='email']")
email_field.send_keys("sophosalamashvili2@gmail.com")
print("Entered Email: sophosalamashvili2@gmail.com")
time.sleep(1)

# 7️⃣ Enter valid password "Sopo12@"
password_field = driver.find_element(By.XPATH, "//input[@id='password']")
password_field.send_keys("Sopo12@")
print("Entered Password")
time.sleep(1)

# 8️⃣ Confirm password "Sopo12@"
confirm_password_field = driver.find_element(By.XPATH, "//input[@id='confirmPassword']")
confirm_password_field.send_keys("Sopo12@")
print("Confirmed Password")
time.sleep(1)

# 9️⃣ Click “Register” button
final_register_button = driver.find_element(By.XPATH, "//button[normalize-space()='Create Account']")
final_register_button.click()
print("Clicked 'Register' button")
time.sleep(3)

print("✅ Registration test completed successfully")
driver.quit()