#Cool Bikes ERP System
#Student: Jose Maria Rico Leal
#Student Number: 10539218
#Module: B8IT131 Project

import sqlite3
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from Loginscreen import Screen
from Manager_menu import Manager
from Mechanic_menu import Mechanic

# MAIN WINDOW
class Main(Screen,Manager,Mechanic):
    #1
    def __init__(self):#Creates the main app frame, it is used in both menus manager & mechanic  
        Screen.__init__(self)
        self.loginn.mainloop()
        self.loginn.state('withdraw')#Login window closes
        self.mainn = Toplevel(bg="#FFFFFF")
        width = 1536
        height = 864
        screen_width = self.mainn.winfo_screenwidth()
        screen_height = self.mainn.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.mainn.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.mainn.title("Cool Bikes, ERP System")
        self.mainn.resizable(0,0)
        self.mainn.protocol('WM_DELETE_WINDOW', self.__Main_del__)
        self.getdetails()

   
    #2
    def __Main_del__(self):#Overrides Log Out button and desctructor for class Screen, this method is triggered when clicking Log Out button.
        if messagebox.askyesno("Cool Bikes, ERP System", " Do you want to Exit Cool Bikes Management System?") == True:
            self.loginn.quit()
            self.mainn.quit()
            exit(0)
        else:
            pass

    #3 
    def getdetails(self):#Table bikes and sales creation and. Fetching user details from bikes, users and invetory table.
        self.cur.execute("CREATE TABLE if not exists bikes(bike_id varchar (20),bike_type varchar (50) NOT NULL,bike_specs varchar (100) NOT NULL,bike_groupset varchar (50),bike_price INTEGER NOT NULL,stocks INTEGER NOT NULL,Customer varchar (20),PRIMARY KEY(bike_id));")
        self.cur.execute("CREATE TABLE if not exists sales (Trans_id	INTEGER,invoice	INTEGER NOT NULL,Bike_id	varchar (20),Quantity INTEGER NOT NULL,Date	varchar (20),Time varchar (20),Customer	varchar (20),PRIMARY KEY(Trans_id));")
        self.cur.execute("select * from bikes ")
        self.bikes = self.cur.fetchall()
        capusernamename = self.username.get()#User name will be shown in capital letters
        capusernamename = capusernamename.upper()
        self.cur.execute("select account_type from users where username= ? ", (capusernamename,))
        l = self.cur.fetchall()
        self.account_type = l[0][0]
        self.buildmain()

    #4  
    def buildmain(self):#Redirects users to its menu, and adding widgets to top of main window. 
        if self.account_type == 'MANAGER':
            super(Manager).__init__()
            self.manager_mainmenu(8,8)
        else:
            super(Mechanic).__init__()
            self.mechanic_mainmenu(8,8)
        self.signout.config(command=self.__Main_del__)
        self.swapuser.config(command=self.swap_user)
        self.logoplace=LabelFrame(self.mainn,width=1536,height=120,bg="#46fb81")
        self.logoplace.place(x=0,y=0)
        self.shopname = 'Cool Bikes'
        self.shoplogo=Label(self.logoplace,text=self.shopname + " Dublin, L.T.D.",bg="#46fb81",anchor="center")
        self.shoplogo.config(font="Roboto 30 bold",fg="black")
        self.shoplogo.place(x=460,y=30)
        ab = PhotoImage(file="images/userprofile.png")
        ab = ab.subsample(4,4)
        self.userprofile = ttk.Label(self.logoplace,text=(self.username.get()).capitalize(),image=ab, compound=TOP)
        self.userprofile.image = ab
        self.userprofile.place(x=30,y=15)
        

    #5 
    def swap_user(self):#Method for changing user.
        if messagebox.askyesno("Cool Bikes, ERP System", "Do  you want to change user?") == True:
            self.base.commit()
            self.mainn.destroy()
            self.loginn.destroy()
            self.__init__()


if __name__ == '__main__':
    w = Main()
    w.base.commit()
    w.mainn.mainloop()
