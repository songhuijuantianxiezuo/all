*** Settings ***
Documentation   register
Library         Selenium2Library
Test Setup      打开浏览器
Test Template   输入内容
Test Teardown   点击提交

# *** Variables ***
# ${a}        aaaaaaaaab


*** Test Cases ***                 
1                 invalid         
12                 sssss
I    invalid
Em                  ssss
E                   sssssss
Ems      fffff

*** Keywords ***
打开浏览器
    Open Browser    http://www.baidu.com    browser=chrome

输入内容
    [Arguments]     ${a}
    Input Text      id:kw       ${a}

点击提交
    Click Element     id:su
    Close Browser