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
        ('Data sources'),
        ('Glossary')
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
        #('Oil and Gas'),
        #('Mining')
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
    
    #Test data in first row matches text data from our fixture
    table = browser.find_element_by_id('projects')
    rows = table.find_elements_by_tag_name('tr')
    assert 'Angola' in rows[1].text
    assert 'Block 0 A' in rows[1].text
    assert 'Oil and Gas' in rows[1].text
    assert '4' in rows[1].text



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
class TestCountryPage:
    @pytest.fixture(autouse=True, scope='module')
    def load_company_page(self, browser):
        browser.get(server_url + 'country/AO')
    
    def test_country_page(self, browser):
        '''Country page table titles'''
        expected_titles = set([
            ('Projects'),
            ('Companies Companies active in this country'),
            ('Payments')
        ])
        titles = []
        #assert "Natural Resource Governance Institute" in browser.title
        section_titles = browser.find_elements_by_tag_name('h2')
        section_titles_text = set([ x.text for x in section_titles ])
        assert expected_titles == section_titles_text
    
    @pytest.mark.parametrize(('table_css', 'expected_headers'), [
        ('.companies', ['Name', 'Group']),
        ('.projects', ['Name', 'Commodity', 'Status', 'No. Companies' ]),
        ('.payments', ['Year','Paid by', 'Payment Type', 'Currency', 'Value', 'Payment or receipt?', 'ID']),
    ])
    def test_table_columns (self, browser, table_css, expected_headers):
        '''Tables in the countries page'''
        table = browser.find_element_by_css_selector(table_css)
        table_headers = table.find_elements_by_tag_name('th')
        table_headers_text = [ x.text for x in table_headers ]
        assert table_headers_text == expected_headers
        
    def test_project_table_rows (self, browser):
        '''Counts the number of expected rows'''
        table = browser.find_element_by_css_selector('.projects')
        rows = table.find_elements_by_tag_name('tr')
        assert len(rows) == 20
    
    @pytest.mark.parametrize(('downloadtext'), [
        ('Payments CSV'),
        ('Companies CSV'),
        ('Projects CSV')
    ])
    def test_download_links (self, browser, downloadtext):
        body = browser.find_element_by_tag_name('body')
        assert downloadtext in body.text

    

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
        
    def test_empty_payments_table (self, browser):
        assert 'No data available' in browser.find_element_by_css_selector('.no-data').text


class TestProjectPage:
    @pytest.fixture(autouse=True, scope='module')
    def load_project_page(self, browser):
        browser.get(server_url + 'project/AO/bl0-0q2anl')

    @pytest.mark.parametrize(('table_css', 'expected_headers'), [
        ('.companies', ['Name', 'Group']),
        ('.production_stats', ['Year', 'Volume', 'Unit', 'Commodity', 'Price', 'Price per unit', 'ID']),
        ('.locations', ['Name', 'Lat', 'Lng']),
        ('.payments', ['Year','Paid by', 'Paid to', 'Payment or receipt?', 'Payment Type', 'Currency', 'Value', 'ID']),
    ])
    def test_table_columns (self, browser, table_css, expected_headers):
        '''Tables in the projects page'''
        table = browser.find_element_by_css_selector(table_css)
        table_headers = table.find_elements_by_tag_name('th')
        table_headers_text = [ x.text for x in table_headers ]
        assert table_headers_text == expected_headers
    
    def test_company_table_rows (self, browser):
        '''Counts the number of expected rows'''
        table = browser.find_element_by_css_selector('.companies')
        rows = table.find_elements_by_tag_name('tr')
        assert len(rows) == 5
        
    def test_aliases (self, browser):
        assert 'BLOCO 0 A, Block 0- Area A offshore,' in browser.find_element_by_css_selector('.aliases').text
        
    def test_project_info_table (self, browser):
        '''Project Info'''
        expected_cells= set([
            ('Country:'),
            ('Aliases:'),
            ('Commodity Type(s):'),
            ('Commodities:'),
            ('Status:'),
            ('Associated Contracts:'),
            ('Associated Concessions:'),
            #('Location(s)') #This cell also contains a table, so this test is not good enough
        ])
        table_cells = browser.find_elements_by_css_selector('.project-label')
        table_cells_text =  set([ x.text for x in table_cells ])
        assert table_cells_text >= expected_cells # >= because Location(s) and a table should also be in found data


def test_glossary_page(browser):
    browser.get(server_url + 'glossary.html')
    assert "Glossary" in browser.find_element_by_tag_name('h1').text
    expected_headings= set([
            ('Projects and interrelated key concepts:'),
            ('Company attributes:'),
            ('Project attributes:'),
            ('Payment attributes:'),
            ('Useful sources:')
        ])
    headings = []
    section_titles = browser.find_elements_by_tag_name('h2')
    section_titles_text = set([ x.text for x in section_titles ])
    assert expected_headings == section_titles_text


class TestSitePage:
    @pytest.fixture(autouse=True, scope='module')
    def load_project_page(self, browser):
        browser.get(server_url + 'site/XX/mano-87nv9k')

    def test_table_rows (self, browser):
        '''Sites Info'''
        expected_cells= set([
            ('Country:'),
            ('Project:'),
            ('Notes:'),
            ('Co-ordinates (lat,lng):'),
            ('Commodity:')
        ])
        table_cells = browser.find_elements_by_css_selector('.project-label')
        table_cells_text =  set([ x.text for x in table_cells ])
        assert table_cells_text == expected_cells
