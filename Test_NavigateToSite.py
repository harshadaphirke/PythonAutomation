import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_verifyaddaccountdetails():
    # create webdriver object
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http://practice.automationtesting.in")
    myaccount = driver.find_element(By.ID, "menu-item-50")
    myaccount.click()

    time.sleep(2)

    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    btnlogin = driver.find_element(By.NAME, "login")

    username.send_keys("harshada.phirke@gmail.com")
    password.send_keys("!QAZ1qaz@#$%")
    btnlogin.click()

    time.sleep(2)

    accountdetails = driver.find_element(By.LINK_TEXT, "Account Details")
    accountdetails.click()

    firstname = driver.find_element(By.ID, "account_first_name")
    lastname = driver.find_element(By.ID, "account_last_name")

    '''TODO: Read test data from testdata files on runtime'''
    firstname.clear()
    firstname.send_keys("Harshada1")

    lastname.clear()
    lastname.send_keys("Phirke1")

    submit = driver.find_element(By.NAME, "save_account_details")
    submit.click()

    logout = driver.find_element(By.LINK_TEXT, "Logout")
    logout.click()
    time.sleep(2)
    driver.close()


def test_verifyaccountdetails():
    # create webdriver object
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http://practice.automationtesting.in")
    myaccount = driver.find_element(By.ID, "menu-item-50")
    myaccount.click()

    '''TO Do:add check for page load event'''
    time.sleep(2)
    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    btnlogin = driver.find_element(By.NAME, "login")

    username.send_keys("harshada.phirke@gmail.com")
    password.send_keys("!QAZ1qaz@#$%")
    btnlogin.click()

    time.sleep(2)

    accountdetails = driver.find_element(By.LINK_TEXT, "Account Details")
    accountdetails.click()

    firstname = driver.find_element(By.ID, "account_first_name")
    lastname = driver.find_element(By.ID, "account_last_name")

    '''TODO: Read test data from testdata files on runtime'''
    assert "Harshada1" == firstname.get_attribute('value')
    assert "Phirke1" == lastname.get_attribute('value')

    logout = driver.find_element(By.LINK_TEXT, "Logout")
    logout.click()
    time.sleep(2)
    driver.close()



