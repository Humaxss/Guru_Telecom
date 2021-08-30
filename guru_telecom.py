from selenium import webdriver
from selenium.webdriver.common.by import By
import time



driver = webdriver.Chrome(executable_path="C:\Python\chromedriver.exe")
driver.maximize_window()
driver.get("http://demo.guru99.com/telecom/index.html")
driver.implicitly_wait(10)

#-----ADD_Customer-----#

#title
title = driver.find_element(By.XPATH, "//a[normalize-space()='Guru99 telecom']").text
print("Meno stránky : " + title)

#Add_customer
driver.find_element(By.LINK_TEXT, "Add Customer").click()
time.sleep(0.5)
#Background_check
driver.find_element(By.XPATH, "//label[.='Pending']").click()
time.sleep(0.5)
driver.find_element(By.XPATH, "//label[.='Done']").click()
#Billing_adress
first_name = driver.find_element(By.XPATH, "//input[@name='fname']").send_keys("Erik")
time.sleep(0.5)
last_name = driver.find_element(By.XPATH, "//input[@id='lname']").send_keys("Masiar")

#Email
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("masiar.erik147@gmail.com")
time.sleep(0.5)

#Desc.
driver.find_element(By.XPATH, "//textarea[@id='message']").send_keys("Skuska 123")
time.sleep(0.5)
#Phone_number
driver.find_element(By.XPATH, "//input[@id='telephoneno']").send_keys("090819942711111")
time.sleep(0.5)
#Submit
driver.find_element(By.XPATH, "//input[@value='Submit']").click()
time.sleep(1)

#Details
Details = driver.find_element(By.XPATH, "//td[position()=2]").text
print("Customer ID : " + Details)
time.sleep(1)

#Home_buttn
driver.find_element(By.XPATH, "//a[@class='button']").click()
time.sleep(1)

#----------Add_Tariff_Plan----------#

#Add_tarif
driver.find_element(By.LINK_TEXT, "Add Tariff Plan").click()
time.sleep(0.5)

#Rental
driver.find_element(By.ID, "rental1").send_keys("95000")
time.sleep(0.5)

#Local_Minutes
driver.find_element(By.NAME, "local_minutes").send_keys("10000")
time.sleep(0.5)

#Internation_Minutes
driver.find_element(By.NAME, "inter_minutes").send_keys("985")
time.sleep(0.5)

#Free_SMS_Pack
driver.find_element(By.ID, "sms_pack").send_keys("758")
time.sleep(0.5)

#Local_Per_Minutes_Charges
driver.find_element(By.ID, "minutes_charges").send_keys("689")
time.sleep(0.5)

#International_Per_Minutes_Charges
driver.find_element(By.ID, "inter_charges").send_keys("147")
time.sleep(0.5)

#SMS_Per_Charges
driver.find_element(By.XPATH, "//input[contains(@placeholder,'SMS Per Charges')]").send_keys("11")
time.sleep(0.5)

#Submit_bnt_2
driver.find_element(By.NAME, "submit").click()
time.sleep(1)

#Nadpis
nadpis = driver.find_element(By.XPATH, "//h1[.='Add Tariff Plans']").text
print(nadpis)
time.sleep(0.5)

nadpis_2 = driver.find_element(By.XPATH, "//h2[last()]").text
print(nadpis_2)
time.sleep(1)

#Home_bbtn_2
driver.find_element(By.XPATH, "//a[@class='button']").click()

#Ukončiť test
print("Test je ukončený !!!")

driver.quit()


