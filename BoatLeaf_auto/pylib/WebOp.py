# coding:utf8
from selenium import webdriver
from config import *
from robot.libraries.BuiltIn import BuiltIn
import time

wd = None

class WebOp:

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        pass


    def openBrowser(self):
        '''打开浏览器'''
        self.wd = webdriver.Chrome()
        print('打开浏览器', ret_time())
        name = 'wd'
        try:
            BuiltIn().set_global_variable('${%s}'%name, self.wd)
        except:
            global wd
            wd = self.wd
        self.wd.implicitly_wait(2)
        self.wd.maximize_window()


    def closeBrowser(self):
        '''关闭浏览器'''
        self.wd.quit()
        print('关闭浏览器', ret_time())

    def loginWebsite(self, username, psw):
        '''登陆iot网站'''
        self.wd.get(iotUrl)
        print(f'进入url:{iotUrl}', ret_time())
        self.wd.find_element_by_css_selector('.loginFrom >div:nth-child(1) input').send_keys(username)
        self.wd.find_element_by_css_selector('.loginFrom >div:nth-child(2) input').send_keys(psw)
        self.wd.find_element_by_css_selector('.loginFrom >div:nth-child(3) input').send_keys('1111')
        print(f'输入用户名{username},密码{psw}', ret_time())
        time.sleep(0.7)
        self.wd.find_element_by_css_selector('.loginFrom >div:nth-child(4) button').click()
        print('点击登陆', ret_time())

'''系统的操作'''
def ret_time():
    # 获取当前时间
    time_now = int(time.time())
    # 转换成localtime
    time_local = time.localtime(time_now)
    # 转换成新的时间格式(2016-05-09 18:59:20)
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    return dt

def compare_ret(input, read):# 比较写入值和读取值
    """
比较写入值和读取值,并打印结果,返回结果
    :param input: 写入值
    :param read: 读取值
    :return: 返回True或False
    """
    if input == read:
        print(f'{input} == {read}')
        return True
    else:
        print(f'{input} != {read}')
        return False

'''selenium的操作'''
try:
    wd = BuiltIn().get_variable_value('${wd}')
except:
    pass

def ele(css, ele = None):# 查找单个元素
    """
查找单个元素
    :param css: css_selector
    :param ele: 让指定元素作为对象去查找,默认是None,让webdriver作为对象
    :return: 查找的元素
    """
    if ele:
        return ele.find_element_by_css_selector(css)
    else:
        return wd.find_element_by_css_selector(css)


def eles(css, ele = None):# 查找多个元素
    """
查找多个元素
    :param css: css_selector
    :param ele: 让指定元素作为对象去查找,默认是None,让webdriver作为对象
    :return: 查找的元素
    """
    if ele:
        return ele.find_elements_by_css_selector(css)
    else:
        eles = wd.find_elements_by_css_selector(css)
    return eles


def ele_click(css, ele_name=None, ele1=None):# 点击单个元素
    """
查找element并点击
    :param css: css_selector
    :param ele_name: element的名称(会被打印)
    :param ele1: element对象,如果传值,会在这个对象基础上查询
    """
    if ele:
        ele(css, ele1).click()
    else:
        ele(css).click()
    if ele_name:
        print(f'点击{ele_name}', ret_time())

def ele_sendKeys(css, key):
    ele(css).send_keys(key)
    print(f'填写:{key}', ret_time())


from pylib.elements.frame import *
def switch_frame(inputName):# 进入frame
    """
进入某个frame
    :param inputName: frame别名如:'首页'
    """
    quit_frame()
    i = 0
    for name in inputNameList:
        if name == inputName:
            wd.switch_to.frame(frameNameList[i])
            print(f'进入frame:{name},{frameNameList[i]}', ret_time())
        i += 1


def quit_frame():# 退出所有iframe
    wd.switch_to.default_content()
    print('退出所有iframe', ret_time())

def choose_dropDown(text, dropDown = '[x-placement="bottom-start"] li > span'):# 下拉框选择
    """
在下拉框中选择一项
    :param text: 选项的text
    :param dropDown: 下拉框的css_selector(有默认值)
    """
    for ele in eles(dropDown):
        if ele.text == text:
            ele.click()
            print(f'选择{text}', ret_time())

def getMsg():
    """
获取消息框
    :return: message,没有获取到消息框返回notFound
    """
    start_time = time.time()
    while True:
        try:
            msgInfo = ele('div[role="alert"] > p').text
            if msgInfo:
                return msgInfo
        except:
            pass
        use_time = time.time()-start_time
        if use_time > 5:
            return 'notFound'


def printMsg(saveMsg):
    """
格式化打印message
    :param saveMsg: message
    """
    if saveMsg:
        print(f'message:{saveMsg}', ret_time())
    elif saveMsg == 'notFound':
        print('没有获取到message')
    else:
        print(f'获取message未知错误:{saveMsg}')

from pylib.elements.settingCenter import settingCenter
def findDtu(imei):
    switch_frame('配置中心')
    text = ele('input[placeholder="id、imei、名称、备注"]')
    if text:
        ele('input[placeholder="id、imei、名称、备注"]').clear()
    ele_sendKeys('input[placeholder="id、imei、名称、备注"]', imei)
    ele_click('div.search-box > button:nth-of-type(1)', '搜索')
    time.sleep(0.6)
    found = False
    for oneEle in eles(settingCenter.dtuInfo):  # 找到指定imei的DTU
        if ele(settingCenter.dtuListImei, oneEle).text == imei:
            found = True
            return oneEle
    if found == False:
        printMsg(f'没有找到该DTU,Imei:{imei}')
        return None

if __name__ == '__main__':
    print(ret_time())
    pass