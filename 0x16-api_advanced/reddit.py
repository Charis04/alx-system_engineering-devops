#!/usr/bin/python3

import requests

url = 'https://www.reddit.com/r/programming/about.json'

res = requests.get(url=url, headers={'User-Agent': 'me'}, allow_redirects=False)
data = res.json()
print(data['data']['subscribers'])
