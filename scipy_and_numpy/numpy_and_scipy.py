#!/usr/bin/python3
# _*_ coding:utf-8  _*_
import timeit

import numpy as np
from scipy.optimize import fsolve

def main():
    arr = np.arange(1e7)

    larr = arr.tolist()

    arr2 = np.zeros((3,3,3,))
    print(arr2)


    # wrong, because the matrix can only be two dimensional.
    # shape too large to be a matrix
    #mat = np.matrix(arr2)

    alist = [1,2,3]
    arr3 = np.array(alist)
    print(arr3)

    arr4 = np.zeros(5,dtype=int)
    print(arr4)

    arr5 = np.arange(100)
    print(arr5)


    recarr = np.zeros((2,),dtype=('i4,f4,a10'))
    toadd = [(1,2.,'Hello'),(2,3,'World')]
    recarr[:] = toadd

    print(recarr)
    recarr.dtype.names = ("Intergers","Floats","Strings")

    #print(type(recarr("Intergers")))


    alist2 = [[1,2],[3,4]]
    arr6 = np.array(alist2)
    print("arra6[0,1]", arr6[0,1])

    print("arr6[:,1] ",arr6[:,1])

    print("arr6[1,:]" ,arr6[1,:])

    arr7 = np.arange(5)
    index = np.where(arr7 > 2)
    print("index >2 ", index, "desired array", arr7[index])

    img1 = np.zeros((20,20))+3
    img1[4:-4,4:-4] = 6
    img1[7:-7,7:-7] = 9

    print(img1)


    arr8 = np.empty((1000,1000))
    np.save("numpy.npy",arr8)
    np.savez('numpy.npz',arr8)


    arr9 = np.linspace(0,10,100)
    print("arr9",arr9,"len()",len(arr9))

    lines = lambda x: x+3
    solution = fsolve(lines,-2)
    print("solution",solution)

def list_times(alist,scalar):
    for i,val in enumerate(alist):
        alist[i] = val * scalar
    return alist





if __name__ == "__main__":
    main()