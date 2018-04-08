from .LoginWjs import OCdriver
from selenium import webdriver


# 微金所登录退出账号

class LoginExitWJS():
    '''
    def LoginWJSElement(self, driver):

        loginbutton = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/span[2]/a[2]')
        loginmobile = self.driver.find_element_by_xpath('//*[@id="mobile"]')
        loginpwd = self.driver.find_element_by_xpath('//*[@id="pwd"]')
        login = self.driver.find_element_by_xpath('//*[@id="login"]')
        return loginbutton,loginmobile,loginpwd,login


    def ExitWJSElement(self,driver):
        loginexit = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/span[3]/a[3]')
    '''
    def LoginWeb(self,driver):
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/span[2]/a[2]').click()
        except Exception as e:
            print('error',e)
    def LoginWJS(self,driver,mobile,pwd):
        try:

            mobileElement = driver.find_element_by_xpath('//*[@id="mobile"]')
            mobileElement.clear()
            mobileElement.send_keys(mobile)
            pwdElement= driver.find_element_by_xpath('//*[@id="pwd"]')
            pwdElement.clear()
            pwdElement.send_keys(pwd)
            driver.find_element_by_xpath('//*[@id="login"]').click()
        except Exception as e:
            print('error',e)

    def ExitWJS(self,driver):
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/span[3]/a[3]').click()
        except Exception as e:
            print('error',e)

