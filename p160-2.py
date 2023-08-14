from tkinter import*
from tkinter import filedialog
from PIL import ImageTk,Image
from tkinter import messagebox
import os
import webbrowser
root=Tk()
root.title("HTML IDE")
root.minsize(650,650)
root.maxsize(650,650)
root.configure(background="skyblue")
open_img=ImageTk.PhotoImage(Image.open("open.png"))
save_img=ImageTk.PhotoImage(Image.open("save.png"))
exit_img=ImageTk.PhotoImage(Image.open("exit.jpg"))
labelfilename=Label(root,text="File Name")
labelfilename.place(relx=0.28,rely=0.03,anchor=CENTER)
inputfilename=Entry(root)
inputfilename.place(relx=0.46,rely=0.03,anchor=CENTER)
my_text=Text(root,height=35,width=80)
my_text.place(relx=0.5,rely=0.55,anchor=CENTER)

name=""


root.mainloop()