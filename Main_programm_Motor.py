# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 22:13:08 2021

@author: WMolina
"""
import pandas as pd
import numpy as np
import math as mt
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib import style
from colorama import init
from numpy.polynomial.polynomial import Polynomial
from pandas.core.indexes.base import Index
import locale 
locale.setlocale(locale.LC_ALL, 'de_DE.utf8')


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
Drehzahl = "" # Hier handelt es sich um die Drehzahl an einem Bemessungspunkt!!
while Drehzahl is not float:
    try:
        Drehzahl = float(locale.atof(input("Geben Sie die gewünschte Drehzahl in [1/min] ein: ")))
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

SpannungU1 = ""
while True:
    SpannungU1 = int(input("Bitte wählen Sie einen Spannungswert 400[V], 425[V] oder 200[V]: \n"))

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
    print("\n")
    Vv = int(input("Wählen Sie den Teilmotor: "))
    
    if Vv not in vv_values.values:
        print("Sie haben das falsch geschrieben, bitte versuchen es noch mal!")
    else:
        break
print("\n")

#------------------Basis-Berechnung mit Aussetzbetreib S3 & S6--------------------------------
Drehzahl_1 = Drehzahl/60
def Frequenz1(data,motor_modell): # Hier muss die Frequenz berechnet werden
    f = data[motor_modell]
    return ((Drehzahl*(f.loc['STK_Magnet']/2)))/60

def EisenVerluste(data,motor_modell):
    Pvfe = data[motor_modell]
    return (Pvfe.loc['VH']*(1/Frequenz1(Daten, Motor_Name))+Pvfe.loc['VW']*(1/Frequenz1(Daten, Motor_Name))**Pvfe.loc['a'])*(Pvfe.loc['Bmax'])

def EisenVerluste1(data,motor_modell):
    Pfe = data[motor_modell]
    return (Pfe.loc['kb']*Pfe.loc['mb']*(EisenVerluste(Daten, Motor_Name)))
    
Motor_Laenge = ""
while Motor_Laenge is not float:
    try:
        Motor_Laenge = int(input("Geben Sie die Länge X in mm ein: "))       
        break 
    except ValueError:
        print("Sie haben das falsch geschrieben, bitte versuchen es noch mal!")

def Kupferverlust(data, motor_modell):
    Pcu = data[motor_modell]
    return (Delta_Teta_gesamt*(Pcu.loc["Rwk"]+Pcu.loc["Rwb"]+Pcu.loc["Rbk"])-Pcu.loc["Rbk"]*(EisenVerluste1(Daten, Motor_Name)))/(Pcu.loc["Rwk"]*(Pcu.loc["Rwb"]+Pcu.loc["Rbk"]))

def KaltwiderstandX(data, motor_modell):
    R1kxs = data[motor_modell]
    return ((R1kxs.loc["R_Strang"]*R1kxs.loc["Want"]+(1-R1kxs.loc["Want"])*R1kxs.loc["R_Strang"])*(Motor_Laenge/100))  

def thermischer_Gesamtwiderstand(data, motor_modell):
    Rthx = data[motor_modell]
    return Rthx.loc["Rth"]*(100/Motor_Laenge)

R1kx = (KaltwiderstandX(Daten,Motor_Name)/Vv**2)
R1w = R1kx * (1+0.004*Delta_Teta_gesamt)
Strangstrom = mt.sqrt((Kupferverlust(Daten, Motor_Name))/(3*R1w))

#---------------Basis-Berechnung des Spannungskonstante---------------------------------------
def Spannungskonstante(data, motor_modell):
    Ku = data[motor_modell]
    return (((Ku.loc['Flussscheiteltwert'])*2*0.93*Ku.loc['N1_Innenspule']*(Ku.loc['STK_Magnet']/2))*(Ku.loc['Nutflaeche_Anzahl']/(3*2*Vv))*((Ku.loc['KorrekturFaktor']/1.4142))/1000)

# muss die Einheit der Frequenz ändert
Up = (Spannungskonstante(Daten, Motor_Name)*2*np.pi*(Drehzahl_1))

#---------------Basis-Berechnung des Drehmomentkonstante---------------------------------------
def Drehmomentkonstante(data, motor_modell):
    KT = data[motor_modell]
    return 3*(Spannungskonstante(Daten, Motor_Name)/KT.loc['KorrekturFaktor'])

#---------------Basis-Berechnung der nmax---------------------------------------

n_max = ((SpannungU1)/(Spannungskonstante(Daten, Motor_Name)*2*np.pi))*60
print("\n")
print('nmax = {:.2f} [rpm]'.format(n_max))

#---------------Ergebnisse auf dem Screen---------------------------------------
print("\n")
print("Drehzahl in [1/s] = {:.3f}".format(Drehzahl_1))
print("\n")
print("Frequenz f = {:.3f} [1/s]".format(Frequenz1(Daten,Motor_Name)))
print("\n")
print('Pfe = {:.2f} [W]'.format(EisenVerluste1(Daten,Motor_Name)))
print("\n")
print('Pcu = {:.2f} [W]'.format(Kupferverlust(Daten,Motor_Name)))
print("\n")
print('R1kxs = {:.2f} [Ω]'.format(KaltwiderstandX(Daten,Motor_Name)))
print("\n")
print("R1kx = ", "{:.2f}".format(R1kx),"[Ω]")
print("\n")
print("R1w = ", "{:.2f}".format(R1w) ,"[Ω]")
print("\n") 
print('Rthx = {:.3f} [Ω]'.format(thermischer_Gesamtwiderstand(Daten,Motor_Name)))
print("\n")
print("Strangstrom = ","{:.2f}".format(Strangstrom),"[A]")
print("\n")
print("Spannungskonstante Ku = ","{:.2f} [Vs]".format(Spannungskonstante(Daten,Motor_Name)))
print("\n")
print("Polradspannung Up = ","{:.2f}".format(Up), "[V]")
print("\n")
print("Drehmomentkonstante KT = ","{:.2f} [Nm/A]".format(Drehmomentkonstante(Daten, Motor_Name)))
print("\n")
#---------------------Stromgrenze im Grunddrehzahlbereich-----------------------------------------

def Stromgrenze(data, motor_modell):
    Ld = data[motor_modell]
    return ((mt.sqrt((SpannungU1**2)-(Up**2)))/(2*np.pi*Ld.loc['Ld'])*1000)

print("Der Stromgrenze im Grunddrehzahlbereich I1g = {:.2f} [A]".format(Stromgrenze(Daten, Motor_Name)))



#---------------------Diagramme-----------------------------------------

def Diagramms(data, motor_modell):
    Wert = data[motor_modell]
    xmax = (n_max*(Wert.loc['STK_Magnet']/2))/60
    x = np.arange(0, xmax, 2)
    y1 = Spannungskonstante(Daten, Motor_Name)*2*np.pi*x 
    y2 = (Wert.loc['VH']*(1/x)+Wert.loc['VW']*(1/x)**Wert.loc['a'])*(Wert.loc['Bmax'])

    fig, axis = plt.subplots(2, figsize=(10,10)) 
    fig.suptitle("Diagramme")
    axis[0].plot(x,y1)
    axis[0].set_title("Up = f(n)")
    #axis[0].set_xlabel("Frequenz [1/s]")
    axis[0].set_ylabel("ind.Spannung [V]")
    axis[0].grid()
    
    axis[1].plot(x,y2, color="red")
    axis[1].set_title("Pvfe = f(n)")
    #axis[1].set_xlabel("Frequenz [1/s]")
    axis[1].set_ylabel("Eisenverluste [W/kg]")
    axis[1].grid()
    
    for ax in axis.flat:
        ax.set(xlabel='Frequenz [1/s]')
    
    for ax in axis.flat:
        ax.label_outer()
    
    plt.show()
Diagramms(Daten, Motor_Name)


    

    

