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


@pytest.mark.parametrize(('nav_item'), [
    ('About'),
    ('Projects'),
    ('Countries'),
    ('Companies'),
    ('Data sources')
    ])
def test_main_nav(browser,nav_item):
    browser.get(server_url)
    assert nav_item in browser.find_element_by_css_selector('.nav-collapse').text


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


# Table in the projects page
@pytest.mark.parametrize(('column_header'), [
    #Company Table
    ('Name'),
    ('Group'),
    #Production Stats
    ('Year'),
    ('Price'),
    ('Price per unit'),
    ('Unit'),
    ('Volume'),
    ('ID')
    ])
def test_table_columns (browser, column_header):
    browser.get(server_url + 'project/ao/bl40-ptvrql')
    headers = []
    table_headers = browser.find_elements_by_tag_name('th')
    for th in table_headers:
        headers.append(th.text)
    assert column_header in headers
