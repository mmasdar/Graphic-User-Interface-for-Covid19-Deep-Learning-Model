# import tkinter and all its functions
from tkinter import * 
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image


root = Tk() # create root window
root.title("Bondo Bismillah!")
root.config(bg="#000000")
root.geometry('835x700')

background = '#313131'
bg_frame = '#212121'

# Create Frame kanan bawah
kanan2_frame = Frame(root, width=620, height=400, bg=bg_frame)
kanan2_frame.place(x=210, y=60)

# Create Frame kanan
kanan_frame = Frame(root, width=620, height=225, bg=bg_frame)
kanan_frame.place(x=210, y=465)


# Create Frame kiri bawah
left2_frame = Frame(root, width=200, height=300, bg=bg_frame)
left2_frame.place(x=5, y=290)

# Create Frame kiri
left_frame = Frame(root, width=200, height=225, bg=bg_frame)
left_frame.place(x=5, y=60)

# Title untuk masing-masing frame 
label1 = Label(root, text="Thorax X-ray Analysis System Based on Artificial Intelligence", font=("Arial Bold", 20), bg='black', fg='white')
label1.place(x=10, y=2)

label12 = Label(root, text="Copyright : mmasadar@gmail.com - Brawijaya University", font=("Arial Bold", 10), bg='black', fg='white')
label12.place(x=230, y=35)

label2 = Label(left2_frame, text="HASIL DIAGNOSIS", bg=bg_frame, font=("Arial Bold", 13), fg='white')
label2.place(x=25, y=5)

label3 = Label(kanan2_frame, text="Feature Extraction of 2D Convolution Layer", bg=bg_frame, font=("Arial", 13), fg='white')
label3.place(x=140, y=5)

label4 = Label(kanan_frame, text="Grafik Flatten Layer", bg=bg_frame, font=("Arial", 13), fg='white')
label4.place(x=230, y=5)

# Membuat frame di dalam frame
tool_bar1 = Frame(left_frame, width=190, height=180, bg=background)
tool_bar1.place(x=5, y=40)

tool_bar2 = Frame(left2_frame, width=190, height=260, bg=background)
tool_bar2.place(x=5, y=35)

tool_bar3 = Frame(kanan_frame, width=610, height=185, bg=background)
tool_bar3.place(x=5, y=35)

tool_bar4 = Frame(kanan2_frame, width=610, height=360, bg=background)
tool_bar4.place(x=5, y=35)


#Bagian UX
def getJPG ():
    global im1

    image = PhotoImage(file="G:\KULIAH\Semester 8\SKRIPSI\Project-Skripsi\GUI dan pip\Case 9 - M70YO - 3.png")
    #import_file_path = filedialog.askopenfilename()
    #image = Image.open(import_file_path)
    original_image = Label(tool_bar1, width=185, height=180, image=image)
    original_image.image = image
    original_image.pack()

def konvolusi ():
    global im1

    image = PhotoImage(file="G:\KULIAH\Semester 8\SKRIPSI\Project-Skripsi\GUI dan pip\Case 9 - M70YO - 3.png")
    #import_file_path = filedialog.askopenfilename()
    #image = Image.open(import_file_path)
    original_image = Label(tool_bar4, width=185, height=180, image=image)
    original_image.image = image
    original_image.pack()

# Create label above the tool_bar
browseButton_JPG = Button(left_frame, width=26, height=0, text="Input Citra Baru", bg='#626262', fg='white', font=("Arial Bold",10),
	command=getJPG).place(x=0, y=0)

browseButton_diagnosis = Button(root, width=16, height=3, bg='#800000', fg='white', text="MULAI ANALISIS", font=("Arial Bold", 15),
	command=konvolusi).place(x=5, y=595)


root.mainloop()