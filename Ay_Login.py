from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://mtngodc.ace.dev-rancher.tecnotree.com/dclm-web-ui/#/login")
# driver.get("https://sso2.tecnotree.com/authenticationendpoint/login.do?client_id=mAMU2p3gRsqFBDrfyMhmXnM6bqIa&commonAuthCallerPath=%2Foauth2%2Fauthorize&forceAuth=false&passiveAuth=false&redirect_uri=https%3A%2F%2Fmtngodc.ace.dev-rancher.tecnotree.com%2Fdclm-web-ui%2Fauth&response_type=code&scope=openid&state=openid&tenantDomain=carbon.super&sessionDataKey=8b00adfa-7279-47c4-9cd4-8bf73e836a95&relyingParty=mAMU2p3gRsqFBDrfyMhmXnM6bqIa&type=oidc&sp=MTNG_ODC_DCLM&isSaaSApp=false&authenticators=BasicAuthenticator%3ALOCAL")
# driver.get("http://dclm-mmp.cluster1.devtestlab2.tecnotree.com/dclm-web-ui/")
# driver.get("http://localhost:3000/dclm-web-ui/dashboard") #Localhost

# Authentication Page
search = driver.find_element_by_name("username")
search.send_keys("dclmappuser1")
password = driver.find_element_by_name("password")
password.send_keys("Tecnotree#3")
driver.find_element_by_name("submit").click()


driver.maximize_window()

# Only for Ayush, Proceed link
# proceed_click = driver.find_element_by_id("details-button").click()
# proceed = driver.find_element_by_id("proceed-link").click()

# SERVER ONLY
# continue_link = driver.find_element_by_link_text('Return to application').click()
advanced = driver.find_element_by_xpath("//button[@id='details-button']").click()
# print(advanced)
wait = WebDriverWait(driver, 50)
time.sleep(10)
driver.find_element_by_link_text('Proceed to mtngodc.ace.dev-rancher.tecnotree.com (unsafe)').click()
# proceed = driver.find_element_by_id('proceed-link').click()

# Registration Page
# Retail = driver.find_element_by_xpath(//input[@name='identificationId']")
# Retail.send_keys("987654323454345")
time.sleep(5)
# Navigate to 360 (Search Customer)
search_customer = driver.find_element_by_xpath("//input[@placeholder='Search for Customers']").send_keys("C5013877")
time.sleep(15)
# search_customer.clear()
# search_customer.click()
# search_customer.send_keys(Keys.RETURN)
wait.until(EC.element_to_be_clickable((By.XPATH,"(//a[@href])[2]"))).click()
#searched = driver.find_element_by_xpath("(//a[@href])[2]").click()
#time.sleep(15)
#pack = driver.find_element_by_xpath("(//div[@data-cy='Overviewservice'])[1]").click()
wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@data-cy='Overviewservice'])[1]"))).click()
time.sleep(25)
service = driver.find_element_by_xpath("(//div[@data-cy='moreActions'])").click()
time.sleep(10)
action = driver.find_element_by_xpath("(//span[text()='Suspension'])").click()
time.sleep(20)
desc = driver.find_element_by_name("description").send_keys("abcdefgh")
time.sleep(2)
driver.find_element_by_xpath("(//button[@type='submit'])[3]").click()

driver.quit()