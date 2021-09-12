from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
from Screenshot import Screenshot_Clipping

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)

wait = WebDriverWait(driver, 25)
time.sleep(10)

# driver.get("https://mtngodc.ace.dev-rancher.tecnotree.com/dclm-web-ui/")
# driver.get("Proceed to mtngodc.ace.dev-rancher.tecnotree.com (unsafe)")
driver.get("http://dclm-mmp.cluster1.devtestlab2.tecnotree.com/dclm-web-ui/")
# driver.get("http://localhost:3000/dclm-web-ui/dashboard") #Localhost
time.sleep(5)

# Authentication Page
search = driver.find_element_by_name("username")
search.send_keys("dclmappuser1")
password = driver.find_element_by_name("password")
password.send_keys("Tecnotree#3")
driver.find_element_by_name("submit").click()
driver.maximize_window()
# time.sleep(15)

# SERVER ONLY
advanced = driver.find_element_by_xpath("//button[@id='details-button']").click()
time.sleep(5)
# Proceed to mtngodc.ace.dev-rancher.tecnotree.com (unsafe)
# Proceed to dclm-mmp.cluster1.devtestlab2.tecnotree.com (unsafe)
driver.find_element_by_link_text('Proceed to dclm-mmp.cluster1.devtestlab2.tecnotree.com (unsafe)').click()
time.sleep(10)


begin = time.time()

#
driver.find_element_by_xpath("//input[@name='identificationId']").send_keys("3451145687654")
driver.find_element_by_xpath("//input[@name='email']").send_keys("rty@wertyiuyiu.com")
driver.find_element_by_xpath("//input[@name='mobile']").send_keys("68322345")
given_name =driver.find_element_by_xpath("//input[@name='givenName']").send_keys("AMibka")

# submit = wait.until(EC.element_to_be_clickable((By.XPATH,"(//*[contains(@class,'containedPrimary')])[1]")))
# submit.click()

submit =driver.find_element_by_xpath("(//button[@type='button' and span[starts-with(.,'Proceed')]])[1]")
submit.click()
time.sleep(5)

driver.find_element_by_xpath("//input[@data-cy='fullNameAR']").send_keys("qwertyurtyu")

driver.find_element_by_xpath("//button[@aria-label='change date']").click()
driver.find_element_by_xpath("(//*[contains(@class,'MuiPickersDay-day-597')])[4]").click()

driver.find_element_by_xpath("//input[@value='GHANAIAN']").click()
time.sleep(3)
driver.find_element_by_xpath("//li[1]").click()

driver.find_element_by_xpath("(//div[@aria-haspopup='listbox'])[6]").click()
time.sleep(3)
driver.find_element_by_xpath("//li[1]").click()

driver.find_element_by_xpath("(//div[@aria-haspopup='listbox'])[9]").click()
time.sleep(3)
driver.find_element_by_xpath("//li[1]").click()


driver.find_element_by_xpath("(//div[@aria-haspopup='listbox'])[10]").click()
time.sleep(3)
driver.find_element_by_xpath("//li[1]").click()


#Billing preference 
driver.find_element_by_xpath("//input[@name='billingName']").send_keys("qwertyui")
driver.find_element_by_xpath("//textarea[@name='billDispatch.email']").send_keys("erty@jh.cij")

creditController = driver,find_element_by_xpath("//div[@id='mui-component-select-creditController']")
creditController.click()
driver.find_element_by_xpath("//li[1]").click()

accountManager = driver.find_element_by_xpath("//div[@id='mui-component-select-accountManager']")
accountManager.click()
driver.find_element_by_xpath("//li[1]").click()


demodet = driver.find_element_by_xpath("//div[@id='mui-component-select-demographicDetails.occupation']")
demodet.click()
driver.find_element_by_xpath("//li[1]").click()

time.sleep(3)
driver.find_element_by_xpath("(//span[starts-with(.,'Upload Later')])[1]").click()
time.sleep(3)
driver.find_element_by_xpath("(//input[@name='reason'])").send_keys("REason")
time.sleep(3)
driver.find_element_by_xpath("(//span[starts-with(.,'Save')])").click()
time.sleep(7)
driver.find_element_by_xpath("//button[@type='submit']").click()


