#!/usr/bin/python3
'''
Loading modules
'''
import requests
'''
Making get requests
'''
def make_get():
    res = requests.get('https://oxylabs.io/')
    print(res.text)

'''
Making post requests
'''
def make_post():
    data = {'key1': 'value1', 'key2': 'value2'}
    response = requests.post('https://oxylabs.io/', data=data)
    print(response.text)

'''
Working with proxies
'''
def with_proxy():
    proxy = {'http': 'http://user:password@pr.oxylabs.io:7777'}
    response = requests.get('https://ip.oxylabs.io/location', proxy=proxy)
    print(response)