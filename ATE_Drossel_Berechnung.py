# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 16:37:09 2022

@author: WMolina
"""

from matplotlib import scale
import numpy as np
import math as mt
import matplotlib.pyplot as plt
import locale

locale.setlocale(locale.LC_ALL, 'de_DE.utf8')

print("\n----------------------Motordaten----------------------\n")

R_Strang = ""
while R_Strang is not float:
    try:
        R_Strang = float(locale.atof(input("Geben Sie den Wicklungswiderstand in [Ω] ein: ")))
        break 
    except ValueError:
        print("Sie haben das falsch geschrieben, bitte versuchen es noch mal!\n")
        
Ind = ""
while Ind is not float:
    try:
        Ind = float(locale.atof(input("Geben Sie den Ankerinduktivität ohne Drossel in [mH] ein: ")))
        break 
    except ValueError:
        print("Sie haben das falsch geschrieben, bitte versuchen es noch mal!\n")
        
Ind_Vordr = ""
while Ind_Vordr is not float:
    try:
        Ind_Vordr = float(locale.atof(input("Geben Sie den Wert der Drossel in [mH] ein: ")))
        break 
    except ValueError:
        print("Sie haben das falsch geschrieben, bitte versuchen es noch mal!\n")

ke = ""
while ke is not float:
    try:
        ke = float(locale.atof(input("Geben Sie den Wert Spannungskonstant ke ein: ")))
        break 
    except ValueError:
        print("Sie haben das falsch geschrieben, bitte versuchen es noch mal!\n")


print("\n-----------------------------------------------------------------\n")

print("Wählen Sie einen Punkt im Grunddrehzahlbereich: ")

print("\n-----------------------------------------------------------------\n")
FU_Spannung = ""
while FU_Spannung is not float:
    try:
        FU_Spannung = float(locale.atof(input("FU-Spannung [V]: ")))
        break 
    except ValueError:
        print("Sie haben das falsch geschrieben, bitte versuchen es noch mal!\n")

MotorSpannung = ""
while MotorSpannung is not float:
    try:
        MotorSpannung = float(locale.atof(input("Motorspanunng [V]: ")))
        break 
    except ValueError:
        print("Sie haben das falsch geschrieben, bitte versuchen es noch mal!\n")

Strom = ""
while Strom is not float:
    try:
        Strom = float(locale.atof(input("Strom [A]: ")))
        break 
    except ValueError:
        print("Sie haben das falsch geschrieben, bitte versuchen es noch mal!\n")
        
Frequenz = ""
while Frequenz is not float:
    try:
        Frequenz = float(locale.atof(input("Frequenz [1/s]: ")))
        break 
    except ValueError:
        print("Sie haben das falsch geschrieben, bitte versuchen es noch mal!\n")
        
Drehzahl = ""
while Drehzahl is not float:
    try:
        Drehzahl = float(locale.atof(input("Drehzahl [rpm]: ")))
        break 
    except ValueError:
        print("Sie haben das falsch geschrieben, bitte versuchen es noch mal!\n")

Leistung = ""
while Leistung is not float:
    try:
        Leistung = float(locale.atof(input("Leistung [kW]: ")))
        break 
    except ValueError:
        print("Sie haben das falsch geschrieben, bitte versuchen es noch mal!\n")
        
Drehmoment = ""
while Drehmoment is not float:
    try:
        Drehmoment = float(locale.atof(input("Drehmoment [Nm]: ")))
        break 
    except ValueError:
        print("Sie haben das falsch geschrieben, bitte versuchen es noch mal!\n")

#----------------------Berechnung S1-Betrieb-----------------------------------------

Ind_Gesamt = Ind + Ind_Vordr
R_Strang120 = R_Strang * 1.4
ke_Strang = ke / 1.732
Ohm_Verlust = 3 * Strom**2 * R_Strang120
Xh = (2*mt.pi*(Frequenz)*(Ind_Gesamt/1000))
#Fe_Verlust = Statorverluste - Ohm_Verlust
Up_Strang = (ke_Strang*Drehzahl)/1000
U_R1 = Strom * R_Strang120
U_xd = Xh * Strom #Mit Vorschaltdrossel
Kontrolle_FU_Sp = mt.sqrt((Up_Strang + U_R1)**2 + (U_xd)**2)*mt.sqrt(3)
Kontrol_I1 = Up_Strang/Xh

print("\n-----------------------------------------------------------------\n")

print("****Im Grunddrehzahlbereich Iq = I1****\n")
print("Pv_Ohm = ", "{:.2f}".format(Ohm_Verlust),"[W]\n")
#print("Pfe = ", "{:.2f}".format(Fe_Verlust),"[W]")
print("Up_Strang = ", "{:.2f}".format(Up_Strang),"[V]\n")
print("U_R1 = ", "{:.2f}".format(U_R1),"[V]\n")
print("U_xd = ", "{:.2f}".format(U_xd),"[V]\n")
print("Kontrol_FU_Sp= ", "{:.2f}".format(Kontrolle_FU_Sp),"[V]\n")
#print("Gesamte Eisenverlust = ","{:.2f}".format(PFGe),"[W/kg]")
print("Kontrol_I1= ","{:.2f}".format(Kontrol_I1),"[A]\n")
print("Hauptreaktanz Xh= ", "{:.2f}".format(Xh),"[Ω]")

print("\n----------------Hier können Sie einen neuen Wert für die Drossel geben:--------------------\n")

Berechnung =""
while True:
    Berechnung = input("***Drücken Sie 1 um den Drosselwert zu änder, sonst [Strg+c] Zum Beenden: ")
    NewInd = int(Berechnung)
    if NewInd == 1:
        NewL = ""
        while NewL is not float:
            try:
                NewL = float(locale.atof(input("Neuer Wert von L [mH] = ")))
                break 
            except ValueError:
                print("Sie haben das falsch geschrieben, bitte versuchen es noch mal!\n")
        
        Ind_Total = Ind + NewL
        Xh = (2*mt.pi*(Frequenz)*(Ind_Total/1000))
        Kontrol_I1 = Up_Strang/Xh
        U_xd = Xh * Strom 
        
        print("Die gesamte ankerinduktivität ist:", "{:.2f}".format(Ind_Total),"[mH]\n")
        print("Hauptreaktanz Xh= ", "{:.2f}".format(Xh),"[Ω]\n")
        print("Kontrol_I1= ","{:.2f}".format(Kontrol_I1),"[A]\n")
        print("U_xd = ", "{:.2f}".format(U_xd),"[V]\n")
        
    else:
        print("Sie haben das falsch geschrieben, bitte versuchen es noch mal!")
        


