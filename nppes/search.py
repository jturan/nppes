import argparse
import requests 

# create parser
parser = argparse.ArgumentParser(description='Search the NPPES.')

# add optional arguments to the parser
parser.add_argument('--npi', help="a healthcare provider's National Provider Identifier")
parser.add_argument('--enumeration_type', help="1: people, 2: places")
parser.add_argument('--taxonomy', help='exact description or exact specialty')
parser.add_argument('--first_name', help="a healthcare provider's first name")
parser.add_argument('--last_name', help="a healthcare provider's last name")
parser.add_argument('--organization_name', help="a healthcare organization's name")
parser.add_argument('--address_purpose', help='options: location, mailing, primary, secondary')
parser.add_argument('--city', help='the city a healthcare provider is located in')
parser.add_argument('--postal_code', help='the zip code a healthcare provider is located in')
parser.add_argument('--limit', help='limit results, default is 10 and max is 200')

# parse args into a dict
args = parser.parse_args()
args_dict = vars(args)

