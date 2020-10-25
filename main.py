from tkinter import *
from tkinter import filedialog 
from tkinter import scrolledtext as st
import re
from nltk.corpus import stopwords 
import nltk
nltk.download('stopwords')
import numpy as np
import matplotlib.pyplot as plt

global filename
filename=""

# Read given input file
def read_file(file):
    data1=open(file,"r") # opens the file 
    text=data1.read()
    return text  

# Returns the frequency, bin length, and count of the unique words
def get_freq(wordl):
    (unique, count) = np.unique(wordl, return_counts=True)
    freq = np.asarray((unique, count)).T
    bin =set(count)
    len_bin=len(bin)
    # Sorting the freq
    freq=sorted(freq,key=lambda row: row[1]) 
    freq=np.array(freq)
    return (len_bin,freq,count)

# Function used for plotting the frequency values of words in a histogram
def hist_p():
    plt.hist(counts2,bins=bin2)
    plt.title("Histogram of frequency of words")
    plt.xlabel("no of times word occoured")
    plt.ylabel("frequency")
    plt.show()

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


# Opens the notepad for editing
def edit_1():
    programName = "notepad.exe"
    sp.Popen([programName, fname])

# Function to find occurence of a particular words in the file
def find_1():
    words=text_area.get()
    if words=="":
        dat=open(fname2,"r")
        txt=dat.read()
        words=words.lower()
        words=txt.split()
    else:
        words=words.lower()
        words=words.split()
    out=""
    # Prints the the setences where word is found onto the text box
    for i in words:
        out+="The word '"+i+"' is in the following statements:\n"
        for k in sentences3:
            mn=k.lower()
            mn=re.sub(r'[^\w\s]', '', mn) 
            if i in mn.split():
                out+= k+"\n"
        out+="\n"

    # Adding the necessary widgets
    t_area = st.ScrolledText(root, 
                            width = 50,  
                            height = 8,  
                            font = ("Times New Roman", 
                                    12),bg='#f2e9e4') 
    t_area.grid(column = 3,row=7, pady = 10, padx = 10,columnspan=5,sticky='w')  
    t_area.insert(INSERT,out)
    t_area.configure(state='disabled')

# Funtion to browse the files using tkinter's filedialog system
def browseFiles_search(): 
    filename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("Text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*"))) 
    lbl_upload_2.configure(text="File Opened: "+filename+"\n(Keep above input blank)") 
    global fname2
    fname2=filename




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

# Defined driver code for opening the file and do the file processing
def driver(file1):
    txt = read_file(file1)  

    # Performing splitting into words and removing '.',' ','\n' characters  
    new_ln,sent = preprocess_text(txt)

    # Lowercasing and Removing the stopwords i.e. the commonly occuring articles preposiitons from the words list
    mod_data,data = remove_common_words(txt)
    word_list = np.array(mod_data)

    # Finding the (word -> frequency) values using the numpy's unique function
    bin1,frequencies,counts = get_freq(word_list)

   # Storing the values in globalvars so as to be used later for plotting 
    global bin2
    bin2=bin1

    global counts2
    counts2=counts
    
    global sentences3
    sentences3=sent

    return frequencies,str(len(sent)),str(len(new_ln)),str(len(data)),frequencies[-1][0],str(frequencies[-1][-1])


# Function to add information to the widgets
def driver_widget():
    # Get stats from driver function
    
    freq,sent_no,nwl_nno,word_no,max_word,max_word_count = driver(filename)
    print(freq)
    # Configure information to display
    lbl_sentences.configure(text="No of sentences in file: "+sent_no)
    lbl_newlines.configure(text="No of newlines in file: "+nwl_nno)
    lbl_wcount.configure(text="No of words in file: "+word_no)
    lbl_frequency.configure(text="word with most frequency in file: '"+max_word+"'\nIts frequency: "+max_word_count)
    
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
    exe_btn =Button(root, text = "Execute" ,command=find_1) 
    exe_btn.grid(column=2,row=5)

    # Button to plot the histogram
    hist_plot_btn= Button(root, text = "Plot Histogram" , 
            command=hist_p,width =20,bg="#9a8c98",highlightthickness=2,highlightbackground="white") 
    hist_plot_btn.grid(column=0,row=1,columnspan=2,sticky='w',padx=5)
    

def browseFiles(): 
    fname = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select the Input File", 
                                          filetypes = (("Text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*"))) 
    label.configure(text="File Opened: "+fname) 
    global filename
    filename=fname

root = Tk() 
# root window title and dimension 
root.title("Text_Analyser_LAB_3") 
root.geometry('800x600') 
  
# adding a label to the root window 
label = Label(root, text = "Choose a file to run") 
label.grid(column=2, row=0) 

lbl_sentences = Label(root,width=40,anchor=W,bg="#c9ada7")
lbl_sentences.grid(column=0,row=3,columnspan=4)

lbl_wcount =Label(root,width=40,anchor=W,bg="#c9ada7")
lbl_wcount.grid(column=0,row=2,columnspan=4)

lbl_newlines =Label(root,width=40,anchor=W,bg="#c9ada7")
lbl_newlines.grid(column=0,row=6,columnspan=4)

lbl_frequency =Label(root,width=40,anchor=W,bg="#c9ada7")
lbl_frequency.grid(column=0,row=4,columnspan=4)

lbl_frequency2 =Label(root,width=40,anchor=W,bg="#c9ada7")
lbl_frequency2.grid(column=0,row=5,columnspan=4)



btn = Button(root, text = "Browse files" , 
            command=browseFiles) 
btn2= Button(root, text = "Show Stats",command=driver_widget) 

btn.grid(column=1, row=0,padx=10,pady=10) 
btn2.grid(column=1,row=1)

root.mainloop()

# root window title and dimension 
root.title("Lap_LAB_3") 
root.geometry('900x700') 
