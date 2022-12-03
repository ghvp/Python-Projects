#python ver 3.11.0

#author vivienne padilla

#tested OS this code was written and tested to work with Windows 10.

#purpose phonebook demo demonstrating OOP. TKinter GUI module, using TKinter
#parent and child relationships

from tkinter import *
import tkinter as tk

#be sure to import other modules to have access to them later
#make sure you revisit and rename these correctly later on
import copy_phonebook_gui
import copy_phonebook_func


#Frame is the tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self,master,*args, **kwargs):
        Frame.__init__(self,master, *args, **kwargs)

    #define our master frame configuration
    self.master =   master
    self.master.minsize(500,300) #(Height, Width)
    self.master.maxsize(500,300)
    #this CenterWindo methodwill center our app on the users screen
    phonebook_func.center_window(self,500,300)
    self.master.title("The tkinter Phone Book Demo")
    self.master.configure(bg="#F0F0F0")
    #this protocol method is a tkinter built in method to catch if
    #the user clicks the upper corner x on window OS
    self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))


    #load in the gui widgets from a seperate module,
    #keeping the code compartmentalized and clutter free
    phonebook_gui.load_gui(self)



    if __name__ == "__main__":
        root = tk.Tk()
        App = ParentWindow(root)
        root.mainloop()
    
