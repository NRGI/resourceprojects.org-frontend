import requests
import pytest
from test_fts import server_url


@pytest.mark.parametrize('pagename', [
    '',
    'about.html',
    'project',
    'project/AO/bl0-0q2anl',
    'country',
    'country/AO',
    'company',
    'company/86d42aaadfcf8888',
    'source',
    'glossary.html'
])
def test_tags_closed(pagename):
    r = requests.get(server_url + pagename)
    assert r.text.count('<div') == r.text.count('</div')
