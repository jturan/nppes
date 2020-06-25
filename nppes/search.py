import argparse
import requests
import pandas as pd

# create parser
nppes_parser = argparse.ArgumentParser(description='search the NPPES file from your terminal')

# add optional arguments to the parser
nppes_parser.add_argument('--number', help="a healthcare provider's National Provider Identifier")
nppes_parser.add_argument('--enumeration_type', choices=range(1,2), help="1: people, 2: places")
nppes_parser.add_argument('--taxonomy_description', help='exact description or exact specialty')
nppes_parser.add_argument('--first_name', help="a healthcare provider's first name")
nppes_parser.add_argument('--last_name', help="a healthcare provider's last name")
nppes_parser.add_argument('--organization_name', help="a healthcare organization's name")
nppes_parser.add_argument('--address_purpose', help='options: location, mailing, primary, secondary')
nppes_parser.add_argument('--city', help='the city a healthcare provider is located in')
nppes_parser.add_argument('--postal_code', help='the zip code a healthcare provider is located in')
nppes_parser.add_argument('--limit', help='limit results, default is 10 and max is 200')

# parse args into a dict
nppes_args = nppes_parser.parse_args()
nppes_args_dict = vars(nppes_args)

# create search function
def search_nppes_api(args: dict) -> dict:
    '''
    Uses arguments from the NPPES CLI to search the NPPES API

    :param args: a dictionary of arguments from the CLI
    '''
    print('getting data from NPPES API...')
    
    nppes_api_endpoint = 'https://npiregistry.cms.hhs.gov/api/?version=2.1'
    r = requests.get(nppes_api_endpoint, params=args)
    
    nppes_result_json = r.json()
    nppes_result_df = pd.json_normalize(nppes_result_json['results'])
    
    print(nppes_result_json)

# run search_nppes_api function
search_nppes_api(nppes_args_dict)