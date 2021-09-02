# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 11:34:20 2021

@author: WMolina
"""

"""
Dieses Programm dient dem besseren Verständnis von ATE-Motoren und deren Eisenverlusten.
"""
from matplotlib import scale
import numpy as np
import math as mt
import matplotlib.pyplot as plt
import locale
from colorama import init
from numpy.polynomial.polynomial import Polynomial

locale.setlocale(locale.LC_ALL, 'de_DE.utf8')

print("\n----------------------Motorgröße1----------------------\n")
Stapelfaktor = 0.95
Außen_DM = float(locale.atof(input("Bitte geben Sie den Außen Durchmesser in mm ein: \n")))
Innen_DM = float(locale.atof(input("Bitte geben Sie den Innen Durchmesser in mm ein: \n")))
Laenge = float(locale.atof(input("Bitte geben Sie die Länge in mm ein: \n")))

print("\n----------------------Motorgröße2----------------------\n")

Gesamt_Volumen = mt.pi / 4*((Außen_DM/100)**2 - (Innen_DM/100)**2)*(Laenge/100)
print("Das Gesamtvolumen ist: {:.4f} [dm^3]".format(Gesamt_Volumen))
Blechvolumen = Gesamt_Volumen * Stapelfaktor
print("Das Blechvolumen ist: {:.4f} [dm^3]".format(Blechvolumen))
Gesamt_Gewicht = Blechvolumen*7.6*0.6
print("Das Gewicht ist: {:.4f} [kg]".format(Gesamt_Gewicht))

print("\n----------------------Motorwerte----------------------\n")

R_Strang = float(locale.atof(input("Geben Sie den Wicklungswiderstand in [Ω] ein: ")))
Ind = float(locale.atof(input("Geben Sie den Ankerinduktivität ohne Drossel in [mH] ein: ")))
Ind_mit_Vordr = float(locale.atof(input("Geben Sie den Ankerinduktivität mit Drossel in [mH] ein: ")))
R_Strang120 = R_Strang * 1.4
ke = float(locale.atof(input("Geben Sie den Wert Spannungskonstant ke ein: ")))
ke_Strang = ke / 1.732

Berechnung =""
while True:
    Berechnung = input("Wählen Sie einen Punkt im Grunddrehzahlbereich (1) oder Feldschwächbereich (2) aus. Zum Beenden [Strg+c] ")

    if Berechnung == "1":
        print("\n----------------------Grunddrehzahlbereich----------------------\n")

        ATE_Angabe_S1 = [[], [], [], [], [], [], [], [], []]

        Größe = 1
        for i in range(Größe):
            print("Geben Sie die Werte von S1:", i + 1)
            FU_Spannung = int(input("FU-Spannung [V]: "))
            MotorSpannung = int(input("Motorspanunng [V]: "))
            Strom = float(locale.atof(input("Strom [A]: ")))
            Frequenz = float(locale.atof(input("Frequenz [1/s]: ")))
            Drehzahl = float(locale.atof(input("Drehzahl [rpm]: ")))
            Leistung = float(locale.atof(input("Leistung [kW]: ")))
            Drehmoment = float(locale.atof(input("Drehmoment [Nm]: ")))
            Statorverluste = float(locale.atof(input("Statorverluste [W]: ")))

            ATE_Angabe_S1[0].append(FU_Spannung)
            ATE_Angabe_S1[1].append(MotorSpannung)
            ATE_Angabe_S1[2].append(Strom)
            ATE_Angabe_S1[3].append(Frequenz)
            ATE_Angabe_S1[4].append(Drehzahl)
            ATE_Angabe_S1[5].append(Leistung)
            ATE_Angabe_S1[6].append(Drehmoment)
            ATE_Angabe_S1[8].append(Statorverluste)
        # print(ATE_Angabe_S1)

            Ohm_Verlust = 3 * Strom**2 * R_Strang120
            print("Pv_Ohm = ", "{:.2f}".format(Ohm_Verlust),"[W]")
            Fe_Verlust = Statorverluste - Ohm_Verlust
            print("Pfe = ", "{:.2f}".format(Fe_Verlust),"[W]")
            print("Im Grunddrehzahlbereich Iq = I1")
            Up_Strang = (ke_Strang*Drehzahl)/1000
            print("Up_Strang = ", "{:.2f}".format(Up_Strang),"[V]")
            U_R1 = Strom * R_Strang120
            print("U_R1 = ", "{:.2f}".format(U_R1),"[V]")
            print("\n")
            NewValue = input("Wenn Sie einen neuen Wert für L eingeben möchten, drücken Sie 1 sonst 2: ")
            NewValue = int(NewValue)
            if NewValue == 1:
                NewL = float(input("Neuer Wert von L [mH] = "))  
                U_xd = (2*mt.pi*(Frequenz)*((NewL+Ind)/1000))*Strom 
                print("U_xd = ", "{:.2f}".format(U_xd),"[V]")  
            else:               
                U_xd = (2*mt.pi*(Frequenz)*(Ind_mit_Vordr/1000))*Strom #Mit Vorschaltdrossel
                print("U_xd = ", "{:.2f}".format(U_xd),"[V]")
            Kontrolle_FU_Sp = mt.sqrt((Up_Strang + U_R1)**2 + (U_xd)**2)*mt.sqrt(3)
            print("K_FU_Sp= ", "{:.2f}".format(Kontrolle_FU_Sp),"[V]")
            PFGe = (1/Gesamt_Gewicht)*(((2**(-5))*Drehzahl**2)+0.1361*Drehzahl-120)
            print("Gesamte Eisenverlust = ","{:.2f}".format(PFGe),"[W/kg]")

            fig = plt.figure(figsize=(8,6))
            plt.quiver([0,0,0,0,1], [0,Up_Strang,(U_R1+Up_Strang),0,0], [0,0,-U_xd,-U_xd,0], [Up_Strang,U_R1,0,(U_R1+Up_Strang),Strom], angles='xy', scale_units='xy', scale=1, color=['black', 'purple', 'green', 'blue', 'red'])
            plt.xlim(-200, 10)
            plt.ylim(0, 200)
            plt.title("Zeiger-Diagramm Grunddrehzahlbereich", fontsize=10)
            plt.grid()
            plt.show()

            break

    elif Berechnung == "2":
        print("\n----------------------Feldschwächungbereich----------------------\n")

        ATE_Angabe_S1 = [[], [], [], [], [], [], [], [], []]

        Größe = 1
        for i in range(Größe):
            print("Geben Sie die Werte von S1:", i + 1)
            FU_Spannung = int(input("FU-Spannung [V]: "))
            MotorSpannung = int(input("Motorspanunng [V]: "))
            Strom = float(locale.atof(input("Strom [A]: ")))
            Frequenz = float(locale.atof(input("Frequenz [1/s]: ")))
            Drehzahl = float(locale.atof(input("Drehzahl [rpm]: ")))
            Leistung = float(locale.atof(input("Leistung [kW]: ")))
            Drehmoment = float(locale.atof(input("Drehmoment [Nm]: ")))
            Mag_Strom = float(locale.atof(input("Mag-Strom [A]: ")))
            Statorverluste = float(locale.atof(input("Statorverluste [W]: ")))
            

            ATE_Angabe_S1[0].append(FU_Spannung)
            ATE_Angabe_S1[1].append(MotorSpannung)
            ATE_Angabe_S1[2].append(Strom)
            ATE_Angabe_S1[3].append(Frequenz)
            ATE_Angabe_S1[4].append(Drehzahl)
            ATE_Angabe_S1[5].append(Leistung)
            ATE_Angabe_S1[6].append(Drehmoment)
            ATE_Angabe_S1[7].append(Mag_Strom)
            ATE_Angabe_S1[8].append(Statorverluste)
            # print(ATE_Angabe_S1)

            Ohm_Verlust = 3 * Strom**2 * R_Strang120
            print("Pv_Ohm = ", "{:.2f}".format(Ohm_Verlust),"[W]")
            Fe_Verlust = Statorverluste - Ohm_Verlust
            print("Pfe = ", "{:.2f}".format(Fe_Verlust),"[W]")
            Iq = mt.sqrt((Strom)**2-(Mag_Strom)**2)
            print("Iq = ", "{:.2f}".format(Iq),"[A]")
            Up_Strang = (ke_Strang*Drehzahl)/1000
            print("Up_Strang = ", "{:.2f}".format(Up_Strang),"[V]")
            U_R1 = Strom * R_Strang120
            print("U_R1 = ", "{:.2f}".format(U_R1),"[V]")
            NewValue = input("Wenn Sie einen neuen Wert für L eingeben möchten, drücken Sie 1 sonst 2: ")
            NewValue = int(NewValue)
            if NewValue == 1:
                NewL = float(locale.atof(input("Neuer Wert von L [mH] = ")))  
                U_xd = (2*mt.pi*(Frequenz)*((NewL+Ind)/1000))*Strom 
                print("U_xd = ", "{:.2f}".format(U_xd),"[V]")  
            else:               
                U_xd = (2*mt.pi*(Frequenz)*(Ind_mit_Vordr/1000))*Strom #Mit Vorschaltdrossel
                print("U_xd = ", "{:.2f}".format(U_xd),"[V]")
            Winkel_Up = np.arccos(Iq/Strom)*(180/mt.pi)
            print("Der Winkel zu Up = ", "{:.2f}".format(Winkel_Up),"[°]")
            Kontrolle_FU_Sp = mt.sqrt((Up_Strang + U_R1)**2 + (U_xd)**2)*mt.sqrt(3)
            print("K_FU_Sp= ", "{:.2f}".format(Kontrolle_FU_Sp),"[V]")
            PFGe = (1/Gesamt_Gewicht)*(((2**(-5))*Drehzahl**2)+0.1361*Drehzahl-120)
            print("Gesamte Eisenverlust = ","{:.2f}".format(PFGe),"[W/kg]")

            """
            fig = plt.figure(figsize=(8,6))
            plt.quiver([0,0,0,0,1], [0,Up_Strang,(U_R1+Up_Strang),0,0], [0,0,-U_xd,-U_xd,0], [Up_Strang,U_R1,0,(U_R1+Up_Strang),Strom], angles='xy', scale_units='xy', scale=1, color=['black', 'purple', 'green', 'blue', 'red'])
            plt.xlim(-500, 10)
            plt.ylim(0, 400)
            plt.title("Zeiger-Diagramm Grunddrehzahlbereich", fontsize=10)
            plt.grid()
            plt.show()
            """
            break

    else:
        print("Sie haben das falsch geschrieben, bitte versuchen es noch mal!")



    





    


        

