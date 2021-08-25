# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 22:13:08 2021

@author: WMolina
"""

import pandas as pd
import numpy as np
import math as mt
import matplotlib.pyplot as plt
from colorama import init
from colored import fg, bg, attr
from numpy.polynomial.polynomial import Polynomial
from pandas.core.indexes.base import Index

#import functionen as func

# Einlesen der CSV-Datei: Hier gehen Sie bitte zuerst dorthin, wo Sie die csv-Datei haben. Klicken Sie auf die Shift-Taste und die rechte Maustaste. Und im Menü suchen Sie nach: Als Pfad kopieren. Zum Schluss kopieren Sie den pfad hier in die Variable Daten
Daten = pd.read_csv('C:/Users/wmolina/Desktop/GUI/TechnoTable.csv',delimiter=';', index_col='Parameter',decimal=',').fillna('')
print(Daten)

Daten[["200HX", "200UHX", "240HX", "240UHX", "310HX", "310UHX", "360UHX", "410HX", "410UHX", "564HX"]] = Daten[["200HX", "200UHX", "240HX", "240UHX", "310HX", "310UHX", "360UHX", "410HX", "410UHX", "564HX"]].apply(pd.to_numeric).fillna('')

# Motorauswahl
Auswahl = input("Bitte wählen Sie den Motor(XXXHX/UHX): ")
Motor_Name = Auswahl.upper()

start = True
while start:
    if Motor_Name in list(Daten.columns):
        print("Variablen sind:\n",Daten['{}'.format(Motor_Name)])
        start = False
    else:
        print("Sie haben das falsch geschrieben, bitte versuchen es noch mal!")
        Auswahl = input("Bitte wählen Sie den Motor(XXXHX/UHX): ")
        Motor_Name = Auswahl.upper()
#print (type(Motor_Name))
print("\n")
print("-------------------------------------Variable Eingaben-------------------------------------\n")
# Eingangsvariablen:
Frequenz1 = ""
while Frequenz1 is not float:
    try:
        Frequenz1 = float(input("Geben Sie die Frequenz in Hz: "))
        break 
    except ValueError:
        print("Sie haben das falsch geschrieben, bitte versuchen es noch mal!")

print("\n")   

Temp_Wicklung = ""
while Temp_Wicklung is not float:
    try:
        Temp_Wicklung = int(input("Geben Sie die Wicklungstemperatur in °C ein: "))
        break 
    except ValueError:
        print("Sie haben das falsch geschrieben, bitte versuchen es noch mal!")

print("\n")

Temp_Kühlung = ""
while Temp_Kühlung is not float:
    try:
        Temp_Kühlung = int(input("Geben Sie die Kühlungstemperatur in °C ein: "))
        break 
    except ValueError:
        print("Sie haben das falsch geschrieben, bitte versuchen es noch mal!")

print("\n")

Delta_Teta_gesamt =  Temp_Wicklung - Temp_Kühlung
print("Delta Teta gesamt ist:",Delta_Teta_gesamt, "[K]\n")

print("\n")

SpannungU1 = ""
while True:
    print("Die verfügbaren Spannungswerte sind 400[V], 425[V] oder 200[V]")
    SpannungU1 = int(input("Bitte wählen Sie einen Wert: "))

    if SpannungU1 == 400 or SpannungU1 == 425 or SpannungU1 ==200:
        print(f"Der gewählte Spannungswert ist: {SpannungU1} [V]")
        break
    else:
        print("Sie haben das falsch geschrieben, bitte versuchen es noch mal!")

#Hier sucht das Programm die verfügbaren Optionen für die Variable Vv in Abhängigkeit vom Motor_Name
print("\n")
vv_keys = ["Seriel", "2TM", "3TM", "4TM", "5TM", "6TM", "8TM", "10TM", "12TM"]
vv_values = Daten[Motor_Name][vv_keys]
vv_values = vv_values[vv_values!=''].astype(int)
Vv = ""
while True:
    print("Die für diesen Motor verfügbaren Teilmotoren sind:\n", vv_values )
    Vv = int(input("Geben Sie den Teilmotor ein: "))
    
    if Vv not in vv_values.values:
        print("Sie haben das falsch geschrieben, bitte versuchen es noch mal!")
    else:
        break
print("\n")

#------------------Basis-Berechnung mit Aussetzbetreib S3 & S6--------------------------------
def Drehzahl (data,motor_modell):
    n = data[motor_modell]
    return (Frequenz1/(n.loc['STK_Magnet']/2)*60)


def EisenVerluste(data,motor_modell):
    Pvfe = data[motor_modell]
    return (Pvfe.loc['VH']*(1/Frequenz1)+Pvfe.loc['VW']*(1/Frequenz1)**Pvfe.loc['a'])*(Pvfe.loc['Bmax'])

def EisenVerluste1(data,motor_modell):
    Pfe = data[motor_modell]
    return (Pfe.loc['kb']*Pfe.loc['mb']*(EisenVerluste(Daten, Motor_Name)))
    
Motor_Laenge = ""
while Motor_Laenge is not float:
    try:
        Motor_Laenge = float(input("Geben Sie die Länge X in mm ein: "))
        print("\n")
        break 
    except ValueError:
        print("Sie haben das falsch geschrieben, bitte versuchen es noch mal!")

def Kupferverlust(data, motor_modell):
    Pcu = data[motor_modell]
    return (Delta_Teta_gesamt*(Pcu.loc["Rwk"]+Pcu.loc["Rwb"]+Pcu.loc["Rbk"])-Pcu.loc["Rbk"]*(EisenVerluste1(Daten, Motor_Name)))/(Pcu.loc["Rwk"]*(Pcu.loc["Rwb"]+Pcu.loc["Rbk"]))

def KaltwiderstandX(data, motor_modell):
    R1kxs = data[motor_modell]
    return ((R1kxs.loc["R_Strang"]*R1kxs.loc["Want"]+(1-R1kxs.loc["Want"])*R1kxs.loc["R_Strang"])*(Motor_Laenge/100))  

print("\n")
print('n = {:.4f} [rpm]'.format(Drehzahl(Daten,Motor_Name)))
print("\n")
print('Pfe = {:.4f} [W]'.format(EisenVerluste1(Daten,Motor_Name)))
print("\n")
#print('Pfe = {} [W]'.format(func.EisenVerluste1(Daten,Motor_Name)))
print('Pcu = {:.4f} [W]'.format(Kupferverlust(Daten,Motor_Name)))
print("\n")
#print('Pcu = {} [W]'.format(func.Kupferverlust(Daten,Motor_Name)))

R1kx = (KaltwiderstandX(Daten,Motor_Name)/Vv**2)
R1w = R1kx * (1+0.004*Delta_Teta_gesamt)
Strangstrom = mt.sqrt((Kupferverlust(Daten, Motor_Name))/(3*R1w))

#---------------Basis-Berechnung des Spannungskonstante---------------------------------------
def Spannungskonstante(data, motor_modell):
    Ku = data[motor_modell]
    return ((Ku.loc['Flussscheiteltwert']/1000)*2*0.93*Ku.loc['N1_Innenspule']*(Ku.loc['STK_Magnet']/2))*(Ku.loc['Nutflaeche_Anzahl']/(3*2*Vv))*((Ku.loc['KorrekturFaktor']/1.4142))
Up = Spannungskonstante(Daten, Motor_Name)*2*np.pi*(Drehzahl(Daten, Motor_Name)/60)

def Drehmomentkonstante(data, motor_modell):
    KT = data[motor_modell]
    return 3*(Spannungskonstante(Daten, Motor_Name)/KT.loc['KorrekturFaktor'])
# KT = 3*Spannungskonstante(Daten, Motor_Name)
#---------------Ergebnisse auf dem Screen---------------------------------------
print('R1kxs = {:.4f} [Ω]'.format(KaltwiderstandX(Daten,Motor_Name)))
print("\n")
print("R1kx = ", "{:.4f}".format(R1kx),"[Ω]")
print("\n")
print("R1w = ", "{:.4f}".format(R1w) ,"[Ω]")
print("\n") 
print("Strangstrom = ","{:.4f}".format(Strangstrom),"[A]")
print("\n")
print("Spannungskonstante Ku = ","{:.4f} [V/1000rpm]".format(Spannungskonstante(Daten,Motor_Name)))
print("\n")
print("Polradspannung Up = ","{:.4f}".format(Up), "[V]")
print("\n")
print("Drehmomentkonstante KT = ","{:.4f} [Nm/A]".format(Drehmomentkonstante(Daten, Motor_Name)))
print("\n")
#---------------------Basis-Berechnung des Drehmoments-----------------------------------------
def move_spines():
    fix, ax = plt.subplots()
    for spine in ["left", "bottom"]:
        ax.spines[spine].set_position("zero")
    
    for spine in ["right", "top"]:
        ax.spines[spine].set_color("none")
    
    return ax

# M = f(Istrang)
# Die Input-variable ist Ke

Ke = Motor_Laenge/100 
def M_Grundzahl(data, motor_modell):
    Mg = data[motor_modell]
    am= (Mg.loc["Mquad"]*((1.4142*Mg.loc["N1_Innenspule"])/Vv)**2)*Ke
    bm = (Mg.loc["Mlin"]*((1.4142*Mg.loc["N1_Innenspule"])/Vv))*Ke
    cm = Mg.loc["Mabs"]*Ke
    M_g = am*(Strangstrom**2) + bm*(Strangstrom) + cm
    print("Drehmoment als Funktion der Durchflutung: {:.4f} [Nm]".format(M_g))
    print("\n")

    xmax = Strangstrom # Es wurde bereits so modifiziert, dass der Graph dieses Drehmoments als Maximalwert den Strangstrom jedes Motors hat.
    x = np.arange(0, xmax, 0.5)
    y = am * x ** 2 +bm * x + cm
    ax = move_spines()
    ax.set_title("M = f(I_Strang)")
    plt.xlabel("Phasenstrom / [A]")
    plt.ylabel("Drehmoment / [Nm]")
    plt.grid(True)
    ax.plot(x, y)

    # Plot a zero line
    ax.hlines(y=0, xmin=min(x), xmax=max(x), colors='r', linestyles='--', lw=1)

    # Show the plot
    plt.show()
M_Grundzahl(Daten, Motor_Name)
def Up_Drehzahl(data, motor_modell):
    
    x = np.arange(0, 200, 0.5)
    y = Spannungskonstante(Daten, Motor_Name)*2*np.pi*x
    
    ax = move_spines()
    ax.set_title("Up = f(n)")
    plt.xlabel("Drehzahl [rpm]")
    plt.ylabel("ind.Spannung [V]")
    plt.grid(True)
    ax.plot(x, y)

    # Plot a zero line
    ax.hlines(y=0, xmin=min(x), xmax=max(x), colors='r', linestyles='--', lw=1)

    # Show the plot
    plt.show()
Up_Drehzahl(Daten, Motor_Name)
    

    



