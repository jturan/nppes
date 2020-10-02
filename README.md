# nppes

Package to interface with the Center for Medicare and Medicaid's (CMS) National Plan and Provider Enumeration System (NPPES).

## To Install

    $ pip install nppes

## Search

To search the NPPES API, simply search via your terminal.

    $ search_nppes_api --first_name James --last_name Moore

To search the NPPES API and put results into a DataFrame:

    from nppes import nppes_df

    df = nppes_df(first_name='James', last_name='Moore')

Optional arguments include:

- number
- enumeration_type
- taxonomy_description
- first_name
- last_name
- organization_name
- address_purpose
- city
- state
- postal_code
- limit
