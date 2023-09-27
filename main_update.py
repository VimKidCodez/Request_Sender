from tkinter import *
import requests

root = Tk()
root.title("Request Sender")
root.geometry("400x150")

#Labels-----------------------------------------------------------
heading = Label(root,text="Welcome to request sender",font=("word",24))
heading.place(x=0,y=0)

url_times_label = Label(root,text="Enter times",font =("word",18))
url_times_label.place(x=100,y=65)

url_name = Label(root,text="Enter url",font = ("word",18))
url_name.place(x=100,y=40)

#Functions-------------------------------------------------------------------------------------
def send():
    url = url_input.get()
    times = int(float(url_times.get()))
    for i in range (1,times):
        req = requests.get(f"{url}")
    show_sent_msg()

def show_sent_msg():
    from tkinter import messagebox
    messagebox.showinfo("Done","Requests have been sent")

def clear():
    url_input.delete(0, END)
    url_times.delete(0, END)

#EntryFields-------------------------------------------------------------------------------
url_input = Entry(root)
url_input.place(x=200,y=46)

url_times = Entry(root)
url_times.place(x=230,y=70)

#Buttons----------------------------------------
send_button = Button(root,text="Send",font=("word",18),command=send)
send_button.place(x=120,y=100)

clear_button = Button(root,text="Clear",font = ('word',18),command=clear)
clear_button.place(x=230,y=100)

root.mainloop()