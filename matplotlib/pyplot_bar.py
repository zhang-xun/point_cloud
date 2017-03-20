#!/usr/bin/python3
# _*_ coding:utf-8 _*_

import  numpy as np
import  matplotlib.pyplot as plt

def main():
    plt.bar([2,4,6,8,10,12],[5,4,5,5,1,8],label="example one")
    plt.bar([1,3,5,7,9,11],[2,6,6,1,2,9],label="example two",color="g")
    plt.legend()
    plt.xlabel("xlabel")
    plt.ylabel("ylabel")

    plt.title("bar historgram")

    plt.show()






if __name__ == '__main__':
    main()