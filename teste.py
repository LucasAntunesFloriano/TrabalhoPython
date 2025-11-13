#Interface
import tkinter
from tkinter.filedialog import askopenfilename


def lerPdf():
    filename = askopenfilename()
    print(filename)

def Exemplo():
    root = tkinter.Tk()
    root.title("Titulo da janela")
    root.resizable(True, True)
    
    test = tkinter.Button(root, text="Escolher PDF")
    test['command'] = lerPdf
    test.pack()

    
    root.mainloop()

Exemplo()
