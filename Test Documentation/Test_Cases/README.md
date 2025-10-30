# Test Cases

## TC_01

- **Title:** Registration with valid credentials
- **Module:** Registration
- **Priority:** High
  
- **Steps:**
  1. Open the website (`www.example.ge`)
  2. Click on ,,Registration,, button
  3. Enter a valid email  (`sopho.@example.com`)
  4. Enter a valid first name  (`Sopho`)
  5. Enter a valid last name  (`Salamashvili`)
  6. Enter a valid password  (`Password123!`)
  7. Confirm password  (`Password123!`)
  8. Click the “Register” button

- **Expected Result:** User is registered successfully and redirected to the dashboard page



## TC_02

- **Title:** Registration Fails with Weak Password
- **Module:** Registration  
- **Priority:** High  

- **Steps:**
  1. Open the website page (`www.example.ge`)
  2. Click on "Registration" button
  3. Enter a valid email address (`sopho.@example.com`)  
  4. Enter first name and last name  (`Sopho`, `Salamashvili`)
  5. Enter a weak password (`12345`)  
  6. Confirm the same weak password  (`12345`) 
  7. Click the “Register” button

- **Expected Result:**
 - System displays an error message: “Password is too weak. Please use at least 8 characters, including uppercase, lowercase, number, and special character.” 
 - User stays on the registration page.




## TC_03

- **Title:** Verify User Can Add Product to Cart  
- **Module:** Cart / Product Page  
- **Priority:** High  
- **Preconditions:** User is logged in
  
- **Steps:**
  1. Open the website (www.example.ge)
  2. Select any category from the header (e.g. ,Women,)
  3. Select any Product (e.g. ,Skirts,)
  4. Select any item (e.g. ,BRAND, - SHORT SKIRT  Product code: 234686 Gray)
  5. Click "Add to Cart" button  
  6. Open the cart
 
- **Expected Result:** Product is added to the cart, quantity = 1, correct price displayed



## TC_04

- **Title:** Verify Price Update on Quantity Change
- **Module:** Cart  
- **Priority:** Medium  
- **Preconditions:** User is logged in 
 
- **Steps:**
  1. Open the website (www.example.ge)
  2. Select any category from the header (e.g. ,Women,)
  3. Select any Product (e.g. ,Skirts,)
  4. Select any item (e.g.  Product code: 234686 Gray)
  5. Click "Add to Cart" button  
  6. Open the cart 
  7. Change product quantity from 1 to 3  

- **Expected Result:** Total price updates correctly and immediately, when product quantity changes in the cart   

