#Cool Bikes ERP System
#Student: Jose Maria Rico Leal
#Student Number: 10539218
#Module: B8IT131 Project

import sqlite3
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from Tkinter_classes import typebox,typeauto
import datetime
import os

# MECHANIC MENU
class Mechanic:
    #1
    def __init__(self,mainn):#Initialising the class objects attributes
         self.mainn=mainn
    #2
    def mechanic_mainmenu(self,a,b):#Setting up mechanic method, creating layout and widgets. Formatting images, frames and buttons.
        self.ppalframe = LabelFrame(self.mainn, width=800, height=140, bg="#46fb81")
        self.ppalframe.place(x=330, y=650)
        ab = PhotoImage(file="images/bikes.png")
        ab = ab.subsample(a, b)
        self.mechitems = Button(self.ppalframe, text="Bikes",bd=5,font="roboto 11 bold",bg="cyan", image=ab, compound=TOP,command=self.createbiketable)
        self.mechitems.image = ab
        self.mechitems.place(x=62, y=17)
        ab = PhotoImage(file="images/cart.png")
        ab = ab.subsample(a,b)
        self.mechitems = Button(self.ppalframe, text="Cart",bd=5,bg="cyan",font="roboto 11 bold", image=ab, compound=TOP,command=self.createinvoice)
        self.mechitems.image = ab
        self.mechitems.place(x=260, y=17)
        ab = PhotoImage(file="images/swapuser.png")
        ab = ab.subsample(a, b)
        self.swapuser = Button(self.ppalframe, text="Change User",bd=5,bg="cyan",font="roboto 11 bold", image=ab, compound=TOP)
        self.swapuser.image = ab
        self.swapuser.place(x=460, y=17)
        ab = PhotoImage(file="images/signout.png")
        ab = ab.subsample(a, b)
        self.signout = Button(self.ppalframe, text="Log out",bd=5,bg="cyan",font="roboto 11 bold", image=ab, compound=TOP)
        self.signout.image = ab
        self.signout.place(x=670, y=17)
        self.ppalwindow =Frame(self.mainn, width=150, height=400,bg="#FFFFFF")
        self.ppalwindow.place(x=1300, y=150, anchor=NE)#Invoice table position
        self.ppalwindowinfo=self.ppalwindow.place_info()
        self.genericwindow =Frame(self.mainn, width=350, height=700,bg="#FFFFFF")
        self.genericwindow.place(x=1110, y=50, anchor=NE)
        self.genericwindowinfo = self.genericwindow.place_info()
        self.firstwindow = Frame(self.mainn, width=800, height=250, bg="#FFFFFF")
        self.firstwindow.place(x=260, y=300+80)#look up by specs
        self.firstwindowinfo = self.firstwindow.place_info()
        self.firstwindow1 = Frame(self.mainn, width=500, height=250, bg="#FFFFFF")
        self.firstwindow1.place(x=750, y=310+60)
        self.firstwindow1info=self.firstwindow1.place_info()
        self.createbiketable()
    #3
    def createbiketable(self):#Creating inventory frame, first screen you see when log into this menu.
         self.firstwindow.place_forget()
         self.firstwindow1.place_forget()
         self.genericwindow.place(x=1300, y=185, anchor=NE)
         self.ppalwindow.place_forget()
         slidebarx = Scrollbar(self.genericwindow, orient=HORIZONTAL)
         slidebary = Scrollbar(self.genericwindow, orient=VERTICAL)
         self.tree = ttk.Treeview(self.genericwindow, columns=("Bike ID", "Type", "Specs", "Groupset",
                                                            'Price €', 'Stock','Customer'), selectmode="extended", height=18,
                                  yscrollcommand=slidebary.set, xscrollcommand=slidebarx.set)
         self.tree.column('#0', stretch=NO, minwidth=0, width=0)
         self.tree.column('#1', stretch=NO, minwidth=0, width=80)
         self.tree.column('#2', stretch=NO, minwidth=0, width=150)
         self.tree.column('#3', stretch=NO, minwidth=0, width=350)
         self.tree.column('#4', stretch=NO, minwidth=0, width=200)
         self.tree.column('#5', stretch=NO, minwidth=0, width=90)
         self.tree.column('#6', stretch=NO, minwidth=0, width=90)
         self.tree.column('#7', stretch=NO, minwidth=0, width=140)
         self.tree.heading('Bike ID', text="Bike ID", anchor=W)
         self.tree.heading('Type', text="Type", anchor=W)
         self.tree.heading('Specs', text="Specs", anchor=W)
         self.tree.heading('Groupset', text="Groupset", anchor=W)
         self.tree.heading('Price €', text="Price €", anchor=W)
         self.tree.heading('Stock', text="Stock", anchor=W)
         self.tree.heading('Customer', text="Customer", anchor=W)
         self.tree.grid(row=1, column=0, sticky="W")
         slidebary.config(command=self.tree.yview)
         slidebarx.grid(row=2, column=0, sticky="we")
         slidebarx.config(command=self.tree.xview)
         slidebary.grid(row=1, column=1, sticky="ns", pady=30)
         self.getbikes()
    #4
    def getbikes(self):#Creating a list including all rows from bikes table.
         self.cur.execute("select * from bikes")
         bikelist = self.cur.fetchall()
         for i in bikelist:
              self.tree.insert('', 'end', values=(i))
    #5
    def createinvoice(self):#Setting up invoice table.
        self.genericwindow.place_forget()
        self.firstwindow.place(self.firstwindowinfo)
        self.firstwindow1.place(self.firstwindow1info)
        self.ppalwindow.place(self.ppalwindowinfo)
        slidebarx = Scrollbar(self.ppalwindow, orient=HORIZONTAL)
        slidebary = Scrollbar(self.ppalwindow, orient=VERTICAL)
        self.tree = ttk.Treeview(self.ppalwindow, columns=("Transaction ID", "Bike ID", "Specs",'Customer',
        'Quantity', 'Price €','Date','Time'), selectmode="browse", height=6,yscrollcommand=slidebary.set, xscrollcommand=slidebarx.set)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=100)
        self.tree.column('#2', stretch=NO, minwidth=0, width=100)
        self.tree.column('#3', stretch=NO, minwidth=0, width=300)
        self.tree.column('#4', stretch=NO, minwidth=0, width=100)
        self.tree.column('#5', stretch=NO, minwidth=0, width=130)
        self.tree.column('#6', stretch=NO, minwidth=0, width=130)
        self.tree.column('#7', stretch=NO, minwidth=0, width=130)
        self.tree.column('#8', stretch=NO, minwidth=0, width=130)
        self.tree.heading('Transaction ID', text="Transaction ID", anchor=W)
        self.tree.heading('Bike ID', text="Bike ID", anchor=W)
        self.tree.heading('Specs', text="Specs", anchor=W)
        self.tree.heading('Customer', text="Customer", anchor=W)
        self.tree.heading('Quantity', text="Quantity", anchor=W)
        self.tree.heading('Price €', text="Price €", anchor=W)
        self.tree.heading('Date', text="Date", anchor=W)
        self.tree.heading('Time', text="Time", anchor=W)
        
        self.tree.grid(row=1, column=0, sticky="W")
        slidebary.config(command=self.tree.yview)
        slidebarx.grid(row=2, column=0, sticky="we")
        slidebarx.config(command=self.tree.xview)
        slidebary.grid(row=1, column=1, sticky="ns", pady=30)
        self.tree.bind("<<TreeviewSelect>>", self.onclickinvoice)
        self.invoiceuserselection()
    #6
    def invoiceuserselection(self):#Adding buttons and widgets to create an invoice.
       self.cur.execute('select max(trans_id) from sales')
       li = self.cur.fetchall()
       if(li[0][0]!=None):
        self.transid = li[0][0] + 1
       else:
           self.transid = 100
       self.qty = StringVar(value=1)
       self.additem=StringVar()
       self.total=IntVar(value=0)
       Button(self.firstwindow,text="Check out",command=self.archiveinvoice,bd=10,width=8,height=3,bg="#FFFFFF",font="roboto 10").place(x=0,y=80)
       Button(self.firstwindow, text="Add", command=self.warningsinvoice, bd=10, width=10, height=3,bg="#FFFFFF",font="roboto 10").place(x=230,y=80)
       Button(self.firstwindow, text="Delete", command=self.deleteinvoice, bd=10, width=10, height=3, bg="#FFFFFF",font="roboto 10").place(x=100, y=80)
       shoppinglist=typebox(self.firstwindow,width=20,textvariable=self.additem,font="roboto 12")
       shoppinglist.place(x=10,y=30,height=40)
       shopqty = Entry(self.firstwindow,textvariable=self.qty,width=9,bg="#ffffff",font="roboto 12")
       shopqty.place(x=220,y=30,height=30)
       shoptotal = Entry(self.firstwindow, textvariable=self.total, width=20, state='readonly', bg="#ffffff", font="roboto 12")
       shoptotal.place(x=130, y=180, height=40)
       Label(self.firstwindow, text="Quantity", font="roboto 12 bold", bg="#ffffff").place(x=218,y=0)
       Label(self.firstwindow, text="Look up by specs", font="roboto 12 bold", bg="#ffffff").place(x=30, y=0)
       Label(self.firstwindow, text="Total", font="roboto 14 bold", bg="#ffffff").place(x=0, y=180)
       self.cur.execute("select max(invoice) from sales")
       self.invoice = self.cur.fetchall()
       self.invoice = self.invoice[0][0] + 1
       Label(self.ppalwindow, text="Invoice No. "+str(self.invoice), font="roboto 14 bold", bg="#ffffff").grid(row=0, column=0)
       self.cur.execute("select bike_specs,bike_price from bikes")
       li=self.cur.fetchall()
       self.stocks = []
       self.desc_price=dict()
       for i in range(0, len(li)):
           if (self.stocks.count(li[i][0]) == 0):
               self.stocks.append(li[i][0])
           self.desc_price[li[i][0]]=li[i][1]
       shoppinglist.set_completion_list(self.stocks)
       li=['Bike Id','Specs','Price','Stock']
       no=5
       for i in range(0,4):
           Label(self.firstwindow1, text=li[i], font="roboto 14 bold", bg="#FFFFFF").place(x=0, y=no)
           no += 65
       self.shopid = StringVar()
       self.shopbike = StringVar()
       self.shopbikeprice = StringVar()
       self.shopbikestock = StringVar()
       Entry(self.firstwindow1, textvariable=self.shopid, font="roboto 14", bg="#FFFFFF", width=25, state='readonly').place(x=162, y=0,height = 40)
       Entry(self.firstwindow1, textvariable=self.shopbike, font="roboto 14", bg="#FFFFFF", width=25, state='readonly').place(x=162, y=65,height=40)
       Entry(self.firstwindow1, textvariable=self.shopbikeprice, font="roboto 14", bg="#FFFFFF", width=25, state='readonly').place(x=162,y=65*2,height=40)
       Entry(self.firstwindow1, textvariable=self.shopbikestock, font="roboto 14", bg="#FFFFFF", width=25, state='readonly').place(x=162,y=65*3,height=40)
       self.id_qty=dict()
       self.cur.execute("select bike_id from bikes")
       l=self.cur.fetchall()
       for i in range(0,len(l)):
           self.id_qty[l[i][0]]=0
    #7
    def warningsinvoice(self):#Getting invoice warnings when fields are not correctly filled up.
        if(len(self.additem.get()) == 0 or self.stocks.count(self.additem.get())==0):
            messagebox.showerror("Cool Bikes, ERP System", "Bike Not Found!")
            return
        else:
            if(not self.qty.get().isdigit()):
                messagebox.showerror('Cool Bikes, ERP System','Invalid quantity!')
                return
            if(int(self.qty.get()) <= 0):
                messagebox.showerror('Cool Bikes, ERP System', 'Invalid quantity!')
                return
            self.cur.execute("select  bike_id,bike_specs,Customer from bikes where bike_specs = ? ",(self.additem.get(),))
            row = self.cur.fetchall()
            row = [list(row[0])]
            row[0].insert(0,self.transid)
            self.transid+=1
            row[0].append(int(self.qty.get()))
            row[0].append((int(self.qty.get())*self.desc_price[self.additem.get()]))
            x=str(datetime.datetime.now().strftime("%d-%m-%y"))
            row[0].append(x)
            x=datetime.datetime.now()
            x=str(x.hour)+' : '+str(x.minute)+' : '+str(x.second)
            row[0].append(x)
            row = [tuple(row[0])]
            self.shopid.set(row[0][1])
            self.shopbikeprice.set(self.desc_price[self.additem.get()])
            self.shopbike.set(row[0][2])
            self.cur.execute("select stocks from bikes where bike_id=?", (row[0][1],))
            li = self.cur.fetchall()
            
            
            if((li[0][0]-self.id_qty[row[0][1]])-int(self.qty.get())<0):
                if(li[0][0]!=0):
                    messagebox.showerror('Cool Bikes, ERP System','Product with this quantity not available!')
                else:
                    messagebox.showerror('Cool Bikes, ERP System', 'Product out of stock!')
                return
            self.id_qty[row[0][1]] += int(self.qty.get())
            self.shopbikestock.set(li[0][0]-self.id_qty[row[0][1]])
            for data in row:
                self.tree.insert('', 'end', values=(data))
            self.total.set(self.total.get() + (int(self.qty.get()) * self.desc_price[self.additem.get()]))
            self.qty.set('1')
            self.additem.set('')
    #8
    def archiveinvoice(self):#Archiving invoice, this addition will be reflected in Manager menu.
        x=self.tree.get_children()
        if(len(x) == 0):
            messagebox.showerror('Cool Bikes, ERP System','Empty cart!')
            return
        if (messagebox.askyesno('Cool Bikes, ERP System','Do you want to proceed?') == False):
            return
        a=[]
        self.cur.execute("select max(invoice) from sales")
        self.invoice=self.cur.fetchall()
        self.invoice=self.invoice[0][0]+1
        for i in x:
            l=self.tree.item(i)
            a.append(l['values'])
        for i in a:
            s = (str(i[6])).split('-')
            i[6] = s[2] + "-" + s[1] + "-" + s[0]
            self.cur.execute("insert into sales values (?,?,?,?,?,?,?)",(int(i[0]),int(self.invoice),int(i[1]),int(i[4]),i[6],i[7],i[3]))
            self.cur.execute("select stocks from bikes where bike_id=?",(int(i[1]),))
            l=self.cur.fetchall()
            self.cur.execute("update bikes set stocks=? where bike_id=?",(l[0][0]-self.id_qty[str(i[1])],int(i[1])))
            self.base.commit()
        messagebox.showinfo('Cool Bikes, ERP System','Transaction Successful!')
     
        self.tree.delete(*self.tree.get_children())
        self.shopbikestock.set('')
        self.shopbike.set('')
        self.shopid.set('')
        self.shopbikeprice.set('')
        self.total.set(0)
        self.additem.set('')
        self.qty.set('1')
        self.cur.execute("select bike_id from bikes")
        l = self.cur.fetchall()
        for i in range(0, len(l)):
            self.id_qty[l[i][0]] = 0
        self.createinvoice()
    #9
    def deleteinvoice(self):#Delete current invoice selection.
        re = self.tree.selection()
        if(len(re)==0):
            messagebox.showerror('Cool Bikes, ERP System','No cart selected')
            return
        if (messagebox.askyesno('Cool Bikes, ERP System!','Remove cart?') == True):
            x = self.tree.get_children()
            re=re[0]
            l=[]
            fi=[]
            for i in x:
                if(i!=re):
                    l.append(tuple((self.tree.item(i))['values']))
                else:
                    fi=((self.tree.item(i))['values'])
            self.tree.delete(*self.tree.get_children())
            for i in l:
                self.tree.insert('', 'end', values=(i))
            self.shopbikestock.set('')
            self.shopbike.set('')
            self.shopid.set('')
            self.shopbikeprice.set('')
            self.additem.set('')
            self.qty.set('1')
            self.id_qty[str(fi[1])]-=fi[3]
            self.total.set(self.total.get()-fi[4])
            return
    
   
    #10 
    def onclickinvoice(self,event):#Onclick event for invoice table
        cur = self.tree.selection()
        cur = self.tree.item(cur)
        li = cur['values']
        if (len(li) == 8):
            self.shopid.set((li[1]))
            self.shopbike.set((li[2]))
            self.cur.execute("select bike_price,stocks from bikes where bike_id=?",(li[1],))
            li = self.cur.fetchall()
            self.shopbikeprice.set(li[0][0])
            self.shopbikestock.set(li[0][1]-self.id_qty[self.shopid.get()])
