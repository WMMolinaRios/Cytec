import pandas as pd
import numpy as np
from os.path import dirname, basename, splitext, join
from glob import glob

#files=glob('folder-path**/*.csv', recursive=True)
#files

def AblesenAuswertung(file):
    Werte= pd.read_csv(file, delimiter=';', decimal=',')
    Werte['Time'] = pd.DatetimeIndex(Werte['Time'])
    Werte = Werte.set_index('Time')

    return (Werte, Werte.describe())


def collectStats(files):
    stats=[]
    for  fname in files:
        name = splitext(basename(fname)) [0]
        data, stt = AblesenAuswertung(fname)
        stt.columns = stt.columns+':'+name
        
        stats.append(stt)
        
    return pd.concat(stats, axis=1) 
#stats.to_csv('Auswertung_all.csv')