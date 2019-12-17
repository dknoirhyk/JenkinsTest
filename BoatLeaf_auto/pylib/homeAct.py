from pylib.WebOp import *
from pylib.elements.homePage import homePage

class homeAct:

    def goSettingCenter(self):
        """
进入配置中心
        """
        wd.get(iotUrl)
        switch_frame('首页')
        ele_click(homePage.settingCenter, '配置中心')