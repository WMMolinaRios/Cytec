"""
Created on Tue Oct  5 15:09:25 2021

@author: WMolina
"""

import openpyxl

book = openpyxl.load_workbook('Motorspindeln mit Informationen_ Stand 17.02.2021.xlsx', data_only=True)

Blatt1 = book.active

celdas = Blatt1['A2': 'D4']
print(celdas.value)