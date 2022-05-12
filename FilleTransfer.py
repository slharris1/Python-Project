import tkinter as tk
from tkinter import *
import shutil
import os
import time
from datetime import datetime, timedelta
from tkinter import filedialog as fd




class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width = False, height = False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('File Transfer') #Sets the title of the window. 
        self.master.config(bg='lightgray')

        self.lblSource = Label(self.master, text='Source Folder:  ', font=('Georgia', 14,), fg = 'black', bg='lightgrey' ) 
        self.lblSource.grid(row=0, column=0, padx=(30,0), pady=(30,0)) 

        self.lblDestination = Label(self.master, text='Destination Folder ', font=('Georgia', 14,), fg = 'black', bg='lightgrey' ) 
        self.lblDestination.grid(row=1, column=0, padx=(30,0), pady=(30,0)) 

        self.txtWeb = Entry(self.master, font=('Georgia', 14,), fg = 'black', bg='salmon')  
        self.txtWeb.grid(row=0, column=1, padx=(10,0), pady=(30,0))

        self.txtWeb2 = Entry(self.master, font=('Georgia', 14,), fg = 'black', bg='salmon')  
        self.txtWeb2.grid(row=1, column=1, padx=(10,0), pady=(30,0)) 

        self.btnSource = Button(self.master, text ="Source", width= 10, height=2, command = self.chooseSource) #This will tie this button to the chooseSource function below
        self.btnSource.grid(row=2, column=0, padx=(30,0), pady=(30,0), sticky=S)  

        self.btnDestination = Button(self.master, text ="Destination", width= 10, height=2, command = self.chooseDestination) #This will tie this button to the chooseDestination function below
        self.btnDestination.grid(row=2, column=2, padx=(0,0), pady=(30,0), sticky=S)  

        self.btnTransfer = Button(self.master, text ="Transfer", width= 10, height=2, command = self.fileTransfer) #This command calls on the file transfer function which is responsible for actually transferring the file. 
        self.btnTransfer.grid(row=2, column=1, padx=(0,0), pady=(30,0), sticky=N)

    def chooseSource(self):
        src = fd.askdirectory() #function that allows for search of directory
        self.txtWeb.delete(0, END) #clears the txt entry box
        self.txtWeb.insert(0, src) #inserts the file into the entry box
    

    def chooseDestination(self):
        dest = fd.askdirectory()
        self.txtWeb2.delete(0, END)
        self.txtWeb2.insert(0, dest)



    def fileTransfer(self):
        source = self.txtWeb.get() #input should be read from line one, char zero
        destination = self.txtWeb2.get() #input should be read from line one, char zero
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
