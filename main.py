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

# Function to add information to the widgets
def driver_widget():
    # Get stats from driver function
    freq,sent_no,nwl_nno,word_no,max_word,max_word_count = driver(fname)
    # Configure information to display
    lbl_sentences.configure(text="No of sentences in file: "+sent_no)
    lbl_newlines.configure(text="No of newlines in file: "+nwl_nno)
    lbl_wcount.configure(text="No of words in file: "+word_no)
    lbl_frequency.configure(text="word with most frequency in file: '"+max_word+"'\nIts frequency: "+max_word_count)
    
    # Add labels
    lbl_search_label = Label(root,text="Enter the words to search separated by space or")
    lbl_search_label.grid(column=1,row=2)  
    
    # Button to plot histogram
    hist_plot_btn= Button(root, text = "Plot Histogram" , 
            command=hist_p) 
    hist_plot_btn.grid(column=0,row=1)
    edit_btn = Button(root, text = "Edit" ,command=edit_1) 
    edit_btn.grid(column=2,row=1)

    # Show results of the search
    global text_area
    text_area = Entry(root, width=10) 
    text_area.grid(column = 1, row=3,pady = 1, padx = 5) 
   
    global lbl_upload_2
    # Labels and buttons
    lbl_upload_2 = Label(root, text = "Upload file of keywords separated by space (keep input text blank)") 
    lbl_upload_2.grid(column=1, row=4) 
    up_btn = Button(root, text = "Upload file" , 
            command=browseFiles_search) 
    up_btn.grid(column=1,row=5)

    # Placing these onto the screen
    exe_btn =Button(root, text = "Execute" ,command=find1) 
    exe_btn.grid(column=2,row=5)
    

def browseFiles(): 
    fname = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select the Input File", 
                                          filetypes = (("Text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*"))) 
    label.configure(text="File Opened: "+fname) 
    filename=fname

root = Tk() 
# root window title and dimension 
root.title("Text_Analyser_LAB_3") 
root.geometry('800x600') 
  
# adding a label to the root window 
label = Label(root, text = "Choose a file to run") 
label.grid(column=2, row=0) 


btn = Button(root, text = "Browse files" , 
            command=browseFiles) 
btn2= Button(root, text = "Show Stats") 

btn.grid(column=1, row=0,padx=10,pady=10) 
btn2.grid(column=1,row=1)

root.mainloop()

# root window title and dimension 
root.title("Lap_LAB_3") 
root.geometry('900x700') 
