'''DTU编辑页面'''

class dtuInfo:

    '''案例下拉框'''
    case = 'div.item:nth-of-type(1) > div'
    '''DTU类型下拉框'''
    dtuType = 'div.item:nth-of-type(2) > div'
    '''imei输入框'''
    imei = 'div.item:nth-of-type(3) > div > input'
    '''密码输入框'''  # 普通DTU下没有
    psw = 'div.item:nth-of-type(4) > div > input'
    '''DTU名称输入框'''
    dtuName = 'div.item:nth-of-type(5) > div > input'
    '''备注输入框'''
    note = 'div.item:nth-of-type(6) > div > input'
    '''下拉框'''
    dropDown = '[x-placement="bottom-start"] li > span'  # 有几个下拉条目,就返回几个elements

    '''提交'''
    confirm = '.right button'
    '''DTU添加是否成功消息'''
    addStatus = 'div[role="alert"] > p'