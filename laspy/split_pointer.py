#!/usr/bin/python3
# _*_ coding:utf-8  _*_

import  laspy
import numpy as np

def main():
    infile = laspy.file.File("read_pc.las",mode="r")
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


if __name__ == "__main__":
    main()