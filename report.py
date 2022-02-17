from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class report:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSYTEM")
        self.root.geometry("1295x550+230+220")

        #################title#####################
        lbl_title = Label(self.root, text=" DEVELOPER DETAILS", font=("times new roman", 18, "bold"), bg="black",
                          fg="yellow", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        ################logo#####################
        img2 = Image.open(r"C:\Users\91944\Desktop\hotelmanagement\logo.jpg")
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.logopageimg = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.logopageimg, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)








if __name__ == "__main1__":
    root=Tk()
    object=report(root)
    root.mainloop()