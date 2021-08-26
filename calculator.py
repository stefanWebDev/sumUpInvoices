import PyPDF2
import tkinter as tk
from tkinter import Label, Button, filedialog
import time
from tika import parser
import re


class App1:
    def __init__(self, top):
        self.top = top


        self.initialdir = "C:/users/me"

        top.title("Invoice Calculator")
        top.geometry("1028x500")
        top.configure(background="#091833")


        self.font10 = "{Courier New} 10 normal"
        self.font11 = "{Courier New} 30 bold"
        self.font12 = "{Courier New} 10 bold"

        self.label11 = tk.Label(master=top, text="Invoice Calculator", background="#091833", font=self.font11, foreground="#f2a343")
        self.label11.place(relx=0.268, rely=0.1, height=51, width= 507)

        self.Button1 = tk.Button(master=top, text='''Upload''', background='#122c63', font=self.font12, command=self.uploadFiles)
        self.Button1.place(relx=0.49, rely=0.33)



    def uploadFiles(self):
        invoiceAmounts = []
        fileNames = filedialog.askopenfilenames(initialdir=self.initialdir, title="Select A File", filetypes=(("pdf files", "*.pdf"),("all files", "*.*")))
        for file in fileNames:
            raw = parser.from_file(file)
            content = raw['content']
            self.getAmountFromContent(content, invoiceAmounts)
        
            

    def getAmountFromContent(self,content, invoiceAmounts):
        
        amountPattern = "[0-9]+\,[0-9]+\ €"

        allAmountsOfOneInvoice = re.findall(amountPattern, content)
        invoiceAmount = allAmountsOfOneInvoice[len(allAmountsOfOneInvoice)-1]
        two = invoiceAmount.replace(',', '.')
        three = two.replace('€', '')
        four = three.replace(' ', '')

        invoiceAmounts.append(four)
        self.displayOutcome(self.top, invoiceAmounts)

    def displayOutcome(self, top, invoiceAmountArra):
        self.label11 = tk.Label(master=top, text=self.sumUpAmounts(invoiceAmountArra), background="#091833", font=self.font11, foreground="#f2a343")
        self.label11.place(relx=0.3, rely=0.2, height=51, width= 507)

    def sumUpAmounts(self, amountArray):
        sum = 0
        for amount in amountArray:
            sum += float(amount)
        sumRounded = round(sum, 2)
        sumFormatted = f'{sumRounded:.2f}'
        sumAsString = str(sumFormatted)
        sumAsString += " €"
        sumAsString = sumAsString.replace('.', ',')
        return sumAsString


root = tk.Tk()
my_gui = App1(root)
root.mainloop()