import tkinter
from tkinter.filedialog import askopenfilename
import PyPDF2
import requests
import re

def ChamadaAPI(Ano):
    url = "https://date.nager.at/api/v3/PublicHolidays/"+Ano+"/BR"

    payload = {}
    headers = {
      'accept': 'application/json'
      }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text
    
def Get_text_from_PDFfiles_usingPyPDF2(in_PdfFile):  
    reader = PyPDF2.PdfReader(in_PdfFile) 
    return reader.pages[0].extract_text()

    
def LerPdf():
    filename = askopenfilename()
    TextoPDF = Get_text_from_PDFfiles_usingPyPDF2(filename)
    ListaAnos = set(re.findall("\d{4}(?=-\d{2}-\d{2})", TextoPDF))

    RespAPI = ""
    for Ano in ListaAnos:
        RespAPI = RespAPI + ChamadaAPI(Ano)
        
    for Data in TextoPDF.split("\n"):
        if Data.strip() in RespAPI:
            print(Data)

def Exemplo():
    root = tkinter.Tk()
    root.title("Titulo da janela")
    root.resizable(True, True)
    
    test = tkinter.Button(root, text="Ler pdf")
    test['command'] = LerPdf
    test.pack()

    root.mainloop()
    
Exemplo()


