# -*- coding: UTF-8 -*-

import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import Imputer

if __name__ == '__main__':
    city_list = []
    input_fp = open('2015taiwan.txt', 'r')
    buffer_fp = open('buffer.txt', 'w')
    fp = open('buffer.txt', 'r')
    output = open('output.txt', 'w')
    for line in input_fp:

        line_list = line.split(',')
        line_list[len(line_list) - 1] = line_list[len(line_list) - 1].strip()
        if line_list[2] != "PM2.5":
            continue
        else:
            for i in xrange(0, len(line_list)):
                if i > 2 and not(line_list[i].isdigit()):
                    line_list[i] = np.NaN
                buffer_fp.write(str(line_list[i]) + " ")
        buffer_fp.write('\n')

    data = pd.read_csv('buffer.txt', sep=" ", header=None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    data.columns = ["date", "location", "obj", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                    "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "end"]
    data.pop('end')
    g = data.groupby(['location'])
    pm_mean = g.mean()
    city_cnt = len(g)
    #city_list = pm_mean['location'].tolist()
    p = []
    for x in xrange(0,24):
        p.append(pm_mean['{}'.format(x)].map('{:,.2f}'.format).tolist())
    print p[0]


    
