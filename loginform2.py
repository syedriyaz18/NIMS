#from tkinter import *
from Tkinter import *
import tkMessageBox as tm
#import pymysql.cursors
import MySQLdb
import ctypes
import sys
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class LoginFrame(Frame):
    

        
    def __init__(self, master):
        super().__init__(master)

       

        self.label_1 = Label(self, text="Username")
        self.label_2 = Label(self, text="Password")

        self.entry_1 = Entry(self)
        self.entry_2 = Entry(self, show="*")

        self.label_1.grid(row=0, sticky=E)
        self.label_2.grid(row=1, sticky=E)
        self.entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)

        #self.checkbox = Checkbutton(self, text="Keep me logged in")
        #self.checkbox.grid(columnspan=2)
        
        self.logbtn = Button(self, text="Login", command = self._login_btn_clickked)
        self.logbtn.grid(columnspan=2)

        self.pack()

    def _login_btn_clickked(self):
        #print("Clicked")
        
        #connection = pymysql.connect(host='192.168.1.99',
         #                    user='root',
          #                   passwd='ShahiSolutionsL0ck3d',
           #                  db='ahims',
            #                 charset='utf8mb4',
             #                cursorclass=pymysql.cursors.DictCursor)
        connection = MySQLdb.connect(host="192.168.1.99", user="root", passwd = "ShahiSolutionsL0ck3d", db="ahims")
        #cursor = conn.cursor()
        try:
            with connection.cursor() as cursor:
                username = self.entry_1.get()
                password = self.entry_2.get()
                cursor.execute("select * from login where userid= %s", (username))
                row = cursor.fetchone()
                if row is not None:
                    usrname = row[0]
                    pwd = row[1]
                    print (usrname, username)
                    
                    if username == usrname and password == pwd:
                        tm.showinfo("Login info", "Welcome %s", (username))
                else:
                    tm.showerror("Login error", "Incorrect username")
        finally:
            connection.close()



root = Tk()
frame = Frame(root, width=270, height=270, borderwidth=1)
root.title('Shah iSolutions')
root.iconbitmap('images/logo.ico')

frame.pack()
lf = LoginFrame(root)
root.mainloop()
