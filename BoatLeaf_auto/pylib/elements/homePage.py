class homePage:

    iframeHome = 'welcome'

    '''配置中心'''
    settingCenter = 'div[id="nav0"]'
    '''中控台'''
    centerConsole = 'div[id="nav1"]'
    '''数据中心'''
    dataCenter = 'div[id="nav2"]'
    '''历史记录'''
    history = 'div[id="nav3"]'
    '''报警历史'''
    alertHistory = 'div[id="nav4"]'
    '''个人中心'''
    personalData = 'div[id="nav5"]'

    '''公告条目'''
    notice = 'div.notice-block > div'# 有几条公告条目，返回几个elements,用来点击查看详情
    '''单个条目的标题'''
    noticeName = '> p'# 在上面element的基础上选择
    '''单个条目的日期'''
    noticeDate = ' span'# 在上面element的基础上选择



    '''公告标题'''