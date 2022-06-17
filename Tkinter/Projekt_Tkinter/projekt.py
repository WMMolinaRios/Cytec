from typing import ValuesView
from pylab import*

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib import style
import matplotlib.animation as animation

from math import *

import pandas as pd
import numpy as np
import sympy

import locale 
locale.setlocale(locale.LC_ALL, 'de_DE.utf8')

class Motoren:
    def __init__(self, Drehzahl, Temp_Wicklung, Temp_Kühlung, SapnnungU1, Vv, Länge):
        self.Drehzahl = Drehzahl
        self.wickTemp = Temp_Wicklung
        self.K_Temp = Temp_Kühlung
        self.SapnnungU1 = SapnnungU1
        self.Vv = Vv
        self.Länge = Länge

    # Einlesen der CSV-Datei: Hier gehen Sie bitte zuerst dorthin, wo Sie die csv-Datei haben. Klicken Sie auf die Shift-Taste und die rechte Maustaste. Und im Menü suchen Sie nach: Als Pfad kopieren. Zum Schluss kopieren Sie den pfad hier in die Variable Daten
    Daten = pd.read_csv('C:/Users/wmolina/Desktop/Python/TechnoTable.csv',delimiter=';', index_col='Parameter',decimal=',').fillna('')
    print(Daten)

    Daten[["200HX", "200UHX", "240HX", "240UHX", "310HX", "310UHX", "360UHX", "410HX", "410UHX", "564HX"]] = Daten[["200HX", "200UHX", "240HX", "240UHX", "310HX", "310UHX", "360UHX", "410HX", "410UHX", "564HX"]].apply(pd.to_numeric).fillna('')

    Auswahl = input("Bitte wählen Sie den Motor(XXXHX/UHX): ")
    Motor_Name = Auswahl.upper()
    start = True
    while start:
        if Motor_Name in list(Daten.columns):
            print("Variablen sind:\n",Daten['{}'.format(Motor_Name)])
            start = False
        else:
            print("Sie haben das falsch geschrieben, bitte versuchen Sie es noch mal!")
            Auswahl = input("Bitte wählen Sie den Motor(XXXHX/UHX): ")
            Motor_Name = Auswahl.upper()   


    def setDrehzahl(self):
        Drehzahl = "" # Hier handelt es sich um die Drehzahl an einem Bemessungspunkt!!
        while Drehzahl is not float:
            try:
                Drehzahl = float(locale.atof(input("Geben Sie die gewünschte Drehzahl in [1/min] ein: ")))
                break
            except ValueError:
                print("Sie haben das falsch geschrieben, bitte versuchen es noch mal!")

    def setTempWicklung(self):
        Temp_Wicklung = ""
        while Temp_Wicklung is not float:
            try:
                Temp_Wicklung = int(input("Geben Sie die Wicklungstemperatur in °C ein: "))
                break 
            except ValueError:
                print("Sie haben das falsch geschrieben, bitte versuchen es noch mal!")

    def setTempKühlung(self):
        Temp_Kühlung = ""
        while Temp_Kühlung is not float:
            try:
                Temp_Kühlung = int(input("Geben Sie die Kühlungstemperatur in °C ein: "))
                break 
            except ValueError:
                print("Sie haben das falsch geschrieben, bitte versuchen es noch mal!")

    def setSpannung(self):
        SpannungU1 = ""
        while True:
            try:
                SpannungU1 = float(input("Bitte wählen Sie einen Spannungswert 400[V], 425[V] oder 200[V]: \n"))

                if SpannungU1 == 400 or SpannungU1 == 425 or SpannungU1 ==200:
                    print(f"Der gewählte Spannungswert ist: {SpannungU1} [V]")
                    break
                else:
                    print("Sie haben das falsch geschrieben, bitte versuchen es noch mal!")
            except:
                print("Das war keine Zahl!!")

        U1 = SpannungU1/1.732

    def setVerschaltung(self):
        #Hier sucht das Programm die verfügbaren Optionen für die Variable Vv in Abhängigkeit vom Motor_Name
        print("\n")
        vv_keys = ["Seriel", "2TM", "3TM", "4TM", "5TM", "6TM", "8TM", "10TM", "12TM"]
        vv_values = [self.Auswahl][vv_keys]
        vv_values = vv_values[vv_values!=''].astype(int)
        Vv = ""
        while True:
            try:
                print("Die für diesen Motor verfügbaren Teilmotoren sind:\n", vv_values )
                print("\n")
                Vv = int(input("Wählen Sie den Teilmotor: "))
                print("\n")
            
                if Vv not in vv_values.values:
                    print("Sie haben das falsch geschrieben, bitte versuchen es noch mal!\n")
                else:
                    break
            except:
                print("Das war falsch!!")
    setDrehzahl()