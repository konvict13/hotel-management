from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
class customer_window:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSYTEM")
        self.root.geometry("1295x550+230+220")

        #################title#####################
        lbl_title = Label(self.root, text="CUSTOMER DETAILS", font=("times new roman", 18, "bold"), bg="black",fg="yellow", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        ################logo#####################
        img2 = Image.open(r"C:\Users\91944\Desktop\hotelmanagement\logo.jpg")
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.logopageimg = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.logopageimg, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)


        ################label#########
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="customer details",font=("times new roman", 12, "bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)


        ###########entry##############


        ###########REFERENCE##########
        lbl_customer_reference=Label(labelframeleft,text="CUSTOMER REF",font=("arial", 12, "bold"),pady=6,padx=2)
        lbl_customer_reference.grid(row=0,column=0,sticky=W)


        entry_reference=ttk.Entry(labelframeleft,width=29,font=("arial", 13, "bold"))
        entry_reference.grid(row=0,column=1)

        ###########NAME##########
        customer_name= Label(labelframeleft, text="CUSTOMER NAME", font=("arial", 12, "bold"),pady=6, padx=2)
        customer_name.grid(row=1, column=0, sticky=W)
        txtcname= ttk.Entry(labelframeleft, width=29, font=("arial", 13, "bold"))
        txtcname.grid(row=1, column=1)


        ###########FATHERS NAME##########
        lbl_father_name = Label(labelframeleft, text="FATHER NAME", font=("arial", 12, "bold"),pady=6, padx=2)
        lbl_father_name.grid(row=2, column=0, sticky=W)
        txtfname = ttk.Entry(labelframeleft, width=29, font=("arial", 13, "bold"))
        txtfname.grid(row=2, column=1)


        ###########GENDER Combobox##########
        lbl_gender = Label(labelframeleft, text="GENDER :", font=("arial", 12, "bold"),pady=6, padx=2)
        lbl_gender.grid(row=3, column=0, sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,font=("arial", 13, "bold"),width=27,state="readonly")
        combo_gender["value"]=("male","female","other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)



        ###########postcode##########
        lblpostcode= Label(labelframeleft, text="POST CODE", font=("arial", 12, "bold"), pady=6,padx=2)
        lblpostcode.grid(row=4, column=0, sticky=W)
        txtpostcode = ttk.Entry(labelframeleft, width=29, font=("arial", 13, "bold"))
        txtpostcode.grid(row=4, column=1)


        ###########mobile number##########
        lblmobile = Label(labelframeleft, text="MOBILE NUMBER", font=("arial", 12, "bold"), pady=6,padx=2)
        lblmobile.grid(row=5, column=0, sticky=W)
        txtmobile = ttk.Entry(labelframeleft, width=29, font=("arial", 13, "bold"))
        txtmobile.grid(row=5, column=1)


        ###########email##########
        lblemail = Label(labelframeleft, text="EMAIL", font=("arial", 12, "bold"), pady=6,padx=2)
        lblemail.grid(row=6, column=0, sticky=W)
        txtemail = ttk.Entry(labelframeleft, width=29, font=("arial", 13, "bold"))
        txtemail.grid(row=6, column=1)


        ###########nationality##########
        lblnationality = Label(labelframeleft, text="NATIONALITY", font=("arial", 12, "bold"), pady=6,padx=2)
        lblnationality.grid(row=7, column=0, sticky=W)

        combo_nationality = ttk.Combobox(labelframeleft, font=("arial", 13, "bold"), width=27, state="readonly")
        combo_nationality["value"] = ("INDIAN", "FOREIGNER", "other")
        combo_nationality.current(0)
        combo_nationality.grid(row=7, column=1)


        ###########id proof##########
        lblidproof = Label(labelframeleft, text="ID PROOF", font=("arial", 12, "bold"), pady=6, padx=2)
        lblidproof.grid(row=8, column=0, sticky=W)

        combo_proof = ttk.Combobox(labelframeleft, font=("arial", 13, "bold"), width=27, state="readonly")
        combo_proof["value"] = ("PASSPORT", "LICENCE", "other")
        combo_proof.current(0)
        combo_proof.grid(row=8, column=1)


        ###########id number##########
        lblidnumber= Label(labelframeleft, text="ID NUMBER", font=("arial", 12, "bold"), pady=6, padx=2)
        lblidnumber.grid(row=9, column=0, sticky=W)
        txtidnumber = ttk.Entry(labelframeleft, width=29, font=("arial", 13, "bold"))
        txtidnumber.grid(row=9, column=1)



        ###########address##########
        lbladdress = Label(labelframeleft, text="ADDRESS", font=("arial", 12, "bold"), pady=6,padx=2)
        lbladdress.grid(row=10, column=0, sticky=W)
        txtaddress = ttk.Entry(labelframeleft, width=29, font=("arial", 13, "bold"))
        txtaddress.grid(row=10, column=1)



        ############BUTTON##########
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnadd=Button(btn_frame,text="ADD", font=("arial", 13, "bold"),bg="black",fg="yellow",width=9)
        btnadd.grid(row=0,column=0,padx=1)

        btnupdate = Button(btn_frame, text="UPDATE", font=("arial", 13, "bold"), bg="black", fg="yellow", width=9)
        btnupdate.grid(row=0, column=1, padx=1)

        btndelete = Button(btn_frame, text="DELETE", font=("arial", 13, "bold"), bg="black", fg="yellow", width=9)
        btndelete.grid(row=0, column=2, padx=1)

        btnreset = Button(btn_frame, text="RESET", font=("arial", 13, "bold"), bg="black", fg="yellow", width=9)
        btnreset.grid(row=0, column=3, padx=1)


        ##############TABLE FRAME############

        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="view details",font=("times new roman", 12, "bold"), padx=2)
        table_frame.place(x=435, y=50, width=860, height=490)

        lbladdress = Label(table_frame, text="SEARCH BY  :", font=("arial", 12, "bold"),bg="red",fg="white")
        lbladdress.grid(row=0, column=0, sticky=W,padx=2)

        combo_search = ttk.Combobox(table_frame, font=("arial", 13, "bold"), width=24, state="readonly")
        combo_search["value"] = ("MOBILE", "REF")
        combo_search.current(0)
        combo_search.grid(row=0, column=1,padx=2)

        txtsearch = ttk.Entry(table_frame, width=24, font=("arial", 13, "bold"))
        txtsearch.grid(row=0, column=2)

        btnsearch = Button(table_frame, text="SEARCH", font=("arial", 13, "bold"), bg="black", fg="yellow", width=9)
        btnsearch.grid(row=0, column=3, padx=1)

        btnshow= Button(table_frame, text="SHOW ALL ", font=("arial", 13, "bold"), bg="black", fg="yellow", width=9)
        btnshow.grid(row=0, column=4, padx=1)



        #################DATA TABLE##########

        details_table = Frame(table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.cust_detail_table=ttk.Treeview(details_table,columns=("ref","name","father","gender","post","mobile",
                                                                   "email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cust_detail_table.xview)
        scroll_y.config(command=self.cust_detail_table.yview)


        self.cust_detail_table.heading("ref",text="REFER NO")
        self.cust_detail_table.heading("name", text="NAME")
        self.cust_detail_table.heading("father", text="FATHER NAME")
        self.cust_detail_table.heading("gender", text="GENDER ")
        self.cust_detail_table.heading("post", text="POSTCODE ")
        self.cust_detail_table.heading("mobile", text="MOBILE ")
        self.cust_detail_table.heading("email", text="EMAIL ")
        self.cust_detail_table.heading("nationality", text="NATIONALITY ")
        self.cust_detail_table.heading("idproof",text="ID PROOF ")
        self.cust_detail_table.heading("idnumber", text="ID NUMBER ")
        self.cust_detail_table.heading("address", text="ADDRESS ")

        self.cust_detail_table["show"] = "headings"
        self.cust_detail_table.column("ref", width=100)
        self.cust_detail_table.column("name", width=100)
        self.cust_detail_table.column("father", width=100)
        self.cust_detail_table.column("gender", width=100)
        self.cust_detail_table.column("post", width=100)
        self.cust_detail_table.column("mobile", width=100)
        self.cust_detail_table.column("email", width=100)
        self.cust_detail_table.column("nationality", width=100)
        self.cust_detail_table.column("idproof", width=100)
        self.cust_detail_table.column("idnumber", width=100)
        self.cust_detail_table.column("address", width=100)





        self.cust_detail_table.pack(fill=BOTH,expand=1)




































if __name__ == "__main1__":
    root=Tk()
    object=customer_window(root)
    root.mainloop()
