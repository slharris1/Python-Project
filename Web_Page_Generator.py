#Author: Shalena Harris
#Objective: Create a basic HTML page using python
# May 7, 2022


import webbrowser
import tkinter as tk
from tkinter import *




class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width = False, height = False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Enter your message here!') #Sets the title of the window. 
        self.master.config(bg='lightgray')

        self.txtWeb = Entry(self.master,text="web text", font=('Georgia', 14,), fg = 'black', bg='salmon')  
        self.txtWeb.grid(row=1, column=1, padx=(200,0), pady=(30,0)) 

        self.btnSubmit = Button(self.master, text ="Submit", width= 10, height=2, command=self.webGenerator) 
        self.btnSubmit.grid(row=2, column=1, padx=(0,0), pady=(30,0), sticky=SE)  

    def webGenerator(self):
        f = open('WebPageGenerator.html', 'w')

        message1 = """ <html>
        <head></head>
        <body><h1>Stay tuned for our amazing summer sale!</h1>"""

        message2 = self.txtWeb.get()
    
        message3 = """</body>
        </html>"""

        f.write(message1 + message2 + message3)
        f.close()

        webbrowser.open_new_tab('WebPageGenerator.html')
        
        
if __name__ == "__main__":
    root = tk.Tk() #syntax in order to create a window from the tkinter
    App = ParentWindow(root)#App is the class, root is the tkninter window
    root.mainloop() #This will fire the code over and over so that it remains on the page
#if this is ran, pythin will know to only run what is underneath it.
