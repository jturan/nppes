import requests
import click
import json
from pygments import highlight, lexers, formatters

def format_json_response(json_data):
    formatted_json = json.dumps(json_data, sort_keys=True, indent=4)
    highlighted_json = highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
    return highlighted_json

@click.command()
@click.option('--number', help="a healthcare provider's National Provider Identifier")
@click.option('--enumeration_type', help="1: people, 2: places")
@click.option('--taxonomy_description', help='exact description or exact specialty')
@click.option('--first_name', help="a healthcare provider's first name")
@click.option('--last_name', help="a healthcare provider's last name")
@click.option('--organization_name', help="a healthcare organization's name")
@click.option('--address_purpose', help='options: location, mailing, primary, secondary')
@click.option('--city', help='the city a healthcare provider is located in')
@click.option('--state', help='the state a healthcare provider is located in')
@click.option('--postal_code', help='the zip code a healthcare provider is located in')
@click.option('--limit', help='limit results, default is 10 and max is 200')
def search_nppes_api(number, enumeration_type, taxonomy_description, first_name, last_name, organization_name, address_purpose, city, state, postal_code, limit):
    click.echo(click.style('searching the NPPES API...🔦', fg='blue'))
    nppes_api_url = 'https://npiregistry.cms.hhs.gov/api/?version=2.1'
    query_params = {
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
    r = requests.get(nppes_api_url, params=query_params)
    json_data = r.json()
    formatted_json_data = format_json_response(json_data)
    click.echo(formatted_json_data)

if __name__ == '__main__':
    search_nppes_api()