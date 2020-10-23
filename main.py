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
