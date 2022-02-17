from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSYTEM")
        self.root.geometry("1295x550+230+220")


        ##########variables##########
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavilable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()




        #################title#####################
        lbl_title = Label(self.root, text="ROOMBOOKING DETAILS", font=("times new roman", 18, "bold"), bg="black",fg="yellow", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        ################logo#####################
        img2 = Image.open(r"C:\Users\91944\Desktop\hotelmanagement\logo.jpg")
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.logopageimg = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.logopageimg, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)

        ################label#########
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Roombooking details",font=("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        ###########entry##############

        ###########customer contact##########
        lbl_customer_contact = Label(labelframeleft, text="CUSTOMER CONT", font=("arial", 12, "bold"), pady=6, padx=2)
        lbl_customer_contact.grid(row=0, column=0, sticky=W)

        entry_contact = ttk.Entry(labelframeleft,textvariable=self.var_contact, width=18, font=("arial", 13, "bold"))
        entry_contact.grid(row=0, column=1,sticky=W)

        ###############FETCH DATA BUTTON#######

        btnfetchdata=Button(labelframeleft,command=self.fetch_contact,text="FETCH DATA", font=("arial", 8, "bold"),bg="black",fg="yellow",width=9)
        btnfetchdata.place(x=347,y=4)

        ###########check in date##########
        check_in_date = Label(labelframeleft, text="CHECK-IN DATE", font=("arial", 12, "bold"), pady=6, padx=2)
        check_in_date.grid(row=1, column=0, sticky=W)
        txtcheck_in_date = ttk.Entry(labelframeleft,textvariable=self.var_checkin, width=27, font=("arial", 13, "bold"))
        txtcheck_in_date.grid(row=1, column=1,sticky=W)

        ###########check out date##########
        check_out_date = Label(labelframeleft, text="CHECK-OUT DATE", font=("arial", 12, "bold"), pady=6, padx=2)
        check_out_date.grid(row=2, column=0, sticky=W)
        txt_check_out = ttk.Entry(labelframeleft,textvariable=self.var_checkout,  width=27, font=("arial", 13, "bold"))
        txt_check_out.grid(row=2, column=1,sticky=W)


        ###########room type##########
        lbl_roomtype = Label(labelframeleft, text="ROOM TYPE", font=("arial", 12, "bold"),pady=6, padx=2)
        lbl_roomtype.grid(row=3, column=0, sticky=W)

        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("select roomtype from details")
        rtype = my_cursor.fetchall()

        combo_roomtype=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial", 13, "bold"),width=25,state="readonly")
        combo_roomtype["value"]=rtype
        combo_roomtype.current(0)
        combo_roomtype.grid(row=3,column=1,sticky=W)

        ###########available room##########
        lblroomavailable = Label(labelframeleft, text="AVAILABLE ROOMS", font=("arial", 12, "bold"), pady=6, padx=2)
        lblroomavailable.grid(row=4, column=0, sticky=W)
        #txtroomavailable = ttk.Entry(labelframeleft,textvariable=self.var_roomavilable, width=27, font=("arial", 13, "bold"))
        #txtroomavailable.grid(row=4, column=1,sticky=W)

        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("select roomno from details")
        rows = my_cursor.fetchall()

        combo_roomno = ttk.Combobox(labelframeleft, textvariable=self.var_roomavilable, font=("arial", 13, "bold"),width=25, state="readonly")
        combo_roomno["value"] = rows
        combo_roomno.current(0)
        combo_roomno.grid(row=4, column=1, sticky=W)


        ###########MEAL##########
        lblmeal = Label(labelframeleft, text="MEAL", font=("arial", 12, "bold"), pady=6,padx=2)
        lblmeal.grid(row=5, column=0, sticky=W)
        txtmeal = ttk.Entry(labelframeleft,textvariable=self.var_meal, width=27, font=("arial", 13, "bold"))
        txtmeal.grid(row=5, column=1,sticky=W)

        ###########NO OF DAYS##########
        lblno_ofdays = Label(labelframeleft, text="NO OF DAYS", font=("arial", 12, "bold"), pady=6, padx=2)
        lblno_ofdays.grid(row=6, column=0, sticky=W)
        txtno_ofdays = ttk.Entry(labelframeleft,textvariable=self.var_noofdays, width=27, font=("arial", 13, "bold"))
        txtno_ofdays.grid(row=6, column=1,sticky=W)

        ###########PAID TAX##########
        lblpaid_tax = Label(labelframeleft, text="PAID TAX", font=("arial", 12, "bold"), pady=6, padx=2)
        lblpaid_tax.grid(row=7, column=0, sticky=W)
        txtpaid_tax = ttk.Entry(labelframeleft,textvariable=self.var_paidtax, width=27, font=("arial", 13, "bold"))
        txtpaid_tax.grid(row=7, column=1,sticky=W)

        ###########SUB TOTAL##########
        lblsub_total = Label(labelframeleft, text="SUB TOTAL ", font=("arial", 12, "bold"), pady=6, padx=2)
        lblsub_total.grid(row=8, column=0, sticky=W)
        txtsub_total = ttk.Entry(labelframeleft,textvariable=self.var_actualtotal, width=27, font=("arial", 13, "bold"))
        txtsub_total.grid(row=8, column=1,sticky=W)

        ###########TOTAL COST##########
        lbltotalcost = Label(labelframeleft, text="TOTAL COST", font=("arial", 12, "bold"), pady=6, padx=2)
        lbltotalcost.grid(row=9, column=0, sticky=W)
        txttotalcost = ttk.Entry(labelframeleft,textvariable=self.var_total, width=27, font=("arial", 13, "bold"))
        txttotalcost.grid(row=9, column=1,sticky=W)

        #######bill button########
        btnbill = Button(labelframeleft,command=self.total, text="BILL", font=("arial", 13, "bold"), bg="black", fg="yellow", width=9)
        btnbill.grid(row=10, column=0, padx=1,sticky=W)


        ############BUTTON##########
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnadd = Button(btn_frame,command=self.add_data, text="ADD", font=("arial", 13, "bold"), bg="black",fg="yellow", width=9)
        btnadd.grid(row=0, column=0, padx=1)

        btnupdate = Button(btn_frame,command=self.update, text="UPDATE", font=("arial", 13, "bold"), bg="black",fg="yellow", width=9)
        btnupdate.grid(row=0, column=1, padx=1)

        btndelete = Button(btn_frame,command=self.delete,  text="DELETE", font=("arial", 13, "bold"), bg="black", fg="yellow", width=9)
        btndelete.grid(row=0, column=2, padx=1)

        btnreset = Button(btn_frame,command=self.reset,  text="RESET", font=("arial", 13, "bold"), bg="black",fg="yellow", width=9)
        btnreset.grid(row=0, column=3, padx=1)

        ###########right side image#####
        img3 = Image.open(r"C:\Users\91944\Desktop\hotelmanagement\room.jpg")
        img3 = img3.resize((520, 300), Image.ANTIALIAS)
        self.roompageimg = ImageTk.PhotoImage(img3)

        lblimg = Label(self.root, image=self.roompageimg, bd=0, relief=RIDGE)
        lblimg.place(x=760, y=55, width=520, height=200)



        ##############TABLE FRAME SEARCH ############

        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="view details",font=("times new roman", 12, "bold"), padx=2)
        table_frame.place(x=435, y=280, width=860, height=260)

        lblsearchby = Label(table_frame, text="SEARCH BY  :", font=("arial", 12, "bold"), bg="red", fg="white")
        lblsearchby.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        combo_search = ttk.Combobox(table_frame, textvariable=self.search_var, font=("arial", 13, "bold"), width=24,state="readonly")
        combo_search["value"] = ("contact", "room")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        txtsearch = ttk.Entry(table_frame, textvariable=self.txt_search, width=24, font=("arial", 13, "bold"))
        txtsearch.grid(row=0, column=2)

        btnsearch = Button(table_frame,command=self.search, text="SEARCH", font=("arial", 13, "bold"), bg="black",fg="yellow", width=9)
        btnsearch.grid(row=0, column=3, padx=1)

        btnshow = Button(table_frame,command=self.fetch_data, text="SHOW ALL ",  font=("arial", 13, "bold"), bg="black",fg="yellow", width=9)
        btnshow.grid(row=0, column=4, padx=1)


        #################DATA TABLE##########
        details_table = Frame(table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=180)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.room_table = ttk.Treeview(details_table,
                                              columns=("contact", "checkindate", "checkoutdate", "roomtype", "roomavailable",
                                                       "meal", "noofdays"),
                                              xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact", text=" CONTACT")
        self.room_table.heading("checkindate", text="CHECK-IN")
        self.room_table.heading("checkoutdate", text="CHECK-OUT ")
        self.room_table.heading("roomtype", text="ROOM-TYPE ")
        self.room_table.heading("roomavailable", text="ROOM AVAILABLE ")
        self.room_table.heading("meal", text="MEAL ")
        self.room_table.heading("noofdays", text="NO-OF-DAYS ")

        self.room_table["show"] = "headings"

        self.room_table.column("contact", width=100)
        self.room_table.column("checkindate", width=100)
        self.room_table.column("checkoutdate", width=100)
        self.room_table.column("roomtype", width=100)
        self.room_table.column("roomavailable", width=100)
        self.room_table.column("meal", width=100)
        self.room_table.column("noofdays", width=100)
        self.room_table.pack(fill=BOTH, expand=1)

        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    ###########add data#########
    def add_data(self):
        if self.var_contact.get() == "" or self.var_checkin.get() == "":
            messagebox.showerror("Error", "FILL ALL FIELDS", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",
                                  (

                                      self.var_contact.get(),
                                      self.var_checkin.get(),
                                      self.var_checkout.get(),
                                      self.var_roomtype.get(),
                                      self.var_roomavilable.get(),
                                      self.var_meal.get(),
                                      self.var_noofdays.get()


                                  ))
                conn.commit()
                conn.close()
                self.fetch_data()

                messagebox.showinfo("success", "Room booking successful", parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning", f"some thing went wrong :{str(es)}", parent=self.root)

    #######fetch data to frame##########
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(* self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #######get cursor######
    def get_cursor(self, event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavilable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6]),


    #######update#####
    def update(self):
        if self.var_contact.get() == "":
            messagebox.showerror("error", "Please enter mobile number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel")
            my_cursor = conn.cursor()
            my_cursor.execute(
                "update room set checkin=%s,checkout=%s,roomtype=%s,roomavailable=%s,meal=%s,noofdays=%s where contact=%s ",
                (

                    self.var_checkin.get(),
                    self.var_checkout.get(),
                    self.var_roomtype.get(),
                    self.var_roomavilable.get(),
                    self.var_meal.get(),
                    self.var_noofdays.get(),
                    self.var_contact.get(),


                ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("update", "room details has been updated successufully", parent=self.root)


    ###########delete#####
    def delete(self):
        delete = messagebox.askyesno("hotel management system", "Do you want to delete this customer booking",
                                     parent=self.root)
        if delete > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel")
            my_cursor = conn.cursor()
            query = "delete from room where contact=%s"
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()


    #######reset#####
    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavilable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")




    ##############data fetch####
    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("ERROR","please enter contact number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel")
            my_cursor = conn.cursor()
            query=("select name from customer where mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This number not found",parent=self.root)
            else:


                showdataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showdataframe.place(x=450,y=55,width=300,height=180)

                #########name#############

                lblname=Label(showdataframe,text="Name:",font=("arial",12,"bold"))
                lblname.place(x=0,y=0)

                lbl=Label(showdataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)

                #############gender#########
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel")
                my_cursor = conn.cursor()
                query = ("select gender from customer where mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblgender = Label(showdataframe, text="Gender:", font=("arial", 12, "bold"))
                lblgender.place(x=0, y=30)
                lbl2 = Label(showdataframe, text=row, font=("arial", 12, "bold"))
                lbl2.place(x=90, y=30)

                ###########email###########
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel")
                my_cursor = conn.cursor()
                query = ("select email from customer where mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblemail = Label(showdataframe, text="Email:", font=("arial", 12, "bold"))
                lblemail.place(x=0, y=60)
                lbl3 = Label(showdataframe, text=row, font=("arial", 12, "bold"))
                lbl3.place(x=90, y=60)

                ###########email###########
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel")
                my_cursor = conn.cursor()
                query = ("select nationality from customer where mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblnationality= Label(showdataframe, text="Nationality:", font=("arial", 12, "bold"))
                lblnationality.place(x=0, y=90)
                lbl4 = Label(showdataframe, text=row, font=("arial", 12, "bold"))
                lbl4.place(x=90, y=90)

                ###########address###########
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel")
                my_cursor = conn.cursor()
                query = ("select address from customer where mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lbladdress = Label(showdataframe, text="Address:", font=("arial", 12, "bold"))
                lbladdress.place(x=0, y=120)
                lbl5 = Label(showdataframe, text=row, font=("arial", 12, "bold"))
                lbl5.place(x=90, y=120)

                conn.commit()
                conn.close()


    ##########calculations############
    def total(self):
        indate=self.var_checkin.get()
        outdate=self.var_checkout.get()
        indate=datetime.strptime(indate,"%d/%m/%Y")
        outdate = datetime.strptime(outdate, "%d/%m/%Y")
        self.var_noofdays.set(abs(outdate-indate).days)

        if (self.var_meal.get()=="dinner"and self.var_roomtype.get()=="luxury"):
            q1=float(300)
            q2=float(800)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax="Rs."+str("%.2f"%((q5)*0.1))
            subtotal="Rs."+str("%.2f"%((q5)))
            total="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(subtotal)
            self.var_total.set(total)

        elif (self.var_meal.get()=="breakfast"and self.var_roomtype.get()=="luxury"):
            q1=float(200)
            q2=float(800)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax="Rs."+str("%.2f"%((q5)*0.1))
            subtotal="Rs."+str("%.2f"%((q5)))
            total="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(subtotal)
            self.var_total.set(total)

        elif (self.var_meal.get()=="breakfast"and self.var_roomtype.get()=="Single"):
            q1=float(200)
            q2=float(500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax="Rs."+str("%.2f"%((q5)*0.1))
            subtotal="Rs."+str("%.2f"%((q5)))
            total="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(subtotal)
            self.var_total.set(total)

        elif (self.var_meal.get()=="lunch"and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax="Rs."+str("%.2f"%((q5)*0.1))
            subtotal="Rs."+str("%.2f"%((q5)))
            total="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(subtotal)
            self.var_total.set(total)

        elif (self.var_meal.get()=="breakfast"and self.var_roomtype.get()=="Double"):
            q1=float(200)
            q2=float(600)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax="Rs."+str("%.2f"%((q5)*0.1))
            subtotal="Rs."+str("%.2f"%((q5)))
            total="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(subtotal)
            self.var_total.set(total)


    #############search#############
    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="hotel")
        my_cursor = conn.cursor()

        my_cursor.execute("select * from room where "+str(self.search_var.get())+"LIKE'%"+str(self.txt_search.get()) +"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()




if __name__ == "__main1__":
    root=Tk()
    object=roombooking(root)
    root.mainloop()
