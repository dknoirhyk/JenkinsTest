*** Settings ***
Variables  config.py
Library  pylib/WebOp.py


Suite Setup     openBrowser
#Suite Teardown  closeBrowser