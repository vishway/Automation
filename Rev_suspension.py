##### From Dashboard##########

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from PIL import Image
from Screenshot import Screenshot_Clipping

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)
# driver.get("https://mtngodc.ace.dev-rancher.tecnotree.com/dclm-web-ui/")
# driver.get("https://sso2.tecnotree.com/authenticationendpoint/login.do?client_id=mAMU2p3gRsqFBDrfyMhmXnM6bqIa&commonAuthCallerPath=%2Foauth2%2Fauthorize&forceAuth=false&passiveAuth=false&redirect_uri=https%3A%2F%2Fmtngodc.ace.dev-rancher.tecnotree.com%2Fdclm-web-ui%2Fauth&response_type=code&scope=openid&state=openid&tenantDomain=carbon.super&sessionDataKey=8b00adfa-7279-47c4-9cd4-8bf73e836a95&relyingParty=mAMU2p3gRsqFBDrfyMhmXnM6bqIa&type=oidc&sp=MTNG_ODC_DCLM&isSaaSApp=false&authenticators=BasicAuthenticator%3ALOCAL")
# driver.get("http://dclm-mmp.cluster1.devtestlab2.tecnotree.com/dclm-web-ui/")
driver.get("http://localhost:3000/dclm-web-ui/dashboard") #Localhost

# SERVER ONLY
# advanced = driver.find_element_by_xpath("//button[@id='details-button']").click()
# time.sleep(5)
# Proceed to mtngodc.ace.dev-rancher.tecnotree.com (unsafe)
# Proceed to dclm-mmp.cluster1.devtestlab2.tecnotree.com (unsafe)
# driver.find_element_by_link_text('Proceed to mtngodc.ace.dev-rancher.tecnotree.com (unsafe)').click()
time.sleep(10)

begin = time.time()
# Authentication Page
search = driver.find_element_by_name("username")
search.send_keys("dclmappuser1")
password = driver.find_element_by_name("password")
password.send_keys("Tecnotree#3")
driver.find_element_by_name("submit").click()
driver.maximize_window()
time.sleep(5)

#SERVICE
driver.find_element_by_xpath("(//div[@data-cy='moreActions'])").click()
time.sleep(3)
driver.find_element_by_xpath("//p[starts-with(.,'Reversal')]").click()
driver.find_element_by_xpath("//input[@value='suspension']").click()
driver.find_element_by_xpath("//input[@id='name']").send_keys("PI467138")
time.sleep(2)
button = driver.find_element_by_xpath("(//button[@type='submit'])[3]")
button.click()

time.sleep(15)

desc = driver.find_element_by_name("description").send_keys("abcdefgh")
time.sleep(2)
driver.find_element_by_xpath("(//button[@type='submit'])[2]").click()
time.sleep(10)
driver.save_screenshot('ss1.png')
screenshot = Image.open('ss1.png')
screenshot.show()
end = time.time()
finish = end - begin
print((finish)/60 , "min Time recorded")

print("DOne")
driver.quit()