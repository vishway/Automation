from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

#from PIL import Image
#from Screenshot import Screenshot_Clipping
# import xlrd

# workbook = xlrd.open_workbook("Customer.xls")
# sheet = workbook.sheet_by_name("sheet1")

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://mtngodc.ace.dev-rancher.tecnotree.com/dclm-web-ui/")
# driver.get("https://sso2.tecnotree.com/authenticationendpoint/login.do?client_id=mAMU2p3gRsqFBDrfyMhmXnM6bqIa&commonAuthCallerPath=%2Foauth2%2Fauthorize&forceAuth=false&passiveAuth=false&redirect_uri=https%3A%2F%2Fmtngodc.ace.dev-rancher.tecnotree.com%2Fdclm-web-ui%2Fauth&response_type=code&scope=openid&state=openid&tenantDomain=carbon.super&sessionDataKey=8b00adfa-7279-47c4-9cd4-8bf73e836a95&relyingParty=mAMU2p3gRsqFBDrfyMhmXnM6bqIa&type=oidc&sp=MTNG_ODC_DCLM&isSaaSApp=false&authenticators=BasicAuthenticator%3ALOCAL")
# driver.get("http://dclm-mmp.cluster1.devtestlab2.tecnotree.com/dclm-web-ui/")
# driver.get("http://localhost:3000/dclm-web-ui/dashboard") #Localhost

# SERVER ONLY
# continue_link = driver.find_element_by_link_text('Return to application').click()
advanced = driver.find_element_by_xpath("//button[@id='details-button']").click()
# print(advanced)
time.sleep(5)
# Proceed to mtngodc.ace.dev-rancher.tecnotree.com (unsafe)
# Proceed to dclm-mmp.cluster1.devtestlab2.tecnotree.com (unsafe)
driver.find_element_by_link_text('Proceed to mtngodc.ace.dev-rancher.tecnotree.com (unsafe)').click()
# proceed = driver.find_element_by_id('proceed-link').click()
time.sleep(10)


# Authentication Page
search = driver.find_element_by_name("username")
search.send_keys("dclmappuser1")
password = driver.find_element_by_name("password")
password.send_keys("Tecnotree#3")
driver.find_element_by_name("submit").click()
driver.maximize_window()
time.sleep(10)
wait = WebDriverWait(driver, 35)
#CompanyName
driver.find_element_by_xpath("//input[@data-cy='companyName']").send_keys("wertyuiytruiuy")
time.sleep(10)
#RegistrationNumber
driver.find_element_by_xpath("//input[@data-cy='registrationNumber']").send_keys("876545678")
time.sleep(3)
#CustomerCategory
driver.find_element_by_xpath("(//div[@aria-haspopup='listbox'])[3]").click()
time.sleep(3)
driver.find_element_by_xpath("//li[1]").click()
time.sleep(3)
#SubCategory
driver.find_element_by_xpath("(//div[@aria-haspopup='listbox'])[4]").click()
time.sleep(3)
driver.find_element_by_xpath("//li[1]").click()
time.sleep(10)
#Proceed
wait.until(EC.element_to_be_clickable((By.XPATH,"(//*[contains(@class,'containedPrimary')])[2]"))).click()

#proceed = driver.find_element_by_xpath("(//*[contains(@class,'containedPrimary')])[2]")
#driver.implicitly_wait(10)
#ActionChains(driver).move_to_element(proceed).perform()
#driver.execute_script("arguments[0].scrollIntoView();", proceed)
#print(type(proceed))
#print(proceed)
#time.sleep(7)
