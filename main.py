# -*- coding: UTF-8 -*-

import numpy as np
import pandas as pd
import math
from sklearn import preprocessing
from sklearn import cross_validation
from sklearn.preprocessing import Imputer

if __name__ == '__main__':
    """pm_array = np.zeros((27705, 24), float)
    pm_sum = []
    for i in xrange(0,24):
        new = []
        pm_sum.append(new)
    cnt = 0
    input_fp = open('2015taiwan.txt', 'r')
    buffer_fp = open('buffer.txt', 'w')
    fp = open('buffer.txt','r')
    output = open('output.txt','w')
    for line in input_fp:

        line_list = line.split(',')
        line_list[len(line_list) - 1] = line_list[len(line_list) - 1].strip()
        if line_list[2] != "PM2.5":
            continue
        else:
            for i in xrange(0,len(line_list)):
                if i > 2 and not(line_list[i].isdigit()):
                    line_list[i] = float('NaN')
                if i < 2:
                    continue
                buffer_fp.write(str(line_list[i]) + " ")
        buffer_fp.write('\n')
        for i in xrange(3,27):
            pm_array[cnt][i-3] = line_list[i]
        cnt += 1
    for i in xrange(0,27705):
        for j in xrange(0,24):
            output.write(str(pm_array[i][j])+',')
        output.write('\n')"""
    fp = open("output.txt",'w')
    data = pd.read_csv('2015taiwan.txt', sep=",", header=None)
    data.columns = ["date","location","obj","00","01","02","03","04","05","06","07","08","09",
                    "10","11","12","13","14","15","16","17","18","19","20","21","22","23"]
    print data[data.obj == 'PM2.5']








