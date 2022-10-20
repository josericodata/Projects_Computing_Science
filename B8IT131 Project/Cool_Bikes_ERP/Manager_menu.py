#Cool Bikes ERP System
#Student: Jose Maria Rico Leal
#Student Number: 10539218
#Module: B8IT131 Project

import sqlite3
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from Tkinter_classes import typebox,typeauto


# MANAGER MENU
class Manager:
    #1
    def __init__(self,mainn):#Initialising the class objects attributes
        self.mainn=mainn

    #2
    def manager_mainmenu(self,a,b):#Setting up manager method, creating layout and widgets. Formatting images, frames and buttons.
         self.ppalframe = LabelFrame(self.mainn, width=1336, height=145,bg="#46fb81")
         self.ppalframe.place(x=100, y=650)#Bottom, frame position add bikes, stocks, invoices, users, change user and log out.
         ab = PhotoImage(file="images/bikes.png")#First button "Add Bikes"
         ab = ab.subsample(a,b)
         self.items = Button(self.ppalframe, text="Add Bikes",bg="cyan",bd=5, image=ab,font="roboto 11 bold", compound=TOP,command=self.additems)
         self.items.image = ab
         self.items.place(x=68, y=27)
         ab = PhotoImage(file="images/stocks.png")#Second button "Stocks"
         ab = ab.subsample(a,b)
         self.stocks = Button(self.ppalframe, text="Stocks",bg="cyan",bd=5, image=ab,font="roboto 11 bold", compound=TOP,command=self.buildprodtable)
         self.stocks.image = ab
         self.stocks.place(x=278, y=27)
         ab = PhotoImage(file="images/invoices.png")#Third button "Invoices"
         ab=ab.subsample(a,b)
         self.sales = Button(self.ppalframe, text="Invoices",bg="cyan",bd=5,font="roboto 11 bold", image=ab, compound=TOP,command=self.createsalestable)
         self.sales.image = ab
         self.sales.place(x=492, y=27)
         ab = PhotoImage(file="images/users.png")#Fourth button "Users"
         ab = ab.subsample(a,b)
         self.accounts = Button(self.ppalframe, text="Users",bg="cyan",font="roboto 11 bold",bd=5,image=ab, compound=TOP,command=self.createusertable)
         self.accounts.image = ab
         self.accounts.place(x=706, y=27)
         ab = PhotoImage(file="images/swapuser.png")#Fifth button "Change User"
         ab = ab.subsample(a,b)
         self.swapuser = Button(self.ppalframe, text="Change User",bg="cyan",bd=5,font="roboto 11 bold", image=ab, compound=TOP)
         self.swapuser.image = ab
         self.swapuser.place(x=920, y=27)
         ab = PhotoImage(file="images/signout.png")#Sixth button "Log Out"
         ab = ab.subsample(a,b)
         self.signout = Button(self.ppalframe, text="Log Out",bg="cyan",bd=5,font="roboto 11 bold", image=ab, compound=TOP)
         self.signout.image = ab
         self.signout.place(x=1180, y=27)#End of bottom buttons bar
         self.windowform = Frame(self.mainn, width=500, height=450, bg="#FFFFFF")
         self.windowform.place(x=100, y=170)#Inventory fields Type, Specs, Groupset, Price, Current Stock and Add Stock.
         self.windowforminfo = self.windowform.place_info()
         self.commontable = LabelFrame(self.mainn, width=350, height=700)
         self.commontable.place(x=1350, y=240, anchor=NE)#User table position
         self.infotable = self.commontable.place_info()
         self.tablewindow = LabelFrame(self.mainn, width=450, height=700)
         self.tablewindow.place(x=1430, y=220, anchor=NE)#Inventory table position
         self.genericwindowinfo=self.tablewindow.place_info()
         self.productwindow = Frame(self.mainn, bg="#FFFFFF", width=600, height=300)
         self.productwindow.place(x=420, y=130, anchor=NW)#Add Bike table
         self.productwindowinfo=self.productwindow.place_info()
         self.windowframe = Frame(self.mainn, width=500, height=445, bg="#FFFFFF")
         self.windowframe.place(x=200,y=150)#User fields position, Create a User, Username, Password, Profile Type, Update & Remove.
         self.templateframeinfo = self.windowframe.place_info()
         self.lookupframe = Frame(self.mainn, width=720, height=70, bg="#FFFFFF")
         self.lookupframe.place(x=575, y=260)
         self.lookupframeinfo = self.lookupframe.place_info()
         self.lookupbutton = Button(self.lookupframe, text="Search Description", font="roboto 14", bg="#FFFFFF", bd=5, command=self.lookupbike)
         self.lookupbutton.place(x=0, y=20, height=40)
         self.lookupvar=StringVar()
         self.lookupentry = typeauto(self.lookupframe, textvariable=self.lookupvar, font="roboto 14", width=25, bg="#FFFFFF")
         self.lookupentry.place(x=210, y=20, height=40)
         self.cur.execute("select bike_specs from bikes")
         li = self.cur.fetchall()
         a = []
         for i in range(0, len(li)):
             a.append(li[i][0])
         self.lookupentry.set_completion_list(a)
         self.cleanbutton = Button(self.lookupframe, text="Clear", font="roboto 14", bd=5, width=8, bg="#FFFFFF", command=self.resetbiketable)
         self.cleanbutton.place(x=510, y=18, height=40)
         self.cond=0
         self.buildprodtable()
         self.additems()#Call the startup function additems
    # MANAGER MAIN MENU ENDS

    #3
    def buildprodtable(self):#Creating product table shown in Stocks tab.
         self.lookupframe.place_forget()
         self.tablewindow.place(self.genericwindowinfo)
         self.windowform.place(self.windowforminfo)
         self.commontable.place_forget()
         self.windowframe.place_forget()
         self.productwindow.place_forget()
         if(self.cond==1):
            self.tree.delete(*self.tree.get_children())
            self.tree.grid_remove()
            self.tree.destroy()
         slidebarx = Scrollbar(self.tablewindow, orient=HORIZONTAL)
         slidebary = Scrollbar(self.tablewindow, orient=VERTICAL)
         self.tree = ttk.Treeview(self.tablewindow, columns=("Bike ID", "Type", "Specs", "Groupset",
         'Price', 'Stocks','Customer'), selectmode="browse", height=18,yscrollcommand=slidebary.set, xscrollcommand=slidebarx.set)
         self.tree.column('#0', stretch=NO, minwidth=0, width=0)
         self.tree.column('#1', stretch=NO, minwidth=0, width=50)
         self.tree.column('#2', stretch=NO, minwidth=0, width=60)
         self.tree.column('#3', stretch=NO, minwidth=0, width=300)
         self.tree.column('#4', stretch=NO, minwidth=0, width=150)
         self.tree.column('#5', stretch=NO, minwidth=0, width=50)
         self.tree.column('#6', stretch=NO, minwidth=0, width=50)
         self.tree.column('#7', stretch=NO, minwidth=0, width=130)
         self.tree.heading('Bike ID', text="Bike ID", anchor=W)
         self.tree.heading('Type', text="Type", anchor=W)
         self.tree.heading('Specs', text="Specs", anchor=W)
         self.tree.heading('Groupset', text="Groupset", anchor=W)
         self.tree.heading('Price', text="Price", anchor=W)
         self.tree.heading('Stocks', text="Stocks", anchor=W)
         self.tree.heading('Customer', text="Customer", anchor=W)
         self.tree.grid(row=1, column=0, sticky="W")
         slidebary.config(command=self.tree.yview)
         slidebarx.grid(row=2, column=0, sticky="we")
         slidebarx.config(command=self.tree.xview)
         slidebary.grid(row=1, column=1, sticky="ns", pady=30)
         self.getbikes()
         self.tree.bind("<<TreeviewSelect>>", self.clickbikestable)
         self.windowform.focus_set()
         self.biketype = StringVar()
         self.bikespecs = StringVar()
         self.bikegroupset = StringVar()
         self.bikeprice = StringVar()
         self.bikestock = StringVar()
         self.customer = StringVar()
         self.addstock = StringVar()
         no = 6
         DF = ['Type', 'Specs', 'Groupset', 'Price', 'Current Stock','Customer','Add Stock']#Inventory fields
         for i in range(0,7):
             Label(self.windowform, text=DF[i], font="roboto 14 bold", bg="#FFFFFF").place(x=0, y=no)
             no += 60
         Entry(self.windowform, textvariable=self.biketype, font="roboto 14",bg="#FFFFFF", width=20).place(x=142, y=0, height=40)
         Entry(self.windowform, textvariable=self.bikespecs, font="roboto 14",bg="#FFFFFF", width=20).place(x=142, y=60, height=40)
         x=typeauto(self.windowform, textvariable=self.bikegroupset, font="roboto 14",bg="#FFFFFF", width=20)
         x.place(x=142, y=120, height=40)
         self.cur.execute("select bike_groupset from bikes")
         li = self.cur.fetchall()
         a = []
         self.desc_name = []
         for i in range(0, len(li)):
             if (a.count(li[i][0]) == 0):
                 a.append(li[i][0])
         x.set_completion_list(a)
         Entry(self.windowform, textvariable=self.bikeprice, font="roboto 14",bg="#FFFFFF", width=20).place(x=142, y=180, height=40)
         Entry(self.windowform, textvariable=self.bikestock, font="roboto 14",bg="#FFFFFF", width=20).place(x=142, y=240, height=40)
         Entry(self.windowform, textvariable=self.customer, font="roboto 14",bg="#FFFFFF", width=20).place(x=142, y=300, height=40)
         Entry(self.windowform, textvariable=self.addstock, font="roboto 14",bg="#FFFFFF", width=20).place(x=142, y=360, height=40)
         Button(self.windowform, text="Change", font="robot 11 bold",bg="#FFFFFF", bd=5, width=10, height=1,
         command=self.changebikestable).place(x=105, y=410)
         Button(self.windowform, text="Delete", font="robot 11 bold",bg="#FFFFFF", bd=5, width=10, height=1,
         command=self.delbikes).place(x=305, y=410)
         self.cond=1
         self.lookupmain(1)

    #4
    def lookupmain(self, f):#Creating search buttons for different tabs.
        self.lookupvar.set('')
        if (f==1):
            self.lookupframe.config(width=720)
            self.lookupframe.place(x=630, y=125)#Position Search Description field, from inventory.
            self.lookupbutton.config(text="Look up by Specs",command=self.lookupbike)
            self.lookupbutton.place(x=0, y=23, height=37)
            self.lookupentry.config(textvariable=self.lookupvar,width=35)
            self.lookupentry.place(x=200, y=25, height=35)
            self.cur.execute("select bike_specs from bikes")
            li = self.cur.fetchall()
            a = []
            for i in range(0, len(li)):
                a.append(li[i][0])
            self.lookupentry.set_completion_list(a)
            self.cleanbutton.config(command=self.resetbiketable)
            self.cleanbutton.place(x=615, y=22, height=37)
        elif(f==0):
            self.lookupframe.place(x=815, y=140)#Search Username position, user tab.
            self.lookupframe.config(width=520)
            self.lookupbutton.config(command=self.lookupuser)
            self.lookupbutton.config(text="Select an Employee")
            self.lookupbutton.place(x=0,y=23)
            self.lookupentry.config(width=18,textvariable=self.lookupvar)
            self.lookupentry.place(x=195, y=25, height=35)
            self.cleanbutton.config(command=self.lookupusertable)
            self.cleanbutton.place(x=415,y=23)
            self.cur.execute("select username from users")
            li = self.cur.fetchall()
            a = []
            for i in range(0, len(li)):
                a.append(li[i][0])
            self.lookupentry.set_completion_list(a)
        else:
            self.lookupframe.place(x=105, y=143)#Search Invoice position, Sales tab. 
            self.lookupframe.config(width=520)
            self.lookupbutton.config(command=self.findinvoice)
            self.lookupbutton.config(text="Look up by Invoice")
            self.lookupbutton.place(x=0, y=23)
            self.lookupentry.config(width=18, textvariable=self.lookupvar)
            self.lookupentry.place(x=195, y=25, height=35)
            self.cleanbutton.config(command=self.createsalestable)
            self.cleanbutton.place(x=415, y=23)
            self.cur.execute("select invoice from sales")
            li = self.cur.fetchall()
            a = []
            for i in range(0, len(li)):
                if(a.count(str(li[i][0]))==0):
                    a.append(str(li[i][0]))
            self.lookupentry.set_completion_list(a)

    #5 
    def getbikes(self,x=0):#Fetch bikes from bikes table, creating a list to populate inventory table in manager and mechanic menus.
         ans=''
         self.cur.execute("select * from bikes")
         bikelist = self.cur.fetchall()
         for i in bikelist:
              self.tree.insert('', 'end', values=(i))
              if (str(x) == i[0]):
                  a=self.tree.get_children()
                  ans=a[len(a)-1]

         return ans

    #6 
    def changebikestable(self):#6 Modifies record from bikes table.
        cur = self.tree.selection()
        cur = self.tree.item(cur)
        li = cur['values']
        self.biketype.set((self.biketype.get()).upper())
        self.bikegroupset.set((self.bikegroupset.get()).upper())
        self.bikespecs.set((self.bikespecs.get()).upper())
        self.customer.set((self.customer.get()).upper())
        if(len(li) == 7):
            if self.biketype.get() == '' or self.bikespecs.get() == '':
                messagebox.showerror("Error", "Please Fill All Fields")
                return
            elif self.bikegroupset.get() == '' or self.bikestock.get() == '' or self.bikeprice.get() == '' or self.customer.get() == '':
                messagebox.showerror("Error", "Please Fill All Fields")
                return
            else:
                l = [self.bikeprice.get(), self.bikestock.get()]
                for i in range(0, len(l)):
                    if (not l[i].isdigit()):
                        messagebox.showerror("Error", "Invalid Data Provided")
                        return
                    elif (int(l[i]) < 0):
                        messagebox.showerror("Error", "Invalid Data Provided")
                        return
            if(self.addstock.get()== ''):
                self.addstock.set('0')

            self.cur.execute("update bikes set bike_type=?,bike_specs=?,bike_groupset=?,bike_price = ?,stocks = ?,Customer = ? where bike_id = ?;",(self.biketype.get(),self.bikespecs.get(),self.bikegroupset.get(),int(self.bikeprice.get()),(int(self.bikestock.get())+int(self.addstock.get())),self.customer.get(),li[0]))
            self.base.commit()
            self.addstock.set('')
            self.tree.delete(*self.tree.get_children())
            cur=self.getbikes(li[0])
            self.tree.selection_set(cur)
    #7
    def delbikes(self):#Delete bike method.
        cur = self.tree.focus()
        cur = self.tree.item(cur)
        li = cur['values']
        if messagebox.askyesno('Cool Bikes, ERP System','Do you want to remove this bike?') == True and len(li) ==7:
            self.cur.execute("delete from bikes where bike_id = ?;", (li[0],))
            self.base.commit()
            self.tree.delete(*self.tree.get_children())
            self.getbikes()
            self.biketype.set('')
            self.bikespecs.set('')
            self.bikegroupset.set('')
            self.bikestock.set('')
            self.bikeprice.set('')
            self.customer.set('')
    #8
    def lookupbike(self):#Method to search bikes by specs in stocks tab.
        if (self.lookupvar.get() == ''):
            return
        self.tree.delete(*self.tree.get_children())
        self.cur.execute("select * from bikes")
        li=self.cur.fetchall()
        for i in li:
            if(i[2]==self.lookupvar.get()):
                self.tree.insert('', 'end', values=(i))
    #9
    def resetbiketable(self):#Method to clear fields in stocks tab.
        self.lookupvar.set('')
        self.tree.delete(*self.tree.get_children())
        self.getbikes()

    #10
    def clickbikestable(self, event):#Onclick event for bikes table in stocks tab.
        cur = self.tree.selection()
        cur = self.tree.item(cur)
        li = cur['values']
        if (len(li) == 7):
            self.biketype.set((li[1]))
            self.bikespecs.set((li[2]))
            self.bikegroupset.set((li[3]))
            self.bikeprice.set(str(li[4]))
            self.bikestock.set(str(li[5]))
            self.customer.set(str(li[6]))
            self.addstock.set('')

    #11
    def additems(self):#11 Method adding bikes, start-up page.
        self.windowframe.place_forget()
        self.lookupframe.place_forget()
        self.tablewindow.place_forget()
        self.commontable.place_forget()
        self.windowform.place_forget()
        self.productwindow.place(self.productwindowinfo)
        self.newbike = StringVar()
        self.newbikedesc = StringVar()
        self.newbikecode = StringVar()
        self.newbikecat = StringVar()
        self.newbikeprice = StringVar()
        self.newbikestock  = StringVar()
        self.newcustomer  = StringVar()
        l=['Bike ID',"Type","Specs","Groupset","Price","Stock","Customer"]
        for i in range(0,len(l)):
            Label(self.productwindow,text=l[i],font="Roboto 14 bold",bg="#ffffff").grid(row=i,column=0,pady=15,sticky="w")
        Entry(self.productwindow, width=60, textvariable=self.newbikecode,font="roboto 11",bg="#ffffff").grid(row=0, column=1,pady=15,padx=10,ipady=3)
        Entry(self.productwindow,width=60,textvariable=self.newbike,font="roboto 11",bg="#ffffff").grid(row=1,column=1,pady=15,padx=10,ipady=3)
        Entry(self.productwindow,width=60,textvariable=self.newbikedesc,font="roboto 11",bg="#ffffff").grid(row=2,column=1,pady=15,padx=8,ipady=3)
        cat=typeauto(self.productwindow,width=60,textvariable=self.newbikecat,font="roboto 11",bg="#ffffff")
        cat.grid(row=3,column=1,pady=15,padx=10,ipady=3)
        Entry(self.productwindow, width=60, textvariable=self.newbikeprice,font="roboto 11",bg="#ffffff").grid(row=4, column=1, pady=15, padx=10,ipady=3)
        Entry(self.productwindow, width=60, textvariable=self.newbikestock,font="roboto 11",bg="#ffffff").grid(row=5, column=1, pady=15, padx=10,ipady=3)
        Entry(self.productwindow, width=60, textvariable=self.newcustomer,font="roboto 11",bg="#ffffff").grid(row=6, column=1, pady=15, padx=10,ipady=3)
        self.cur.execute("select bike_groupset,bike_type,bike_specs from bikes")
        li=self.cur.fetchall()
        a=[]
        self.desc_name=[]
        for i in range(0,len(li)):
            if(a.count(li[i][0])==0):
                a.append(li[i][0])
            self.desc_name.append(li[i][2])
        cat.set_completion_list(a)
        Button(self.productwindow,text="Add bike", font="robot 12 bold",height=1,bd=5,command=self.insertbike,bg="#FFFFFF").grid(row=7,column=1,pady=10,padx=12,sticky="w",ipadx=10)
        Button(self.productwindow, text="Back", font="robot 12 bold",height=1,width=8, bd=5,command=self.buildprodtable,bg="#FFFFFF").grid(row=7, column=1,padx=16, pady=10,sticky="e",ipadx=10)

    #12 
    def insertbike(self):#Method that checks if fields to add a bike are filled up correctly.
        self.newbike.set((self.newbike.get()).upper())
        self.newbikedesc.set((self.newbikedesc.get()).upper())
        self.newbikecat.set((self.newbikecat.get()).upper())
        if self.newbikecode.get() == '' or self.newbike.get() == '' or self.newbikedesc.get() == '':
            messagebox.showerror("Error", "Please Fill All Fields")
            return
        elif self.newbikecat.get() == '' or self.newbikeprice.get() == '' or self.newbikestock.get() == '':
            messagebox.showerror("Error", "Please Fill All Fields")
            return
        else:
            l=[self.newbikecode.get(),self.newbikeprice.get(),self.newbikestock.get()]
            for i in range(0,len(l)):
                if(not l[i].isdigit()):
                    if(i==0):
                        messagebox.showerror("Error", "Bike ID should be in numeral")
                    else:
                        messagebox.showerror("Error", "Invalid Data Provided")
                    return
                elif(int(l[i])<0):
                    messagebox.showerror("Error", "Invalid Data Provided")
                    return
        self.cur.execute('select * from bikes where bike_id = ?',(int(self.newbikecode.get()),))
        l=self.cur.fetchall()
        if(len(l)>0):
            messagebox.showerror("Error", "Bike ID Should Be Unique")
            return
        if(self.desc_name.count(self.newbikedesc.get())!=0):
            messagebox.showerror('Error','Bike with same description exists!')
            return
        x=int(self.newbikecode.get())
        y=int(self.newbikeprice.get())
        z=int(self.newbikestock.get())
        self.cur.execute("insert into bikes values(?,?,?,?,?,?,?)",(x,self.newbike.get(),self.newbikedesc.get(),
        self.newbikecat.get(),y,z,self.newcustomer.get()))
        self.newbike.set('')
        self.newbikestock.set('')
        self.newbikeprice.set('')
        self.newbikedesc.set('')
        self.newbikecode.set('')
        self.newbikecat.set('')
        self.newcustomer.set('')
        messagebox.showinfo('Success','Item Added Successfully')
        self.base.commit()

    #13
    def createusertable(self):#Building user table.
         self.lookupframe.place_forget()
         self.windowform.place_forget()
         self.tablewindow.place_forget()
         self.productwindow.place_forget()
         self.windowframe.place(self.templateframeinfo)
         self.commontable.place(self.infotable)
         self.tree.delete(*self.tree.get_children())
         self.tree.grid_remove()
         self.tree.destroy()
         slidebarx = Scrollbar(self.commontable, orient=HORIZONTAL)
         slidebary = Scrollbar(self.commontable, orient=VERTICAL)
         self.tree = ttk.Treeview(self.commontable, columns=("Username", "Password", "Account Type"),
         selectmode="browse", height=17,yscrollcommand=slidebary.set, xscrollcommand=slidebarx.set)
         self.tree.column('#0', stretch=NO, minwidth=0, width=0)
         self.tree.column('#1', stretch=NO, minwidth=0, width=170)
         self.tree.column('#2', stretch=NO, minwidth=0, width=170)
         self.tree.column('#3', stretch=NO, minwidth=0, width=170)
         self.tree.heading('Username', text="Username", anchor=W)
         self.tree.heading('Password', text="Password", anchor=W)
         self.tree.heading('Account Type', text="Account Type", anchor=W)
         self.tree.grid(row=1, column=0, sticky="W")
         slidebary.config(command=self.tree.yview)
         slidebarx.grid(row=2, column=0, sticky="we")
         slidebarx.config(command=self.tree.xview)
         slidebary.grid(row=1, column=1, sticky="ns", pady=30)
         self.findusers()
         self.tree.bind("<<TreeviewSelect>>", self.onclickusertable)
         self.windowframe.focus_set()
         self.typeusername = StringVar()
         self.typepassword = StringVar()
         self.accedit = StringVar()
         no = 110
         DF = ['Username', 'Password','Profile Type']
         for i in range(0,3):
             Label(self.windowframe, text=DF[i], font="roboto 14 bold", bg="#FFFFFF").place(x=0, y=no)
             no += 70
         Entry(self.windowframe, textvariable=self.typeusername, font="roboto 14", bg="#FFFFFF", width=25,state='readonly').place(x=162, y=105, height=40)#Table Fields create user, Username, Password and Profile type.
         Entry(self.windowframe, textvariable=self.typepassword, font="roboto 14", bg="#FFFFFF", width=25).place(x=162, y=180, height=40)
         profiles=typebox(self.windowframe, font="robot 14", width=23, textvariable=self.accedit)
         profiles.place(x=162,y=245,height=40)
         profiles.set_completion_list(['MANAGER','MECHANIC'])
         Button(self.windowframe, text="Add an Employee", font="robot 12 bold", bg="#FFFFFF", bd=5, width=15, height=2,
                command=self.newuser).place(x=0, y=381)
         Button(self.windowframe, text="Change", font="robot 12 bold", bg="#FFFFFF", bd=5, width=10, height=2,
                command=self.modifyusertable).place(x=210, y=381)
         Button(self.windowframe, text="Delete", font="robot 12 bold", bg="#FFFFFF", bd=5, width=10, height=2,
                command=self.wipuser).place(x=370, y=381)

         self.lookupmain(0)

    #14
    def findusers(self,x=0):#Fetching records from users table.
         ans=''
         self.cur.execute("select * from users")
         userslist = self.cur.fetchall()
         for i in userslist:
              self.tree.insert('', 'end', values=(i))
              if (str(x) == i[0]):
                  a = self.tree.get_children()
                  ans = a[len(a) - 1]

         return ans
    #15
    def modifyusertable(self):#Method to modify existing users.
        cur = self.tree.selection()
        cur = self.tree.item(cur)
        li = cur['values']
        self.typeusername.set((self.typeusername.get()).upper())
        self.typepassword.set((self.typepassword.get()).upper())
        self.accedit.set((self.accedit.get()).upper())
        if (len(li) == 3):
            if self.typeusername.get() == '' or self.accedit.get() == '':
                messagebox.showerror("Error", "Please Fill All Fields")
                return
            if(self.accedit.get()!='MANAGER' and self.accedit.get()!='MECHANIC' ):
                messagebox.showerror("Error", "Unknown account type!")
                return
            self.cur.execute(
            "update users set password = ?,account_type = ? where username = ?;", (
            self.typepassword.get(), self.accedit.get(),self.typeusername.get()))
            self.base.commit()
            self.tree.delete(*self.tree.get_children())
            cur = self.findusers(li[0])
            self.tree.selection_set(cur)
    #16
    def wipuser(self):#Deleting a user.
        cur = self.tree.focus()
        cur = self.tree.item(cur)
        li = cur['values']
        fa=0
        if(self.username.get()==li[0]):
            if(messagebox.askyesno("Cool Bikes, ERP System","Remove Current User?")==True):
                fa=1
            else:
                return
        if messagebox.askyesno('Cool Bikes, ERP System', 'Do you want to remove this user?') == True and len(li) == 3:
            self.cur.execute("delete from users where username = ?;", (li[0],))
            self.base.commit()
            self.tree.delete(*self.tree.get_children())
            self.findusers()
            self.typeusername.set('')
            self.typepassword.set('')
            self.accedit.set('')
        if(fa==1):
            self.swap_user()
    #17
    def newuser(self):#Creating new users,here we call method 8 reguser from Loginscreen.py line 119.
        self.reguser()
        self.loginn.state('normal')  # LOGIN WINDOW ENTERS
    #18
    def lookupuser(self):#Fetching users and sending them into a list to be used in next method.
        if(self.lookupvar.get()==''):
            return
        self.tree.delete(*self.tree.get_children())
        self.cur.execute("select * from users")
        li=self.cur.fetchall()
        for i in li:
            if(i[0]==self.lookupvar.get()):
                self.tree.insert('', 'end', values=(i))
    #19
    def lookupusertable(self):#Search user by typing its name
        self.lookupvar.set('')
        self.tree.delete(*self.tree.get_children())
        self.findusers()
    #20
    def onclickusertable(self,event):#Onclick event for user table.
        cur = self.tree.selection()
        cur = self.tree.item(cur)
        li = cur['values']
        if (len(li) == 3):
            self.typeusername.set((li[0]))
            self.typepassword.set((li[1]))
            self.accedit.set((li[2]))
    #21
    def createsalestable(self):#Building sales table
        self.lookupframe.place_forget()
        self.windowform.place_forget()
        self.tablewindow.place_forget()
        self.productwindow.place_forget()
        self.windowframe.place_forget()
        self.commontable.place(x=1427, y=250, anchor=NE)#Position Invoice table
        self.tree.delete(*self.tree.get_children())
        self.tree.grid_remove()
        self.tree.destroy()
        slidebarx = Scrollbar(self.commontable, orient=HORIZONTAL)
        slidebary = Scrollbar(self.commontable, orient=VERTICAL)
        self.tree = ttk.Treeview(self.commontable, columns=("Transaction ID","Invoice No.", "Bike ID", "Specs",
                                                            'Quantity', 'Total Price €', 'Date', 'Time','Customer'), selectmode="browse", height=16,
                                 yscrollcommand=slidebary.set, xscrollcommand=slidebarx.set)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=100)
        self.tree.column('#2', stretch=NO, minwidth=0, width=100)
        self.tree.column('#3', stretch=NO, minwidth=0, width=100)
        self.tree.column('#4', stretch=NO, minwidth=0, width=400)
        self.tree.column('#5', stretch=NO, minwidth=0, width=100)
        self.tree.column('#6', stretch=NO, minwidth=0, width=100)
        self.tree.column('#7', stretch=NO, minwidth=0, width=100)
        self.tree.column('#8', stretch=NO, minwidth=0, width=100)
        self.tree.column('#8', stretch=NO, minwidth=0, width=100)
        self.tree.column('#9', stretch=NO, minwidth=0, width=200)
        self.tree.heading('Transaction ID', text="Transaction ID", anchor=W)
        self.tree.heading('Invoice No.', text="Invoice No.", anchor=W)
        self.tree.heading('Bike ID', text="Bike ID", anchor=W)
        self.tree.heading('Specs', text="Specs", anchor=W)
        self.tree.heading('Quantity', text="Quantity", anchor=W)
        self.tree.heading('Total Price €', text="Total Price €", anchor=W)
        self.tree.heading('Date', text="Date", anchor=W)
        self.tree.heading('Time', text="Time", anchor=W)
        self.tree.heading('Customer', text="Customer", anchor=W)
        self.tree.grid(row=1, column=0, sticky="W")
        slidebary.config(command=self.tree.yview)
        slidebarx.grid(row=2, column=0, sticky="we")
        slidebarx.config(command=self.tree.xview)
        slidebary.grid(row=1, column=1, sticky="ns", pady=30)
        self.listsales()
        self.lookupmain(2)
        self.totalsales=Label(self.commontable,text="Total Sales",font="roboto 14 bold").place(x=0,y=400)
    #22
    def listsales(self):#Select all invoices and create a list.
        self.cur.execute("select * from sales")
        salesarchive = self.cur.fetchall()
        for i in range(0,len(salesarchive)):
            salesarchive[i] = list(salesarchive[i])
            self.cur.execute("select bike_specs,bike_price from bikes where bike_id=?",(int(salesarchive[i][2]),))
            l=self.cur.fetchall()
            s=(str(salesarchive[i][4])).split('-')
            salesarchive[i][4]=s[2]+" - "+s[1]+" - "+s[0]
            salesarchive[i]=[salesarchive[i][0],salesarchive[i][1],salesarchive[i][2],l[0][0],salesarchive[i][3],l[0][1]*(int(salesarchive[i][3])),salesarchive[i][4],salesarchive[i][5],salesarchive[i][6]]
            salesarchive[i]=tuple(salesarchive[i])
        for i in salesarchive:
            self.tree.insert('', 'end', values=(i))

    #23
    def findinvoice(self):#Search invoice by typing its number.
        if (self.lookupvar.get() == ''):
            return
        self.tree.delete(*self.tree.get_children())
        self.cur.execute("select * from sales")
        salesarchive = self.cur.fetchall()
        for i in range(0, len(salesarchive)):
                salesarchive[i] = list(salesarchive[i])
                self.cur.execute("select bike_specs,bike_price from bikes where bike_id=?", (int(salesarchive[i][2]),))
                l = self.cur.fetchall()
                s = (str(salesarchive[i][4])).split('-')
                salesarchive[i][4]=s[2]+" - "+s[1]+" - "+s[0]
                salesarchive[i] = [salesarchive[i][0], salesarchive[i][1], salesarchive[i][2], l[0][0], salesarchive[i][3], l[0][1] * (int(salesarchive[i][3])),
                            salesarchive[i][4], salesarchive[i][5],salesarchive[i][6]]
                salesarchive[i] = tuple(salesarchive[i])
        for j in salesarchive:
            if (str(j[1]) == str(self.lookupvar.get())):
                self.tree.insert('', 'end', values=(j))
   
