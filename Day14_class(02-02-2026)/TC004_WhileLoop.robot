*** Test Cases ***
while loop with break
    ${i}=    Set Variable    1
    WHILE    True 
        IF    ${i} == 4
            BREAK
        END
        Log To Console    ${i}
        ${i}=    Evaluate    ${i}+1
    END

Error handling
    TRY
        Fail    Something went wrong
    EXCEPT
        Log To Console    Error Handled
    FINALLY
        Log To Console    Always executed
    END


