from tkinter import *
from subprocess import Popen
import sys


def none_contr_run():
    Popen(['python', 'none_contr.py'])


def div_rein_run():
    Popen(['python', 'div_rein.py'])


def stable_annual_run():
    Popen(['python', 'stable_annual.py'])


window = Tk()
window.title('ETF/Index Fund Investment Calculator')
window.geometry('700x400')
window.config(bg='#cfceca')

mainLabel = Label(window,
                  text='Investment Calculator',
                  font=('Arial',25),
                  bg='#b0b0ae',
                  padx=5,
                  pady=5)
mainLabel.place(anchor='n',
                relx=0.5,
                rely=0.05)

noneContrButton = Button(window,
                         text='No Contribution',
                         font=('Arial',25),
                         command=none_contr_run)
noneContrButton.place(anchor='n',
                      relx=0.5,
                      rely=0.22)

divReinButton = Button(window,
                       text='Dividend Reinvestment',
                       font=('Arial',25),
                       command=div_rein_run)
divReinButton.place(anchor='n',
                    relx=0.5,
                    rely=0.45)

stableAnnualButton = Button(window,
                            text='Stable Annual Contribution',
                            font=('Arial',25),
                            command=stable_annual_run)
stableAnnualButton.place(anchor='n',
                         relx=0.5,
                         rely=0.68)


window.mainloop()
