*** Settings ***
Library    SeleniumLibrary
Suite Setup    Open Browser    file:///C:/Users/abhir/PycharmProjects/Wipro_2026/CaseStudy4/patient_form.html    chrome
Suite Teardown    Close Browser

*** Test Cases ***
Register Patient
    Input Text    name=name    John
    Sleep    1s
    Input Text    name=age     30
    Sleep    1s
    Click Element    xpath=//input[@value='Male']
    Sleep    1s
    Input Text    name=contact    9988776655
    Input Text    name=disease    Fever
    Select From List By Label    name=doctor    Dr. Smith
    Sleep    2s
    Click Button    Register

