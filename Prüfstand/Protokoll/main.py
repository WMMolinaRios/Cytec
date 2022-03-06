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

wb = xl.load_workbook(Excel_Path)

ws = wb.worksheets['man. aufgezeichnete Messwerte']
print(ws)