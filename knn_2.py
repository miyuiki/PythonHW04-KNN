# -*- coding: UTF-8 -*-

import numpy as np
import pandas as pd

if __name__ == '__main__':
	date = raw_input('select a date : ')
	location = raw_input('select a location : ')
	k = input('selsect a "k" value : ')

	data = pd.read_csv('output.txt', sep=" ", header=None)
	data = data.dropna(axis=0, how='any')
	data.columns = ["date", "location", "obj", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                    "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]
    
	city_list = data['location'].drop_duplicates().tolist()
	data = data[data.location == '{}'.format(location)]
	print data
