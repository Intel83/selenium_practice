*** Settings ***
Library    RequestsLibrary
Variables     ./../Resources/json_api_variables.py

*** Test Cases ***
Send a GET request
    [Documentation]    This test case sends a GET request to the specified API endpoint and verifies the response.
    [Tags]    api    smoke
    Create Session    my_api    ${TARGET_URL}
    ${response}=    GET On Session    my_api    ${TARGET_ENDPOINT}
    Log    Response: ${response.json()}
    Validate Response Body    ${response}

*** Keywords ***
Validate Response Body
    [Documentation]    Validates the response body for the expected status code and content.
    [Arguments]    ${response}
    Should Be Equal As Numbers    ${response.status_code}    ${EXPECTED_STATUS_CODE}
    Should Contain                ${response.text}           ${EXPECTED TEXT}
    Should Not Be Empty           ${response.json().get('title')}