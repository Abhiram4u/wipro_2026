*** Settings ***
Library           SeleniumLibrary
Library    SeleniumLibrary
*** Keywords ***
Open Application
    Open Browser    https://www.google.com    chrome
    Maximize Browser Window

*** Test Cases ***
launchapp.robot
    Open Application
    Close Browser
