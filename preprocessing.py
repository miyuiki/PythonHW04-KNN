# -*- coding: UTF-8 -*-

import numpy as np
import pandas as pd

if __name__ == '__main__':
    city_list = []
    city_dic = {}
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
    city_list = data.sort_values(by = "location")['location'].drop_duplicates().tolist()
    p = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for x in xrange(0,24):
        p[x] = pm_mean['{}'.format(x)].map('{:,.2f}'.format).tolist()
    p = map(list, zip(*p))
    for x in xrange(0,len(city_list)):
        city_dic['{}'.format(city_list[x])] = x
    for line in fp:
        line_list = line.split(' ')
        for i in xrange(0, len(line_list)):
            if line_list[i] == 'nan':
                line_list[i] = p[city_dic['{}'.format(line_list[1])]][i-3]
            if i != len(line_list)-2:
                output.write(str(line_list[i]) + " ")
            else:
                output.write(str(line_list[i]))
        output.write('\n')






    
