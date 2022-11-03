from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

def test_code(browsertype):
    if browsertype == "chrome":
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browsertype == "firefox":
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)

    actionChains =ActionChains(driver)



    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(10)
    driver.find_element(By.XPATH, value="//input[@placeholder='Username']").send_keys("Admin")
    driver.find_element(By.XPATH, value="//input[@placeholder='Password']").send_keys("admin123")
    driver.find_element(By.XPATH, value="//button[@type='submit']").click()
    time.sleep(10)


#Add an employee

    driver.find_element(By.CSS_SELECTOR, value="button.oxd-button--secondary:nth-child(1)").click()
    time.sleep(10)
    driver.find_element(By.XPATH, value='//input[@placeholder="First Name"]').send_keys("Amaila")
    time.sleep(5)
    driver.find_element(By.XPATH, value='//input[@placeholder="Middle Name"]').send_keys("Marry")
    time.sleep(5)
    driver.find_element(By.XPATH, value='//input[@placeholder="Last Name"]').send_keys("Peter")
    time.sleep(5)
    #delete employee id
    driver.find_element(By.CSS_SELECTOR, value="div.oxd-grid-2:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)").clear()
    driver.find_element(By.CSS_SELECTOR, value="div.oxd-grid-2:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)").send_keys("1236")
    #Create Login Details
    driver.find_element(By.CSS_SELECTOR, value=".oxd-switch-input").click()
    driver.find_element(By.CSS_SELECTOR, value="div.oxd-form-row:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)").send_keys("AmailaMarry")
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, value=".user-password-cell > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)").send_keys("Amaila01234@pw")
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, value="div.oxd-form-row:nth-child(5) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)").send_keys("Amaila01234@pw")
    time.sleep(5)
    driver.find_element(By.XPATH, value='//button[@type="submit"]').click()
    time.sleep(10)


    #Employee Personal Details Open

    #driver.find_element(By.CSS_SELECTOR, value="div.orangehrm-horizontal-padding:nth-child(1) > form:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)").send_keys("Nupur")
    time.sleep(2)
    #license
    driver.find_element(By.CSS_SELECTOR, value="div.oxd-form-row:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input").send_keys("MP201234789")


    time.sleep(5)
    #Save
    driver.find_element(By.CSS_SELECTOR, value="button.oxd-button--secondary:nth-child(2)").click()
    time.sleep(5)


#Go to Admin create admin
    driver.find_element(By.CSS_SELECTOR, value="a[href='/web/index.php/admin/viewAdminModule']").click()
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR, value="button.oxd-button--secondary:nth-child(1)").click()
    time.sleep(10)
    # Username
    driver.find_element(By.CSS_SELECTOR,value="div.oxd-form-row:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, value="div.oxd-select-option:nth-child(2) > span").click()

    #driver.find_element(By.CSS_SELECTOR, value="div.oxd-select-option:nth-child(2) > span").click()
    time.sleep(3)

    #EmployeeName
    search=driver.find_element(By.XPATH, value='//input[@placeholder="Type for hints..."]')
    search.send_keys("Amaila")
    time.sleep(5)
    search.send_keys(Keys.ARROW_DOWN)
    search.send_keys(Keys.CONTROL)
    #search_dropdown=driver.find_element(By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]')
    #actionChains.click(search_dropdown).perform()

    #auto_com=driver.find_element(By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]')
    time.sleep(5)







    time.sleep(5)



    #Enabled?
    ele2 = driver.find_element(By.CSS_SELECTOR, value='div.oxd-grid-item:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
    ele2.send_keys(Keys.ARROW_DOWN)

    # Username
    driver.find_element(By.CSS_SELECTOR,  value='div.oxd-grid-item:nth-child(4) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)').send_keys('Amaila')

    time.sleep(2)

    #Password
    time.sleep(5)
    driver.find_element(By.XPATH, value='/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input').send_keys('Amaila@123')
    time.sleep(2)
    driver.find_element(By.XPATH, value='/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input').send_keys('Amaila@123')
    time.sleep(2)
    driver.find_element(By.XPATH, value='//button[@type="submit"]').click()

    #Go to Admin and search for user created

    driver.find_element(By.CSS_SELECTOR, value="a[href='/web/index.php/admin/viewAdminModule']").click()
    time.sleep(5)
    #search for admin username
    driver.find_element(By.CSS_SELECTOR, value ="input.oxd-input:nth-child(1)").send_keys("Amaila")
    #search for Employee name
    emp_name = driver.find_element(By.XPATH, value='//input[@placeholder="Type for hints..."]')
    emp_name.send_keys("Amalia Marry Peter")
    emp_name.send_keys(Keys.ARROW_DOWN)
    time.sleep(5)
    #emp_name_hint=driver.find_element(By.CSS_SELECTOR, value='html body div#app div.oxd-layout div.oxd-layout-container div.oxd-layout-context div.orangehrm-background-container div.oxd-table-filter div.oxd-table-filter-area form.oxd-form div.oxd-form-row div.oxd-grid-4.orangehrm-full-width-grid div.oxd-grid-item.oxd-grid-item--gutters div.oxd-input-group.oxd-input-field-bottom-space div div.oxd-autocomplete-wrapper div.oxd-autocomplete-text-input.oxd-autocomplete-text-input--active div.oxd-autocomplete-text-input--after')


    #select admin in User Role

    driver.find_element(By.CSS_SELECTOR,value="div.oxd-grid-item:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)").click()
    time.sleep(5)
    driver.find_element(By.XPATH, value="//button[@type='submit']").click()

    #Logout from application
    driver.find_element(By.CSS_SELECTOR,value="i.oxd-icon:nth-child(3)").click()
    driver.find_element(By.XPATH, value='//a[@href="/web/index.php/auth/logout"]').click()
    time.sleep(5)

    #Login with new credentials
    driver.find_element(By.XPATH, value="//input[@placeholder='Username']").send_keys("AmailaMarry")
    driver.find_element(By.XPATH, value="//input[@placeholder='Password']").send_keys("Amaila01234@pw")
    driver.find_element(By.XPATH, value="//button[@type='submit']").click()




test_code("firefox")


