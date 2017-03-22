#!/usr/bin/python3
# _*_ coding:utf-8  _*_
import matplotlib.pyplot as plt
import  numpy as np
from bs4 import BeautifulSoup


import  requests

def main(stock):

    target_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10y/csv'
    r = requests.get(url=target_url).text
    print(len(r))
    print(type(r))
    print(r)

if __name__ == "__main__":
    main("a")