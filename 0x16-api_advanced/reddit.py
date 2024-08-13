#!/usr/bin/python3

import requests

url = 'https://www.reddit.com/r/programming/hot.json'

res = requests.get(url=url, headers={'User-Agent': 'me'}, allow_redirects=False)
data = res.json()['data']['children']
for i in range(10):
    print(data[i]['data']['title'])
