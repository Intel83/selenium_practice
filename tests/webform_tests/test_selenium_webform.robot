*** Settings ***
Library         SeleniumLibrary
Test Setup      Open Browser To Form Page
Test Teardown   Close Browser

*** Variables ***
${URL}              https://www.selenium.dev/selenium/web/web-form.html
${TEXT_INPUT}       Marcin
${TEXT_AREA}        Weekend robot test
${DATE}             2025-08-01
${DROPDOWN_LABEL}   One
${EXPECTED_TEXT}    Form submitted

*** Test Cases ***
Submit Web Form
    [Documentation]     This test case fills out a web form and submits it.
    [Tags]              smoke positive webform selenium
    Fill Form           ${TEXT_INPUT}    ${TEXT_AREA}    ${DATE}    ${DROPDOWN_LABEL}
    Submit Form
    Wait Until Page Contains Text    ${EXPECTED_TEXT}
    Page Should Contain  ${EXPECTED_TEXT}

*** Keywords ***
Open Browser To Form Page
    [Documentation]    Opens the web form page in incognito mode using Chrome.
    ${options}=         Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys
    Call Method         ${options}  add_argument                                        --incognito
    Create WebDriver    Chrome      options=${options}
    Go To               ${URL}
    Wait Until Page Contains Element    xpath=//input[@id='my-text-id']    timeout=10s
    Maximize Browser Window

Wait Until Page Contains Text
    [Arguments]         ${text}
    [Documentation]     Waits until the page contains the specified text.
    Wait Until Page Contains    ${text}    timeout=10s

Fill Form
    [Documentation]    Fills out the web form with provided values.
    [Arguments]                 ${text_input}    ${text_area}    ${date}    ${dropdown_label}
    Input Text                  id:my-text-id       ${text_input}
    Input Text                  name:my-textarea  ${text_area}
    Input Text                  name:my-date      ${date}
    Select From List By Label   name:my-select  ${dropdown_label}

Submit Form
    [Documentation]    Submits the web form.
    Click Button                xpath=//button[contains(text(), 'Submit')]
