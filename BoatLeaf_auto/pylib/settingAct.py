from pylib.WebOp import *
from pylib.elements.homePage import homePage
from pylib.elements.settingCenter import settingCenter
from pylib.elements.dtuInfo import dtuInfo

class settingAct:

    def __init__(self):
        self.inputDtuInfo = {}# 添加DTU时填写的信息
        self.addDtuMsg = None# 添加DTU后的提醒内容
        self.readDtuInfo = {}# 读取的DTU信息

        self.addePdrMsg = None# 添加PDR后的提醒内容

        self.dtuEle = None# 操作的DTU的element

        self.inputEquInfo = {}# 写入的设备信息
        self.readEquInfo = {}# 读取的设备信息

    def addDtu(self,imei='300619020010', psw='6574', case='恒压供水', type='高速DTU', name='自动化新增DTU', note='自动化测试备注'):
        """
添加DTU
        """
        self.inputDtuInfo = {'case': case, 'type': type, 'imei': imei, 'psw': psw, 'name': name, 'note': note}
        switch_frame('配置中心')
        ele_click(settingCenter.addDtu, '添加DTU')

        switch_frame('DTU信息')
        ele_click(dtuInfo.case, '案例')
        choose_dropDown(case)
        ele_click(dtuInfo.dtuType, 'DTU类型')
        choose_dropDown(type)
        ele_sendKeys(dtuInfo.imei, imei)
        ele_sendKeys(dtuInfo.psw, psw)
        ele_sendKeys(dtuInfo.dtuName, name)
        ele_sendKeys(dtuInfo.note, note)
        ele_click(dtuInfo.confirm)
        quit_frame()

        self.addDtuMsg = getMsg()
        printMsg(self.addDtuMsg)# 打印message



    def read_dtuInfo(self):
        """
获取DTU信息
        """
        id = None
        name = None
        case = None
        imei = None
        type = None

        dtuEle = findDtu(self.inputDtuInfo['imei'])
        self.dtuEle = dtuEle
        id = ele(settingCenter.dtuListId, dtuEle).text
        name = ele(settingCenter.dtuListName, dtuEle).text
        case = ele(settingCenter.dtuListCase, dtuEle).text
        imei = ele(settingCenter.dtuListImei, dtuEle).text
        type = ele(settingCenter.dtuListType, dtuEle).text

        self.readDtuInfo = {'id': id, 'name': name, 'case': case, 'imei': imei,'type': type}
        print(self.readDtuInfo)
        return self.readDtuInfo


    def compareDtuInfo(self, read = None):
        """
比较DTU新增的写入值和读取值
        :param read: 用于比较的读取值
        :return: 返回True或FalseD
        """

        from pprint import pprint
        input = self.inputDtuInfo
        if read:
            read = read
        else:
            read = self.readDtuInfo
        pprint(f'写入值:{input}')
        pprint(f'读取值:{read}')

        ret = True
        compareList = ['case', 'name', 'imei', 'type']
        for compare_key in compareList:
            if compare_ret(input[compare_key], read[compare_key]) == False:
                ret = False
        return ret

    def checkDelDtu(self, imei):
        """
查找并删除DTU(如果该DTU在列表中)
        :param imei: 要删除DTU的Imei
        """
        dtuEle = findDtu(imei)
        ele(settingCenter.dtuListDelete, dtuEle).click()
        ele_click(settingCenter.comfirmDel)
        print(f'删除DTU,imei:{imei}')

        # found = False
        # switch_frame('配置中心')
        # for oneEle in eles(settingCenter.dtuInfo):
        #     if ele(settingCenter.dtuListImei, oneEle).text == imei:
        #         found = True
        #         ele(settingCenter.dtuListDelete, oneEle).click()
        #         ele_click(settingCenter.comfirmDel)
        #         print(f'删除DTU,imei:{imei}')
        # if found == False:
        #     print('没有找到这个DTU,删除失败')

    def checkAddDtu(self, imei):
        """
查找并添加DTU(如果该DTU不在列表中)
        :param imei: 需要添加的DTU的Imei
        """
        switch_frame('配置中心')
        text = ele('input[placeholder="id、imei、名称、备注"]')
        if text:
            ele('input[placeholder="id、imei、名称、备注"]').clear()
        ele_sendKeys('input[placeholder="id、imei、名称、备注"]', imei)
        ele_click('div.search-box > button:nth-of-type(1)', '搜索')
        time.sleep(0.6)
        found = False
        for oneEle in eles(settingCenter.dtuInfo):
            if ele(settingCenter.dtuListImei, oneEle).text == imei:
                found = True
                print(f'找到imei为{imei}的DTU,不需要添加')
        if found == False:
            self.addDtu(imei)

    def addEqu(self, imei='300619020010',type = 'PD R',modbusAddr='1', equName='自动化测试新增PD R', equNote='自动化测试备注'):
        """
在指定DTU下添加type
        :param type: 设备类型
        :param imei: 所属DTU的imei
        :param modbusAddr: modbus地址
        :param equName: 设备名称
        :param equNote: 设备备注
        """
        self.inputEquInfo = {'type': type, 'addr': modbusAddr, 'name': equName, 'note': equNote}
        dtuEle = findDtu(imei)
        ele_click(settingCenter.dtuListAddEqu, '添加设备', dtuEle)
        print(f'点击添加设备,imei:{imei}')

        # switch_frame('配置中心')
        # found = False
        # for oneEle in eles(settingCenter.dtuInfo):# 找到指定imei的DTU,点击添加设备
        #     if ele(settingCenter.dtuListImei, oneEle).text == imei:
        #         found = True
        #         ele_click(settingCenter.dtuListAddEqu, '添加设备', oneEle)
        # if found == False:
        #     print(f'没有找到该DTU,Imei:{imei}')


        # 填写设备信息
        ele_click(settingCenter.equType)
        choose_dropDown(type)
        ele_sendKeys(settingCenter.modbusAddr, modbusAddr)
        ele_sendKeys(settingCenter.equName, equName)
        ele_sendKeys(settingCenter.equNote, equNote)
        ele_click(settingCenter.equComfirm)
        # 获取message
        quit_frame()
        self.addePdrMsg = getMsg()
        printMsg(self.addePdrMsg)# 打印message

    def read_equInfo(self, imei='300619020010', modbusAddr='1'):
        id  = None
        name = None
        addr = None
        type = None
        note = None
        dtuEle = findDtu(imei)
        found = False
        for oneEle in eles(settingCenter.equipmentInfo, dtuEle):
            if ele(settingCenter.equListAddr, oneEle).text == modbusAddr:
                found = True
                id = ele(settingCenter.equListId, oneEle).text
                name = ele(settingCenter.equListName, oneEle).text
                addr = ele(settingCenter.equListAddr, oneEle).text
                type = ele(settingCenter.equType, oneEle).text
                note = ele(settingCenter.equListNote, oneEle)
            if found == False:
                print(f'没有找到该设备,所属DTUimei:{imei},modbus地址:{modbusAddr}')
        self.readEquInfo = {'id': id, 'name': name, 'addr': addr, 'type': type, 'note': note}
        print(self.readEquInfo)
        return self.readEquInfo

    def compareEquInfo(self, read=None):
        """
比较设备的写入值和读取值
        :param read: 用于比较的读取值
        :return: 返回True或FalseD
        """

        from pprint import pprint
        input = self.inputEquInfo
        if read:
            read = read
        else:
            read = self.readEquInfo
        pprint(f'写入值:{input}')
        pprint(f'读取值:{read}')

        ret = True
        compareList = ['type', 'addr', 'name', 'note']
        for compare_key in compareList:
            if compare_ret(input[compare_key], read[compare_key]) == False:
                ret = False
        return ret

if __name__ == '__main__':
    webOp = WebOp()
    webOp.openBrowser()
    webOp.loginWebsite('123', '123456')

    switch_frame('首页')
    ele_click(homePage.settingCenter)
    switch_frame('配置中心')
    dtuEle = eles(settingCenter.dtuInfo)[0]  # 取第一条DTU
    id = dtuEle.find_element_by_css_selector(settingCenter.dtuListId).text
    print(id)
    webOp.closeBrowser()
