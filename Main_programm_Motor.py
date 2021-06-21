# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 22:13:08 2021

@author: WMolina
"""

import pandas as pd
import numpy as np
import math
import cmath
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial
from pandas.core.indexes.base import Index
#import functionen as func

# Einlesen der CSV-Datei:
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

#------------------Basis-Berechnung mit Aussetzbetreib S3 & S6--------------------------------

Frequenz1 = float(input("Geben Sie die Frequenz in Hz: "))
Temp_Wicklung = int(input("Geben Sie die Wicklungstemperatur in °C ein:"))
Temp_Kühlung = int(input("Geben Sie die Kühlungstemperatur in °C ein:"))

def EisenVerluste(data,motor_modell):
    Pvfe = data[motor_modell]
    return (Pvfe.loc['VH']*(1/Frequenz1)+Pvfe.loc['VW']*(1/Frequenz1)**Pvfe.loc['a'])*(Pvfe.loc['Bmax'])

def EisenVerluste1(data,motor_modell):
    Pfe = data[motor_modell]
    return (Pfe.loc['kb']*Pfe.loc['mb']*(EisenVerluste(Daten, Motor_Name)))
    
Delta_Teta_gesamt =  Temp_Wicklung - Temp_Kühlung
print("Delta Teta gesamt ist:",Delta_Teta_gesamt, "[K]")
Vv = int(input("Geben Sie die Verschaltungsvariante ein:"))
Motor_Laenge = float(input("Geben Sie die Länge X in mm ein:"))

def Kupferverlust(data, motor_modell):
    Pcu = data[motor_modell]
    return (Delta_Teta_gesamt*(Pcu.loc["Rwk"]+Pcu.loc["Rwb"]+Pcu.loc["Rbk"])-Pcu.loc["Rbk"]*(EisenVerluste1(Daten, Motor_Name)))/(Pcu.loc["Rwk"]*(Pcu.loc["Rwb"]+Pcu.loc["Rbk"]))

print('Pfe = {:.4f} [W]'.format(EisenVerluste1(Daten,Motor_Name)))
#print('Pfe = {} [W]'.format(func.EisenVerluste1(Daten,Motor_Name)))
print('Pcu = {:.4f} [W]'.format(Kupferverlust(Daten,Motor_Name)))
#print('Pcu = {} [W]'.format(func.Kupferverlust(Daten,Motor_Name)))


def KaltwiderstandX(data, motor_modell):
    R1kxs = data[motor_modell]
    return ((R1kxs.loc["R_Strang"]*R1kxs.loc["Want"]+(1-R1kxs.loc["Want"])*R1kxs.loc["R_Strang"])*(Motor_Laenge/100))

R1kx = (KaltwiderstandX(Daten,Motor_Name)/(Vv)**2)
R1w = R1kx * (1+0.004*Delta_Teta_gesamt)
Strangstrom = math.sqrt((Kupferverlust(Daten, Motor_Name))/(3*R1w))

print('R1kxs = {:.4f} [Ω]'.format(KaltwiderstandX(Daten,Motor_Name)))
print("R1kx = ", "{:.4f}".format(R1kx),"[Ω]")
print("R1w = ", "{:.4f}".format(R1w) ,"[Ω]") 
print("Pulsstrom bzw. Strangstrom = ","{:.4f}".format(Strangstrom),"[A]")

#---------------------Basis-Berechnung des Drehmoments-----------------------------------------
# M = f(Istrang)
# Die Input-variable ist Ke

Ke = Motor_Laenge/100 #mm
def M_Grundzahl(data, motor_modell):
    Mg = data[motor_modell]
    cm= (Mg.loc["Mabs"]*((1.4142*Mg.loc["N1_Innenspule"])/Vv)**2)*Ke
    bm = (Mg.loc["Mlin"]*((1.4142*Mg.loc["N1_Innenspule"])/Vv))*Ke
    am = Mg.loc["Mquad"]*Ke
    d = (bm**2)-(4*am*cm)

    #checking condition for discriminant
    if(d > 0):
        sol1 = (-bm + math.sqrt(d) / (2*am))
        sol2 = (-bm - math.sqrt(d) / (2*am))
        print("Zwei reelle Lösungen sind %.2f und %.2f" %(sol1, sol2))
    
    elif(d == 0):
        sol1 = sol2 = -bm / (2*am)
        print("Zwei gleiche und reelle Wurzeln sind %.2f and %.2f" %(sol1, sol2))

    elif(d <= 0):
        sol1 = sol2 = -bm / (2*am)
        imaginary = math.sqrt(-d) / (2*am)
        print("Zwei verschiedene komplexe Wurzeln sind: %.2f+%.2f and %.2f-%.2f" 
                          %(sol1, imaginary, sol2, imaginary))

    x = np.linspace(0, 100, 50)
    y = cm * x ** 2 +bm * x + am
    # Plot the x, y pairs
    # fig = plt.figure()
    fig, ax = plt.subplots()
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
