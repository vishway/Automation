from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
from Screenshot import Screenshot_Clipping
# import xlrd

# workbook = xlrd.open_workbook("Customer.xls")
# sheet = workbook.sheet_by_name("sheet1")

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)
# driver.get("https://mtngodc.ace.dev-rancher.tecnotree.com/dclm-web-ui/")
# driver.get("https://sso2.tecnotree.com/authenticationendpoint/login.do?client_id=mAMU2p3gRsqFBDrfyMhmXnM6bqIa&commonAuthCallerPath=%2Foauth2%2Fauthorize&forceAuth=false&passiveAuth=false&redirect_uri=https%3A%2F%2Fmtngodc.ace.dev-rancher.tecnotree.com%2Fdclm-web-ui%2Fauth&response_type=code&scope=openid&state=openid&tenantDomain=carbon.super&sessionDataKey=8b00adfa-7279-47c4-9cd4-8bf73e836a95&relyingParty=mAMU2p3gRsqFBDrfyMhmXnM6bqIa&type=oidc&sp=MTNG_ODC_DCLM&isSaaSApp=false&authenticators=BasicAuthenticator%3ALOCAL")
driver.get("http://dclm-mmp.cluster1.devtestlab2.tecnotree.com/dclm-web-ui/")
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
# Navigate to 360 (Search Customer)
search_customer = driver.find_element_by_xpath("//input[@placeholder='Search for Customers']").send_keys("C5024948")
time.sleep(10)

wait = WebDriverWait(driver, 25)
time.sleep(10)

try:
    no_found = driver.find_element_by_xpath("//p[starts-with(.,'No Data Available')]")
    print("Customer Not found")
    time.sleep(2)
except: 
    searched = driver.find_element_by_xpath("(//a[@href])[2]").click()
    # Suspension
    class PretoPost ():
        def pre(self):
            # time.sleep(15)
            # pack = driver.find_element_by_xpath("(//div[@data-cy='Overaccount'])[1]").click()
            time.sleep(10)
            driver.find_element_by_xpath("(//div[@data-cy='moreActions'])").click()
            # wait.until(EC.element_to_be_selected((By.XPATH,"(//div[@data-cy='moreActions'])"))).click()
            print("hi")
            # more = driver.find_element_by_xpath("(//div[@data-cy='moreActions'])")
            # more.click()
            time.sleep(10)
            action = driver.find_element_by_xpath("(//span[text()='Prepaid To Postpaid'])").click()
            time.sleep(20)
            desc = driver.find_element_by_name("description").send_keys("abcdefgh")
            time.sleep(2)
            # driver.find_element_by_xpath("(//button[@type='submit'])[3]").click()
            driver.find_element_by_xpath("(//button[@type='submit'])[2]").click() #mtng only#
            time.sleep(8)
    post = PretoPost()
    post.pre()

if (driver.find_element_by_xpath("//h6[starts-with(.,'No data found')]")):
    driver.find_element_by_xpath("//button[@type='button' and span[starts-with(.,'Want a New Account?')]]").click()
    time.sleep(3)
    driver.find_element_by_xpath("//input[@data-cy='addressLine1']").send_keys("RMZ INFINITY")
    time.sleep(10)
    # driver.find_element_by_xpath("//div()")
    # region = driver.find_element_by_xpath("//div[@data-cy='POState']")
    time.sleep(2)
    address2 = driver.find_element_by_xpath("//input[@data-cy='addressLine2']").click()
    address2.send_keys("wertyu")
    time.sleep(2)
    driver.find_element_by_xpath("(//div[@aria-haspopup='listbox'])[1]").click()
    driver.find_element_by_xpath("//li[1]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//div[@data-cy='POCity']").click()
    driver.find_element_by_xpath("(//div[@aria-haspopup='listbox'])[2]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//li[1]").click()
    driver.find_element_by_xpath("//input[@name='billingName']").send_keys("RCAHNAAAA")
    driver.find_element_by_xpath("//textarea[@name='billDispatch.email']").send_keys("werty@hj.com")
    driver.find_element_by_xpath("//input[@name='creditController']").click()
    driver.find_element_by_xpath("//p[starts-with(.,'ttuser7')]").click()
    driver.find_element_by_xpath("//input[@name='accountManager']").click()
    driver.find_element_by_xpath("//p[starts-with(.,'ttuser5')]").click()

    driver.find_element_by_xpath("(//button[@type='button' and span[starts-with(.,'Upload Later')]])[1]").click()
    driver.find_element_by_xpath("(//input[@name='reason'])").send_keys("REason")



else:
    print("Account present")

time.sleep(15)
driver.quit()
