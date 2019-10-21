#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import numpy as np
import SimpleITK as sitk
import caffe
import shutil
import sys
import h5py
sys.path.append("./3D-Caffe/python")
sys.path.append("./3D-Caffe/python")

caffe_model = './snapshot/_iter_30000.caffemodel'

deploy = './deploy.prototxt'
net = caffe.Net(deploy, caffe_model, caffe.TEST)


#=============================need change===================================
Path_Input = "./test.list"

Path_Output = "./result/"
print Path_Output
#===========================================================================

def alter(file,old_str,new_str):
    file_data = ""
    with open(file,"r",encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = lines.replace(old_str,new_str)
            file_data += line
    with open(file,"w",encoding="utf-8") as f:
        f.write(file_data)


#----------------------------begin code-----------------
f1 = open(Path_Input, 'r')
lines = "/home"
while lines != "":
    if lines:
        lines = f1.readline()
        lines = lines.strip()
        # print lines
        if 'h5' in lines:
            filename = lines
            print filename
            mhd_filename = filename[0:-3] + '.mhd'
            print 'mhd_filename is:'
            print mhd_filename

            f = h5py.File(filename,'r')
            img_array = f['data']
            print img_array.shape

            net.blobs['data'].data[...] = img_array
            #print  net.blobs['data'].shape
            net.forward()
            prob = net.blobs['prob_2'].data[0]
            a = prob[0]
            b = prob[1]
            c = prob[2]
            d = prob[3]
            e = prob[4]
            f = prob[5]
            g = prob[6]
            output_name = Path_Output + filename[filename.rindex('/')+1:]
            f2 = output_name[:-3] + '.raw'
            f3 = output_name[:-3] + '_1.raw'
            f4 = output_name[:-3] + '_2.raw'
            f5 = output_name[:-3] + '_3.raw'
            f6 = output_name[:-3] + '_4.raw'
            f7 = output_name[:-3] + '_5.raw'
            f8 = output_name[:-3] + '_6.raw'
            #print f2
            a.tofile(f2)
            b.tofile(f3)
            c.tofile(f4)
            d.tofile(f5)
            e.tofile(f6)
            f.tofile(f7)
            g.tofile(f8)
            print '==================================='
            print 'Finished segmentation'
            print '==================================='
            #break

    else:
        break