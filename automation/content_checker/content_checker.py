import csv
from bs4 import BeautifulSoup as bs
import requests
from requests.auth import HTTPBasicAuth
import argparse

# Get dev and prod website base URL's
parser = argparse.ArgumentParser(description='Dev and Prod base URL\'s')
parser.add_argument('-d', type=str, help='Dev base URL', required=True)
parser.add_argument('-p', type=str, help='Prod base URL', required=True)
parser.add_argument('-f', type=str, help='File for subpages (dev first then prod) - Defaults to home URL only', required=False)


args = parser.parse_args()
dev = args.d
prod = args.p
file = args.f if args.f else None


# Compare two URL's together
def compare(dev_url='', prod_url=''):
  dev_content = requests.get(dev + dev_url, auth=HTTPBasicAuth('client', 'access'))
  prod_content = requests.get(prod + prod_url)
  bs_d = bs(dev_content.text, 'html.parser')
  bs_p = bs(prod_content.text, 'html.parser')
  if (bs_d.find('p') == bs_p.find('p')): print(dev, 'checks out!')
  else: print(dev, 'and', prod,'do not match.')


# Check if file
if file:
  try:
    with open(file, 'r') as f:
      content = csv.reader(f)
      for row in content:
        dev_url = row[0]
        prod_url = row[0]
        compare(dev_url, prod_url)
  except Exception as e:
    print(e)
    print('ERROR: File', file, 'does not exist.')
else:
  compare()
