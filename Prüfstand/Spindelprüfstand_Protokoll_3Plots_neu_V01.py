# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 11:19:49 2020

@author: JPHilger
"""
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import pandas as pd

#----------Eingabe des Dateinamen, der Endung sowie der Überspringenden Endungen----------
filename =  'M2_2000rpm_65Nm_30l_min'       # Name der Auszulesenden csv Datei
name     =  '-Test'                             # Zusatz zum Dateinamen
legend   = 18                                   # Wie viele Zeilen am Anfang übersprungen werden sollen

#----------Einlesen und Ausgeben der Legende----------
df_legend = pd.read_csv("C:/Users/wmolina/Desktop/GUI/Prüfstand/data/" + str(filename) + '.csv' ,sep=",",nrows=legend-2, encoding = 'latin2')
print('Überschriften der Einzelnen Kanäle:')
print(list(df_legend.columns))
print('Zuordnung der Sensoren in den Signal/key Spalten:')
print(df_legend[['Signal','key','description']])

#----------Einlesen der Messdaten und Umrechnen der Zeit----------
df = pd.read_csv("C:/Users/wmolina/Desktop/GUI/Prüfstand/data/" + str(filename) + '.csv', sep=",", skiprows = legend, encoding = 'latin2') #, encoding = 'latin2'
df.insert(loc = 1, column = 'time [min]', value= df['time'].apply(lambda x: x/60))
df.insert(loc = 1, column = 'time [h]', value= df['time'].apply(lambda x: x/3600))
print(df)

#----------Festlegen des Styles für die Drehzahl-------
spindel_speed =                 df['f2\s3']
spindel_speed_color =           "red"
spindel_speed_linestyle =       "-."
spindel_speed_line_width =      2
spindel_speed_label =           'Spindeldrehzahl [1/min]'
sec_y_axs_label =               'Drehzal [1/min]'

#---------Festlegend der Paramter für die Zeitachse
time =                          df['time [min]']
x_axs_label =                   str('time [min]')
xaxs_set_lim =                 25

#----------Festlegen der Variablen zum Plotten-----------
front_bearing_temperature =     df['f7\s12']
rear_bearing_temperature =      df['f8\s13']
spindel_motor_temperatur =      df['f1\s1']
#spindle_growth =                df['f12\s2']

cooling_flow_rate_VL =      df['f13\s16']
cooling_VL          =      df['f14\s10']
cooling_RL          =      df['f15\s11']

actual_torque_value   =    df['f6\s9']

output_voltage       =    df['f3\s5']

actual_current_feld    = df['f4\s7']
actual_current_moment  = df['f5\s8']

########################################################
#---------ab hier die Darstellung des Diagrams----------
fig, axs = plt.subplots(3, 1, figsize=(25, 15))     #hier 3 untereinander, eine Spalte

#----------Plotten der Verschiedene Linien----------
axs[0].plot(time, front_bearing_temperature,    label='Frontlager Temperatur')
axs[0].plot(time, rear_bearing_temperature,     label='Loslager Temperatur')

axs[0].plot(time, cooling_flow_rate_VL,     label='Kühlung Durchflussmenge VL')
axs[0].plot(time, cooling_VL,               label='Kühlung Temperatur VL')
axs[0].plot(time, cooling_RL,               label='Kühlung Temperatur RL')

axs[1].plot(time, spindel_motor_temperatur ,    label='Motor Temperatur')
#axs[1].plot(time, spindle_growth,               label='Spindelwachstum')
#axs[2].plot(time, spindle_growth,               label='Umwucht')

axs[1].plot(time, actual_torque_value ,    label='Drehmomentistwert')
axs[1].plot(time, output_voltage ,         label='Ausgangsspannung')
axs[2].plot(time, actual_current_feld ,    label='Stromistwert feldbildend')
axs[2].plot(time, actual_current_moment ,  label='Stromistwert momentenbildend')

#----------Festlegen der Überschriften, Achsbeschriftungen, Grenzen der Achsen, Einteilung der Achsen----------
fig.suptitle((filename + name), fontsize=24, y =1.00)

axs[0].set_title("Temperaturen")
axs[1].set_title("")
axs[2].set_title("Stromistwerte")

axs[0].set_xlabel(x_axs_label)
axs[1].set_xlabel(x_axs_label)
axs[2].set_xlabel(x_axs_label)

axs[0].set_ylabel("Temperatur [°C]")
axs[1].set_ylabel('Drehmoment []')
axs[1].set_ylabel('Motor Temperatur []')
axs[2].set_ylabel('Strom []')

axs[0].set_xlim(0,xaxs_set_lim) 
axs[1].set_xlim(0,xaxs_set_lim) 
axs[2].set_xlim(0,xaxs_set_lim) 

axs[0].set_ylim([0,50])

axs[0].yaxis.set_major_locator(plticker.MultipleLocator(base=5)) 

#----------Plotten der Sekundärachse----------
axsd= axs[0].twinx()
axsd.plot(time, spindel_speed, color = spindel_speed_color, linestyle = spindel_speed_linestyle, lw= spindel_speed_line_width , label= spindel_speed_label)
axsd.set_ylabel(sec_y_axs_label)
axsd= axs[1].twinx()
axsd.plot(time, spindel_speed, color = spindel_speed_color, linestyle = spindel_speed_linestyle, lw= spindel_speed_line_width , label= spindel_speed_label)
axsd.set_ylabel(sec_y_axs_label)
axsd= axs[2].twinx()
axsd.plot(time, spindel_speed, color = spindel_speed_color, linestyle = spindel_speed_linestyle, lw= spindel_speed_line_width , label= spindel_speed_label)
axsd.set_ylabel(sec_y_axs_label)

#----------Definition des Gitternetzes----------
axs[0].legend(loc='upper left', bbox_to_anchor=(0, -0.13),ncol=10)
axs[1].legend(loc='upper center', bbox_to_anchor=(0.1, -0.05),ncol=10)
axs[2].legend(loc='upper center', bbox_to_anchor=(0.1, -0.05),ncol=10)

axs[0].grid(b=True, which='major', color='#666666', linestyle='-')#Gitternetz Show the major grid lines with dark grey lines
axs[0].minorticks_on()# Show the minor grid lines with very faint and almost transparent grey lines
axs[0].grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

axs[1].grid(b=True, which='major', color='#666666', linestyle='-')#Gitternetz Show the major grid lines with dark grey lines
axs[1].minorticks_on()# Show the minor grid lines with very faint and almost transparent grey lines
axs[1].grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

axs[2].grid(b=True, which='major', color='#666666', linestyle='-')#Gitternetz Show the major grid lines with dark grey lines
axs[2].minorticks_on()# Show the minor grid lines with very faint and almost transparent grey lines
axs[2].grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

fig.tight_layout()

#----------Anzeigen und Abspeichern des Diagramms----------
plt.show()
fig.savefig("C:/Users/wmolina/Desktop/GUI/Prüfstand/plot/" + str(filename) + str(name) + '.pdf')