import requests
from pprint import pprint

url = 'https://undauntedmettle.com/chapters/chapter-1'
print('Trying iambic')

data = {
    'post_password': 'iambic',
    'Submit': 'Enter'
}

req = requests.post(url, data= data, allow_redirects=True)
pprint(req.__dict__)

