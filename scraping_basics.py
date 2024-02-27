#!/usr/bin/python3
'''
Loading modules
'''
import requests
from bs4 import BeautifulSoup
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.by import By

'''
Converting response to parser with beutifulsoup
'''

url = 'https://oxylabs.io/blog'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title)

'''
Getting text in html tags
'''
#using find() or find_all()
'''
Gets all tags given as argument
'''
blog_titles = soup.find_all('a', class_= 'e1dscegp1')
for title in blog_titles:
    print(title.text)

# Using select()
'''
For more explicit results and exact tag use select()
'''
blog_titles = soup.select('a.e1dscegp1')
for title in blog_titles:
    print(title.text)

'''
Basics of lxml
'''
tree = html.fromstring(response.text)
blog_titles = tree.xpath('//a[contains(@class, "e1dscegp1")]')
for title in blog_titles:
    print(title.text)

'''
Basics of selenium
'''
driver = webdriver.Chrome()
driver.get('https://oxylabs.io/blog')
blog_titles = driver.find_elements(By.CSS_SELECTOR, 'a.e1dscegp1')
for title in blog_titles:
    print(title.text)
# closing the browser
driver.quit()