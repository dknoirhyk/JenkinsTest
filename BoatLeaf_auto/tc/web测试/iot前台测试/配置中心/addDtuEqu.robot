*** Settings ***
Library  pylib/homeAct.py
Library  pylib/settingAct.py

Suite Setup  goSettingCenter

*** Test Cases ***
添加DTU
    [Tags]      Basic   DTU
    [Setup]     checkDelDtu      300619020010
    addDtu      300619020010    6574
    ${readDtuInfo}=     read_dtuInfo
    ${result}=          compareDtuInfo      ${readDtuInfo}
    should be true      ${result}


#添加PD R
#    [Tags]      Basic   Equ
#    [Setup]     checkAddDtu     300619020010
#    addEqu      300619020010
#    ${readEquInfo}=     read_equInfo
#    ${result}=          compareEquInfo      ${readEquInfo}
#    should be true      ${result}
