import requests
import sys
from bs4 import BeautifulSoup

resp = requests.get("https://www.flipkart.com")
if resp.status_code != 200:
    print("Sorry! Could not read data from flipkart.com. Quitting...")
    sys.exit(1)

bs = BeautifulSoup(resp.text,'html.parser')

for script in  bs.find_all('script'):
    if 'src' in script.attrs:  # does script tag have src attribute
        print(script['src'])


