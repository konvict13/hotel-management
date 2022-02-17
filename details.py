from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class detailsroom:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSYTEM")
        self.root.geometry("1295x550+230+220")

        #################title#####################
        lbl_title = Label(self.root, text="ROOMBOOKING DETAILS", font=("times new roman", 18, "bold"), bg="black",
                          fg="yellow", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        ################logo#####################
        img2 = Image.open(r"C:\Users\91944\Desktop\hotelmanagement\logo.jpg")
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.logopageimg = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.logopageimg, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)

        ################label#########
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="NEW ROOM ADDING",font=("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=540, height=350)

        ###########FLOOR##########
        lbl_floor = Label(labelframeleft, text="FLOOR", font=("arial", 12, "bold"), pady=6, padx=2)
        lbl_floor.grid(row=0, column=0, sticky=W)

        self.var_floor=StringVar()
        entry_floor = ttk.Entry(labelframeleft,textvariable=self.var_floor, width=27, font=("arial", 13, "bold"))
        entry_floor.grid(row=0, column=1, sticky=W)

        ###########room no##########
        lbl_roomno = Label(labelframeleft, text="ROOM NO", font=("arial", 12, "bold"), pady=6, padx=2)
        lbl_roomno.grid(row=1, column=0, sticky=W)

        self.var_roomno=StringVar()
        entry_roomno = ttk.Entry(labelframeleft,textvariable=self.var_roomno, width=27,font=("arial", 13, "bold"))
        entry_roomno.grid(row=1, column=1, sticky=W)

        ###########room type##########
        lbl_roomtype = Label(labelframeleft, text="ROOM TYPE", font=("arial", 12, "bold"), pady=6, padx=2)
        lbl_roomtype.grid(row=2, column=0, sticky=W)
        self.var_roomtype=StringVar()
        entry_roomtype = ttk.Entry(labelframeleft,textvariable=self.var_roomtype, width=27, font=("arial", 13, "bold"))
        entry_roomtype.grid(row=2, column=1, sticky=W)

        ############BUTTON##########
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=412, height=40)

        btnadd = Button(btn_frame,command=self.add_data,  text="ADD", font=("arial", 13, "bold"), bg="black",fg="yellow", width=9)
        btnadd.grid(row=0, column=0, padx=1)

        btnupdate = Button(btn_frame,command=self.update, text="UPDATE", font=("arial", 13, "bold"), bg="black",fg="yellow", width=9)
        btnupdate.grid(row=0, column=1, padx=1)

        btndelete = Button(btn_frame,command=self.delete, text="DELETE", font=("arial", 13, "bold"), bg="black",fg="yellow", width=9)
        btndelete.grid(row=0, column=2, padx=1)

        btnreset = Button(btn_frame,command=self.reset,text="RESET", font=("arial", 13, "bold"), bg="black",fg="yellow", width=9)
        btnreset.grid(row=0, column=3, padx=1)

        ##############TABLE FRAME SEARCH ############
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="SHOW ROOM DETAILS",font=("times new roman", 12, "bold"), padx=2)
        table_frame.place(x=600, y=55, width=600, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.room_table = ttk.Treeview(table_frame,
                                       columns=("floor", "roomno", "roomtype"),
                                       xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor", text=" FLOOR")
        self.room_table.heading("roomno", text="ROOM NO")
        self.room_table.heading("roomtype", text="ROOM TYPE ")

        self.room_table["show"] = "headings"

        self.room_table.column("floor", width=100)
        self.room_table.column("roomno", width=100)
        self.room_table.column("roomtype", width=100)
        self.room_table.pack(fill=BOTH, expand=1)

        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

        ###########add data#########

    def add_data(self):
        if self.var_floor.get() == "" or self.var_roomtype.get() == "":
            messagebox.showerror("Error", "FILL ALL FIELDS", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",
                                  (

                                      self.var_floor.get(),
                                      self.var_roomno.get(),
                                      self.var_roomtype.get(),


                                  ))
                conn.commit()
                conn.close()
                self.fetch_data()

                messagebox.showinfo("success", "NEW Room ADDED SUCCESSFULLY", parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning", f"some thing went wrong :{str(es)}", parent=self.root)

        #######fetch data to frame##########

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from details")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            conn.commit()
        conn.close()

        #######get cursor######

    def get_cursor(self, event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]

        self.var_floor.set(row[0]),
        self.var_roomno.set(row[1]),
        self.var_roomtype.set(row[2]),


#######update#####
    def update(self):
        if self.var_floor.get() == "":
            messagebox.showerror("error", "Please enter floor number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel")
            my_cursor = conn.cursor()
            my_cursor.execute(
                "update details set floor=%s,roomtype=%s where roomno=%s ",
                (

                    self.var_floor.get(),
                    self.var_roomtype.get(),
                    self.var_roomno.get()



                ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("update", "room details has been updated successufully", parent=self.root)

 ###########delete#####
    def delete(self):
        delete = messagebox.askyesno("hotel management system", "Do you want to delete this room details",
                                     parent=self.root)
        if delete > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel")
            my_cursor = conn.cursor()
            query = "delete from details where roomno=%s"
            value = (self.var_roomno.get(),)
            my_cursor.execute(query, value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

  #######reset#####
    def reset(self):
        self.var_floor.set(""),
        self.var_roomno.set(""),
        self.var_roomtype.set(""),






































if __name__ == "__main1__":
    root=Tk()
    object=detailsroom(root)
    root.mainloop()