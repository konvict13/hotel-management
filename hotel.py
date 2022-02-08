
from tkinter import *
from PIL import Image,ImageTk
from customer import customer_window



class Hotelmanagementsystem:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSYTEM")
        self.root.geometry("1550x800+0+0")


    ###############backgroundimage#############
        img1=Image.open(r"C:\Users\91944\Desktop\hotelmanagement\pic3.jpg")
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.mainpageimg=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.mainpageimg,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)


    ################logo#####################
        img2 = Image.open(r"C:\Users\91944\Desktop\hotelmanagement\logo.jpg")
        img2 = img2.resize((230, 140), Image.ANTIALIAS)
        self.logopageimg = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.logopageimg, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=140)


    #################title#####################
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="yellow",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)


    #################frame#####################
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)


    ##################menu######################
        lbl_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="black",fg="blue", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)


    #################button frame#####################
        button_frame=Frame(main_frame,bd=4,relief=RIDGE)
        button_frame.place(x=0,y=35,width=228,height=190)

        customer_button=Button(button_frame,text="CUSTOMER",command=self.cust_details(),width=22,font=("times new roman", 14, "bold"), bg="black",fg="gold",bd=0, cursor="hand2")
        customer_button.grid(row=0,column=0,pady=1)


        room_button = Button(button_frame, text="ROOM", width=22, font=("times new roman", 14, "bold"),bg="black", fg="gold", bd=0,cursor="hand2")
        room_button.grid(row=1, column=0,pady=1)

        details_button = Button(button_frame, text="DETAILS", width=22, font=("times new roman", 14, "bold"),bg="black", fg="gold", bd=0, cursor="hand2")
        details_button.grid(row=2, column=0,pady=1)

        report_button = Button(button_frame, text="REPORT", width=22, font=("times new roman", 14, "bold"),bg="black", fg="gold", bd=0, cursor="hand2")
        report_button.grid(row=3, column=0,pady=1)

        logout_button = Button(button_frame, text="LOGOUT", width=22, font=("times new roman", 14, "bold"),bg="black", fg="gold", bd=0,cursor="hand2")
        logout_button.grid(row=4, column=0,pady=1)


    ###################right side image##############
        img3 = Image.open(r"C:\Users\91944\Desktop\hotelmanagement\pic2.jpg")
        img3 = img3.resize((1310, 590), Image.ANTIALIAS)
        self.rightpageimg = ImageTk.PhotoImage(img3)

        lblimg1 = Label(main_frame, image=self.rightpageimg, bd=4, relief=RIDGE)
        lblimg1.place(x=225, y=0, width=1310, height=590)


    #################menu image#######################
        img4 = Image.open(r"C:\Users\91944\Desktop\hotelmanagement\pic5.jpg")
        img4 = img4.resize((230, 210), Image.ANTIALIAS)
        self.menupageimg = ImageTk.PhotoImage(img4)

        lblimg2 = Label(main_frame, image=self.menupageimg, bd=4, relief=RIDGE)
        lblimg2.place(x=0, y=225, width=230, height=210)

        img5 = Image.open(r"C:\Users\91944\Desktop\hotelmanagement\pic4.jpg")
        img5 = img5.resize((230, 190), Image.ANTIALIAS)
        self.menupageimg1 = ImageTk.PhotoImage(img5)

        lblimg3 = Label(main_frame, image=self.menupageimg1, bd=4, relief=RIDGE)
        lblimg3.place(x=0, y=420, width=230, height=190)


    def cust_details(self):
        self.new_window: Toplevel = Toplevel(self.root)
        self.app = customer_window(self.new_window)















if __name__ == '__main__':
    root=Tk()
    object=Hotelmanagementsystem(root)
    root.mainloop()




        

  

