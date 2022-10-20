#Cool Bikes ERP System
#Student: Jose Maria Rico Leal
#Student Number: 10539218
#Module: B8IT131 Project

import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


# POP-UP LOGIN WINDOW
class Screen:
    #1
    def __init__(self):#Welcome pop-up window, we must enter our credentials to log in.
        self.loginn=Tk()
        self.loginn.title("Cool Bikes, ERP System")
        width = 500
        height = 600
        screen_width = self.loginn.winfo_screenwidth()
        screen_height = self.loginn.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.loginn.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.loginn.resizable(0, 0)
        self.loginn.protocol('WM_DELETE_WINDOW', self.__login_del__)
        self.loginn.config(bg="#4bf5f1")
        self.logintable()
        self.username = StringVar(value="Username")
        self.password = StringVar(value="Password")
        self.obj()
    #2
    def __login_del__(self):#Exit method to leave this screen and exit the app.
        if messagebox.askyesno("Cool Bikes, ERP System", "Exit ERP System?") == True:
            self.loginn.destroy()
            exit(0)                  

    #3
    def logintable(self):#Database connection and users table creation
        self.base = sqlite3.connect("cool_bikes_db.db")
        self.cur = self.base.cursor()
        self.cur.execute("CREATE TABLE if not exists users ( username varchar (20),password	 varchar (20) NOT NULL,account_type varchar ( 10 ) NOT NULL,PRIMARY KEY(username));")

    #4
    def obj(self):#Creating widgets and format.
        self.loginframe=LabelFrame(self.loginn,bg="#4bf5f1",height=603,width=503)
        self.loginn.bind('<Return>',self.checkuser)
        self.loginframe.place(x=0,y=0)
        self.toplabel = Label(self.loginframe, fg="black", bg="#4bf5f1", anchor="center", text="Login", font="Roboto 40 bold")
        self.toplabel.place(x=150,y=25)
        self.us = ttk.Entry(self.loginframe, width=20, textvariable=self.username,font="Roboto 14 ")
        self.us.place(x=120,y=145,height=40)
        self.pa = ttk.Entry(self.loginframe, width=20, textvariable=self.password,font="Roboto 14 ")
        self.pa.place(x=120,y=185,height=40)
        self.us.bind('<Button-1>', self.onclick)
        self.pa.bind('<Button-1>', self.onclick1)
        self.signin = Button(self.loginframe,width=20, text="Sign in",bg="#ffffff",fg="black",command=self.checkuser,font="Roboto 14")
        self.signin.place(x=120,y=250)
        ab = PhotoImage(file="images/bike.png")
        self.signon = Button(self.loginframe,width=465,height=240,bg="#ffffff",image=ab,font="Roboto 14",compound=TOP)
        self.signon.place(x=10,y=340)
        self.signon.image=ab
        
    

    #5
    def checkuser(self,event=0):#Method that checks if the user exists.
        s = self.username.get()
        s1 = self.password.get()
        s = s.upper()
        s1 = s1.upper()
        self.cur.execute("select * from users where username=? and password=? ",(s,s1))
        l = self.cur.fetchall()
        if(len(l)>0):
            self.success()
        else:
            self.fail()

    #6
    def success(self):#Throws a message when login is successful.
        messagebox.showinfo("Welcome to","Cool Bikes, ERP System")
        self.loginn.quit()

    #7
    def fail(self):##Throws a message when login fails.
        messagebox.showerror("Error","The username or password is incorrect")

    #8
    def reguser(self):#Registering users, this pop-up box kicks in when method  newuser is called in Manager_menu.py line 496.
        self.toplabel.config(text="New User")#We only create users in that level.
        self.toplabel.place(x=125,y=25)
        self.username.set("Username")
        self.password.set("Password")
        self.signin.config(text="Ok",command=self.insert)
        self.register = Button(self.loginframe,width=20, text = "Back",bg="#4bf5f1",fg="black",command = self.revert,font="Roboto 14")
        self.signin.place(x=35, y=260)
        self.signin.config()
        self.signin.place(x=115, y=260) #Ok button place
        self.pa.config(show='')
        self.loginn.focus()
        self.loginn.bind('<Return>',self.insert)
        self.loginn.title('Cool Bikes, ERP System')

    #9
    def insert(self,event=0):#Inserting user into the database.
        s = self.username.get()
        s1 = self.password.get()
        s = s.upper()
        s1 = s1.upper()
        self.cur.execute("select username from users where username = ?",(s,))
        l = self.cur.fetchall()
        if(len(l)>0 ):
            messagebox.showerror("Error", "Username already exist")
            self.username.set('Choose your username')
            self.loginn.focus()
            return
        if(len(s) == 0 or len(s1) == 0 or len(s)>20 or len(s1)>20 or s1 == "CREATE A PASSWORD" or s =='CHOOSE YOUR USERNAME'):
            messagebox.showerror("Error", "Invalid username or password")
            self.username.set('Choose your username')
            self.password.set('Create a password')
            self.pa.config(show='')
            self.loginn.focus()
            return
        else:
            self.cur.execute("insert into users values(?,?,?)",(s,s1,'MECHANIC'))
            messagebox.showinfo("Success", "User registered")
            self.base.commit()
            self.revert()
            # ADD
            self.loginn.state('withdraw')
            self.tree.delete(*self.tree.get_children())
            self.findusers()

    #10
    def revert(self):#Formatting some other widgets.
        self.toplabel.config(text="Login")
        self.toplabel.place(x=75,y=25)
        self.signin.config(text="Sign in", command=self.checkuser)
        self.register.config(text="Register", command=self.reguser)
        self.username.set('Username')
        self.password.set('Password')
        self.pa.config(show='')
        self.signin.config(state=NORMAL)
        self.loginn.focus()
        self.loginn.bind('<Return>',self.checkuser)
        self.signin.place(x=35, y=290) #Sign in button place
        self.loginn.title('Login')
        self.loginn.state('withdraw')

    #11
    def onclick(self,event):#Field to type in the user name
        if (self.username.get() == "Username" or self.username.get() == "Choose your username"):
            self.us.delete(0, "end")
    #12
    def onclick1(self,event):#Field to type in the password
        if (self.password.get() == "Password" or self.password.get() == "Create a password"):
            self.pa.delete(0, "end")
            self.pa.config(show = "*")




