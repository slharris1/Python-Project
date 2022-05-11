import tkinter as tk
from tkinter import *
import shutil
import os
import time
from datetime import datetime, timedelta




class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width = False, height = False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('File Transfer') #Sets the title of the window. 
        self.master.config(bg='lightgray')

        self.lblSource = Label(self.master, text='Source File:  ', font=('Georgia', 14,), fg = 'black', bg='lightgrey' ) 
        self.lblSource.grid(row=0, column=0, padx=(30,0), pady=(30,0)) 0px

        self.lblDestination = Label(self.master, text='Destination File ', font=('Georgia', 14,), fg = 'black', bg='lightgrey' ) 
        self.lblDestination.grid(row=1, column=0, padx=(30,0), pady=(30,0)) 

        self.txtWeb = Entry(self.master,text="web text", font=('Georgia', 14,), fg = 'black', bg='salmon')  
        self.txtWeb.grid(row=1, column=1, padx=(10,0), pady=(30,0))

        self.txtWeb = Entry(self.master,text="web text", font=('Georgia', 14,), fg = 'black', bg='salmon')  
        self.txtWeb.grid(row=0, column=1, padx=(10,0), pady=(30,0)) 

        self.btnSource = Button(self.master, text ="Source", width= 10, height=2) 
        self.btnSource.grid(row=2, column=0, padx=(30,0), pady=(30,0), sticky=S)  

        self.btnDestination = Button(self.master, text ="Destination", width= 10, height=2) 
        self.btnDestination.grid(row=2, column=2, padx=(0,0), pady=(30,0), sticky=S)  

        self.btnTransfer = Button(self.master, text ="Transfer", width= 10, height=2) 
        self.btnTransfer.grid(row=2, column=1, padx=(0,0), pady=(30,0), sticky=N)

    def chooseSource(self):
        src = filedialog.askdirectory()

    def chooseDestination(self):
        src = filedialog.askdirectory()



    def fileTransfer(self):
        #set where the source of the files are
        source = '/Users/harri/Onedrive/Desktop/Folder C/'
        #set the destination path to folder D
        destination = '/Users/harri/Onedrive/Desktop/Folder D/'
        files = os.listdir(source)

        for i in files:
            #to get the absolute path to the file
            absolutePath = os.path.join(source, i)

            #gets the modification time
            mtime = os.path.getmtime(absolutePath)

            #converts that mtime to a date time format.
            modTime=datetime.fromtimestamp(mtime)

            current = datetime.now()

            twentyFour = current - timedelta(hours=24)

            if modTime > twentyFour:
                shutil.move(absolutePath, destination)





        
if __name__ == "__main__":
    root = tk.Tk() #syntax in order to create a window from the tkinter
    App = ParentWindow(root)#App is the class, root is the tkninter window
    root.mainloop() #This will fire the code over and over so that it remains on the page
#if this is ran, pythin will know to only run what is underneath it.
