*** Settings ***
Library    SeleniumLibrary
Library    ../Resources/Libraries/CommonKeywords.py
Library    ../listeners/ScreenshotListener.py
Suite Setup    Open Browser And Signup   ${USER_NAME}    ${USER_PASS}   ${BROWSER}
Suite Teardown    CommonKeywords.Close Browser

*** Variables ***
${BROWSER}    chrome
${USER_NAME}    admin
${USER_PASS}    admin

*** Test Cases ***
Open Index Page and Log In
    Click Login
    Assert Login Textboxes
    Populate Login Popup Click      ${USER_NAME}    ${USER_PASS}
    ${actual_text}=  Get Welcome Text
    ${expected_text} =    Evaluate    "Welcome {}".format('${USER_NAME}')
    Should Be Equal    ${actual_text}    ${expected_text}    case_insensitive=True
