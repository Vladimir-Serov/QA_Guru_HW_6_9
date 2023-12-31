import pytest
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
import allure
from allure_commons.types import Severity


@allure.label("owner", "v_serov")
@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.story('Test  selene')


@pytest.fixture()
def browser_setup():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()


def test_github(browser_setup):
    browser.open('https://github.com')

    s('.header-search-button').click()
    s('#query-builder-test').type('eroshenkoam/allure-example').press_enter()
    s(by.link_text('eroshenkoam/allure-example')).click()
    s('#issues-tab').click()
    s(by.partial_text('#76')).should(be.visible)
