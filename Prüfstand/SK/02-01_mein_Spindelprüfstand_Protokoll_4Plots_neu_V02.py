# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 11:19:49 2020

@author: JPHilger

file_open und save_file dialoge eingebaut.
input_Data() eingefügt. 30.05.22
Messsignalauswahl eingefügt.Verarbeitung in read_data_make_plot.31.05.22
KommNr und weitere Inputs überprüfen 31.05.22
Schleife in SpeichernDialog wg. Datei Überschreiben 31.05.22
input_Data geändert. Prüfdatum hinzu (aktuelles Datum) und prüfen 01.06.22
Fehlerbehandlung bei Messwertedatei mit fehlenden Signalen oder falsche Formate. 01.06.22
Ermitteln des aktuellen Scriptpfad hinzu, für einbindung Fehlerbild bei Messwertedatei mit falschen Signalen. 07.06.2022
"""
import traceback

import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import pandas as pd

import easygui as eg
import sys
import os

import datetime

#Messwertedatei öffnen
def file_open_dialogs():
    Excel_Path = eg.fileopenbox(msg = "Bitte die Messwerte-Datei auswählen", default = "*.csv")
    if Excel_Path == None:
        sys.exit()
    return Excel_Path

#Datei speichern Dialog mit Überprüfung Datei überschreiben
def save_file_dialogs(default_filename, extension = "png"):
    saveornot = eg.buttonbox(msg="Soll die Datei gespeichert werden?",choices = ("No", "Yes") )
    if saveornot == "Yes":
        while 1:
            filename = eg.filesavebox(msg = "Dateiname eingeben (die Erweiterung %s wird automatisch angehängt)?" %(extension), default = default_filename)
            if filename is None:
                return None
            filename = filename + "." + extension
            if os.path.exists(filename):
                ok_to_overwrite = eg.buttonbox(msg="Datei %s besteht bereits. Überschreiben?" %(filename), choices = ("No", "Yes") )
                if ok_to_overwrite == "Yes":
                    return filename
                    break
                elif ok_to_overwrite == "No":
                    continue
            else:
                return filename
    else:
        return None

# Eingabe Spindeldaten
def input_Data():
    now = datetime.datetime.now()
    today = now.strftime('%d.%m.%Y')
    
    #Eingabe von allgemeinen Spindeldaten
    msg = "Geben sie Verwaltungsinformationen ein."
    title = "Allgemeine Angaben"
    fieldNames = ["Kundenname", 
                  "Kommissionsnummer", 
                  "Spindelbezeichnung", 
                  "AS-Nr.", 
                  "Motorbez.", 
                  "DBL.Nr. 204-", 
                  "Nennleistung", 
                  "Nenndrehzahl", 
                  "max.Drehzahl", 
                  "Prüfdatum", 
                  "Prüfer/in"]
    
    fieldValues = ["KuNA","123456","CS/HSKA063/034W/240F-0841","0815","0070027200","0002","34","4530","24000",today,"ich"]  # Vorbelegung der Eingabefelder # nur für Faulheit
    #fieldValues = ["","","","","","","","","",today,""]  # Vorbelegung der Eingabefelder # soll verwendet werden
    fieldValues = eg.multenterbox(msg,title,fieldNames,fieldValues)
    
    # make sure that none of the fields was left blank and has correct input
    while 1:
        if fieldValues is None: #wenn Button Cancel
            eg.msgbox(msg='Abbruch durch Benutzer!', title='Benutzerabbruch', ok_button='OK', image=None, root=None)
            sys.exit()
        errmsg = ""
        #Überprüfen ob alle Felder ausgefüllt
        for i in range(len(fieldNames)):
            if fieldValues[i].strip() == "":
                errmsg += ('"%s" ist eine erforderliche Eingabe.\n\n' % fieldNames[i])
        #Länge der Kommnr. überprüfen. Muss = 6
        if len(fieldValues[1]) != 6:
            errmsg += ('Die Kommissionsnr. muß eine 6-Stellige Zahl sein!\n')
        #Überprüfen von KommNr. auf Ganzzahl.
        try: int(fieldValues[1])
        except ValueError: errmsg += ('Die Kommissionsnr. darf nur Ziffern enthalten!\n')
        #Länge der AS-Nr. überprüfen. Muss = 4
        if len(fieldValues[3]) != 4:
            errmsg += ('Die AS-Nr. muß eine 4-Stellige Zahl sein!\n')
        #Überprüfen von AS-Nr. auf Ganzzahl.
        try: int(fieldValues[3])
        except ValueError: errmsg += ('Die AS-Nr. darf nur Ziffern enthalten!\n')
        #Länge der DBL-Nr. überprüfen. Muss = 4
        if len(fieldValues[5]) != 4:
            errmsg += ('Die DBL-Nr. muß eine 4-Stellige Zahl sein!\n')
        #Überprüfen von DBL-Nr. auf Ganzzahl.
        try: int(fieldValues[5])
        except ValueError: errmsg += ('Die DBL-Nr. darf nur Ziffern enthalten sein!\n')
        #Länge der Nennleistung überprüfen. Muss <4
        if len(fieldValues[6]) > 3:
            errmsg += ('Nennleistung zu groß. Max. 3-Stellig!\n')
        #Überprüfen von Nennleistung auf Ganzzahl.
        try: int(fieldValues[6])
        except ValueError: errmsg += ('Die Nennleistung darf nur Ziffern enthalten!\n')
        #Länge der Nennldrehzahl überprüfen. Muss <5
        if len(fieldValues[7]) > 5:
            errmsg += ('Nennldrehzahl zu groß. Max. 5-Stellig!\n')
        #Überprüfen von Nenndrehzahl auf Ganzzahl.
        try: int(fieldValues[7])
        except ValueError: errmsg += ('Die Nennldrehzahl darf nur Ziffern enthalten!\n')
        #Länge der max.Drehzahl überprüfen. Muss <5
        if len(fieldValues[8]) > 5:
            errmsg += ('max.Drehzahl zu groß. Max. 5-Stellig!\n')
        #Überprüfen von max.Drehzahl auf Ganzzahl.
        try: int(fieldValues[8])
        except ValueError: errmsg += ('Die max.Drehzahl darf nur Ziffern enthalten!\n')
        #Überprüfen von Prüfdatum.
        try:
            d = datetime.datetime.strptime(fieldValues[9],'%d.%m.%Y') #wandelt string in Datum
            datetime.datetime.date(d) # prüft Datum auf Gültigkeit.
            if d < datetime.datetime(2022,1,1) or d > datetime.datetime.now(): #Prüft Datum auf Zeitbereich
                raise(ValueError)# Fehler werfen.
        except ValueError: errmsg += ('Prüfdatum ist falsch!\ndas Datum muss zwischen 01.01.2022 und heute liegen.\n')
        
        #wenn keine Probleme
        if errmsg == "":
            break # no problems found
        fieldValues = eg.multenterbox(errmsg, title, fieldNames, fieldValues)
    
    spinDat = dict(zip(fieldNames, fieldValues))
    #print('Spindelbezeichnung = ' + spinDat['Spindelbezeichnung']) #DEBUG
    
    spinType = eg.choicebox(msg='Pick an item', title='', choices=['Synchron', 'Asynchron'], preselect=0)
    #print(spinType) #DEBUG
    if spinType == None:
        eg.msgbox(msg='Abbruch durch Benutzer!', title='Benutzerabbruch', ok_button='OK', image=None, root=None)
        sys.exit()
        
    return (spinDat, spinType)

# Auswahl der Messsignale
def signal_Choice():
    pre_measuring_signals = ['Motortemp r35', 
                         'Drehzahlistwert r21', 
                         'Ausgangsspannung r25', 
                         'Stromistwert feldbildend r29', 
                         'Stromistwert momentenbildend r30', 
                         'Drehmomentistwert r80', 
                         'PT100_Frontlager_Ch1_4AI', 
                         'PT100_DD Test aufgespritzte_CH3_4AI', 
                         'Längenausdehnung vorne 1 DB130.DBD682', 
                         'PT1000_Kuehlung_VL', 
                         'PT1000_Kuehlung_RL', 
                         'Durchfluss DB130.DBD686']
    
    measuring_signals = eg.multchoicebox(msg='Verwendete Messsignale auswählen!', 
                           title='Messsignale', 
                           choices=pre_measuring_signals, 
                           preselect=0, 
                           callback=None, 
                           run=True)
    if measuring_signals == None:
        eg.msgbox(msg='Abbruch durch Benutzer!', title='Benutzerabbruch', ok_button='OK', image=None, root=None)
        sys.exit()
    return measuring_signals

def read_data_make_plot(Excel_Path, spinDat, sc):
    #----------Eingabe des Dateinamen, der Endung sowie der Überspringenden Endungen----------
    filename =  Excel_Path
    name     =  '-Data1'                         # Zusatz zum Dateinamen
    legend   = 14                                # Wie viele Zeilen am Anfang übersprungen werden sollen
    
    actFilePath, actFileName = os.path.split(os.path.abspath(__file__)) # aktueller Script-Pfad ermitteln.
    print("image Pfad = " + actFilePath + "\n") # Debug
    
    #----------Einlesen und Ausgeben der Legende----------
    df_legend = pd.read_csv(filename ,sep=",",nrows=legend-2, encoding = 'latin2')
    print('Überschriften der Einzelnen Kanäle:')
    print(list(df_legend.columns))
    print('Zuordnung der Sensoren in den Signal/key Spalten:')
    print(df_legend[['Signal','key','description']])
    
    #----------Einlesen der Messdaten und Umrechnen der Zeit----------
    try:
        df = pd.read_csv(filename, sep=",", skiprows = legend, encoding = 'latin2')
        df.insert(loc = 1, column = 'time [min]', value= df['time'].apply(lambda x: x/60))
        df.insert(loc = 1, column = 'time [h]', value= df['time'].apply(lambda x: x/3600))
        print(df)
    
    #----------Festlegen des Styles für die Drehzahl-------
        spindel_speed =                 df['f2\s3'] #ok
        spindel_speed_color =           "red"
        spindel_speed_linestyle =       "-."
        spindel_speed_line_width =      2
        spindel_speed_label =           'Spindeldrehzahl [1/min]'
        sec_y_axs_label =               'Drehzal [1/min]'
        
        #---------Festlegend der Paramter für die Zeitachse
        time =                          df['time [min]']
        x_axs_label =                   str('time [min]')
        xaxs_min =                      0
        xaxs_max =                      150
    
        #----------Festlegen der Variablen zum Plotten-----------
        if 'PT100_Frontlager_Ch1_4AI' in sc:
            front_bearing_temperature =     df['f7\s12'] #ok
        if 'PT100_DD Test aufgespritzte_CH3_4AI' in sc:
            rear_bearing_temperature1 =      df['f8\s13'] #ok
            
        #rear_bearing_temperature2 =      df['f4\s13'] #gibts nicht mehr!!!!!!!!
        
        if 'Motortemp r35' in sc:
            spindel_motor_temperatur =      df['f1\s1'] #ok
            
        #drossel_temperature =           df['f16\s17'] #gibts nicht mehr!!!!!!!!
        
        # if 'PT100_DD Test aufgespritzte_CH3_4AI' in sc:
        #     #rotary_unit_temperature1 =     df['f8\s13'] #ok Alternativ zu rear_bearing_temperature1
            
        #rotary_unit_temperature2 =     df['f10\s18'] #gibts nicht mehr!!!!!!!!
        
        if 'Längenausdehnung vorne 1 DB130.DBD682' in sc:
            spindle_growth_front =                df['f9\s15'] # ok
        
        # if 'PT1000_Kuehlung_VL' in sc:
        #     #spindle_growth_rear =                df['f10\s10'] #ok Alternativ zu cooling_VL
        
        if 'Durchfluss DB130.DBD686' in sc:
            cooling_flow_rate_VL =      df['f12\s2'] #ok
        if 'PT1000_Kuehlung_VL' in sc:
            cooling_VL          =      df['f10\s10'] #ok
        if 'PT1000_Kuehlung_RL' in sc:
            cooling_RL          =      df['f11\s11'] #ok
        if 'Drehmomentistwert r80' in sc:
            actual_torque_value   =    df['f6\s9'] #ok
        if 'Ausgangsspannung r25' in sc:
            output_voltage       =    df['f3\s5'] #ok
        if 'Stromistwert feldbildend r29' in sc:
            actual_current_field    = df['f4\s7'] #ok
        if 'Stromistwert momentenbildend r30' in sc:
            actual_current_torque  = df['f5\s8'] #ok
        
        #shaft_bending_front    = df['f5\s8'] #gibts nicht mehr!!!!!!!!
        
        ########################################################
        #---------ab hier die Darstellung des Diagrams----------
        fig, axs = plt.subplots(4, 1, figsize=(25, 15))     #hier 4 untereinander, eine Spalte
        
        #----------Plotten der Verschiedene Linien----------
        if 'PT100_Frontlager_Ch1_4AI' in sc:
            axs[0].plot(time, front_bearing_temperature,    label='Frontlager Temperatur') #ok
        if 'PT100_DD Test aufgespritzte_CH3_4AI' in sc:
            axs[0].plot(time, rear_bearing_temperature1,     label='Loslager Temperatur außen') #ok
        
            #axs[0].plot(time, rear_bearing_temperature2,     label='Loslager Temperatur innen') #gibts nicht mehr!!!!!!!!
        
        if 'Durchfluss DB130.DBD686' in sc:
            axs[0].plot(time, cooling_flow_rate_VL,     label='Kühlung Durchflussmenge VL') #ok
        if 'PT1000_Kuehlung_VL' in sc:
            axs[1].plot(time, cooling_VL,               label='Kühlung Temperatur VL') #ok
        if 'PT1000_Kuehlung_RL' in sc:
            axs[1].plot(time, cooling_RL,               label='Kühlung Temperatur RL') #ok
        if 'Motortemp r35' in sc:
            axs[0].plot(time, spindel_motor_temperatur ,    label='Motor Temperatur') #ok
        if 'Längenausdehnung vorne 1 DB130.DBD682' in sc:
            axs[2].plot(time, spindle_growth_front,               label='Spindelwachstum vorne') #ok
        #if 'PT1000_Kuehlung_VL' in sc:
            #axs[1].plot(time, spindle_growth_rear,               label='Spindelwachstum hinten')#ok Alternativ zu cooling_VL
        if 'Drehmomentistwert r80' in sc:
            axs[3].plot(time, actual_torque_value ,    label='Drehmomentistwert') #ok
        if 'Ausgangsspannung r25' in sc:
            axs[2].plot(time, output_voltage ,         label='Ausgangsspannung') #ok
        if 'Stromistwert feldbildend r29' in sc:
            axs[2].plot(time, actual_current_field ,    label='Stromistwert feldbildend') #ok
        if 'Stromistwert momentenbildend r30' in sc:
            axs[2].plot(time, actual_current_torque ,    label='Stromistwert momentenbildend') #ok
        
        #if 'PT100_DD Test aufgespritzte_CH3_4AI' in sc:
            #axs[3].plot(time, rotary_unit_temperature1 ,    label='Drehdurchfuerung Temperatur innen') #ok Alternativ zu rear_bearing_temperature1
        
            #axs[3].plot(time, rotary_unit_temperature2 ,    label='Drehdurchfuerung Temperatur außen') #gibts nicht mehr!!!!!!!!
        
        #----------Festlegen der Überschriften, Achsbeschriftungen, Grenzen der Achsen, Einteilung der Achsen----------
        fig.suptitle(('Comm.No: ' + spinDat['Kommissionsnummer'] + '    Motor-Type: ' + spinDat['Motorbez.'] + '    ' + name + '    Date: ' + spinDat['Prüfdatum']), 
                     fontsize=24, y =1.00)
        
        
        axs[0].set_title("Temperaturen")
        axs[1].set_title("Kühltemperatur-DD")
        axs[2].set_title("Spindelwachstum")
        axs[3].set_title("Drehdurchführung")
        
        axs[0].set_xlabel(x_axs_label)
        axs[1].set_xlabel(x_axs_label)
        axs[2].set_xlabel(x_axs_label)
        axs[3].set_xlabel(x_axs_label)
        
        axs[0].set_ylabel("Temperatur [°C]")
        axs[1].set_ylabel("Temperatur [°C]")
        axs[2].set_ylabel('Spindelwachstum []')
        axs[3].set_ylabel("Temperatur [°C]")
        
        axs[0].set_xlim(xaxs_min,xaxs_max)
        axs[1].set_xlim(xaxs_min,xaxs_max)
        axs[2].set_xlim(xaxs_min,xaxs_max)
        axs[3].set_xlim(xaxs_min,xaxs_max)
        
        axs[0].set_ylim([0,80])
        axs[1].set_ylim([15,60])
        axs[3].set_ylim([15,120])
        
        axs[0].yaxis.set_major_locator(plticker.MultipleLocator(base=10))
        #axs[1].yaxis.set_major_locator(plticker.MultipleLocator(base=2.5))
        
        #axs[0].xaxis.set_major_locator(plticker.MultipleLocator(base=0.25))
        
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
        axsd= axs[3].twinx()
        axsd.plot(time, spindel_speed, color = spindel_speed_color, linestyle = spindel_speed_linestyle, lw= spindel_speed_line_width , label= spindel_speed_label)
        axsd.set_ylabel(sec_y_axs_label)
        
        #----------Definition des Gitternetzes----------
        axs[0].legend(loc='upper left', bbox_to_anchor=(0, -0.13),ncol=10)
        axs[1].legend(loc='upper left', bbox_to_anchor=(0, -0.05),ncol=10)
        axs[2].legend(loc='upper left', bbox_to_anchor=(0, -0.05),ncol=10)
        axs[3].legend(loc='upper left', bbox_to_anchor=(0, -0.05),ncol=10)
        
        axs[0].grid(b=True, which='major', color='#666666', linestyle='-')#Gitternetz Show the major grid lines with dark grey lines
        axs[0].minorticks_on()# Show the minor grid lines with very faint and almost transparent grey lines
        axs[0].grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
        
        axs[1].grid(b=True, which='major', color='#666666', linestyle='-')#Gitternetz Show the major grid lines with dark grey lines
        axs[1].minorticks_on()# Show the minor grid lines with very faint and almost transparent grey lines
        axs[1].grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
        
        axs[2].grid(b=True, which='major', color='#666666', linestyle='-')#Gitternetz Show the major grid lines with dark grey lines
        axs[2].minorticks_on()# Show the minor grid lines with very faint and almost transparent grey lines
        axs[2].grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
        
        axs[3].grid(b=True, which='major', color='#666666', linestyle='-')#Gitternetz Show the major grid lines with dark grey lines
        axs[3].minorticks_on()# Show the minor grid lines with very faint and almost transparent grey lines
        axs[3].grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
        
        fig.tight_layout()
        
        #----------Anzeigen und Abspeichern des Diagramms----------
        plt.show()
        return fig
    
            
    except KeyError as err:
        eg.msgbox(msg='Messwerte-Datei fehlerhaft!\nsind alle Signale vorhanden?\n\nFehler = ' + str(err), 
                  title='Fehler Messwertedatei', ok_button='OK', image=actFilePath + '\Messwertedatei.png', root=None)
        sys.exit()
    except BaseException as err:
        print("Fehler :   " + traceback.format_exc())
        eg.msgbox(msg='Messwerte-Datei fehlerhaft!\nsind alle Signale vorhanden?\n\nFehler = ' + str(err), 
                  title='Fehler Messwertedatei', ok_button='OK', image=actFilePath + '\Messwertedatei.png', root=None)
        sys.exit()

# ----------Ruting principal----------
def main():
    # Data-file open
    Excel_Path = file_open_dialogs()
    
    #Spindeldaten eingeben
    spindleData = input_Data()
    
    spinDat = spindleData[0] #Allgemeine Angaben
    spinType = spindleData[1] #Synchron/Asynchron

    
    #Auswahl der Messsignale
    sc = signal_Choice()

    #Daten lesen und Graph generieren
    fig = read_data_make_plot(Excel_Path, spinDat, sc)
    
    #Plot speichern
    default_filename = spinDat['Kommissionsnummer']
    saveyesno = save_file_dialogs(default_filename)
    if saveyesno != None:
        fig.savefig(saveyesno)
        if eg.buttonbox(msg = "Protokolldatei wurde unter %s gespeichert.\n\n Soll die Datei geöffnet werden?" %(saveyesno),choices=('Ja', 'Nein')) == 'Ja':
            os.startfile(saveyesno)



if __name__ == '__main__':
    main()