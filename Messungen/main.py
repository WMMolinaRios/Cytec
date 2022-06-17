import pandas as pd
import numpy as np
import os
import easygui as eg
import sys
from datetime import date 
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm
from sympy import rotations
from FunktionAblesen import *
from os.path import dirname, basename, splitext, join
from glob import glob
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
#%matplotlib inline

# file1 = pd.read_csv(r'C:\Users\wmolina\Documents\EV_und_Messung\HauptVerteilung\KomplettHV1_15-min-data.csv', sep=';', index_col=0, decimal=',')

# df_Strom = file1[['L1 Irms avg [A]','L2 Irms avg [A]','L3 Irms avg [A]']]

# plt.figure(figsize=(100, 10), dpi=100)
# plt.plot(df_Strom, label=df_Strom.columns)
# plt.xlabel('Zeit')
# #plt.xticks(rotation = 45)
# plt.gcf().autofmt_xdate()
# plt.ylabel('Strom [A]')
# plt.grid(True)
# plt.legend(loc='best')
# plt.title("2-Woche Messung")
# plt.show()
################# Benutzereinstellungen #################

CSV_Path = eg.fileopenbox(msg = "Bitte die Messwerte-Datei auswählen", default = "*.csv")
if CSV_Path == None:
    sys.exit()

# Read csv_data:
def ReadData(path, WorkSheet):
    csv_df = pd.read_csv(path, WorkSheet)
    #print(csv_df)
    return csv_df



# Ruting principal
def main():
    # Read the Excel Data
    df_messung = ReadData(CSV_Path, 'sens3_10-min-data')
    print(df_messung)
    # Fehler:
    #Fehler(df_messung)

    # Create the Wordfile:
    #CreateWord(df_messung)


if __name__ == '__main__':
    main()
