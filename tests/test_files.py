import requests

import pytest

from nppes import files


@pytest.fixture
def url():
    """Fixture for getting a sample url."""
    return 'https://download.cms.gov/nppes/NPPES_Data_Dissemination_July_2020.zip'


def test_validate_url(url):
    """It validates a given url."""
    assert files.validate_url(url) == True
