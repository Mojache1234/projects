import requests
import csv
import pprint

old_url = 'wavecomp.ai'
new_url = 'dev-wavecomp.pantheonsite.io'
old_urls = []
broken_urls = {}

# open file
with open('wc_redirect.csv', newline='') as file:
  file.readline()
  reader = csv.reader(file, delimiter=',')
  for row in reader:
    # check for duplicates caused by hash
    url = row[0].split('#')[0] if '#' in row[0] else row[0]

    # make sure it ends with a slash
    url = url if url.endswith('/') else url + '/'

    # replace old url with new url
    url = url.replace(old_url, new_url)

    if url not in old_urls:
      old_urls.append(url)

# go through each one, check to see if 404
for url in old_urls:
  res = requests.head(url)

  # if 404, add to list
  if res.status_code != 200:
    res = requests.head(url, allow_redirects=True)
    if res.status_code == 200:
      broken_urls[url] = res.url
    else:
      broken_urls[url] = url


pprint.pprint(broken_urls)

# once done, create csv with list (or write to next column)
