#! /usr/bin/python3
# _*_ coding:utf-8 _*_

import laspy
import scipy
import numpy as np


infile = laspy.file.File("read_pc.las",mode="r")

data = np.vstack([infile.X, infile.Y, infile.Z]).transpose()

tree = scipy.spatial.kdtree(data)
tree.query(data[100,],k=5)

num_return = infile.num_returns
return_num = infile.return_num
ground_points = infile.points[num_return == return_num ]
print("%i points out %i were ground points"%(len(ground_points),len(infile)))