*** Settings ***
Library         SeleniumLibrary
Suite Setup     Open Browser To Login Page
Suite Teardown  Close Browser

*** Variables ***
${LOGIN_URL}           https://the-internet.herokuapp.com/login
${BAD_USERNAME}        testuser
${BAD_PASSWORD}        wrongpass
${USERNAME}            tomsmith
${PASSWORD}            SuperSecretPassword!

*** Test Cases ***
Invalid Login Should Show Error
    [Tags]                  login   negative    smoke
    Submit Credentials      ${BAD_USERNAME}  ${BAD_PASSWORD}
    Verify Flash Message    Your username is invalid!
    [Documentation]         Attempt to log in with invalid credentials and verify the error message.

Valid Login Should Succeed
    [Tags]                  login   positive    smoke
    Submit Credentials      ${USERNAME}  ${PASSWORD}
    Verify Flash Message    You logged into a secure area!
    [Documentation]         Attempt to log in with valid credentials and verify the success message.

*** Keywords ***
Open Browser To Login Page
    Open Browser            ${LOGIN_URL}    chrome
    Maximize Browser Window
    [Documentation]         Open the login page in a Chrome browser and maximize the window.

Submit Credentials
    [Arguments]         ${username}    ${password}
    Input Text          id=username    ${username}
    Input Text          id=password    ${password}
    Click Button        css=.radius
    [Documentation]     Fill in the login form with the provided username and password, then submit the form.

Verify Flash Message
    [Arguments]    ${expected_message}
    Wait Until Page Contains Element    id=flash
    Element Should Contain              id=flash    ${expected_message}
    [Documentation]                     Verify that the flash message contains the expected text.
