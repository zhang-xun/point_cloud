#!/usr/bin/python3
# _*_ coding:utf-8  _*_
import random

import  numpy as np
import matplotlib.pyplot as plt


def main():
    #generate the data file to be test
    generate_txt("example.txt")

    x,y = np.loadtxt("example.txt",delimiter=",",unpack=True)
    plt.plot(x,y,label="loadtxt")
    plt.legend()
    plt.show()

def generate_txt(filename):
    """
    just write some txt into filenames
    :return:
    """
    with open(filename,mode="w") as f:
        count = 0
        for i in range(15):
            f.write("%s,%s\n" %(count,random.randint(1,20)))
            count += 1


if __name__ == "__main__":
    main()