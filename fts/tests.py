import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def browser(request):
    browser = webdriver.Firefox()
    browser.implicitly_wait(3)
    request.addfinalizer(lambda: browser.quit())
    return browser


@pytest.fixture(scope="module")
def server_url():
    return "http://127.0.0.2/"




   
@pytest.mark.parametrize(('nav_item'), [
    ('About'),
    ('Projects'),
    ('Countries'),
    ('Companies'),
    ('Data sources')
    ])
def test_main_nav(server_url,browser,nav_item):
    browser.get(server_url)
    assert nav_item in browser.find_element_by_css_selector('.nav-collapse').text


def test_index_page(server_url,browser):
    browser.get(server_url)
    assert "Natural Resource Governance Institute" in browser.title
    assert 'ResourceProjects.org' in browser.find_element_by_tag_name('body').text
    '''
    href = browser.find_element_by_xpath("//*[@id='post-17']/div[1]/div/div[3]/p[1]/a[1]")
    href = href.get_attribute("href")
    assert "http://www.threesixtygiving.org/get-involved/publish-your-data/" in href
    '''
    

@pytest.mark.parametrize(('heading'), [
    ('Projects'),
    ('Companies Companies active in this country'),
    ('Payments'),
    ])
def test_country_page(server_url,browser,heading):
    browser.get(server_url + 'country/dz.html')
    titles = []
    #assert "Natural Resource Governance Institute" in browser.title
    section_titles = browser.find_elements_by_tag_name('h2')
    for h2 in section_titles:
        titles.append(h2.text)
    #assert 'Projects' in titles
    assert heading in titles
    
    
    '''
    href = browser.find_element_by_xpath("//*[@id='post-17']/div[1]/div/div[3]/p[1]/a[1]")
    href = href.get_attribute("href")
    assert "http://www.threesixtygiving.org/get-involved/publish-your-data/" in href
    '''
    
'''
def test_identifiers_page(server_url,browser):
    browser.get(server_url + 'standard/identifiers/')
    assert '360Giving' in browser.find_element_by_tag_name('body').text
    assert '360 Giving' not in browser.find_element_by_tag_name('body').text


def test_cove_link(server_url,browser):
  browser.get(server_url + 'standard/reference/')
  href = browser.find_element_by_xpath("//*[@id='post-35']/div[1]/p[6]/a")
  href = href.get_attribute("href")
  assert "http://cove.opendataservices.coop/360/" in href
  
  
@pytest.mark.parametrize(('logo'), [
    ('heritage-lottery-fund'),
    ('heritage-lottery-fund.jpg'),
    ('arts-council-england.JPG'),
    ('arts-council-northern-ireland.jpg'),
    ('arts-council-wales.jpg'),
    ('department-social-development-northern-ireland.jpg'),
    ('sport-england.jpg'),
    ('wellcome-trust.jpg')
    ])
def test_index_page_logos(server_url,browser,logo):
  browser.get(server_url)
  src = []
  imgs = browser.find_elements_by_tag_name('img')
  for img in imgs:
    src.append(img.get_attribute('src'))
  path = "http://opendataservic.wpengine.com/wp-content/themes/responsive-child/ckan/logos/"
  string = path + logo
  assert string not in src
'''
