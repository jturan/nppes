from nppes import __version__
import click.testing
import pytest
from nppes.search import search_nppes_api


def test_version():
    assert __version__ == '0.1.0'

@pytest.fixture
def runner():
    return click.testing.CliRunner()

def test_search_nppes_api(runner):
    result = runner.invoke(search_nppes_api, ['--last_name', 'Gomez'])
    assert result.exit_code == 0