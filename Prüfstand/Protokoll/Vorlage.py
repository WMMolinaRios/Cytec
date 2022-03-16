import os
import shutil
import pandas as pd
import openpyxl as xl
import copy 
from datetime import date 
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm
import locale
locale.setlocale(locale.LC_ALL, 'de_DE.utf8')

################# Benutzereinstellungen #################

OUTPUT_PATH = "C:/Users/wmolina/Desktop/Python/Prüfstand/Protokoll/Outputs"

Excel_Path = 'C:/Users/wmolina/Desktop/Python/Prüfstand/Protokoll/Inputs/Belastungsmessung Prüfprotokoll.xlsx'

Word_Path = 'C:/Users/wmolina/Desktop/Python/Prüfstand/Protokoll/Inputs/Templates/Wordtemplate.docx'

IMAGE_PATH = "C:/Users/wmolina/Desktop/Python/Prüfstand/Protokoll/Inputs/Diagramms/Test.jpg"

# Farbebereich: In google = rgb to hex
# HochTemp_Farbe = 'eb4634'
# NiedigTemp_Farbe = '49eb34'

# Löschung und Neuanlage des Ausgabeordners.
def DeleteCreateFolder(path):
    # Check if the folder exists and delete it
    if (os.path.exists(path)):
        shutil.rmtree(path)

    # Create a new folder:
    os.mkdir(OUTPUT_PATH) 

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

# Erzeugung Worddateien
def CreateWord(df_Data):
    KNr = ""
    while KNr is not float:
        try:
            KNr = int(input("Geben Sie die Kommissionsnummer ein: "))
            break 
        except ValueError:
            print("Sie haben das falsch geschrieben, bitte versuchen es noch mal!\n")

    print("\n")
    Leistung = ""
    while Leistung is not float:
        try:
            Leistung = int(input("Geben Sie die Leistung in [kW] ein: "))
            break 
        except ValueError:
            print("Sie haben das falsch geschrieben, bitte versuchen es noch mal!\n")
    
    print("\n")
    MotorTyp = input("Geben Sie das Motortyp: ")
    
    print("\n")
    Hersteller = input("Geben Sie den Hersteller ein: ")

    print("\n")
    Datenbaltt = ""
    while Datenbaltt is not float:
        try:
            Datenbaltt = str(input("Geben Sie das Datenblatt ein: "))
            break 
        except ValueError:
            print("Sie haben das falsch geschrieben, bitte versuchen es noch mal!\n")


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
            'date' : date.today(),
            'K_Nr' : KNr,
            'SpindelP' : Leistung,
            'Motortyp' : MotorTyp,
            'Hersteller' : Hersteller,
            'DB' : Datenbaltt,
            'zeit_list' : ZeitList,
            'bild' : img,
        }

        docx_tpl.render(context)

        # Save File
        name_file = 'Messung_Vorlage' +'.docx'
        docx_tpl.save(OUTPUT_PATH + '\\' + name_file)



# Ruting principal
def main():
    # Delete and recreate the folder OUTPUTS
    DeleteCreateFolder(OUTPUT_PATH) 

    # Read the Excel Data
    df_messung = ReadData(Excel_Path, 'man. aufgezeichnete Messwerte')

    # Fehler:
    Fehler(df_messung)

    # Create the Wordfile:
    CreateWord(df_messung)


if __name__ == '__main__':
    main()


