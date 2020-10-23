from tkinter import *
from tkinter import filedialog 
from tkinter import scrolledtext as st

filename=""

# Function to perform preprocessing like remove punctuations etc and extract words
def preprocess(txt):
    lines=txt.split("\n")
    sentences=txt.split(".")
    sentences=sentences[:-1]
    words=[]
    for i in sentences:
        k=0
        if i[k]==" ":
            k+=1
        if i[k]=="\n":
            k+=1
        words.append(i[k:])
    return (lines,words)


# Read the input file
def read_file(file):
    dat=open(file,"r") # opens the file 
    txt=dat.read()
    return txt

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
