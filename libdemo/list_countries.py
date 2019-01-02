import requests
import sys

resp = requests.get("https://restcountries.eu/rest/v2/all")
if resp.status_code != 200:
    sys.exit(1)

countries = resp.json()

for country in sorted(countries,key=lambda c: c['population']):
    if len(country['borders']) == 0:  # country not sharing borders with any
       print( f"{country['name']:40s} {country['capital']:30s}  {country['population']:12d}")
