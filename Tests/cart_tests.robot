*** Settings ***
Library    SeleniumLibrary
Library    ../Resources/Libraries/CommonKeywords.py
Library    ../listeners/ScreenshotListener.py
Suite Setup    Open Browser And Login   ${USER_NAME}    ${USER_PASS}   ${BROWSER}
Suite Teardown    CommonKeywords.Close Browser



*** Variables ***
${BROWSER}    chrome
${USER_NAME}    admin
${USER_PASS}    admin

*** Test Cases ***
Add Monitor To Cart
    [Tags]    Functional
    ${max_price}    ${max_title}=   Get Most Expensive Monitor
    ${actual_name}=    Get Name Price At Product Page
    Should Be Equal    ${actual_name}    ${max_title}    case_insensitive=True
    Add Product To Cart
    ${cart_products}=   Get Products At Cart
    ${product_exists}=    Evaluate    """('${max_title}', ${max_price}) in ${cart_products}"""
    Should Be True    ${product_exists}    Product ${max_title} with price ${max_price} is not in cart.
