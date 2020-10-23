from tkinter import *
from tkinter import filedialog 
from tkinter import scrolledtext as st

filename=""

def browseFiles(): 
    fname = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select the Input File", 
                                          filetypes = (("Text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*"))) 
    lbl.configure(text="File Opened: "+filename) 
    filename=fname

root = Tk() 
# root window title and dimension 
root.title("Text_Analyser_LAB_3") 
root.geometry('800x600') 
  
# adding a label to the root window 
lbl = Label(root, text = "Choose a file to run") 
lbl.grid(column=0, row=0) 


btn = Button(root, text = "Browse files" , 
            command=browseFiles) 
btn2= Button(root, text = "Show Stats") 

btn.grid(column=1, row=0,padx=10,pady=10) 
btn2.grid(column=1,row=1)

root.mainloop()

# root window title and dimension 
root.title("Lap_LAB_3") 
root.geometry('900x700') 