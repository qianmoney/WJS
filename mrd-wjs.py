from login import LoginWjs
from login import LoginExit
from login import wjsSHB
from time import *
import csv

#配置参数
'''
file = open ('username.txt','r')
lines = file.readlines()
file.close()
for line in lines:
    mobile=line.split(',')[0]
    pwd=line.split(',')[1]
'''


hr = 'http://weijinsuo.com/'
data = csv.reader(open('F:/test/wjs/qjp.csv', 'r'))
#打开浏览器
brow = LoginWjs.OCdriver()
dr = brow.browser()
#打开微金所网站
brow.OpenWjsDriver(dr,hr)
sleep(2)
#登录
test = LoginExit.LoginExitWJS()
def qjplogin():
    try:
        mobile = '17326835246'
        pwd = 'qianhao@1234'
        sleep(1)
        test.LoginWeb(dr)
        sleep(1)
        test.LoginWJS(dr, mobile, pwd)
        sleep(1)

        print(mobile, 'is ok')

    except Exception as e:
        print(e)
        print(mobile, 'is error')

if __name__ == '__main__':
    qjplogin()
    qjpset = wjsSHB.WjsBasicInformationSet()
    qjpset.OpenBasicInformationWeb(dr)
    for user in data:
        qjpset.BasicInformationWrite(dr,user[1],user[2],user[3],user[3])
    qjpset.commitBasicInformation(dr)

    dr.find_element_by_xpath('//*[@id="dialog-jftf5r31"]/div/div/div[3]/button').click()
    #判断是否修改成功
    '''
    resultsText = dr.find_element_by_xpath('//*[@id="dialog-jftf5r31"]/div/div/div[2]/div').text
    if resultsText == '修改成功':
        print(resultsText)
        dr.find_element_by_xpath('//*[@id="dialog-jftf5r31"]/div/div/div[3]/button').click()
    else:
        print(resultsText)
     '''
    #安全设置-实名认证
    qjpCertification = wjsSHB.Certification()
    qjpCertification.safeSet(dr)
    qjpCertification.CertificationSet(dr,user[1],user[2])



    #test.ExitWJS(dr)




