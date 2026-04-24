# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 09:01:58 2026

@author: Amadu
"""

import warnings

warnings.simplefilter("ignore")
import urllib.request
from bs4 import BeautifulSoup as bs

h = {
    "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
}
url = "https://epa.gov.sl/"

# 1. Create the Request object
req = urllib.request.Request(url, headers=h)

# 2. Pass the object to urlopen
doc = urllib.request.urlopen(req).read()
web_data = bs(doc, "html.parser").text
print(web_data)
