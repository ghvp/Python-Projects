import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
import datetime
from datetime import datetime, timedelta

#setting up the GUI window
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        #Setting the title of the GUI window
        self.master.title("File Transfer")



        #Creates the button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        #Positions source button in the GUI using tkinter grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        #Creates entry for source directory selection
        self.source_dir = Entry(width=75)
        #Positions entry in GUI
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))

        #Creates button to select destination of files from destination directory
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        #Positions destination button in GUI on the next row under the source btn
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        #Creates entry for destination directory selection
        self.destination_dir = Entry(width=75)
        #Positions entry in GUI, the padx and pady are the same so it'll line
        #up with the button
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))

        #creates button to transfers files
        self.transfer_btn = Button(text='Transfer Files', width=20, command=self.transferFiles)
        #positions transfer files button
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))

        #creates an exit button
        self.exit_btn = Button(text='Exit', width=20, command=self.exit_program)
        #positions exit button
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))



   #Creates function to select source directory
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #the .delete(0, END) will clear the content that is inserted in the entry widget,
        #this allows the path to be inserted into the Entry widget properly
        self.source_dir.delete(0, END)
        #The .insert method will insert the user selection to the source_dir Entry
        self.source_dir.insert(0, selectSourceDir)



    #Creates function to select destination directory
    def destDir(self):
        selectDestDir= tkinter.filedialog.askdirectory()
        #the .delete(0, END) will clear the content that is inserted in the entry widget
        #this allows the path to be inserted into the entry widget properly
        self.destination_dir.delete(0, END)
        #the .insert method will insert the user selection to the destination_dir entry widget
        self.destination_dir.insert(0, selectDestDir)




#creates a function that will check for any new or edited files with the
    #last 24 hours
    def file_time(self):
        #get device current date and time
        cur_date = datetime.datetime.now()
        #specifying a folder path for the os module to use
        path = "C:\\Users\\maggi\\OneDrive\\Desktop\\Customer Source"
        #creating a variable to store the os.path.getmtime module
        mod_time = os.path.getmtime(path)
        #deducting the current time from the mod_time of the folder
        diff_time = cur_time - mod_time
        #creating an if statement that won't allow for files older than 24
        #hours to be transferred into the destination folder
        #if diff_time <= datetime.timedelta(1):
                




    #Creates function to transfer files from one directory to another
    def transferFiles(self):
        #gets source directory
        source = self.source_dir.get()
        #gets destination directory
        destination = self.destination_dir.get()
        #gets a list of files in the source directory
        source_files = os.listdir(source)
        #runs through each file in the source directory
        for i in source_files:
            #moves each file from the source to the destination
            diff_time = cur_time - mod_time

            if diff_time <= datetime.timedelta(1):

                shutil.move(source + '/' + i, destination)
                print(i + ' was successfully transferred')
           



    #creates function to exit program
    def exit_program(self):
         #root is the main gui window, the tkinter destroy method
         #tells python to terminate root.mainloop and all widgets inside the
         #gui window
        root.destroy()

    
    
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
