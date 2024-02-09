from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
from allure import step


def test_open_article_python(mobile_management_android):
    with step('Open article'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type(
            'Python'
        )

    with step('Verify article opened and valid'):
        result = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        result.should(have.size_greater_than(0))
        result.first.should(have.text('Python'))


def test_open_article_wiki(mobile_management_android):
    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Wiki')

    with step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Wiki'))