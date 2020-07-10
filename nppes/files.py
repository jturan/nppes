from zipfile import ZipFile

import requests

from .settings import DOWNLOADS_FOLDER


BASE_URL = 'https://download.cms.gov/nppes/'
BASE_FILE_NAME = 'NPPES_Data_Dissemination_'


def validate_url(url: str) -> bool:
    '''
    Validates if a url is valid and returns a status code of 200

    :param url: a web url
    '''
    r = requests.head(url)
    if r.status_code == 200:
        return True
    else:
        return False


def download_file(url: str, save_path: str, chunk_size: int = 128) -> None:
    '''
    Downloads a specific NPI file

    :param url: a web url
    :param save_path: location where file is downloaded
    :param chunk_size: the number of bytes read into memory
    '''
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        print("Downloading...")
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)
        print("Done!")


def unzip_file(file_name: str) -> None:
    '''
    Unzips a downloaded file
    :param file_name: name of file to be unzipped
    '''
    file_path = DOWNLOADS_FOLDER + file_name
    unzip_folder = file_path.replace('.zip', '')
    
    with ZipFile(file_path, 'r') as z:
        print("Directory:")
        z.printdir()
        print("\n")

        print("Unzipping...")
        z.extractall(unzip_folder)
        print("Done!")


def extract(month_year, unzip: bool = False) -> None:
    '''
    Downloads a file based on month/year and auto-unzips into directory

    :param month_year: the month and year of the specified file (ie, 'June 2020')
    :param unzip: 
    '''
    month_year_formatted = month_year.replace(' ', '_')
    file_name = BASE_FILE_NAME + month_year_formatted + '.zip'
    
    # construct paths for url and download destination
    url = BASE_URL + file_name
    save_path = f'{DOWNLOADS_FOLDER}{file_name}'

    # validate url
    is_valid_url = validate_url(url)
    
    # download file
    if is_valid_url:
        download_file(url, save_path)
    else:
        print("Invalid URL")
        return
    
    # unzip file
    if unzip:
        unzip_file(file_name)
