#!/usr/bin/env python

import requests

print(requests.__version__)

r = requests.get("https://raw.githubusercontent.com/kkwong02/cmput404-lab1/master/main.py")
print(r.text)
# print(r.status_code)
