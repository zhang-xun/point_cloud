#!/usr/bin/python3
# _*_ coding:utf-8  _*_

import  laspy
import numpy as np
import matplotlib.pyplot as plt
from vispy.util.transforms import translate


def main():
    infile = laspy.file.File("simple.las",mode="r")
    point_record = infile.points              #numpy.ndarray
    print "*****" * 200
    """
    print point_record.size 213093
    print point_record.ndim 1
    print point_record.shape (213093,)

    <type 'numpy.ndarray'>
       [((63049995, 483474917, 6215, 60, 18, 1, 0, 2, 0, 413162.5604),)
        ((63049983, 483474888, 6268, 90, 9, 1, 0, 2, 0, 413162.5636),)
        ((63049954, 483474966, 6266, 70, 9, 1, 0, 2, 0, 413162.5636),) ...,
        ((63025012, 483450186, 6331, 50, 9, 1, 0, 4, 0, 414095.31820000004),)
        ((63025019, 483450107, 6363, 60, 18, 1, 0, 4, 0, 414095.32200000004),)
        ((63025047, 483450029, 6354, 60, 18, 1, 0, 4, 0, 414095.32200000004),)]
    """

    print point_record.dtype
    x = point_record["point"]["X"]
    y = point_record["point"]["Y"]
    z = point_record["point"]["Z"]
    print type(x), type(y), type(z)

    # plt.plot(x,label="xvalue")
    # plt.plot(y,label="yvalue")
    plt.plot(y,label="zvalue")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()
    data = np.vstack([x,y,z]).transpose()
    print type(0.45 * np.random.randn(10, 3))


    for index,item in enumerate(data):
        if index < 100:
            print item
    print type(data)

    print(translate((0, 0, -10)))



if __name__ == "__main__":
    main()