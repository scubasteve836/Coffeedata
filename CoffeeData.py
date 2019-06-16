from __future__ import print_function
import pickle
import os.path
import gspread
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import sys
if sys.version_info[0] == 3:
    # for Python3
    from tkinter import *
else:
    # for Python2
    from Tkinter import *

import csv



csvfile = "coffee.csv"

spreadsheet_id = '10gIsAO2j5qxmsvujx7QFdjygIvcQvwgZFnkinoMoMkE'
range_name = 'Pour Over!A1:M1'

def getsheet(spreadsheet_id, range_name ) :
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    gsheet = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    header = gsheet.get('values', [])[0]
    print(header)
    return gsheet
    return creds

def readitem(gsheet) :
    header = gsheet.get('values', [])[0]
    print(header)
getsheet(spreadsheet_id, range_name)


#readitem(gsheet)
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
        row1 = [[g1], [g2], [g3], [g4], [g5], [g6], [g7], [g8], [g9], [g10], [g11]]

        writer = csv.writer(csvFile)
        writer.writerow(row)
        csvFile.close()
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    body = {
        "majorDimension": "COLUMNS",
        'values': row1
    }
    service = build('sheets', 'v4', credentials=creds)
    result = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id, range=range_name,
        valueInputOption='USER_ENTERED', body=body).execute()
    print(result)



#build the gui
master = Tk()
master.title("Enter Coffee Data")

brewmethod = StringVar(master)
brewmethod.set("Pour Over")
dropdown = OptionMenu(master, brewmethod, "Pour Over", "Siphon", "Auto Drip")
dropdown.pack


Label(master, text="Roaster").grid(row=0)
Label(master, text="Origin/Blend").grid(row=1)
Label(master, text="Roast Date").grid(row=2)
Label(master, text="Brew Date").grid(row=3)
Label(master, text="Mug Size(oz)").grid(row=4)
Label(master, text="Grind Setting").grid(row=5)
Label(master, text="Grinder").grid(row=6)
Label(master, text="Coffee(grams").grid(row=7)
Label(master, text="Brew Time (Min:Sec)").grid(row=8)
Label(master, text="Temp(F)").grid(row=9)
Label(master, text="Roaster Notes").grid(row=10)
Label(master, text="My Notes").grid(row=11)

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
e12 = Entry(master)

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
e12.grid(row=11, column=1)

#buttons!
Button(master, text='Quit', command=master.destroy).grid(row=12, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=12, column=1, sticky=W, pady=4)
Button(master, text='Submit', command=writeToFile).grid(row=12, column=2, sticky=W, pady=4)

mainloop()
