import os
import shutil
import pandas as pd
import openpyxl as xl 
from datetime import date 
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm
from docx.shared import Cm

################# Benutzereinstellungen #################

OUTPUT_PATH = "C:/Users/wmolina/Desktop/Python/Prüfstand/Protokoll/Outputs"

Excel_Path = 'C:/Users/wmolina/Desktop/Python/Prüfstand/Protokoll/Inputs/Belastungsmessung Prüfprotokoll.xlsx'

Word_Path = 'C:/Users/wmolina/Desktop/Python/Prüfstand/Protokoll/Inputs/Templates/Wordtemplate.docx'

IMAGE_PATH = "C:/Users/wmolina/Desktop/Python/Prüfstand/Protokoll/Inputs/Diagramms/Test.jpg"

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

# Erzeugung Worddateien
def CreateWord(df_Data):
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

    # Create the Wordfile:
    CreateWord(df_messung)


if __name__ == '__main__':
    main()


