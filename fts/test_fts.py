# This Python file uses the following encoding: utf-8
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
        ('Commodities'),
        ('Sources'),
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
    # All 'count' cells have css class="count"
    # This works while we only have one country in our fixtures
    assert '15' in browser.find_element_by_css_selector('.count').text


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
    ## NB These rows will change if more, or less, fixture data is used
    assert 'Angola' in rows[23].text
    assert 'Block 0 A' in rows[23].text
    assert 'Oil and Gas' in rows[23].text
    assert '4' in rows[23].text
    
    #Test link to map page exists
    assert 'Projects Map' in browser.find_element_by_css_selector('.page-header').text
    #could add a click through to see if we get to /map


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


def test_commodities_page(browser):
    '''Commodities List page'''
    #Table headers
    expected_headers = set([
        ('Name'),
        ('No. Projects')
    ])
    browser.get(server_url + 'commodity')
    #assert "Natural Resource Governance Institute" in browser.title
    table_headers = browser.find_elements_by_tag_name('th')
    table_headers_text = set([ x.text for x in table_headers ])
    assert expected_headers == table_headers_text
    #Page title
    assert 'Commodities' in browser.find_element_by_tag_name('h1').text

    #Test data in first row matches text data from our fixture
    table = browser.find_element_by_id('commodities')
    rows = table.find_elements_by_tag_name('tr')
    assert 'Bauxite' in rows[1].text
    assert '2' in rows[1].text


def test_sources_page(browser):
    '''Sources List page'''
    #Table headers
    expected_headers = set([
        ('Source'),
        ('Source type'),
        ('Source date'),
        ('Details')
    ])
    browser.get(server_url + 'source')
    #assert "Natural Resource Governance Institute" in browser.title
    table_headers = browser.find_elements_by_tag_name('th')
    table_headers_text = set([ x.text for x in table_headers ])
    assert expected_headers == table_headers_text
    #Page title
    assert 'Sources' in browser.find_element_by_tag_name('h1').text

    #Test data in first row matches text data from our fixture
    table = browser.find_element_by_tag_name('table')
    rows = table.find_elements_by_tag_name('tr')
    ## NB These rows will change if more, or less, fixture data is used
    assert 'Hudbay Minerals' in rows[9].text
    assert 'Company database' in rows[9].text
    assert '2015-04-30' in rows[9].text
    assert '1970-01-01' not in table.text

    
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
        ('.payments', ['Year', 'Project', 'Paid by', 'Payment Type', 'Currency', 'Value', 'Payment or receipt?', 'ID']),
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
        assert len(rows) == 16
    
    def test_download_links (self, browser):
        expected_download_text = set([
            ('Download: Payments CSV'),
            ('Download: Companies CSV'),
            ('Download: Projects CSV')
        ])
        downloads = browser.find_elements_by_css_selector('.download')
        download_text = set([ x.text for x in downloads ])
        assert expected_download_text == download_text

    @pytest.mark.parametrize(('expected_headers'), [
        ('Status'),
        ('Company Group'),
        ('Commodity')
    ])
    def test_filters_are_gone (self, browser, expected_headers):
        assert expected_headers not in browser.find_element_by_tag_name('h4').text

    
class TestCompanyPage:
    @pytest.fixture(autouse=True, scope='module')
    def load_company_page(self, browser):
        browser.get(server_url + 'company/3ba56569aac5dcc3'), #Mineracao Paragominas SA

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
    '''
    def test_empty_payments_table (self, browser):
        assert 'No data available' in browser.find_element_by_css_selector('.no-data').text
    '''
    def test_company_info_table (self, browser):
        '''Company Info'''
        expected_cells= set([
            ('Our Company ID:'),
            ('Website:'),
            ('Country:'),
            ('Part of:'),
            ('Open Corporates:')
        ])
        table_cells = browser.find_elements_by_css_selector('.project-label')
        table_cells_text =  set([ x.text for x in table_cells ])
        assert table_cells_text >= expected_cells # >= because Location(s) and a table should also be in found data

        
class TestCompanyPage2:
    @pytest.fixture(autouse=True, scope='module')
    def load_company_page(self, browser):
        browser.get(server_url + 'company/2a71986494d44606') #Compania Minera Ares Hochschild Mining
    
    @pytest.mark.parametrize('linkText', [
        ('Peru'),
        ('Hochschild Mining'),
    ])
    def test_company_info_table (self, browser, linkText):
        '''Company Info'''
        table = browser.find_element_by_css_selector('#project-info')
        assert linkText in table.text
        
    def test_download_links (self, browser):
        expected_download_text = set([
            #('Download: Payments CSV'),
            ('Download: Projects CSV')
        ])
        downloads = browser.find_elements_by_css_selector('.download')
        download_text = set([ x.text for x in downloads ])
        assert expected_download_text == download_text
        
        
# Various company page data tests
def test_empty_payments_table (browser):
      browser.get(server_url + 'company/5b682b0b720c3597')
      assert 'No data available' in browser.find_element_by_css_selector('.no-data').text
      
def test_website_link (browser):
      browser.get(server_url + 'company/2fe073c29814ab6d')
      assert 'http://peruvianpmc.com/corporate/about/' in browser.find_element_by_css_selector('.info-box').text

def test_open_corporates_link (browser):
      browser.get(server_url + 'company/b6e57c43738d9979')
      assert 'https://opencorporates.com/companies/je/EXTUID_266101' in browser.find_element_by_css_selector('.info-box').text
      

class TestProjectPage:
    @pytest.fixture(autouse=True, scope='module')
    def load_project_page(self, browser):
        browser.get(server_url + 'project/AO/bl0-c9kv88')

    @pytest.mark.parametrize(('table_css', 'expected_headers'), [
        ('.companies', ['Name', 'Group']),
        ('.production_stats', ['Year', 'Volume', 'Unit', 'Commodity', 'Price', 'Price per unit', 'ID']),
        ('.locations', ['Name', 'Lat', 'Lng']),
        ('.payments', ['Year','Paid by', 'Paid to', 'Payment Type', 'Currency', 'Value', 'Payment or receipt?', 'ID']),
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
        
    def test_download_links (self, browser):
        expected_download_text = set([
            ('Download: Payments CSV'),
            ('Download: Companies CSV'),
            ('Download: Production Stats CSV')
        ])
        downloads = browser.find_elements_by_css_selector('.download')
        download_text = set([ x.text for x in downloads ])
        assert expected_download_text == download_text
        
    def test_production_stats_table (self, browser): 
        table = browser.find_element_by_css_selector('.production_stats')
        assert 'Oil' in table.text
        # Add test to check no duplicates in table NB There are no duplicates in the test fixtures at the moment, but there are in live data!
        rows = table.find_elements_by_tag_name('tr')
        assert len(rows) == 7


class TestProjectPage2:
    @pytest.fixture(autouse=True, scope='module')
    def load_project_page(self, browser):
        browser.get(server_url + 'project/PE/anim-oy3zxa') # Animon

    @pytest.mark.parametrize(('css', 'expected_text'), [
        ('.commodity-types', 'Mining,'),
        ('.commodities', 'Copper, Lead, Silver, Zinc,'),
        ('.status', 'Production (True at: 2014-01-01)'),
    ])
    def test_no_duplicates (self, browser, css, expected_text):
        '''CommodityTypes, Commodities and Status in project info box'''
        found_text = browser.find_element_by_css_selector(css).text
        assert found_text == expected_text
    
    @pytest.mark.parametrize(('css', 'expected_no_rows'), [
        ('.companies', 2),
        ('.production_stats', 5),
        #('.payments', 10),
    ])
    def test_table_rows (self, browser, css, expected_no_rows):
        '''Counts the number of expected rows'''
        table = browser.find_element_by_css_selector(css)
        rows = table.find_elements_by_tag_name('tr')
        assert len(rows) == expected_no_rows
        

class TestProjectPage3:
    @pytest.fixture(autouse=True, scope='module')
    def load_project_page(self, browser):
        browser.get(server_url + '/project/PH/apma-l9nepr') # Apex Maco
    
    def test_payments_table_payer (self, browser):
        '''Checks the payer name is shown'''
        table = browser.find_element_by_css_selector('.payments')
        rows = table.find_elements_by_tag_name('tr')
        rows.pop(0)  #removes the first row of tabkle headers
        for row in rows:
            assert 'Apex Mining Company Inc.' in row.text
            
    # https://github.com/NRGI/resourceprojects.org-frontend/issues/259
    def test_payments_table_gov_receipt (self, browser):
        '''Checks that if GovernmentRecipt then paid to is not Philippines'''
        table = browser.find_element_by_css_selector('.payments')
        rows = table.find_elements_by_tag_name('tr')
        rows.pop(0)  #removes the first row of tabkle headers
        for row in rows:
            if 'GovernmentReceipt' in row.text:
                assert 'Philippines' not in row.text

        

class TestCompanyGroupPage:
    @pytest.fixture(autouse=True, scope='module')
    def load_project_page(self, browser):
        browser.get(server_url + 'group/bp-3067') #BP

    @pytest.mark.parametrize(('css', 'expected_no_rows'), [
        ('.companies', 2),
        ('.projects', 5),
        #('.payments', 10),
    ])
    def test_company_table_rows (self, browser, css, expected_no_rows):
        '''Counts the number of expected rows'''
        table = browser.find_element_by_css_selector(css)
        rows = table.find_elements_by_tag_name('tr')
        assert len(rows) == expected_no_rows

    def test_project_info_table (self, browser):
        '''Group Info'''
        expected_cells= set([
            ('Our Company Group ID:'),
        ])
        table_cells = browser.find_elements_by_css_selector('.project-label')
        table_cells_text =  set([ x.text for x in table_cells ])
        assert table_cells_text == expected_cells 
    
    #NB BP only has no data in this table with current test fixture data
    def test_empty_payments_table (self, browser):
        assert 'No data available' in browser.find_element_by_css_selector('.no-data').text
        
    def test_download_links (self, browser):
        expected_download_text = set([
            #('Download: Payments CSV'), # Not in this company group as it has no payments!
            ('Download: Companies CSV'),
            ('Download: Projects CSV') 
        ])
        downloads = browser.find_elements_by_css_selector('.download')
        download_text = set([ x.text for x in downloads ])
        assert expected_download_text == download_text


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


class TestMapPage:
    @pytest.fixture(autouse=True, scope='module')
    def load_project_page(self, browser):
        browser.get(server_url + 'map')
    
    def test_page_title (self, browser):
        assert 'Projects Map' in browser.find_element_by_tag_name('h1').text
    
    #def test_map_present (self, browser):
    #    browser.find_elements_by_css_selector('.leaflet-map-pane')


#Test Global Tables
@pytest.mark.parametrize(('page'), [
    ('company/3ba56569aac5dcc3'), #Mineracao Paragominas SA
    ('project/BR/para-s4sbrx'), #Paragominas
    ('country/AO'), #Angola
])
def test_payments_table (browser, page):
    browser.get(server_url + page)
    assert 'Taxes levied on the income, production or profits of companies,' not in browser.find_element_by_css_selector('.payments').text


class TestCommodityPage:
    @pytest.fixture(autouse=True, scope='module')
    def load_project_page(self, browser):
        browser.get(server_url + '/commodity/Copper')

    @pytest.mark.parametrize(('table_css', 'expected_headers'), [
        ('.companies', ['Name', 'Group']),
        ('.projects', ['Name', 'Country']),
    ])
    def test_table_columns (self, browser, table_css, expected_headers):
        '''Tables in the commodity page'''
        table = browser.find_element_by_css_selector(table_css)
        table_headers = table.find_elements_by_tag_name('th')
        table_headers_text = [ x.text for x in table_headers ]
        assert table_headers_text == expected_headers
        


@pytest.mark.parametrize(('path', 'dates'), [
    ('/source/EIACountryAnalysisBriefAngola-60hgg2', ['', '2015-08-09']),  # EIA Country Analysis Brief: Angola
    ('/source/ExportaeseReceitasdePetrleo2014-udikid', ['2015-01-01', '2015-07-31']),  # Exportações e Receitas de Petróleo 2014
    ])

def test_source_dates (browser, path, dates): 
    browser.get(server_url + path)
    table = browser.find_element_by_tag_name('table')
    rows = table.find_elements_by_tag_name('tr')
    assert dates[0] in rows[2].text
    assert dates[1] in rows[3].text
