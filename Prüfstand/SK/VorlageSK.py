import os
import shutil
import pandas as pd
#import openpyxl as xl
#import copy 
from datetime import date 
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm

import easygui as eg
import sys

import locale
#locale.setlocale(locale.LC_ALL, 'de_DE.utf8') # geht nicht mit enterbox/multenterbox

################# Benutzereinstellungen #################

#OUTPUT_PATH = eg.diropenbox(msg = "Bitte den Ausgabepfad angeben")
#OUTPUT_PATH = "C:/Users/wmolina/Desktop/Python/Prüfstand/Protokoll/Outputs"

Excel_Path = eg.fileopenbox(msg = "Bitte die Messwerte-Datei auswählen", default = "*.xlsx")
if Excel_Path == None:
    sys.exit()
#Excel_Path = 'C:/Users/wmolina/Desktop/Python/Prüfstand/Protokoll/Inputs/Belastungsmessung Prüfprotokoll.xlsx'

Word_Path = eg.fileopenbox(msg = "Bitte die Protokoll-Vorlage auswählen", default = "*.docx")
if Word_Path == None:
    sys.exit()
#Word_Path = 'C:/Users/wmolina/Desktop/Python/Prüfstand/Protokoll/Inputs/Templates/Wordtemplate.docx'

IMAGE_PATH = eg.fileopenbox(msg = "Bitte das Diagramm auswählen", default = "*.jpg")
if IMAGE_PATH == None:
    sys.exit()
#IMAGE_PATH = "C:/Users/wmolina/Desktop/Python/Prüfstand/Protokoll/Inputs/Diagramms/Test.jpg"

# Farbebereich: In google = rgb to hex
# HochTemp_Farbe = 'eb4634'
# NiedigTemp_Farbe = '49eb34'


# Löschung und Neuanlage des Ausgabeordners.
# def DeleteCreateFolder(path):
#     # Check if the folder exists and delete it
#     if (os.path.exists(path)):
#         shutil.rmtree(path)

#     # Create a new folder:
#     os.mkdir(OUTPUT_PATH) 

# Read Exceldata:
def ReadData(path, WorkSheet):
    excel_df = pd.read_excel(path, WorkSheet)
    #print(excel_df)
    return excel_df

# Fehlererkennung
def Fehler(df_Data):
    for index, row in df_Data.iterrows():
        Temperatur = ['Drosseltemp. 0,42mH "Eisen" Prüfling', 'Drosseltemp. 0,41mH "Eisen" Belastungsmaschine']

        for temp in Temperatur:
            if not((row[temp] >= 25) and (row[temp] <= 32)):
                print("Error", Temperatur, "Fehlerwert:" + str(row[temp]))
                print("\n")

def save_file_dialogs(extension = "docx"):
    saveornot = eg.buttonbox(msg="Soll die Datei gespeichert werden?", choices = ("No", "Yes") )
    if saveornot == "Yes":
        filename = eg.filesavebox(msg = "Dateiname eingeben (die Erweiterung %s wird automatisch angehängt)?" %(extension))
        if filename is None:
            return None
        filename = filename + "." + extension
        if os.path.exists(filename):
            ok_to_overwrite = eg.buttonbox(msg="Datei %s besteht bereits. Überschreiben?" %(filename), choices = ("No", "Yes") )
            if ok_to_overwrite == "Yes":
                return filename
            else:
                return None
        else:
            return filename
    else:
        return None


# Erzeugung Worddateien
def CreateWord(df_Data):
    # KNr = ""
    # while KNr is not float:
    #     try:
    #         KNr = int(input("Geben Sie die Kommissionsnummer ein: "))
    #         break 
    #     except ValueError:
    #         print("Sie haben das falsch geschrieben, bitte versuchen es noch mal!\n")

    # print("\n")
    # Leistung = ""
    # while Leistung is not float:
    #     try:
    #         Leistung = int(input("Geben Sie die Leistung in [kW] ein: "))
    #         break 
    #     except ValueError:
    #         print("Sie haben das falsch geschrieben, bitte versuchen es noch mal!\n")
    
    # print("\n")
    # MotorTyp = input("Geben Sie das Motortyp: ")
    
    # print("\n")
    # Hersteller = input("Geben Sie den Hersteller ein: ")

    # print("\n")
    # Datenbaltt = ""
    # while Datenbaltt is not float:
    #     try:
    #         Datenbaltt = str(input("Geben Sie das Datenblatt ein: "))
    #         break 
    #     except ValueError:
    #         print("Sie haben das falsch geschrieben, bitte versuchen es noch mal!\n")

    msg = "Geben sie Verwaltungsinformationen ein."
    title = "Allgemeine Angaben"
    fieldNames = ["Kundenname","Kommissionsnummer","Spindelbezeichnung","AS-Nr.","Motorbez.","DBL.Nr.","Nennleistung","Nenndrehzahl","max.Drehzahl","Prüfer/in"]
    fieldValues = []  # we start with blanks for the values
    fieldValues = eg.multenterbox(msg,title, fieldNames)
    
    # make sure that none of the fields was left blank
    while 1:
        if fieldValues is None: break
        errmsg = ""
        for i in range(len(fieldNames)):
            if fieldValues[i].strip() == "":
                errmsg += ('"%s" ist eine erforderliche Eingabe.\n\n' % fieldNames[i])
        if errmsg == "":
            break # no problems found
        fieldValues = eg.multenterbox(errmsg, title, fieldNames, fieldValues)
    
    genDat = dict(zip(fieldNames, fieldValues))
    #print('Spindelbezeichnung = ' + genDat['Spindelbezeichnung'])
    
    spinType = eg.choicebox(msg='Pick an item', title='', choices=['Synchron', 'Asynchron'], preselect=0) #, callback=None, run=True
    #print(spinType)


    ZeitList = []
    for index, r_val in df_Data.iterrows():
        zeit_dict = {
            'Zeit': str(r_val['Zeit']),
            'Temp1': str(r_val['Kopftemperatur des Prüflings']),
            'Temp2': str(r_val['Drosseltemp. 0,42mH "Eisen" Prüfling']),
            'Temp3': str(r_val['Drosseltemp. 0,41mH "Eisen" Belastungsmaschine']),
            'Unwucht': str(r_val['Unwucht (seitlich am Spindelkopf gemessen)']),
        }        
        ZeitList.append(zeit_dict)
        #print(ZeitList)
        l_tpl = Word_Path 
        docx_tpl = DocxTemplate(l_tpl)

        imag_path = IMAGE_PATH
        img = InlineImage(docx_tpl, imag_path, height = Mm(95))

        context = {
            # 'date' : date.today(),
            # 'K_Nr' : KNr,
            # 'SpindelP' : Leistung,
            # 'Motortyp' : MotorTyp,
            # 'Hersteller' : Hersteller,
            # 'DB' : Datenbaltt,
            # 'zeit_list' : ZeitList,
            # 'bild' : img,
            'K_name' : genDat['Kundenname'],
            'K_Nr' : genDat['Kommissionsnummer'],
            'WZ' : genDat['Spindelbezeichnung'],
            'AS' : genDat['AS-Nr.'],
            'M_name' : genDat['Motorbez.'],
            'DB' : genDat['DBL.Nr.'],
            'Motortyp' : spinType,
            'SpindelP' : genDat['Nennleistung'],
            'Nn' : genDat['Nenndrehzahl'],
            'Nmax':genDat['max.Drehzahl'],
            'Pr' : genDat['Prüfer/in'],
            'date' : date.today(),
            'zeit_list' : ZeitList,
            'bild' : img,
        }

        docx_tpl.render(context)

        # Save File
        #name_file = 'Messung_Vorlage' +'.docx'
        #docx_tpl.save(OUTPUT_PATH + '\\' + name_file)
    saveyesno = save_file_dialogs()
    if saveyesno != None:
        docx_tpl.save(saveyesno)
        #eg.msgbox(msg = "Protokolldatei wurde unter %s gespeichert." %(saveyesno) )
        if eg.buttonbox(msg = "Protokolldatei wurde unter %s gespeichert.\n\n Soll die Datei geöffnet werden?" %(saveyesno),choices=('Ja', 'Nein')) == 'Ja':
            os.startfile(saveyesno)

# Ruting principal
def main():
    # Delete and recreate the folder OUTPUTS
    #DeleteCreateFolder(OUTPUT_PATH) 

    # Read the Excel Data
    df_messung = ReadData(Excel_Path, 'man. aufgezeichnete Messwerte')

    # Fehler:
    Fehler(df_messung)

    # Create the Wordfile:
    CreateWord(df_messung)


if __name__ == '__main__':
    main()
                    

