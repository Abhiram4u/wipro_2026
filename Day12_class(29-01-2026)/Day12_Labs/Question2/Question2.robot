*** Settings ***
Library    BuiltIn
Library    Process
Library    SeleniumLibrary

*** Variables ***
${PYTHON_CMD}    python

*** Test Cases ***
Verify Environment Setup
    [Documentation]    Verifies Python, Robot Framework, SeleniumLibrary and prints Robot version
    Verify Python Installation
    Verify Robot Framework Installation
    Print Robot Framework Version
    Log To Console    Environment setup verification completed successfully

*** Keywords ***
Verify Python Installation
    Log    Checking Python installation...
    ${result}=    Run Process    ${PYTHON_CMD}    --version    stdout=PIPE    stderr=PIPE
    Run Keyword If    ${result.rc} != 0    Fail    Python is not installed or not added to PATH
    Log    Python Version: ${result.stdout}
    Log To Console     Python is installed

Verify Robot Framework Installation
    Log    Checking Robot Framework installation...
    ${result}=    Run Process    ${PYTHON_CMD}    -c    import robot; print(robot.__version__)    stdout=PIPE    stderr=PIPE
    Run Keyword If    ${result.rc} != 0    Fail     Robot Framework is not installed
    Log    Robot Framework Version: ${result.stdout}
    Log To Console     Robot Framework is installed

Print Robot Framework Version
    ${result}=    Run Process    ${PYTHON_CMD}    -c    import robot; print(robot.__version__)    stdout=PIPE
    Log To Console    Robot Framework Version: ${result.stdout}
