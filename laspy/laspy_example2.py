#!/usr/bin/python3
# _*_ coding:utf-8  _*_
import  numpy as np
import laspy

def main():
    inFile = laspy.file.File("./example2.las",mode="r")
    point_records = inFile.points
    print type(point_records)
    print point_records.ndim
    print point_records.shape
    print point_records.dtype



if __name__ == "__main__":
    main()