*** Settings ***
Library    RequestsLibrary


*** Variables ***
${BASE_URL}    http://127.0.0.1:5000


*** Test Cases ***


#  RESTAURANT MODULE (1–4)
# --------------------------------------------------------

1 Register Restaurant
    Create Session    foodie    ${BASE_URL}

    ${headers}=    Create Dictionary    Content-Type=application/json
    ${body}=       Set Variable    {"name":"Robot Hub","category":"Veg","location":"Hyderabad","contact":"99999"}

    ${res}=    POST On Session    foodie    url=/api/v1/restaurants
    ...    data=${body}
    ...    headers=${headers}

    Status Should Be    201    ${res}


2 Update Restaurant
    ${headers}=    Create Dictionary    Content-Type=application/json
    ${body}=       Set Variable    {"location":"Bangalore"}

    ${res}=    PUT On Session    foodie    url=/api/v1/restaurants/1
    ...    data=${body}
    ...    headers=${headers}

    Status Should Be    200    ${res}


3 Disable Restaurant
    ${res}=    PUT On Session    foodie    url=/api/v1/restaurants/1/disable
    Status Should Be    200    ${res}


4 View Restaurant Profile
    ${res}=    GET On Session    foodie    url=/api/v1/restaurants/1
    Status Should Be    200    ${res}



#  DISH MODULE (5–8)
# -------------------------------------------------------------

5 Add Dish
    ${headers}=    Create Dictionary    Content-Type=application/json
    ${body}=       Set Variable    {"name":"Pizza","price":200}

    ${res}=    POST On Session    foodie    url=/api/v1/restaurants/1/dishes
    ...    data=${body}
    ...    headers=${headers}

    Status Should Be    201    ${res}


6 Update Dish
    ${headers}=    Create Dictionary    Content-Type=application/json
    ${body}=       Set Variable    {"price":250}

    ${res}=    PUT On Session    foodie    url=/api/v1/dishes/1
    ...    data=${body}
    ...    headers=${headers}

    Status Should Be    200    ${res}


7 Enable Disable Dish
    ${headers}=    Create Dictionary    Content-Type=application/json
    ${body}=       Set Variable    {"enabled":false}

    ${res}=    PUT On Session    foodie    url=/api/v1/dishes/1/status
    ...    data=${body}
    ...    headers=${headers}

    Status Should Be    200    ${res}


8 Delete Dish
    ${res}=    DELETE On Session    foodie    url=/api/v1/dishes/1
    Status Should Be    200    ${res}



#   ADMIN MODULE (9–12)
# -----------------------------------------

9 Approve Restaurant
    ${res}=    PUT On Session    foodie    url=/api/v1/admin/restaurants/1/approve
    Status Should Be    200    ${res}


10 Admin Disable Restaurant
    ${res}=    PUT On Session    foodie    url=/api/v1/admin/restaurants/1/disable
    Status Should Be    200    ${res}


11 View Feedback
    ${res}=    GET On Session    foodie    url=/api/v1/admin/feedback
    Status Should Be    200    ${res}


12 View Order Status
    ${res}=    GET On Session    foodie    url=/api/v1/admin/orders
    Status Should Be    200    ${res}



#    USER/CUSTOMER MODULE (13–16)
# -----------------------------------------------------------

13 User Registration
    ${headers}=    Create Dictionary    Content-Type=application/json
    ${body}=       Set Variable    {"name":"Abhi","email":"abhi@gmail.com","password":"1234"}

    ${res}=    POST On Session    foodie    url=/api/v1/users/register
    ...    data=${body}
    ...    headers=${headers}

    Status Should Be    201    ${res}


14 Search Restaurants
    ${res}=    GET On Session    foodie    url=/api/v1/restaurants/search
    ...    params=name=Robot

    Status Should Be    200    ${res}


15 Place Order
    ${headers}=    Create Dictionary    Content-Type=application/json
    ${body}=       Set Variable    {"user_id":1,"restaurant_id":1,"dish":"Pizza"}

    ${res}=    POST On Session    foodie    url=/api/v1/orders
    ...    data=${body}
    ...    headers=${headers}

    Status Should Be    201    ${res}


16 Give Rating
    ${headers}=    Create Dictionary    Content-Type=application/json
    ${body}=       Set Variable    {"order_id":1,"rating":5,"comment":"Excellent Taste"}

    ${res}=    POST On Session    foodie    url=/api/v1/ratings
    ...    data=${body}
    ...    headers=${headers}

    Status Should Be    201    ${res}



#  ORDER MODULE (17–18)
# -------------------------------------------------------------

17 View Orders By Restaurant
    ${res}=    GET On Session    foodie    url=/api/v1/restaurants/1/orders
    Status Should Be    200    ${res}


18 View Orders By User
    ${res}=    GET On Session    foodie    url=/api/v1/users/1/orders
    Status Should Be    200    ${res}
