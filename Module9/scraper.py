"""
Program: scraper.py
Author: Paul Ford
Last date modified: 06/27/2020
Purpose: My first scraper
"""

import requests
from bs4 import BeautifulSoup

url = 'https://www.dmacc.edu/schedule/Pages/result.aspx?Term=201903&Campus=1;4&S'
response = requests.get(url)
html = response.content
f = open("requestResult.txt", "w+")
f.writelines(str(html))
f.close()

soup = BeautifulSoup(open("requestResult.txt"), 'html.parser')
f = open("requestResultBeautiful.txt", "w+")
f.writelines(soup.prettify())
print(soup.prettify())
