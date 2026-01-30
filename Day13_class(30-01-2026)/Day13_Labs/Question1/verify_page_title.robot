*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}       https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}   chrome
    
*** Test Cases ***
Verify Page Title
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Title Should Be    OrangeHRM
    Sleep    5s
    Capture Page Screenshot
    Close Browser