#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pdfkit, sys
from tkinter import *
from PyPDF2 import PdfFileMerger, PdfFileReader
from time import sleep
from tqdm import tqdm


weblis = []
GUI = Tk()


def command():
    weblis.append(str(entry.get()).strip)
    print(weblis)


def Download():
    global weblis
    count = 0
    for fileNumber in tqdm(range(1,len(weblis)+1)):
        try:
            count += 1
            pdfkit.from_url(weblis[fileNumber],'file'+str(count)+'.pdf')
        except OSError:
            print("Error Can't Download")
        except KeyboardInterrupt:
            sys.exit("Exit")

    mergedObject = PdfFileMerger()

    for fileNumber in tqdm(range(1,int(count)+1)):
        print(fileNumber)
        try:
            mergedObject.append(PdfFileReader('file' + str(fileNumber)+ '.pdf', 'rb'))
        except FileNotFoundError:
            print(f"Error Can't Download {fileNumber}")
        except KeyboardInterrupt:
            sys.exit("Exit")

    mergedObject.write("output.pdf")


GUI.title("HTML 2 PDF")
entry = Entry(GUI)
button_add = Button(GUI, text="Add", command=command)
button_start = Button(GUI, text="Download", command=Download)
GUI.geometry("500x200")
entry.pack()
button_add.pack()
button_start.pack()
GUI.mainloop()
