# nppes

Package to interface with the Center for Medicare and Medicaid's (CMS) National Plan and Provider Enumeration System (NPPES).

## Search

To search the NPPES API, simply search via your terminal.

    >>> poetry run python search.py --first_name James --last_name Moore

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
