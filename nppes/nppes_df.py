import requests
import pandas as pd
import numpy as np
from functools import reduce

def get_nppes_data(**kwargs: str) -> dict:
    '''
    Searches the NPPES API based on various fields and returns response in json format
    
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
    search_params = locals()['kwargs']
    
    user_defined_search_params = list(search_params.keys())
    allowed_search_params = ['number', 'enumeration_type', 'taxonomy_description', 'first_name', 'last_name', 'organization_name', 'address_purpose', 'city', 'state', 'postal_code', 'limit']
    disallowed_search_params = np.setdiff1d(user_defined_search_params, allowed_search_params)
    
    if len(disallowed_search_params) > 0:
        print('Ensure your search parameters are valid. Invalid search params: ', disallowed_search_params)

    else:
        print('Searching the NPPES API...🔦')
        nppes_api_url = 'https://npiregistry.cms.hhs.gov/api/?version=2.1'
        json_data = requests.get(nppes_api_url, params=search_params).json()
        return json_data

def json_data_to_df(json_data: dict) -> pd.DataFrame:
    '''
    Converts json data from the NPPES API into a DataFrame

    :param json_data: list of json data, returned by the NPPES API from the `get_nppes_data` function
    '''
    main_results_df = pd.json_normalize(json_data['results'])[['number', 'basic.name','basic.name_prefix', 'basic.first_name', 'basic.last_name', 'basic.middle_name', 'basic.credential', 'basic.gender']]
    addresses_df = pd.json_normalize(json_data['results'], 'addresses', 'number')
    taxonomies_df = pd.json_normalize(json_data['results'], 'taxonomies', 'number')

    dataframes_to_merge = [main_results_df, addresses_df, taxonomies_df]

    print('Complete.')
    return reduce(lambda left, right: pd.merge(left, right, on = ['number'],
                                        how = 'outer'), dataframes_to_merge)

        
def nppes_df(**kwargs: str) -> pd.DataFrame:
    '''
    Searches the NPPES API based on various fields and returns a DataFrame with the results
    
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
    json_data = get_nppes_data(**kwargs)
    
    return json_data_to_df(json_data)