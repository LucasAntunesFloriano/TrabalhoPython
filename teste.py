#Interface
import tkinter
from tkinter.filedialog import askopenfilename
#Ler PDf
import PyPDF2
#Fazer chamada api
import requests
import re


re.match
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

def lerPdf():
    filename = askopenfilename()
    ConteudoPDF = Get_text_from_PDFfiles_usingPyPDF2(filename)
    print(ConteudoPDF.split("\n"))
    x = re.findall("\d{4}(?=-\d{2}-\d{2})", ConteudoPDF)
    ConteudoAPI=""
    for Ano in set(x):
        ConteudoAPI = ConteudoAPI + ChamadaAPI(Ano)
    print(ConteudoAPI)

def Exemplo():
    root = tkinter.Tk()
    root.title("Titulo da janela")
    root.resizable(True, True)
    
    test = tkinter.Button(root, text="Escolher PDF")
    test['command'] = lerPdf
    test.pack()

    
    root.mainloop()

Exemplo()
