*** Test Cases ***
Print Vote Eligibility
    ${age}=    Set Variable    20
    IF    ${age} >= 18
        Log To Console    Eligible to vote
    ELSE
        Log To Console    Not Eligible to vote
    END
Print Check Number Greater 
    ${num}=    Set Variable    5
    IF    ${num} > 10
        Log To Console    Greater than 10
    ELSE
        Log To Console    Less than or equal to 10
    END
Print Grades Using IF-ELSEIF-ELSE
        ${marks}=    Set Variable    75
        IF    ${marks} >= 90
            Log To Console    Grade A
        ELSE IF    ${marks} >= 75
            Log To Console    Grade B
        ELSE
            Log To Console    Grade C
        END
Inline If
    ${status}=    Set Variable    PASS 
    IF     '${status}' == 'PASS'
        Log To Console    Test Passed

    END