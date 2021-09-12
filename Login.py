from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# import xlrd

# workbook = xlrd.open_workbook("Customer.xls")
# sheet = workbook.sheet_by_name("sheet1")

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)
# driver.get("https://mtngodc.ace.dev-rancher.tecnotree.com/dclm-web-ui/#/login")
# driver.get("https://sso2.tecnotree.com/authenticationendpoint/login.do?client_id=mAMU2p3gRsqFBDrfyMhmXnM6bqIa&commonAuthCallerPath=%2Foauth2%2Fauthorize&forceAuth=false&passiveAuth=false&redirect_uri=https%3A%2F%2Fmtngodc.ace.dev-rancher.tecnotree.com%2Fdclm-web-ui%2Fauth&response_type=code&scope=openid&state=openid&tenantDomain=carbon.super&sessionDataKey=8b00adfa-7279-47c4-9cd4-8bf73e836a95&relyingParty=mAMU2p3gRsqFBDrfyMhmXnM6bqIa&type=oidc&sp=MTNG_ODC_DCLM&isSaaSApp=false&authenticators=BasicAuthenticator%3ALOCAL")
driver.get("http://dclm-mmp.cluster1.devtestlab2.tecnotree.com/dclm-web-ui/")
# driver.get("http://localhost:3000/dclm-web-ui/dashboard") #Localhost

# Authentication Page
search = driver.find_element_by_name("username")
search.send_keys("dclmappuser1")
password = driver.find_element_by_name("password")
password.send_keys("Tecnotree#3")
driver.find_element_by_name("submit").click()
driver.maximize_window()

# SERVER ONLY
# time.sleep(10)
# continue_link = driver.find_element_by_link_text('Return to application').click()
time.sleep(2)
advanced = driver.find_element_by_xpath("//button[@id='details-button']").click()
print(advanced)
time.sleep(10)
driver.find_element_by_link_text('Proceed to dclm-mmp.cluster1.devtestlab2.tecnotree.com (unsafe)').click()
# proceed = driver.find_element_by_id('proceed-link').click()
time.sleep(10)

# Registration Page
Reg_num = driver.find_element_by_xpath("//input[@name='identificationId']")
Reg_num.send_keys("987654323454345")
phone = driver.find_element_by_xpath("//input[@name='mobile']").send_keys("66543234")
email =driver.find_element_by_xpath("//input[@name='email']").send_keys("rty@ghj.com")
given_name =driver.find_element_by_xpath("//input[@name='givenName']").send_keys("AMibka")
# familyName =driver.find_element_by_xpath("//input[@name='familyName']").send_keys("AMibka")
time.sleep(5)
driver.find_element_by_xpath("(//button[@type='button' and span[starts-with(.,'Proceed')]])[1]").click()
# Navigate to 360 (Search Customer)
# search_customer = driver.find_element_by_xpath("//input[@placeholder='Search for Customers']").send_keys("C5024948")
# time.sleep(5)

#Suspension
# class Suspension ():
#     def susp(self):
#         searched = driver.find_element_by_xpath("(//a[@href])[2]").click()
#         time.sleep(15)
#         pack = driver.find_element_by_xpath("(//div[@data-cy='Overviewservice'])[1]").click()
#         time.sleep(25)
#         service = driver.find_element_by_xpath("(//div[@data-cy='moreActions'])").click()
#         time.sleep(10)
#         action = driver.find_element_by_xpath("(//span[text()='Suspension'])").click()
#         time.sleep(20)
#         desc = driver.find_element_by_name("description").send_keys("abcdefgh")
#         time.sleep(2)
#         driver.find_element_by_xpath("(//button[@type='submit'])[3]").click()
        
# suspend = Suspension()
# suspend.susp()

#Revoke Suspend
# class Revoke_Suspension ():
#     def revsusp(self):
#         searched = driver.find_element_by_xpath("(//a[@href])[2]").click()
#         time.sleep(15)
#         pack = driver.find_element_by_xpath("(//div[@data-cy='Overaccount'])").click()
#         time.sleep(25)
#         service = driver.find_element_by_xpath("(//div[@data-cy='moreActions'])").click()
#         time.sleep(10)
#         action = driver.find_element_by_xpath("(//span[text()='Revoke Suspend'])").click()
#         time.sleep(20)
#         desc = driver.find_element_by_name("description").send_keys("abcdefgh")
#         time.sleep(2)
#         driver.find_element_by_xpath("(//button[@type='submit'])[3]").click()

# revoke = Revoke_Suspension()
# revoke.revsusp() 



time.sleep(25)
driver.quit()