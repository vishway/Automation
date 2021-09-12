#Tested Customers
# C2518 << mtng
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
from Screenshot import Screenshot_Clipping


#enTER cUSTOMER DETAILS
print("Enter Customer Id")
cust_Id = input()

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)


driver.get("https://mtngodc.ace.dev-rancher.tecnotree.com/dclm-web-ui/")
# driver.get("Proceed to mtngodc.ace.dev-rancher.tecnotree.com (unsafe)")
# driver.get("http://localhost:3000/dclm-web-ui/dashboard") #Localhost
time.sleep(5)

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

begin = time.time()

# Navigate to 360 (Search Customer)
search_customer = driver.find_element_by_xpath("//input[@placeholder='Search for Customers']").send_keys(cust_Id)
time.sleep(10)

wait = WebDriverWait(driver, 25)
time.sleep(10)

try:
    no_found = driver.find_element_by_xpath("//p[starts-with(.,'No Data Available')]")
    print("Customer Not found")
    time.sleep(2)
except: 
    # Suspension
    class Termination ():
        def pre(self):
            searched = driver.find_element_by_xpath("(//a[@href])[2]").click()
            time.sleep(15)
            # driver.find_element_by_xpath("(//div[@data-cy='Overviewservice'])[1]").click()
            driver.find_element_by_xpath("(//div[@data-cy='Overaccount'])[1]").click()      #mtng only
            time.sleep(25)
            driver.find_element_by_xpath("(//div[@data-cy='moreActions'])").click()
            # wait.until(EC.element_to_be_selected((By.XPATH,"(//div[@data-cy='moreActions'])"))).click()
            print("Initiated Suspension")
            # more = driver.find_element_by_xpath("(//div[@data-cy='moreActions'])")
            # more.click()
            time.sleep(10)
            action = driver.find_element_by_xpath("(//span[text()='Soft Suspension'])").click()
            time.sleep(20)
            desc = driver.find_element_by_name("description").send_keys("abcdefgh")
            time.sleep(2)
            # driver.find_element_by_xpath("(//button[@type='submit'])[3]").click()
            driver.find_element_by_xpath("(//button[@type='submit'])[2]").click() #mtng only #Localhost
            # time.sleep(8)
            # driver.find_element_by_xpath("//button[@type='submit']").click()
            time.sleep(3)
            driver.find_element_by_xpath("//button[@data-cy='addPayment']").click()
            time.sleep(2)
            driver.find_element_by_xpath("//input[@type='text']").send_keys("Later")
            driver.find_element_by_xpath("//button[@type='submit']").click()
            time.sleep(8)
            driver.save_screenshot('ss2.png')
            screenshot = Image.open('ss2.png')
            screenshot.show()
    post = Termination()
    post.pre()
end = time.time()
finish = end - begin
print((finish)/60,"min Time recored")
time.sleep(15)
driver.quit()
