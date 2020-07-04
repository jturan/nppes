from zipfile import ZipFile

import requests

import settings


BASE_URL = 'https://download.cms.gov/nppes/'
BASE_FILE_NAME = 'NPPES_Data_Dissemination_'


def validate_url():
    r = requests.head(url)
    if r.status_code == 200:
        return True
    else:
        return False


def download_file(url, save_path, chunk_size=128):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        print("Downloading...")
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)
        print("Done!")


def unzip_file(file_name):
    with ZipFile(file_name, 'r') as z:
        z.printdir()
        
        print("Unzipping...")
        z.extractall()
        print("Done!")


def extract(url, unzip=False):
    save_path = f'{settings.DOWNLOADS_FOLDER}{file_name}'
    
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
        unzip_file(save_path)
