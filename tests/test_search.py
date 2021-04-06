from nppes import __version__
import click.testing
import pytest
from nppes.search import search_nppes_api


def test_version():
    assert __version__ == '0.1.3'

@pytest.fixture
def runner():
    return click.testing.CliRunner()

def test_search_nppes_api(runner, mock_requests_get):
    result = runner.invoke(search_nppes_api)
    assert result.exit_code == 0

@pytest.fixture
def mock_requests_get(mocker):
    mock = mocker.patch("requests.get")
    mock.return_value.json.return_value = {
        "id": 1,
        "name": "Stephen King",
        "username": "kingofhorror"
    }
    return mock