import tkinter as tk
from convert import bin2dec

class Aplication:

    convertido = False

    def __init__(self, master=None):
        self.wid1 = tk.Frame(master)
        self.wid1.pack()
        self.msg = tk.Label(self.wid1, text="Testando a interface")
        self.msg.pack()
        self.label = tk.Label(self.wid1)
        self.label.pack()
        self.btn1 = tk.Button(self.wid1,text='      0        ')
        self.btn2 = tk.Button(self.wid1,text='      1        ')
        self.execute = tk.Button(self.wid1,text="Converter")
        self.btn1.bind("<Button-1>",self.add0)
        self.btn2.bind("<Button-1>",self.add1)
        self.execute.bind('<Button-1>', self.conv)
        self.btn1.pack(side='left')
        self.btn2.pack(side='right')
        self.execute.pack(side='top')
    
    def add1(self,event):
        if self.check_conv():
            self.label['text'] = '1'
        else:
            self.label['text'] += "1"
    
    def add0(self, event):
         if self.check_conv():
                self.label['text'] = '0'
         else:
            self.label['text'] += "0"

    def conv(self, event):
        self.convertido = True
        self.label['text'] = str(bin2dec(self.label['text']))
    
    def check_conv(self):
        if self.convertido:
            self.convertido = False
            return True
        else:
            return False

    