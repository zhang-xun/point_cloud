#!/usr/bin/python3
# _*_ coding:utf-8 _*_
import  laspy
import numpy as np

def main():
    infile = laspy.file.File("read_pc.las",mode="r")
    point_record = infile.points               #numpy.ndarray

    scale_x = scaled_x_dimension(infile)

    #find the point format look like
    show_point_format(infile)

    #XML
    point_format = infile.point_format
    a_mess_of_xml = point_format.xml()
    an_etree_object = point_format.etree()

    #blue = infile.blue

    header_format = infile.header.header_format
    for spec in header_format:
        print(spec.name)

    print(infile.header.max)

    x_invalid = np.logical_or((infile.header.min[0] > infile.x),
                              (infile.header.min[0] < infile.x))
    y_invalid = np.logical_or((infile.header.min[1] > infile.y),
                              (infile.header.min[1] < infile.y))
    z_invalid = np.logical_or((infile.header.min[2] > infile.z),
                              (infile.header.min[2] <infile.z))

    bad_indice = np.where(np.logical_or(x_invalid,y_invalid,z_invalid))

    print bad_indice



    coords = np.vstack((infile.x,infile.y,infile.z)).transpose()

    first_point = coords[0,:]

    distance = np.sum((coords - first_point)**2, axis=1 )
    keep_points = distance <  50000
    point_kept = infile.points[keep_points]
    print "we are keeping %i points out %i total" %(len(point_kept),len(infile))

    outfile = laspy.file.File("write_pc.las",mode="w",header=infile.header)
    outfile.points = point_kept
    outfile.close()

def show_point_format(las_file):
    """

    :param las_file:
    :return: show the format of the point
    """
    for index ,item  in enumerate(las_file.point_format):
        print 'item {0}: {1}'.format(index,item.name)

    print(type((las_file.point_format)[0]))


def scaled_x_dimension(las_file):
    x_dimension = las_file.X                 #numpy.ndarray
    print(type(las_file.X))
    scale = las_file.header.scale[0]
    offset = las_file.header.offset[0]
    return (x_dimension*scale + offset)


if __name__ == '__main__':
    main()