*** Settings ***
Documentation   sendtopic
Library         Selenium2Library

*** Variables ***
${a}    ddddddddd
${b}    css:#reply_form > div > div > div.CodeMirror.cm-s-paper > div.CodeMirror-scroll


*** Test Cases ***
testcse1:
    打开浏览器
    输入内容    ${b}    ${a}
    点击提交


*** Keywords ***
打开浏览器
    Open Browser    http://118.31.19.120:3000/topic/5b9a794bbddb97bf61c1ffdc    browser=chrome
    Add Cookie      club        s%3A5b58481a0ec61db748a52c36%24%24%24%24.HQxF4bK%2ByCBrn4%2BGFL63RRv9wTnIIMSAmbjUy9NGtn8
    Add Cookie      connect.sid         s%3AZYo3VcMYrpTErWCJzuH3vrGVadAaxqum.RmOamVo0Nrh5sYFA6S276xIEzyAqg9e6HFdHR7WURNU
    Go To   http://118.31.19.120:3000/topic/5b9a794bbddb97bf61c1ffdc

输入内容
    [Arguments]     ${b}    ${a}        #关注变量的使用
    mouse_down_click_sendkeys       ${b}    ${a}
点击提交
    Click Element     css:#reply_form > div > div > div.editor_buttons > input
    Close Browser