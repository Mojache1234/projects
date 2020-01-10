import socket
from pprint import pprint
import argparse
import csv

# parse argument
parser = argparse.ArgumentParser(description='Get IP addresses given a csv list of URLs')
parser.add_argument('-f', metavar='csvfile', type=str, help='name of csv file')

args = parser.parse_args()

urls = []

# parse csv
with open(args.f, newline='\n') as csvfile:
  urls_raw = csv.reader(csvfile)
  for url_raw in urls_raw:
    urls.append(url_raw[0])

ips = {}

for url in urls:
  ip = socket.gethostbyname(url)
  ips[url] = ip


with open('results.csv', 'w') as newfile:
  for url, ip in ips.items():
    newfile.write(','.join([url, ip]) + '\n')
