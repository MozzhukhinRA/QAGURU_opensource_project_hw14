import allure

from data.resource import HeaderPage, OpenBrowser, MainPage

open_browser = OpenBrowser()
search_address = HeaderPage()
product = MainPage()

@allure.feature('Taste case #1: Assert input address')
def test_address():

    allure.title('Open page and input address')
    with allure.step('Open Wildberries'):
        open_browser.open_page()
    with allure.step('Input address'):
        search_address.address()

@allure.feature('Taste case #2: Assert input address and add card')
def test_card():

     allure.title('Open page, input address + add to card')
     with allure.step('Input address'):
        test_address()
     with allure.step('Add to card'):
        product.card()

@allure.feature('Taste case #3: Assert input address and order product')
def test_bag():

    allure.title('Open page, input address + add to card')
    with allure.step('Input address'):
        test_address()
    with allure.step('Add to card'):
        product.card()
    with allure.step('Order product'):
        search_address.order()

@allure.feature('Taste case #4: Assert string of search')
def test_search():

    allure.title('Search')
    with allure.step('Search product'):
        open_browser.open_page()
        product.panel_search()

@allure.feature('Taste case #5: Assert active checkbox sales')
def test_sales():

    allure.title('Checkbox sales')
    with allure.step('Click checkbox'):
        open_browser.open_page()
        product.panel_search()
        product.button_sales()