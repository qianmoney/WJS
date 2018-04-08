#chrome打开微金所，退出微金所，关闭浏览器
from selenium import webdriver

#open driver,open wjs
class OCdriver():
    def browser(self):
        self.driver = webdriver.Chrome()
        return self.driver
    def OpenWjsDriver(self,driver,hr):
        self.driver.get(hr)

    def CloseDriver(self,driver):
        self.driver.quit()



