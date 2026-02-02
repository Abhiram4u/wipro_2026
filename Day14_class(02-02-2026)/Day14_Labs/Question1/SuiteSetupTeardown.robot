*** Settings ***
Library    SeleniumLibrary

# Suite-level setup and teardown
Suite Setup       Suite Initialization
Suite Teardown    Suite Cleanup

# Test-level setup and teardown
Test Setup        Test Initialization
Test Teardown     Test Cleanup


*** Variables ***
${URL}      https://example.com
${BROWSER}  Chrome


*** Keywords ***
Suite Initialization
    Log    ===== SUITE SETUP: Test Suite Execution Started =====

Suite Cleanup
    Log    ===== SUITE TEARDOWN: Test Suite Execution Finished =====

Test Initialization
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

Test Cleanup
    Capture Page Screenshot
    Close Browser


*** Test Cases ***
Verify Example Page Title
    [Tags]    smoke    regression
    Title Should Be    Example Domain

Verify Page Contains Text
    [Tags]    sanity
    Page Should Contain    Example Domain
