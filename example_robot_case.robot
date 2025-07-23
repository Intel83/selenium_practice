*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${LOGIN_URL}           https://the-internet.herokuapp.com/login
${BAD_USERNAME}        testuser
${BAD_PASSWORD}        wrongpass
${USERNAME}            tomsmith
${PASSWORD}            SuperSecretPassword!

*** Test Cases ***
Invalid Login Should Show Error
    [Setup]    Open Browser To Login Page
    Enter Invalid Credentials
    Submit Login Form
    Verify Login Error
    [Teardown]    Close Browser

Valid Login Should Succeed
    [Setup]    Open Browser To Login Page
    Enter Valid Credentials
    Submit Login Form
    Verify Login Success
    [Teardown]    Close Browser

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN_URL}    chrome
    Maximize Browser Window
    [Documentation]    Open the login page in a Chrome browser and maximize the window.

Enter Invalid Credentials
    Input Text    id=username    ${BAD_USERNAME}
    Input Text    id=password    ${BAD_PASSWORD}
    [Documentation]    Enter invalid username and password into the login form.

Enter Valid Credentials
    Input Text    id=username    ${USERNAME}
    Input Text    id=password    ${PASSWORD}
    [Documentation]    Enter valid username and password into the login form.

Submit Login Form
    Click Button    css=.radius
    [Documentation]    Click the login button to submit the form.

Verify Login Error
    Wait Until Page Contains Element    id=flash
    Element Should Contain              id=flash    Your username is invalid!
    [Documentation]                     Verify that the error message is displayed correctly after an invalid login attempt.

Verify Login Success
    Wait Until Page Contains Element    id=flash
    Element Should Contain              id=flash    You logged into a secure area!
    [Documentation]                     Verify that the success message is displayed correctly after a valid login attempt.