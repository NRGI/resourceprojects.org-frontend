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


class TestIndexPage:
    @pytest.fixture(autouse=True, scope='module')
    def load_index_page(self, browser):
        browser.get(server_url)

    @pytest.mark.parametrize(('nav_item'), [
        ('About'),
        ('Projects'),
        ('Countries'),
        ('Companies'),
        ('Data sources')
        ])
    def test_main_nav(self, browser, nav_item):
        assert nav_item in browser.find_element_by_css_selector('.nav-collapse').text

    def test_index_page(self, browser):
        assert "Natural Resource Governance Institute" in browser.title
        assert 'ResourceProjects.org' in browser.find_element_by_tag_name('body').text


#List pages - Countries, Projects, Companies, Company Groups


def test_countries_page(browser):
    '''Countries list'''
    #Table headers
    expected_headers = set([
        ('Country'),
        ('No. Projects'),
        ('Oil and Gas'),
        ('Mining')
    ])
    browser.get(server_url + 'country')
    #assert "Natural Resource Governance Institute" in browser.title
    table_headers = browser.find_elements_by_tag_name('th')
    table_headers_text = set([ x.text for x in table_headers ])
    assert expected_headers == table_headers_text
    #Page title
    assert 'Countries' in browser.find_element_by_tag_name('h1').text


def test_projects_page(browser):
    '''Projects List page'''
    #Table headers
    expected_headers = set([
        ('Project'),
        ('Country'),
        ('Commodity Types'),
        ('No.Companies')
    ])
    browser.get(server_url + 'project')
    #assert "Natural Resource Governance Institute" in browser.title
    table_headers = browser.find_elements_by_tag_name('th')
    table_headers_text = set([ x.text for x in table_headers ])
    assert expected_headers == table_headers_text
    #Page title
    assert 'Projects' in browser.find_element_by_tag_name('h1').text


def test_companies_page(browser):
    '''Companies List page'''
    #Table headers
    expected_headers = set([
        ('Company'),
        ('Group'),
        ('No. Projects')
    ])
    browser.get(server_url + 'company')
    #assert "Natural Resource Governance Institute" in browser.title
    table_headers = browser.find_elements_by_tag_name('th')
    table_headers_text = set([ x.text for x in table_headers ])
    assert expected_headers == table_headers_text
    #Page title
    assert 'Companies' in browser.find_element_by_tag_name('h1').text
    assert 'Switch to Company Groups view' in browser.find_element_by_tag_name('button').text


def test_company_groups_page(browser):
    '''Company Groups List page'''
    #Table headers
    expected_headers = set([
        ('Name'),
        ('No. Companies'),
        ('No. Projects')
    ])
    browser.get(server_url + 'group')
    #assert "Natural Resource Governance Institute" in browser.title
    table_headers = browser.find_elements_by_tag_name('th')
    table_headers_text = set([ x.text for x in table_headers ])
    assert expected_headers == table_headers_text
    #Page title
    assert 'Company Groups' in browser.find_element_by_tag_name('h1').text
    assert 'Switch to Companies view' in browser.find_element_by_tag_name('button').text
    
    
## Idividual pages tests

def test_country_page(browser):
    '''Country page table titles'''
    expected_titles = set([
        ('Projects'),
        ('Companies Companies active in this country'),
        ('Payments')
    ])
    browser.get(server_url + 'country/AO')
    titles = []
    #assert "Natural Resource Governance Institute" in browser.title
    section_titles = browser.find_elements_by_tag_name('h2')
    section_titles_text = set([ x.text for x in section_titles ])
    assert expected_titles == section_titles_text
    

class TestCompanyPage:
    @pytest.fixture(autouse=True, scope='module')
    def load_company_page(self, browser):
        browser.get(server_url + 'company/140af236fafe23da')

    def test_company_page(self, browser):
        '''Company page table titles'''
        expected_titles = set([
            ('Company Info'),
            ('Projects'),
            ('Payments')
        ])
        titles = []
        #assert "Natural Resource Governance Institute" in browser.title
        section_titles = browser.find_elements_by_tag_name('h2')
        section_titles_text = set([ x.text for x in section_titles ])
        assert expected_titles == section_titles_text


    def test_company_page_table_columns (self, browser):
        '''Table in the company page'''
        expected_headers = set([
            #Project Table
            ('Name'),
            ('Country'),
            ('Commodity Type')
        ])
        table_headers = browser.find_elements_by_tag_name('th')
        table_headers_text = set([ x.text for x in table_headers ])
        assert expected_headers <= table_headers_text


def test_table_columns (browser):
    '''Table in the projects page'''
    expected_headers = set([
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
    browser.get(server_url + 'project/ao/bl40-ptvrql')
    table_headers = browser.find_elements_by_tag_name('th')
    table_headers_text = set([ x.text for x in table_headers ])
    assert expected_headers <= table_headers_text
