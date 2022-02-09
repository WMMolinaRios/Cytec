# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 08:02:59 2021

@author: SKlein
"""

#!/usr/bin/env python3
import traceback

import tkinter as tk
from tkinter.filedialog import askopenfilename

import pandas as pd
import plotly
import plotly.graph_objects as go
#from plotly.subplots import make_subplots
from plotly import subplots


def werte_verarbeiten(datnam):
    try:
        # Import der Daten 
        df = pd.read_csv(datnam)
        
        ## Block 2
        # Vorbereiten der Daten für die Auswertung im Graphen
        #Hier müssen Filter angepasst werden
        #lennord = df[df['Drehzahl_>_0_(Siemens)'].str.contains('')]
        lennord = df #alle Signale werden ausgewertet
    
        
        #Selektieren der Daten für die Visualisierung 
        ms = lennord['X_(ms)']/1000
        motortemp = lennord['SERVO_03.r35:_Motortemperatur_PT1000']
        drehzahl = lennord['SERVO_03.r63:_Drehzahlistwert_geglättet']
        feldstrom = lennord['SERVO_03.r76:_Stromistwert_feldbildend']
        momentstrom = lennord['SERVO_03.r78[1]:_Stromistwert_momentenbildend._Geglättet_mit_p0045']
        spannung = lennord['SERVO_03.r72:_Ausgangsspannung']
        drehgroe0sie = lennord['Drehzahl_>_0_(Siemens)']
        kty = lennord['TM150_04.r4105[1]:_TM150_Temperaturistwert._Temperaturkanal_1_KTY']
        kwvor = lennord['Channel_1-Vor_Kühlwasser_PT100_an_Muffe']
        kwrueck = lennord['Channel_2-Ruek_Kühlwasser_PT100_an_Muffe']
        drehgroe0PT1000 = lennord['Drehzahl_>_0_(PT104)']
        rotortemproh = lennord['RotorTemp']
        rotortempc = lennord['Channel_3-Rot_RotorTemp_(Wert_/_0.0125_=_°C)']
        drehgroe0cu = lennord['Control_Unit.r747:_CU_Digitalausgänge_Status_Drehzahl_>_0']
        drehgroe0700 = lennord['Channel_4_ON_wenn_>_700_dann_Drehzahl_>_0']
        
        ## Block 3
        # Erstellen der Charts
        # Objekt "fig" bilden
        fig = subplots.make_subplots(rows=2, cols=1)#, specs=[{"secondary_y": True}]) #(5)
        
        #Datenreihen erstellen
        fig.add_traces([go.Scatter(x=ms, y=drehzahl, name='Drehzahl [U/min]'),go.Scatter(x=ms, y=spannung, name='Ausgangsspannung [V]'),go.Scatter(x=ms, y=motortemp, name='Motortemperatur [°C]'), go.Scatter(x=ms,y=feldstrom, name='Stromistwert feldbildend [A]'),go.Scatter(x=ms,y=momentstrom, name='Stromistwert momentenbildend [A]'), go.Scatter(x=ms,y=kwvor, name='Kühlw. Vorl. [°C]'), go.Scatter(x=ms,y=kwrueck, name='Kühlw. Rückl. [°C]'), go.Scatter(x=ms,y=rotortempc, name='Rotortemp. [°C]')],rows=[1, 1, 2, 2, 2, 2, 2, 2], cols=[1, 1, 1, 1, 1, 1, 1, 1]) #(5)
        
        ## Block 4 
        # Layout erstellen
        #Eine Cursorbox mit allen Werten des Graphen an der Cursorstelle
        #fig.update_layout(title="500rpm Motor Test", xaxis_title="Zeit in [s]", yaxis_title="Messwerte", hovermode="x unified", plot_bgcolor='rgb(242,242,242)' , autosize=True )
        #Für jedes Signal eine Box an der Cursorstelle
        fig.update_layout(title="500rpm Motor Test", xaxis_title="Zeit in [s]", yaxis_title="Messwerte", hovermode="x", plot_bgcolor='rgb(242,242,242)' , autosize=True )
        
        
        #Abbilden des Graphen
        plotly.offline.plot(fig, filename=(str(datnam) + '.html'))
    except BaseException as err:
        print('---')
        print(err)
        print('---')
        print("Fehler :   " + traceback.format_exc())
        quit()


def choose_filename():
    datnam = (askopenfilename())
    print(datnam)
    werte_verarbeiten(datnam)
    
    return datnam


def quit():     
    #root.quit()
    root.destroy()

def main():
    global root
    root = tk.Tk()
    root.geometry("600x150")
    # make Esc exit the program
    root.bind('<Escape>', lambda e: root.destroy())
    root.title('Messwerte-Datei auswählen.')


    tk.Label(text='\nDie Spaltenüberschriften und Messwerte müssen Komma-separiert sein.\nDas Dezimaltrennzeichen muss ein Punkt sein.\n').pack()
    #tk.Button(root, text="Dateinamen wählen", command=choose_filename).pack()
    datnam = tk.Button(root, text="Dateinamen wählen", command=choose_filename).pack()
    tk.Button(root, text="Abbrechen / beenden", command=quit).pack()
    print('Hallo Test innerhalb -> ' + str(datnam))
    root.mainloop()
    
    print('Hallo Test  -> ' + str(datnam))



if __name__ == "__main__":
    main()
