class settingCenter:

    iframeSetting = 'iframe[name="machine-dtumanager"]'


    '''添加DTU'''
    addDtu = 'button[id="addDtu"]'

    '''DTU信息'''
    dtuInfo = 'div[id="app"] > div.mainBox .dtu-item'# 有几个DTU就返回几个elements
    '''DTU列表展示的数据'''
    dtuListId = ' div.dtu-info > span:nth-child(2) > em'
    dtuListName = ' div.dtu-info > span:nth-child(3) > em'
    dtuListCase = ' div.dtu-info > span:nth-child(4) > em'
    dtuListImei = ' div.dtu-info > span:nth-child(5) > em'
    dtuListType = ' div.dtu-info > span:nth-child(6) > em'
    dtuListEdit = ' button.edit-dtu-btn'
    dtuListDelete = ' button.del-dtu-btn'
    dtuListAddEqu = ' button.add-machine-btn'

    '''设备信息'''
    equipmentInfo = ' .tableData tr.el-table__row'# 有几个设备就返回几个elements
    '''设备列表展示的数据'''
    equListId = ' > td:nth-child(1) > div.cell'
    equListName = ' > td:nth-child(2) > div.cell'
    equListAddr = ' > td:nth-child(3) > div.cell'
    equListType = ' > td:nth-child(4) > div.cell'
    equListTime = ' > td:nth-child(5) > div.cell'
    equListNote = ' > td:nth-child(6) > div.cell'
    equListSetting = ' > td:nth-child(7)  button.set-machine-btn'
    equListEdit = ' > td:nth-child(7)  button.edit-machine-btn'
    equListDelete = ' > td:nth-child(7)  button.del-machine-btn'

    '''确认删除'''
    comfirmDel = 'div.el-message-box > .el-message-box__btns button:nth-child(2)'

    '''新增、编辑设备界面'''
    tag = 'div.dialog-main > h2'# 标签名:新增设备、编辑设备
    underDtu = 'div.dialog-main > div:nth-child(2) > span:nth-child(2)'
    equType = 'div.dialog-main > div:nth-child(3)'
    modbusAddr = 'div.dialog-main > div:nth-child(4) input'
    equName = 'div.dialog-main > div:nth-child(5) input'
    equNote = 'div.dialog-main > div:nth-child(6) input'
    equComfirm = 'div.el-dialog__body > button'
    '''下拉框'''
    dropDown = '[x-placement="bottom-start"] li > span'  # 有几个下拉条目,就返回几个elements