*** Settings ***
Library         SeleniumLibrary
Suite Setup     Open Browser To Login Page
Suite Teardown  Close Browser
Test Teardown   Reset App State

*** Variables ***
${LOGIN_URL}           https://the-internet.herokuapp.com/login
${BAD_USERNAME}        testuser
${BAD_PASSWORD}        wrongpass
${USERNAME}            tomsmith
${PASSWORD}            SuperSecretPassword!

*** Test Cases ***
Valid Login Should Succeed
    [Tags]                  login   positive    smoke
    Submit Credentials      ${USERNAME}  ${PASSWORD}
    Verify Flash Message    You logged into a secure area!
    [Documentation]         Attempt to log in with valid credentials and verify the success message.

Invalid Login Should Show Error
    [Tags]                  login   negative    smoke
    Submit Credentials      ${BAD_USERNAME}  ${BAD_PASSWORD}
    Verify Flash Message    Your username is invalid!
    [Documentation]         Attempt to log in with invalid credentials and verify the error message.

Login With Empty Credentials Should Show Error
    [Tags]                  login   negative    smoke
    Click Button            css=.radius
    Verify Flash Message    Your username is invalid!
    [Documentation]         Attempt to log in with empty credentials and verify the error message.

*** Keywords ***
Open Browser To Login Page
    ${options}=         Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys
    Call Method         ${options}  add_argument                                        --incognito
    Create WebDriver    Chrome      options=${options}
    Go To               ${LOGIN_URL}
    Maximize Browser Window

Click Logout Link
    Click Link                      css=a.button.secondary.radius
    Wait Until Page Contains        Login Page
    [Documentation]                 Click the logout link and wait for the login page to load.

Reset App State
    Run Keyword And Ignore Error    Click Logout Link
    [Documentation]                 Reset the application state by clicking the logout link if logged in.

Submit Credentials
    [Arguments]         ${username}    ${password}
    Input Text          id=username    ${username}
    Input Text          id=password    ${password}
    Click Button        css=.radius
    [Documentation]     Fill in the login form with the provided username and password, then submit the form.

Verify Flash Message
    [Arguments]                         ${expected_message}
    Wait Until Page Contains Element    id=flash
    Element Should Contain              id=flash    ${expected_message}
    [Documentation]                     Verify that the flash message contains the expected text.
