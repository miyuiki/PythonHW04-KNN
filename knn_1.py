# -*- coding: UTF-8 -*-

import numpy as np
import pandas as pd

if __name__ == '__main__':
    cnt1 = 0
    cnt2 = 0
    distant_list = []
    similarity_list = []
    city_dic1 = {'龍潭':0}
    city_dic2 = {'龍潭':0}
    data = pd.read_csv('output.txt', sep=" ", header=None)
    data = data.dropna(axis=0, how='any')
    data.columns = ["date", "location", "obj", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                    "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]
    city_list = data['location'].drop_duplicates().tolist()
    data = data[data.date == '2015/01/01']
    p = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    for x in xrange(0,24):
        p[x] = data['{}'.format(x)].tolist()
    p = map(list, zip(*p))
    for i in xrange(1,len(p)):
        d = 0
        s = 0
        s1 = 0
        s2 = 0
        s3 = 0
        for j in xrange(0,len(p[i])):
            d += (p[0][j]-p[i][j])**2
            s1 += p[0][j]*p[i][j]
            s2 += p[0][j]**2
            s2 = np.sqrt(s2)
            s3 += p[i][j]**2
            s3 = np.sqrt(s3)
            s = s1/s2*s3
        distant_list.append(np.sqrt(d))
        similarity_list.append(s)
    for x in xrange(1,len(city_list)):
        city_dic1['{}'.format(city_list[x])] = distant_list[x-1]
    for x in xrange(1,len(city_list)):
        city_dic2['{}'.format(city_list[x])] = similarity_list[x-1]
    city_dic1.pop('龍潭')
    city_dic2.pop('龍潭')
    city_tuple1 = sorted(city_dic1.iteritems(), key=lambda d: d[1])
    city_tuple2 = sorted(city_dic2.iteritems(), key=lambda d: d[1])
    print "--------find by distant---------"
    for i in iter(city_tuple1):
        if cnt1 == 5:
            break
        else:
            print i[0]
        cnt1 += 1
    print "--------find by similarity---------"
    for i in iter(city_tuple2):
        if cnt2 == 5:
            break
        else:
            print i[0]
        cnt2 += 1