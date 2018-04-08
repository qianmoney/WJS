#个人设置-基本信息设置

class WjsBasicInformationSet():

    #进入到基本信息设置页面
    def OpenBasicInformationWeb(self,driver):
        driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/ul/li[6]/a').click()
        driver.find_element_by_xpath('//*[@id="account-menu-userinfo"]').click

    #填写基本信息
    def BasicInformationWrite(self,driver):
        trueName = driver.find_element_by_xpath('//*[@id="userInfo-form"]/ul/li[1]/input')
        card = driver.find_element_by_xpath('//*[@id="userInfo-form"]/ul/li[2]/input')


