*** Settings ***
Library         Selenium2Library
Library         BuiltIn

*** Test Cases ***
testcase3:
    Open Browser    url=http://www.baidu.com      browser=chrome
    sleep           3s
    Maximize Browser Window
    Click Element   link:hao123
    Input Text      class:input-hook        ffffffffff           #class name只能放一个
    Click Button    class:button-hook
    sleep           3s
    ${handle} =      Select Window              NEW
    Title Should Be     ffffffffff_百度搜索
    ${allwindows} =     Get Window Handles
    # Capture Page Screenshot
    Log To Console  Hello, console!
    ${time} =       Get Time
    Log To Console      ${time}
    
