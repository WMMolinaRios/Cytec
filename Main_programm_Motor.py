# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 22:13:08 2021

@author: WMolina
"""

import pandas as pd
import numpy as np
import math
import cmath
from pandas.core.indexes.base import Index
import matplotlib.pyplot as plt
import functionen as func

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

print('Pfe = {} [W]'.format(EisenVerluste1(Daten,Motor_Name)))
#print('Pfe = {} [W]'.format(func.EisenVerluste1(Daten,Motor_Name)))
print('Pcu = {} [W]'.format(Kupferverlust(Daten,Motor_Name)))
#print('Pcu = {} [W]'.format(func.Kupferverlust(Daten,Motor_Name)))


def KaltwiderstandX(data, motor_modell):
    R1kxs = data[motor_modell]
    return ((R1kxs.loc["R_Strang"]*R1kxs.loc["Want"]+(1-R1kxs.loc["Want"])*R1kxs.loc["R_Strang"])*(Motor_Laenge/100))

R1kx = (KaltwiderstandX(Daten,Motor_Name)/(Vv)**2)
R1w = R1kx * (1+0.004*Delta_Teta_gesamt)
Strangstrom = math.sqrt((Kupferverlust(Daten, Motor_Name))/(3*R1w))

print('R1kxs = {} [Ω]'.format(KaltwiderstandX(Daten,Motor_Name)))
print("R1kx = ",R1kx,"[Ω]")
print("R1w = ", R1w,"[Ω]") 
print("Pulsstrom bzw. Strangstrom = ",Strangstrom,"[A]")

#-----------------------Basis-Berechnung des Drehmoments-----------------------------------------
# M = f(Istrang)
# Das Input-variable ist Ke
Ke = Motor_Laenge/100 #mm
def M_Grundzahl(data, motor_modell):
    Mg = data[motor_modell]
    cm= (Mg.loc["Mabs"]*((1.4142*Mg.loc["N1_Innenspule"])/Vv)**2)*Ke
    bm = (Mg.loc["Mlin"]*((1.4142*Mg.loc["N1_Innenspule"])/Vv))*Ke
    am = Mg.loc["Mquad"]*Ke
    d = (bm**2)-(4*am*cm)
    sol1 = (-bm-cmath.sqrt(d))/(2*am)
    sol2 = (-bm+cmath.sqrt(d))/(2*am)
    return sol1, sol2

# if d < 0:
#     print("The equation has no real solutions")
# elif d == 0:
#     x = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
#     print(f"The equation has one solution: {x} ")
# else:
#     x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
#     x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
#     print(f"The equation has two solutions: {x1} or {x2}")


# if M_Grundzahl > 0:
#     num_roots=2
#     print("M = %f and %f" % (sol1, sol2))

print("Das Drehmoment ist:{} [Nm]".format(M_Grundzahl(Daten, Motor_Name)))

# Create 1000 equally spaced points between -10 and 10
# x = np.linspace(-10, 10, 1000)

# # Calculate the y value for each x value
# y = a * x ** 2 + b * x + c

# # Plot the x, y pairs
# fig, ax = plt.subplots()
# ax.set_title("Quadratic Equations with Python")
# ax.plot(x, y)

# # Plot a zero line
# ax.hlines(y=0, xmin=min(x), xmax=max(x), colors='r', linestyles='--', lw=1)

# # Show the plot
# plt.show()

# %%
