# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 09:33:19 2021

@author: WMolina
"""
# import numpy as np
# import pandas as pd
# import csv, sys
 
# filename = 'Teil1.csv'

# data1 = np.genfromtxt('Teil1.csv', delimiter=';', names=True, dtype=None)
# print(data1)

# # data2 = np.recfromcsv('Teil1.csv', delimiter=';')
# # print(data2)




# # with open(filename, newline='', encoding='utf-8') as f:
# #     reader = csv.reader(f, delimiter=';')



# #-----------------------------------------------------------------------------
import numpy as np
import csv, sys


filename = 'Teil1_200UHX.csv'
with open(filename, newline='', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    try:
        for row in reader:
            print(row)
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))


# import csv

# def read_variable(filename)
# with open('Teil1_200HX.csv', newline='', encoding='utf-8') as file:
#     csv_file = csv.DictReader(file, delimiter=';', skipinitialspace=True) 
#     for row in csv_file:
#         print(dict(row))
        

# import csv
# from collections import OrderedDict as od

# data = od() # ordered dict object remembers the order in the csv file

# with open('Teil1_200UHX.csv','rb') as f:
#     reader = csv.reader(f, delimiter = ';', encoding='utf-8')
#     for row in reader:
#         data[row[0]] = row[1:]
#         print(data)
