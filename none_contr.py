from tkinter import *
from tkinter import messagebox
from subprocess import Popen
import sys
import os


def submit():
    boolean = True
    try:
        init_investment = float(initInvestmentEntry.get())
    except Exception:
        boolean = False
    try:
        annual_return = float(annualReturnEntry.get())
    except Exception:
        boolean = False
    try:
        years_investing = int(yearsInvestingEntry.get())
    except Exception:
        boolean = False

    if boolean:
        pass
    else:
        response = messagebox.askretrycancel(title='Oh no!',
                                             message='Something went wrong! :(',
                                             icon='warning')
        if response:
            restart_program()
        else:
            exit()

    end = round(none_monthly(init_investment,annual_return,years_investing),2)

    endResultEntry.delete(0, END)
    endResultEntry.insert(0, end)

def reset():
    initInvestmentEntry.delete(0,END)
    annualReturnEntry.delete(0,END)
    yearsInvestingEntry.delete(0,END)
    endResultEntry.delete(0,END)

def none_monthly(init_investment,annual_return,years_investing):
    for i in range(int(years_investing)):
        init_investment = init_investment + (init_investment * (annual_return/100))
    return init_investment

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def return_main():
    # Popen(['python','main.py'])
    window.destroy()


window = Tk()
window.title('ETF/Index Fund Investment Calculator, without any additional contribution')
window.geometry('700x400')
window.config(bg='#cfceca')

submitButton = Button(window,
                      text='Submit',
                      command=submit,
                      font=('Arial',20))

resetButton = Button(window,
                     text='Reset',
                     command=reset,
                     font=('Arial',20))

submitButton.place(x=290,
                   y=390,
                   anchor='s')

resetButton.place(x=410,
                  y=390,
                  anchor='s')

initInvestmentLabel = Label(window,
                            text='Initial Investment ($)',
                            font=('Arial',20),
                            bg='#b0b0ae')
initInvestmentLabel.place(x=90,
                          y=50)

initInvestmentEntry = Entry(window,
                            font=('Arial',20))

initInvestmentEntry.place(x=350,
                          y=50)

annualReturnLabel = Label(window,
                          text='Annual Return Rate (%)',
                          font=('Arial',20),
                          bg='#b0b0ae')

annualReturnLabel.place(x=47,
                        y=100)

annualReturnEntry = Entry(window,
                          font=('Arial',20))

annualReturnEntry.place(x=350,
                        y=100)

yearsInvestingLabel = Label(window,
                            text='Length of time in years',
                            font=('Arial',20),
                            bg='#b0b0ae')

yearsInvestingLabel.place(x=61,
                          y=150)

yearsInvestingEntry = Entry(window,
                            font=('Arial',20))

yearsInvestingEntry.place(x=350,
                          y=150)

endResultLabel = Label(window,
                       text='End Result:',
                       font=('Arial', 20),
                       bg='#b0b0ae')

endResultLabel.place(x=195,
                     y=220)

endResultEntry = Entry(window,
                       font=('Arial',20))

endResultEntry.place(x=350,
                     y=220)

returnButton = Button(window,
                      text='Return',
                      command=return_main,
                      font=('Arial',20))
returnButton.place(x=630,
                   y=390,
                   anchor='s')

window.mainloop()
