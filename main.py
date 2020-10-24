from tkinter import *
from tkinter import filedialog 
from tkinter import scrolledtext as st
import re

global filename
filename=""

# Read given input file
def read_file(file):
    data1=open(file,"r") # opens the file 
    text=data1.read()
    return text  

# Returns the frequency, bin length, and count of the unique words
def get_freq(wordl):
    (unique, count) = np.unique(wordl, return_count=True)
    freq = np.asarray((unique, count)).T
    bin =set(count)
    len_bin=len(bin)
    # Sorting the freq
    freq=sorted(freq,key=lambda row: row[1]) 
    freq=np.array(freq)
    return (len_bin,freq,count)

# splitting and removing ' ','.','\n' characters 
def preprocess_text(text):
    nwln=text.split("\n")
    sentencespl=text.split(".")
    sentencespl=sentencespl[:-1]
    sentences=[]
    for i in sentencespl:
        k=0
        if i[k]==" ":
            k+=1
        if i[k]=="\n":
            k+=1
        sentences.append(i[k:])
    return (nwln,sentences)
# removing the stopwords from the words list and lowercasing
def remove_common_words(text):
    data=re.sub(r'[^\w\s]', '', text) 
    data=data.lower()
    data=data.split()
    # Commonly occured words 
    extra=set(stopwords.words('english'))
    mod_data=[]
    for i in data:
        if i not in extra:
            mod_data.append(i)
    return (mod_data,data)

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
