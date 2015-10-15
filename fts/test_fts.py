import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


server_url = os.environ.get('SERVER_URL', 'http://127.0.0.2/')


@pytest.fixture(scope="module")
def browser(request):
    browser = webdriver.Firefox()
    browser.implicitly_wait(3)
    request.addfinalizer(lambda: browser.quit())
    return browser


def test_main_nav(browser):
    browser.get(server_url)
    navigation = ['About','Projects','Countries','Companies','Data sources']
    found_navigation_items = browser.find_element_by_css_selector('.nav-collapse').text
    for nav_item in navigation:
        assert nav_item in found_navigation_items


def test_index_page(browser):
    browser.get(server_url)
    assert "Natural Resource Governance Institute" in browser.title
    assert 'ResourceProjects.org' in browser.find_element_by_tag_name('body').text


@pytest.mark.parametrize(('heading'), [
    ('Projects'),
    ('Companies Companies active in this country')
    ])
def test_country_page(browser,heading):
    browser.get(server_url + 'country/AO')
    titles = []
    #assert "Natural Resource Governance Institute" in browser.title
    section_titles = browser.find_elements_by_tag_name('h2')
    for h2 in section_titles:
        titles.append(h2.text)
    #assert 'Projects' in titles
    assert heading in titles
