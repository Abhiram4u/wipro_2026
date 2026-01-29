*** Settings ***
Library    BuiltIn

*** Variables ***
${Name}     Abhiram
${Role}     Automation Tester
@{Skills}   Python   Robot Framework   Selenium

*** Test Cases ***
Test Case 1 - Log Messages
    Log  This is a log message using log keyword
    Log To Console    Hello ${Name}, welcome to Robot Framework!
Test Case 2 - Variables Demo
    Log    User Role is: ${Role}
    Log    Skills List: ${Skills}
    Log To Console    First skill is: ${Skills[0]}