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
def openfile():
    global name
    my_text.delete(1.0,END)
    inputfilename.delete(0,END)
    html_file=filedialog.askopenfilename(title="Open html File",filetypes=(("html files","*.html"),))
    print(html_file)
    name=os.path.basename(html_file)
    formated_name=name.split(".")[0]
    inputfilename.insert(END,formatedname)
    root.title(formatedname)
    html_file=open(name,'r')
    paragraph=html_file.read()
    my_text.insert(END,paragraph)
    html_file.close()
    
def save():
    inputname=inputfilename.get()
    file=open(inputname+".html","w")
    data=my_text.get("1.0",END)
    print(data)
    file.write(data)
    inputfilename.delete(0,END)
    my_text.delete(1.0,END)
    messagebox.showinfo("update","successfully saved the file")
    
def run_html_file():
    global name
    webbrowser.open(name)
    
open_btn=Button(root,image=open_img,text="open file",command=openfile)
open_btn.place(relx=0.05,rely=0.03,anchor=CENTER)

savebtn=Button(root,image=save_img,text="savefile",command=save)
savebtn.place(relx=0.11,rely=0.03,anchor=CENTER)

exitbtn=Button(root,image=exit_img,text="exitfile",command=run_html_file)
exitbtn.place(relx=0.17,rely=0.03,anchor=CENTER)


root.mainloop()