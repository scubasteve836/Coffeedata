import sys
if sys.version_info[0] == 3:
    # for Python3
    from tkinter import *
else:
    # for Python2
    from Tkinter import *

import csv

csvfile = "coffee.csv"


def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
    e1.delete(0, END)
    e2.delete(0, END)


def output(self):
    Label(text='Name:').pack(side=LEFT, padx=5, pady=5)
    self.e = Entry(root, width=10)
    self.e.pack(side=LEFT, padx=5, pady=5)

    self.b = Button(root, text='Submit', command=self.writeToFile)
    self.b.pack(side=RIGHT, padx=5, pady=5)


def writeToFile():
    with open('coffee.csv', 'a') as csvFile:
        g1 = e1.get()
        g2 = e2.get()
        g3 = e3.get()
        g4 = e4.get()
        g5 = e5.get()
        g6 = e6.get()
        g7 = e7.get()
        g8 = e8.get()
        g9 = e9.get()
        g10 = e10.get()
        g11 = e11.get()
        row = [g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11]
        writer = csv.writer(csvFile)
        writer.writerow(row)
        csvFile.close()


master = Tk()
master.title("Enter Data")
Label(master, text="Roaster").grid(row=0)
Label(master, text="Origin/Blend").grid(row=1)
Label(master, text="Roast Date").grid(row=2)
Label(master, text="Brew Date").grid(row=3)
Label(master, text="Mug Size(oz)").grid(row=4)
Label(master, text="Grind Setting").grid(row=5)
Label(master, text="Coffee(grams").grid(row=6)
Label(master, text="Brew Time (Min:Sec)").grid(row=7)
Label(master, text="Temp(F)").grid(row=8)
Label(master, text="Roaster Notes").grid(row=9)
Label(master, text="My Notes").grid(row=10)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
e6 = Entry(master)
e7 = Entry(master)
e8 = Entry(master)
e9 = Entry(master)
e10 = Entry(master)
e11 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)
e6.grid(row=5, column=1)
e7.grid(row=6, column=1)
e8.grid(row=7, column=1)
e9.grid(row=8, column=1)
e10.grid(row=9, column=1)
e11.grid(row=10, column=1)

Button(master, text='Quit', command=master.destroy).grid(row=12, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=12, column=1, sticky=W, pady=4)
Button(master, text='Submit', command=writeToFile).grid(row=12, column=2, sticky=W, pady=4)

mainloop()
