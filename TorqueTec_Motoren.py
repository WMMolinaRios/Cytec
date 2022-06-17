"""@author: WMolina"""
from calendar import day_abbr
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


# Einlesen der CSV-Datei: Hier gehen Sie bitte zuerst dorthin, wo Sie die csv-Datei haben. Klicken Sie auf die Shift-Taste und die rechte Maustaste. Und im Menü suchen Sie nach: Als Pfad kopieren. Zum Schluss kopieren Sie den pfad hier in die Variable Daten.
Daten = pd.read_csv('C:/Users/wmolina/Desktop/Python/TechnoTable.csv',delimiter=';', index_col='Parameter',decimal=',').fillna('')
print(Daten)

Daten[["200HX", "200UHX", "240HX", "240UHX", "310HX", "310UHX", "360UHX", "410HX", "410UHX", "564HX"]] = Daten[["200HX", "200UHX", "240HX", "240UHX", "310HX", "310UHX", "360UHX", "410HX", "410UHX", "564HX"]].apply(pd.to_numeric).fillna('')

#--------------------------------- Motorauswahl ---------------------------------#
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

print("\n")
print("-------------------------------------Variable Eingaben-------------------------------------\n")

#--------------------------------- Eingangsvariablen ---------------------------------#
Temp_Wicklung = ""
while Temp_Wicklung is not float:
    try:
        Temp_Wicklung = int(input("Geben Sie die max. Wicklungstemperatur in °C ein: "))
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

SpannungU1 = ""
while True:
    try:
        SpannungU1 = float(input("Bitte wählen Sie einen Spannungswert 400[V], 425[V] oder 200[V]: \n")) #Leiter-Leiter Spannung

        if SpannungU1 == 400 or SpannungU1 == 425 or SpannungU1 ==200:
            print(f"Der gewählte Spannungswert ist: {SpannungU1} [V]")
            break
        else:
            print("Sie haben das falsch geschrieben, bitte versuchen es noch mal!")
    except:
        print("Das war keine Zahl!!")

U1 = SpannungU1/1.732 # Strangspannung
#Hier sucht das Programm die verfügbaren Optionen für die Verschaltung Vv in Abhängigkeit vom Motor_Name
print("\n")
vv_keys = ["Seriel", "2TM", "3TM", "4TM", "5TM", "6TM", "8TM", "10TM", "12TM"]
vv_values = Daten[Motor_Name][vv_keys]
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

Motor_Laenge = ""
while Motor_Laenge is not float:
    try:
        Motor_Laenge = int(input("Geben Sie die Länge X in mm ein: "))       
        break 
    except ValueError:
        print("Sie haben das falsch geschrieben, bitte versuchen es noch mal!")
print("\n")

Drehzahl = "" # Hier handelt es sich um die Drehzahl an einem Bemessungspunkt!!
while Drehzahl is not float:
    try:
        Drehzahl = float(locale.atof(input("Geben Sie die gewünschte Drehzahl in [1/min] ein: ")))
        break
    except ValueError:
        print("Sie haben das falsch geschrieben, bitte versuchen es noch mal!")
print("\n")

#--------------------------------- Basis-Berechnung ---------------------------------#

Delta_Teta_gesamt =  Temp_Wicklung - Temp_Kühlung
print("Delta Teta gesamt ist:",Delta_Teta_gesamt, "[K]\n")

Drehzahl_1 = Drehzahl/60 # Es wird in 1/s umgewandelt
def Frequenz1(data,motor_modell): # Hier muss die Frequenz berechnet werden
    f = data[motor_modell]
    return ((Drehzahl*(f.loc['STK_Magnet']/2)))/60

def EisenVerluste(data,motor_modell): # Spezifische Eisenverluste pro Kg
    Pvfe = data[motor_modell]
    return (Pvfe.loc['VH']*(Frequenz1(Daten, Motor_Name)/50)+Pvfe.loc['VW']*(Frequenz1(Daten, Motor_Name)/50)**Pvfe.loc['a'])*(Pvfe.loc['Bmax']**Pvfe.loc['b'])

def EisenVerluste1(data,motor_modell): # Masse des Blechpaketes ohne die Masse der Kühlhülse ??
    Pfe = data[motor_modell]
    return (Pfe.loc['kb']*Pfe.loc['mb']*(EisenVerluste(Daten, Motor_Name)))

# Stationäre Kennlinien: Das Modell wird ohne die Kapazitäten betrachtet und wird hauptsächlich die Eisen- und Kupferverluste berücksichtigen.
def Kupferverlust(data, motor_modell):
    Pcu = data[motor_modell]
    return (Delta_Teta_gesamt*(Pcu.loc["Rwk"]+Pcu.loc["Rwb"]+Pcu.loc["Rbk"])-Pcu.loc["Rbk"]*(EisenVerluste1(Daten, Motor_Name)))/(Pcu.loc["Rwk"]*(Pcu.loc["Rwb"]+Pcu.loc["Rbk"]))

def KaltwiderstandX(data, motor_modell): # Berechnung des ohmnischen Widerstand mit der Anpassung der Motorlänge
    R1kxs = data[motor_modell] # Want = Anteil des Wicklekopfkupfers
    return ((R1kxs.loc["R_Strang"]*R1kxs.loc["Want"]+(1-R1kxs.loc["Want"])*R1kxs.loc["R_Strang"])*(Motor_Laenge/100))  
R1kx = (KaltwiderstandX(Daten,Motor_Name)/Vv**2) # gesamter Kalt-Widerstand
R1w = R1kx * (1+0.004*Delta_Teta_gesamt)# Warmwiderstand

def thermischer_Gesamtwiderstand(data, motor_modell): # Anpassung des thermischen Widerstandes
    Rthx = data[motor_modell]
    return Rthx.loc["Rth"]*(100/Motor_Laenge)

# Im Grunddrehzahlbereich
Bemessungsstrom = np.sqrt((Kupferverlust(Daten, Motor_Name))/(3*R1w))        

# def Stromgrenze(data, motor_modell):
#     I1g = data[motor_modell]
#     return ((np.sqrt((U1**2)-(Up_strang**2)))/(2*np.pi*Frequenz1(Daten, Motor_Name)*I1g.loc['Ld'])*1000)

def Spannungskonstante(data, motor_modell): # Berechnung des Spannungskonstante
    Ku = data[motor_modell]
    return (((Ku.loc['Flussscheiteltwert'])*2*0.93*Ku.loc['N1_Innenspule']*(Ku.loc['STK_Magnet']/2))*(Ku.loc['Nutflaeche_Anzahl']/(3*2*Vv))*((Ku.loc['KorrekturFaktor']/1.4142))/1000)

Up_strang = (Spannungskonstante(Daten, Motor_Name)*2*np.pi*(Drehzahl_1)) # muss die Einheit der Drehzahl in 1/s verwendet

def Drehmomentkonstante(data, motor_modell): # Berechnung des Drehmomentkonstante
    KT = data[motor_modell]
    return 3*(Spannungskonstante(Daten, Motor_Name)/KT.loc['KorrekturFaktor'])

n_max = ((SpannungU1)/(Spannungskonstante(Daten, Motor_Name)*2*np.pi))*60

# Berechnung der Koeffizienten:
def Mabs(data, motor_modell):
    M_abs = data[motor_modell]
    return M_abs.loc['Mabs']*(Motor_Laenge/100)

def Mlin(data, motor_modell):
    M_lin = data[motor_modell]
    return (M_lin.loc['Mlin'])*(Motor_Laenge/100)*(np.sqrt(2)*(M_lin.loc['N1_Innenspule'])/Vv)

def Mquad(data, motor_modell):
    M_quad = data[motor_modell]
    return M_quad.loc['Mquad']*(Motor_Laenge/100)*(np.sqrt(2)*(M_quad.loc['N1_Innenspule'])/Vv)**2

# Drehmmoment:
M_1 = Mquad(Daten, Motor_Name)*(Bemessungsstrom)**2 + Mlin(Daten, Motor_Name)*Bemessungsstrom + Mabs(Daten, Motor_Name)


#--------------------------------- Ergebnisse auf dem Screen ---------------------------------#
print("\n")
print("Drehzahl in [1/s] = {:.3f}".format(Drehzahl_1))
print("\n")
print('nmax = {:.2f} [rpm]'.format(n_max))
print("\n")
print("Frequenz f = {:.3f} [1/s]".format(Frequenz1(Daten,Motor_Name)))
print("\n")
print('Pvfe pro kg = {:.2f} [W/kg]'.format(EisenVerluste(Daten,Motor_Name)))
print("\n")
print('Pv_fe = {:.2f} [W]'.format(EisenVerluste1(Daten,Motor_Name)))
print("\n")
print('Pv_cu = {:.2f} [W]'.format(Kupferverlust(Daten,Motor_Name)))
print("\n")
print('R1kxs = {:.2f} [Ω]'.format(KaltwiderstandX(Daten,Motor_Name)))
print("\n")
print("R1kx = ", "{:.2f}".format(R1kx),"[Ω]")
print("\n")
print("R1w = ", "{:.2f}".format(R1w) ,"[Ω]")
print("\n") 
print('Rthx = {:.3f} [Ω]'.format(thermischer_Gesamtwiderstand(Daten,Motor_Name)))
print("\n")
print("Bemessungsstrom = ","{:.2f}".format(Bemessungsstrom),"[A]")
print("\n") #print("Der Stromgrenze im Grunddrehzahlbereich I1g = {:.2f} [A]".format(Stromgrenze(Daten, Motor_Name)))
print("Spannungskonstante Ku = ","{:.2f} [Vs]".format(Spannungskonstante(Daten,Motor_Name)))
print("\n")
print("Polradspannung Up_str = ","{:.2f}".format(Up_strang), "[V]")
print("\n")
print("Drehmomentkonstante KT = ","{:.2f} [Nm/A]".format(Drehmomentkonstante(Daten, Motor_Name)))
print("\n")
print("Der Koeffizient Am = ", "{:.3f}".format(Mquad(Daten, Motor_Name)))
print("\n")
print("Der Koeffizient Bm = ", "{:.3f}".format(Mlin(Daten, Motor_Name)))
print("\n")
print("Der Koeffizient Cm = ", "{:.5f}".format(Mabs(Daten, Motor_Name)))
print("\n")
print("Drehmoment1 = ","{:.5f}".format(M_1),"[Nm]")
print("\n")

#--------------------------------- Diagramme ---------------------------------#
def Diagramm1(data, motor_modell):
    Wert = data[motor_modell]
    
    xmax = n_max/60 # Drehazhl wird in 1/s umgerechnet
    x = np.arange(0.1, xmax, 0.01) # Drehzahlwerte
            
    y1 = Spannungskonstante(Daten, Motor_Name)*2*np.pi*x 
    
    plt.figure(figsize=(9, 5), dpi=80)
    plt.title("Induzierte Spannung")
    plt.plot(x, y1, color="blue", label="Up(n)")
    plt.legend(loc="best")
    plt.xlabel("Drehzahl [1/s]")
    plt.ylabel("Up-Strang [V]")
    plt.grid()

    xmax1 = xmax*(Wert.loc['STK_Magnet']/2) # Frequenz wird von Drehzahl berechnet.
    x1 = np.arange(0.1, xmax1, 0.5) # Frequenzwerte
    
    y2 = Wert.loc['kb']*Wert.loc['mb']*(Wert.loc['VH']*(x1/50)+Wert.loc['VW']*(x1/50)**Wert.loc['a'])*Wert.loc['Bmax']**Wert.loc['b']
    
    plt.figure(figsize=(9, 5), dpi=80)
    plt.title("Eisenverlust")
    plt.plot(x1, y2, color="orange", label="Pvfe(f)")
    plt.legend(loc="best")
    plt.xlabel("Frequenz [1/s]")
    plt.ylabel("Pv_fe [W]")
    plt.grid()

    y3 = (Delta_Teta_gesamt*(Wert.loc["Rwk"]+Wert.loc["Rwb"]+Wert.loc["Rbk"])-Wert.loc["Rbk"]*(y2))/(Wert.loc["Rwk"]*(Wert.loc["Rwb"]+Wert.loc["Rbk"]))
    
    plt.figure(figsize=(9, 5), dpi=80)
    plt.title("Kupferverlust")
    plt.plot(x1, y3, color="orange", label="Pvcu(f)")
    plt.legend(loc="best")
    plt.xlabel("Frequenz [1/s]")
    plt.ylabel("Pv_cu [W]")
    plt.grid()

    # y4 = ((np.sqrt((U1**2)-((Spannungskonstante(Daten, Motor_Name)*2*np.pi*x1)**2)))/(2*np.pi*x1*Wert.loc['Ld'])*1000)

    # plt.figure(figsize=(9, 5), dpi=80)
    # plt.title("Grenzstrom")
    # plt.plot(x1, y4, color="red", label="I1g(f)")
    # plt.legend(loc="best")
    # plt.xlabel("Frequenz [1/s]")
    # plt.ylabel("I_1g [A]")
    # plt.grid()

    y5 = np.sqrt(((Delta_Teta_gesamt*(Wert.loc["Rwk"]+Wert.loc["Rwb"]+Wert.loc["Rbk"])-Wert.loc["Rbk"]*(y2))/(Wert.loc["Rwk"]*(Wert.loc["Rwb"]+Wert.loc["Rbk"])))/(3*R1w))
    
    plt.figure(figsize=(9, 5), dpi=80)
    plt.title("Bemesungsstrom")
    plt.plot(x1, y5, color="red", label="I1(f)")
    plt.legend(loc="best")
    plt.xlabel("Frequenz [1/s]")
    plt.ylabel("I1 [A]")
    plt.grid()

    x2 = np.arange(250, 3750, 15)
    y6 = Mquad(Daten, Motor_Name)*(x2)**2 + Mlin(Daten, Motor_Name)*x2 + Mabs(Daten, Motor_Name)
    plt.figure(figsize=(9, 5), dpi=80)
    plt.title("Drehmoment")
    plt.plot(x2, y6, color="red", label="M(I1)")
    plt.legend(loc="best")
    plt.xlabel("Strom [A]")
    plt.ylabel("Drehmoment [Nm]")
    plt.grid()
    
    plt.show()   
Diagramm1(Daten, Motor_Name)