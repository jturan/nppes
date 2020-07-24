from pathlib import Path
from zipfile import ZipFile

import requests


BASE_URL = 'https://download.cms.gov/nppes/'
BASE_FILE_NAME = 'NPPES_Data_Dissemination_'

ETL_HOME_DIR = 'npi_etl' # main project folder
ETL_DOWNLOADS_DIR = 'npi_etl/downloads' # folder for all file downloads
ETL_SOURCE_FILES_DIR = 'npi_etl/source_files' # folder for all unzipped files

ETL_DIRS = (
    ETL_HOME_DIR,
    ETL_DOWNLOADS_DIR,
    ETL_SOURCE_FILES_DIR
)


def create_etl_pipeline():
    for folder in ETL_DIRS:
        p = Path(folder)
        if p.exists() == False:
            p.mkdir(parents=True)


def validate_etl_pipeline():
    for folder in ETL_DIRS:
        if Path(folder).exists() == False:
            print(f"ERROR: Required folder '{folder}' does not exist!")
    

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
    Download a specific NPI file

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
    Unzip a downloaded file
    :param file_name: name of file to be unzipped
    '''
    unzip_folder_name = file_name.replace('.zip', '')
    file_path = Path(ETL_DOWNLOADS_DIR).absolute() / file_name
    unzip_path = Path(ETL_SOURCE_FILES_DIR).absolute() / unzip_folder_name
    
    with ZipFile(file_path, 'r') as z:
        print("Directory:")
        z.printdir()
        print("\n")

        print("Unzipping...")
        z.extractall(unzip_path)
        print("Done!")


def extract(month_year, unzip: bool = False) -> None:
    '''
    Download a file based on month/year and auto-unzip into directory

    :param month_year: the month and year of the specified file (ie, 'June 2020')
    :param unzip: 
    '''
    month_year_formatted = month_year.replace(' ', '_')
    file_name = BASE_FILE_NAME + month_year_formatted + '.zip'
    
    # construct paths for url and download destination
    url = BASE_URL + file_name
    save_path = Path(ETL_DOWNLOADS_DIR).absolute() / file_name

    # validate url
    is_valid_url = validate_url(url)
    
    # download file
    if is_valid_url:
        download_file(url, save_path)
    else:
        print("ERROR: Invalid URL!")
        return
    
    # unzip file
    if unzip:
        unzip_file(file_name)
