*** Test Cases ***

Run keyword if
    ${status}=        Set Variable    PASS 
    Run Keyword If    '${status}' == 'PASS'  Log To Console    Test passed 

Run keyword unless
    ${status}=    Set Variable    FAIL 
    Run Keyword Unless    '${status}' == 'PASS'  Log To Console    Test Failed