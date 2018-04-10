#个人设置-基本信息设置
# -*- coding: utf-8 -*-
from selenium.webdriver import ActionChains
import select,socket
import random
from time import *
from selenium.webdriver.support.ui import Select

class WjsBasicInformationSet():

    #进入到基本信息设置页面
    def OpenBasicInformationWeb(self,driver):
        try:
            BasicInformationButton = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/ul/li[6]/a')
            action0 = ActionChains(driver)
            action0.move_to_element(BasicInformationButton).click().perform()
            print('OpenBasicInformationWeb is ok')
        except Exception as e:
            print('OpenBasicInformationWeb is error')

        try:
            driver.find_element_by_xpath('//*[@id="account-menu-userinfo"]').click()
            print('OpenBasicInformationWeb is ok')
        except Exception as e:
            print('OpenBasicInformationWeb is error')

    #填写基本信息
    def BasicInformationWrite(self,driver,trueNameParameter,cardParameter,birthPlaceParameter,accountPlaceParameter):
        #定位元素
        trueName = driver.find_element_by_xpath('//*[@id="userInfo-form"]/ul/li[1]/input')
        card = driver.find_element_by_xpath('//*[@id="userInfo-form"]/ul/li[2]/input')
        education = driver.find_element_by_id('education')
        birthPlaceProvince = driver.find_element_by_id('province')
        birthPlaceCity = driver.find_element_by_id('city')
        birthPlaceCountry = driver.find_element_by_id('country')
        accountPlace = driver.find_element_by_xpath('//*[@id="userInfo-form"]/ul/li[9]/input')
        Address = driver.find_element_by_xpath('//*[@id="userInfo-form"]/ul/li[10]/input')
        sexwoman = driver.find_element_by_xpath('//*[@id="userInfo-form"]/ul/li[11]/label[1]/input')
        sexman = driver.find_element_by_xpath('//*[@id="userInfo-form"]/ul/li[11]/label[2]/input')
        marriage = driver.find_element_by_xpath('//*[@id="userInfo-form"]/ul/li[12]/label[1]/input')
        children = driver.find_element_by_xpath('//*[@id="userInfo-form"]/ul/li[13]/label[2]/input')
        house = driver.find_element_by_xpath('//*[@id="userInfo-form"]/ul/li[14]/label[2]/input')
        houseLoan = driver.find_element_by_xpath('//*[@id="userInfo-form"]/ul/li[15]/label[2]/input')
        car = driver.find_element_by_xpath('//*[@id="userInfo-form"]/ul/li[16]/label[2]/input')
        carLoan = driver.find_element_by_xpath('//*[@id="userInfo-form"]/ul/li[17]/label[2]/input')

        #元素赋值
        trueName.send_keys(trueNameParameter)
        card.send_keys(cardParameter)
        #最高学历下边随机选一个学历
        action = ActionChains(driver)
        action.move_to_element(education).click().perform()
        driver.find_element_by_xpath('//*[@id="education"]/option[3]').click()

        #籍贯选择，选择省
        actionbirthPlacePlaceProvince = ActionChains(driver)
        actionbirthPlacePlaceProvince.move_to_element(birthPlaceProvince).click().perform()
        selectProvince = Select(birthPlaceProvince)
        selectProvince.select_by_visible_text(birthPlaceParameter[0:3])
        #选择市
        actionbirthPlacePlaceCity = ActionChains(driver)
        actionbirthPlacePlaceCity.move_to_element(birthPlaceCity).click().perform()
        selectCity = Select(birthPlaceCity)
        selectCity.select_by_visible_text(birthPlaceParameter[3:5])
        #选择县
        actionbirthPlacePlaceCountry = ActionChains(driver)
        actionbirthPlacePlaceCountry.move_to_element(birthPlaceCountry).click().perform()
        selectCountry = Select(birthPlaceCountry)
        selectCountry.select_by_visible_text(birthPlaceParameter[5:8])


        #户口所在地
        accountPlace.send_keys(accountPlaceParameter)
        Address.send_keys(accountPlaceParameter)
        #性别，身份证号最后一位，是偶数为2女，非偶数为男
        sexlast = cardParameter[-1]
        if sexlast == 'x' or sexlast == 'X':
            sexman.click()
        elif int(sexlast)%2 == 0:
            sexwoman.click()
        else:
            sexman.click()
        marriage.click()
        children.click()
        house.click()
        houseLoan.click()
        car.click()
        carLoan.click()

    def commitBasicInformation(self,driver):
        driver.find_element_by_xpath('//*[@id="userInfo-form"]/ul/li[18]/span/button').click()

class Certification():
    def safeSet(self,driver):
        safeButton = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/ul/li[6]/a')
        action1 = ActionChains(driver)
        action1.move_to_element(safeButton).click().perform()
        driver.find_element_by_xpath('//*[@id="account-menu-safe"]').click()
    def CertificationSet(self,driver,trueNameParameter,cardParameter):
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/ul/li[2]/p/span[4]').click()
        trueName = driver.find_element_by_xpath('//*[@id="auth-form"]/p[1]/input')
        card = driver.find_element_by_xpath('//*[@id="auth-form"]/p[2]/input[1]')
        trueName.send_keys(trueNameParameter)
        card.send_keys(cardParameter)
        driver.find_element_by_xpath('//*[@id="auth-btn"]').click()







