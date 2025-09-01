import time

from selene import browser, have, by, be


class OpenBrowser:
    def open_page(self):
        browser.open('https://www.wildberries.ru')
        time.sleep(3)

class HeaderPage:

    def address(self):

        time.sleep(3)

        browser.element('.simple-menu__link--address').click()

        browser.element('.map-search__input').type('село Малокурильское, Улица Гренада 14')

        time.sleep(3)

        browser.element(by.text('Найти')).with_(timeout=5).click()

        browser.all('.address-item.j-poo-option').element_by(have.text('село Малокурильское, Улица Гренада 14')).with_(timeout=5).click()

        browser.element(by.text('Заберу отсюда')).click()


    def order(self):
        browser.element('[href="/lk/basket"]').click()
        browser.element('[name="ConfirmOrderByRegisteredUser"]').click()
        time.sleep(3)

class MainPage:
    
    def card(self):
        browser.element('.product-card__order-wrap').click()
        browser.element('.navbar-pc__notify').should(have.text('1'))

    def panel_search(self):
        browser.element('#searchInput').type('Oil').with_(timeout=3).press_enter()


    def button_sales(self):
        browser.element('.btn-switch__btn').click()
        time.sleep(5)