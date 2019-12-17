*** Settings ***
Variables  config.py
Library  pylib/WebOp.py

# 登陆Iot前台
Suite Setup  loginWebsite   ${iotUserInfo}[name]    ${iotUserInfo}[psw]