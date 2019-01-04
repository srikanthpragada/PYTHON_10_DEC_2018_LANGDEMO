import requests
from bs4 import BeautifulSoup
import sys

resp = requests.get("http://www.srikanthtechnologies.com/schedule.xml")
if resp.status_code != 200:
    sys.exit(1)

bs = BeautifulSoup(resp.text,"xml")
for batch in bs.find_all("batch"):
    print( f"{batch['subject']:50s}  {batch['timing']:20s}  {batch['stdate']} ")
