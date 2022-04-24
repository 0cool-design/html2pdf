import pdfkit, sys
from PyPDF2 import PdfFileMerger, PdfFileReader
from time import sleep
from tqdm import tqdm
import tkinter as tk
import tkinter.ttk as ttk

weblist = ["link 1", "link 2", "link 3", "link 4"]

class GUI_H2P:
    def __init__(self, master=None):
        global weblist
        # build ui
        self.main = ttk.Frame(master)
        self.label1 = ttk.Label(self.main)
        self.label1.configure(font='{TkMenuFont } 15 {bold}', justify='center', text='HTML to PDF')
        self.label1.pack(side='top')

        self.entry1 = ttk.Entry(self.main)
        self.entry1.configure(width='60')
        _text_ = '''URL:'''
        self.entry1.delete('0', 'end')
        self.entry1.insert('0', _text_)
        self.entry1.pack(expand='true', ipadx='13', ipady='10', padx='20', pady='13', side='top')

        self.Add_button = ttk.Button(self.main)
        self.Add_button.configure(text='Add', width='10')
        self.Add_button.pack(ipadx='10', ipady='5', padx='10', pady='30', side='left')
        self.Add_button.configure(command=self.Add)

        self.Delete_button = ttk.Button(self.main)
        self.Delete_button.configure(text='Delete', width='10')
        self.Delete_button.pack(ipadx='10', ipady='5', padx='25', pady='30', side='left')
        self.Delete_button.configure(command=self.Delete)

        self.Download_button = tk.Button(self.main, bg='green', fg='white')
        self.Download_button.configure(text='Start Download', width='15')
        self.Download_button.pack(ipadx='15', ipady='5', padx='30', pady='30', side='bottom')
        self.Download_button.configure(command=self.Download)

        self.links_tree = ttk.Treeview(self.main)
        self.links_tree["columns"]=("#0","#1")
        self.links_tree.column("#1", width=30)
        self.links_tree.column("#0", width=10)
        self.links_tree.heading("#1", text="URLs")
        self.links_tree.heading("#0", text="#")

        count_id = 0
        tree_list = []
        for urllink in weblist:
            count_id += 1
            tree_list.append("%-10d %30s" %(count_id,urllink))
        for column in tree_list:
            self.links_tree.insert('', tk.END, values=column)


        self.links_tree.pack(expand='true', ipadx='60', ipady='50', pady='20', side='right')
        #self.links_tree.heading('#1', text='URLs')

        self.separator1 = ttk.Separator(self.main)
        self.separator1.configure(orient='vertical')
        self.separator1.pack(expand='true', ipadx='9', ipady='150', padx='4', pady='9', side='left')

        self.main.configure(borderwidth='5', height='300', padding='10', width='500')
        self.main.pack(side='top')

        # Main widget
        self.mainwindow = self.main

    def Add(urllink):
        global weblist
        #urllink = urllink.strip()
        weblist.append(urllink)

    def Download():
        global weblist
        count = 0
        for fileNumber in tqdm(range(1,len(weblist)+1)):
            try:
                count += 1
                pdfkit.from_url(weblist[fileNumber],'file'+str(count)+'.pdf')
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
        mergedObject.write("Final.pdf")


    def Delete(self):
        pass

    def run(self):
        self.mainwindow.mainloop()

if __name__ == '__main__':
    import tkinter as tk
    root = tk.Tk()
    root.title("HTML 2 PDF")
    app = GUI_H2P(root)
    app.run()
