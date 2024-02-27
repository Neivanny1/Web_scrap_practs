#!/usr/bin/python3
'''
Loading modules
'''
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

'''
Selecting browser driver
'''
# For Chrome
#driver = webdriver.Chrome()
#Firefox
driver = webdriver.Firefox()

url = 'https://fbref.com/en/comps/9/Premier-League-Stats'
driver.get(url)

'''
Defining objects and building lists
'''
results = []
# Add the page source to the variable `content`.
content = driver.page_source
# Load the contents of the page, its source, into BeautifulSoup 
soup = BeautifulSoup(content, 'html.parser')

'''
Extracting data with a Python web scraper
 Loop over all elements returned by the `findAll` call. 
It has the filter `attrs` given
'''
for element in soup.find_all(attrs={'class': 'title'}):
    name = a.find('a')
    if name not in results:
        results.append(name.text)

'''
Exporting the data to CSV
'''
df = pd.DataFrame({'Names': results})
df.to_csv('names.csv', index=False, encoding='utf-8')