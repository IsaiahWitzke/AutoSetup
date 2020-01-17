import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    # autoconfig github
    os.system('git config --global user.name "IsaiahWitzke"')
    os.system('git config --global user.email "isaiah.witzke@gmail.com"')
    
    # so that my password isn't all over the internet
    #   my password will be saved in a separte file
    #   that I just wont upload
    try:
        passwordFile = open("password.txt", "r")
    except IOError:
        print("please make a password.txt file with your google password in it in the "
              +os.path.abspath(os.getcwd())+ " directory")
        return

    usernameStr = 'isaiah.witzke@gmail.com'
    passwordStr = passwordFile.read()

    pathToChromeExe = os.path.abspath(os.getcwd())+'/chromedriver'
    browser = webdriver.Chrome(executable_path=pathToChromeExe)
    browser.get(('https://accounts.google.com/signin/chrome/sync/identifier?ssp=1&continue=https%3A%2F%2Fwww.google.com%2F&flowName=GlifDesktopChromeSync'))

    # filling in email + passwords
    username = browser.find_element_by_id('identifierId')
    username.send_keys(usernameStr)
    nextButton = browser.find_element_by_id('identifierNext')
    nextButton.click()

    # password
    # wait for transition then continue to fill items
    time.sleep(1)
    password = browser.find_element_by_class_name('whsOnd')
    password.send_keys(passwordStr)

if __name__ == "__main__":
    main()
