import requests
import click
import json
from pygments import highlight, lexers, formatters

def format_json_response_cli(json_data):
    formatted_json = json.dumps(json_data, sort_keys=True, indent=4)
    highlighted_json = highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
    return highlighted_json

@click.command()
@click.option('--number', help="a healthcare provider's National Provider Identifier")
@click.option('--enumeration_type', type=click.Choice(['NPI-1', 'NPI-2']), help="1: people, 2: places")
@click.option('--taxonomy_description', help='exact description or exact specialty')
@click.option('--first_name', help="a healthcare provider's first name")
@click.option('--last_name', help="a healthcare provider's last name")
@click.option('--organization_name', help="a healthcare organization's name")
@click.option('--address_purpose', type=click.Choice(['LOCATION', 'MAILING', 'PRIMARY', 'SECONDARY']), help='options: location, mailing, primary, secondary')
@click.option('--city', help='the city a healthcare provider is located in')
@click.option('--state', help='the state a healthcare provider is located in')
@click.option('--postal_code', help='the zip code a healthcare provider is located in')
@click.option('--limit', help='limit results, default is 10 and max is 200')
def search_nppes_api(number: int, enumeration_type: str, taxonomy_description: str, first_name: str, last_name: str, organization_name: str, address_purpose: str, city: str, state: str, postal_code: int, limit: int) -> str:
    '''
    Click command that creates a CLI where the end user can search the NPPES API with different fields

    :param number: a healthcare provider's National Provider Identifier
    :param enumeration_type: the type of healthcare provider, 1: people, 2: places
    :param taxonomy_description: exact description or exact specialty
    :param first_name: a healthcare provider's first name
    :param last_name: a healthcare provider's last name
    :param organization_name: a healthcare organization's name
    :param address_purpose: the type of address (location, mailing, primary, or specialty)
    :param city: the city a healthcare provider is located in
    :param state: the state a healthcare provider is located in
    :param postal_code: the zip code a healthcare provider is located in
    :param limit: limit results, default is 10 and max is 200
    '''
    click.echo(click.style('Searching the NPPES API...🔦', fg='blue'))
    nppes_api_url = 'https://npiregistry.cms.hhs.gov/api/?version=2.1'
    search_params = {
        'number': number,
        'enumeration_type': enumeration_type,
        'taxonomy_description': taxonomy_description,
        'first_name': first_name,
        'last_name': last_name,
        'organization_name': organization_name,
        'address_purpose': address_purpose,
        'city': city,
        'state': state,
        'postal_code': postal_code,
        'limit': limit 
    }
    json_data = requests.get(nppes_api_url, params=search_params).json()
    formatted_json_data = format_json_response_cli(json_data)
    click.echo(formatted_json_data)

def main():
    search_nppes_api()