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

driver.get("https://mtngodc.ace.dev-rancher.tecnotree.com/dclm-web-ui/")
# driver.get("Proceed to mtngodc.ace.dev-rancher.tecnotree.com (unsafe)")
# driver.get("http://localhost:3000/dclm-web-ui/dashboard") #Localhost
time.sleep(5)

# SERVER ONLY
advanced = driver.find_element_by_xpath("//button[@id='details-button']").click()
time.sleep(5)
# Proceed to mtngodc.ace.dev-rancher.tecnotree.com (unsafe)
# Proceed to dclm-mmp.cluster1.devtestlab2.tecnotree.com (unsafe)
driver.find_element_by_link_text('Proceed to mtngodc.ace.dev-rancher.tecnotree.com (unsafe)').click()
time.sleep(10)

begin = time.time()

# Authentication Page
search = driver.find_element_by_name("username")
search.send_keys("dclmappuser1")
password = driver.find_element_by_name("password")
password.send_keys("Tecnotree#3")
driver.find_element_by_name("submit").click()
driver.maximize_window()
# time.sleep(15)

# radio = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='MuiIconButton-label' and input[@value='F']]"))).click()
# driver.execute_script('arguments[0].click()', radio)

radio = driver.find_element_by_xpath("//span[@class='MuiIconButton-label' and input[@value='F']]").click()
radio.click()
time.sleep(2)
driver.find_element_by_xpath("//input[@name='identificationId']").send_keys("3456787654")
driver.find_element_by_xpath("//input[@name='customerEmailPhone']").send_keys("rty@yiuyiu.com")
given_name =driver.find_element_by_xpath("//input[@name='givenName']").send_keys("AMibka")
familyName =driver.find_element_by_xpath("//input[@name='familyName']").send_keys("AMibka")
time.sleep(5)
driver.find_element_by_xpath("(//*[contains(@class,'containedPrimary')])[1]").click()
time.sleep(10)
driver.find_element_by_xpath("//button[@aria-label='change date']").click()
driver.find_element_by_xpath("(//*[contains(@class,'MuiPickersDay-day-597')])[4]").click()

#address
driver.find_element_by_xpath("//input[@data-cy='addressLine1']").send_keys("RMZ INFINITY")
driver.find_element_by_xpath("//input[@data-cy='addressLine2']").click()
time.sleep(3)
driver.find_element_by_xpath("(//div[@aria-haspopup='listbox'])[1]").click()
time.sleep(3)
driver.find_element_by_xpath("//li[1]").click()
time.sleep(3)
driver.find_element_by_xpath("(//div[@aria-haspopup='listbox'])[2]").click()
time.sleep(3)
driver.find_element_by_xpath("//li[1]").click()
time.sleep(3)
driver.find_element_by_xpath("(//span[starts-with(.,'Upload Later')])[1]").click()
time.sleep(3)
driver.find_element_by_xpath("(//input[@name='reason'])").send_keys("REason")
time.sleep(3)
driver.find_element_by_xpath("(//span[starts-with(.,'Save')])").click()
time.sleep(7)
driver.find_element_by_xpath("//button[@type='submit']").click()

end = time.time()
finish = end - begin
print((finish)/60,"min Time recored")
time.sleep(30)
driver.quit()
