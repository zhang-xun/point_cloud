#! /usr/bin/python2
# _*_ coding:utf-8 _*_

import  pyflann as pf
import laspy
import  numpy as np

infile = laspy.file.File("read_pc.las",mode="r")

dataset = np.vstack([infile.X, infile.Y, infile.Z]).transpose()

neighbors = pf.flann.nn(dataset, dataset[100,], num_neighbors=5)
print("five  nearst neighbors of point 100:")
print neighbors[0]
print("Distance : ")
print(neighbors[1])