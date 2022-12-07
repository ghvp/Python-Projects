import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        self.btn = Button(self.master, text="Default HTML page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=2,column=3,padx=(10,10) , pady=(10,10))
        #creating a button for the user to submit their custom text
        self.custom_btn = Button(self.master, text="Submit Custom text",width=30, height= 2, command=self.customHTML)
        self.custom_btn.grid(row=2,column=2,padx=(10,10), pady=(10,10))
        #creating an entry field for the user to write their custom text in
        self.custom_text = tk.Entry(self.master, text = '', width=75)
        self.custom_text.grid(row=2, column= 1)
        #creating a lbl for the custom text field
        self.custom_lbl = tk.Label(self.master, text="Enter your custom text here --->")
        self.custom_lbl.grid(row=2, column=0)
        


    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</html>\n</body>\n</h1>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")


    #creating a function for the custom text 
    def customHTML(self):
        #creating a variable that will hold the entry
        custText = (self.custom_text.get())
        #opens the file index.html
        custFile = open("index.html", "w")
        #formatting for the html page and the user entry 
        custContent = "<html>\n<body>\n<h1>" + custText + "</html>\n</body>\n</h1>"
        #writes the content onto the html file
        custFile.write(custContent)
        #closes the html file
        custFile.close()
        #opens the html file in a new tab on the browser
        webbrowser.open_new_tab("index.html")
        
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
