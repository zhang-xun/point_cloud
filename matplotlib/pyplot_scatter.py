#!/usr/bin/python3
# _*_ coding:utf-8 _*_
import  matplotlib.pyplot as plt
import  numpy as np


def main():
    x = [1,2,3,4,5,6,7,8]
    y = [5,2,4,2,1,4,5,2]
    plt.scatter(x,y,label="skitscat")
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("scatter")
    plt.show()


if __name__ == '__main__':
    main()
