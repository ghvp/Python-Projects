from tkinter import *
import tkinter as tk

import copy_phonebook_main
import copy_phonebook_func



def load_gui(self):

    #f name label
    self.lbl_fname = tk.Label(self.master,text='First Name: ')
    self.lbl_fname.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    #l name label
    self.lbl_lname = tk.Label(self.master,text='Last Name: ')
    self.lbl_lname.grid(row=2,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    #phone label
    self.lbl_phone = tk.Label(self.master,text='Phone Number: ')
    self.lbl_phone.grid(row=4,column=0,padx=(27,0),pady(10,0),sticky=N+W)
    #email label
    self.lbl_email = tk.Label(self.master,text='Email Address: ')
    self.lbl_email.grid(row=6,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    #info label
    self.lbl_info = tk.Label(self.master,text='Information: ')
    self.lbl_info.grid(row=0,column=2,padx(0,0),pady=(10,0),sticky=N+W)

    #fname text
    self.txt_fname = tk.Entry(self.master,text='')
    self.txt_fname.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    #lname text
    self.txt_lname = tk.Entry(self.master,text='')
    self.txt_lname.grid(row=3,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    #phone text
    self.txt_phone = tk.Entry(self.master,text='')
    self.txt_phone.grid(row=5,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    #email text
    self.txt_email = tk.Entry(self.master,text='')
    self.txt_email.grid(row=7,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)


    #define the listbox with a scrollbar and grid them
    self.scrollbar = Scrollbar(self.master,orient=VERTICAL)
    self.lstList = Listbox(self.master,exportselection=0,yscrollcommand=self.scrollbar1.set)
    self.lstList.bind('<<ListboxSelect>>',lambda event: copy_phonebook_func.onSelect(self,event))
    self.scrollbar1.config(command=self.lstList.yview)
    self.scrollbar1.grid(row=1,column=5,rowspan=7,columnspan=1,padx=(0,0),pady=(0,0),sticky=N+E+S)
    self.lstList.grid(row=1,column=2,rowspan=7,columnspan=3,padx=(0,0),pady=(0,0),sticky=N+E+S+W)

    #button add and close
    self.btn_add = tk.Button(self.master,width=12,height=2,text='Add',command=lambda: copy_phonebook_func.addToList(self))
    self.btn_add.grid(row=8,column=0,padx=(25,0),pady=(45,10),sticky=W)
    self.btn_update = tk.Button(self.master,width=12,height=2,text='Update',command=lambda: copy_phonebook_func.onUpdate(self))
    self.btn_update.grid(row=8,column=1,padx=(15,0),pady=(45,10),sticky=W)
    self.btn_delete = tk.Button(self.master,width=12,height=2,text='Delete',command=lambda: copy_phonebook_func.onDelete(self))
    self.btn_delete.grid(row=8,column=2,padx=(15,0),pady=(45,10),sticky=W)
    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close',command=lambda: copy_phonebook_func.ask_quit(self))
    self.btn_close.grid(row=8,column=4,columnspan=1,padx=(15,0),pady=(45,10),sticky=E)

    copy_phonebook_func.create_db(self)
    copy_phonebook_func.onRefresh(self)

    



if __name__ == "__main__":
    pass

    
    
                              
    
