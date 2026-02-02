*** Variables ***
@{Colors}  Red Green Blue
@{users}  admin  user 
@{pwds}  admin123  user123

*** Test Cases ***

Breaking or exit loop
    FOR    ${i}    IN RANGE    1  10
        IF    ${i} == 5
            BREAK
        END
        Log To Console    ${i}
    END
    
Continue or Skip iteration
    FOR    ${i}    IN RANGE    1  6
        IF    ${i} == 3
            CONTINUE
        END
        Log To Console    ${i}
    END


For loop list
    FOR    ${item}    IN    one  two  Three
        Log To Console    Item:${item}
    END
    
For loop list variable
    FOR    ${color}    IN    @{Colors}
        Log To Console    Color:${Color}

    END
    
For Loop - with step
    FOR    ${i}    IN RANGE    0  10  2 
        Log To Console    Value:${i}
    END
    
    
For loop - ENUMERATE
    FOR    ${index}  ${value}    IN ENUMERATE  a  b  c
        Log To Console    ${index} = ${value}

    END
    
For loop - Zip multiple lists
    FOR    ${u}  ${p}    IN     ZIP  @{users}  @{pwds}
        Log To Console    ${u}/${p}
    END
    
For loop with if conditon
       FOR    ${n}    IN RANGE    1    6
           IF    ${n} == 3
           Log To Console        Found 3
           END
       END


    