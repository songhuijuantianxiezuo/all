*** Settings ***
Library          Selenium2Library
Test Setup       op browser
Test Template    put into text
Test Teardown    close browser

*** Test Cases ***
0   testuser1
1   testuser2
2   testuser3

*** Keywords ***

put into text
    [Arguments]     ${text}     
    Input Text  id:kw     ${text}
    Click Element   id:su

op browser
    Open Browser    http://www.baidu.com    browser=chrome

close browser
    Close Browser