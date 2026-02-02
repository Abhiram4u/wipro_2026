*** Settings ***
Library    SeleniumLibrary


*** Variables ***
${URL}      https://demo.automationtesting.in/Register.html
${BROWSER}  Chrome


*** Test Cases ***
Form Interaction Using SeleniumLibrary
    # 1. Open Browser
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    # 2. Text Box Interaction
    Input Text    xpath=//input[@placeholder='First Name']    Abhi
    Input Text    xpath=//input[@placeholder='Last Name']     Ram
    Input Text    xpath=//textarea[@ng-model='Adress']        Hyderabad
    Input Text    xpath=//input[@type='email']                abhi@gmail.com
    Input Text    xpath=//input[@type='tel']                  9876543210

    #2 Radio Button
    Click Element    xpath=//input[@value='Male']

    #2. Check Box
    Click Element    id=checkbox1

    # 2. Drop-down
    Select From List By Value    id=Skills    Python

    # 3. Built-in Keyword- Run Keyword If
    Run Keyword If    '${BROWSER}' == 'Chrome'    Log    Test executed in Chrome browser

    # 3. Sleep
    Sleep    2s

    # Submit the form
    Click Button    id=submitbtn

    # 4. Validation using Built-in Keyword: Should Be Equal
    ${title}=    Get Title
    Should Be Equal    ${title}    Register

    # 5. Close Browser
    Close Browser
