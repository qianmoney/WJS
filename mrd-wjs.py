from login import LoginWjs
from login import LoginExit
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

#打开浏览器
brow = LoginWjs.OCdriver()
dr = brow.browser()
#打开微金所网站
brow.OpenWjsDriver(dr,hr)
sleep(2)
#登录
test = LoginExit.LoginExitWJS()
data = csv.reader(open('usename.csv','r'))
for user in data:
    try:
        mobile = user[0]
        pwd=user[1]
        sleep(1)
        test.LoginWeb(dr)
        sleep(1)
        test.LoginWJS(dr,mobile,pwd)
        sleep(1)
        test.ExitWJS(dr)

        print(mobile,'is ok')

    except Exception as e:
        print(e)
        print(mobile,'is error')
