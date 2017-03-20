#!/usr/bin/python
# _*_ coding:utf-8 _*_


import matplotlib.pyplot as plt
import numpy as np

def main():
   data = [22,55,62,21,22,34,42,42,4,99,102,110,120,121,130,111,115,115,112,80,75,65,54,44,43,42,48]
   bins=[0,10,20,30,40,50,60,70,80,90,100,110,120,130]
   plt.hist(data,bins,histtype="bar",rwidth=0.8,label="helloworld")
   plt.xlabel("x")
   plt.ylabel("y")
   plt.title("Internation Graph\nCheck it out")
   plt.legend()
   plt.show()



if __name__ == '__main__':
    main()
