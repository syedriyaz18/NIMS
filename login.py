from Tkinter import *
import ctypes
import sys
import MySQLdb
import tkMessageBox as tm
#import mainform



myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class Login(Frame):
    

    def _init_(self, master):
          self.master = master

    def create_widgets(self):
        self.topframe = Frame(root, width=100, height=100, relief=GROOVE, borderwidth=2 )
        self.topframe.pack(padx=5, pady=20)

        self.welcomelbl = Label(self.topframe, text="Welcome To", width="20")
        self.welcomelbl.grid(row=0, column=0, pady=5 )

        self.cnamelbl = Label(self.topframe, text="Shah iSolutions", width="20", fg="RED", font="10")
        self.cnamelbl.grid(row=1, column=0, pady=5 )

        self.ahimslbl = Label(self.topframe, text="AHIMS", width="20")
        self.ahimslbl.grid(row=2, column=0, pady=5 )

        self.bottomframe = Frame(root, width=100, height=100, relief=GROOVE, borderwidth=2)
        self.bottomframe.pack(padx=5, pady=60)
       

        self.useridlbl = Label(self.bottomframe, text="User ID", width="20")
        self.useridlbl.grid(row=0, column=0, pady=5 )
            
        self.useridtxt = Entry (self.bottomframe, width="20")
        self.useridtxt.grid(row=0, column=1, pady=5) 

        self.pwdlbl = Label(self.bottomframe, text="Password", width="20")
        self.pwdlbl.grid(row=1, column=0, pady=5)

            
        self.pwdtxt = Entry (self.bottomframe, width="20", show="*")
        self.pwdtxt.grid(row=1, column=1, pady=5)
        
        self.blackbutton = Button(self.bottomframe, text="Login", fg="black", command = self.login_verify)
        self.blackbutton.grid(row=2, column=3, pady=5)


    def login_verify(self):
        username = self.useridtxt.get()
        password = self.pwdtxt.get()
        print username
        print password
        connection = MySQLdb.connect(host="192.168.1.99", user="root", passwd = "ShahiSolutionsL0ck3d", db="ahims")
        cursor = connection.cursor ()
        cursor.execute("select * from login where userid= %s", (username))
        row = cursor.fetchone()

        
            
        if row is not None:
            usrname = row[0]
            pwd = row[1]
            print usrname
            print username
                    
            if username == usrname and password == pwd:
                tm.showinfo("Welcome %s", (username))
                Main.show()
                '''self.top = Toplevel()
                self.top.title("title")
                self.top.geometry("300x150+30+30")
                self.top.transient(self)
                self.wButton.config(state='disabled')

                self.topButton = Button(self.top, text="CLOSE", command = self.OnChildClose)
                self.topButton.pack()'''

                                          
            elif pwd <> password:
                tm.showinfo("Wrong Password %s", (password))
        else:
            tm.showinfo("Wrong UserName %s",(username))


        cursor.close ()
        connection.close()

        
       


root = Tk()
root.title("Shah iSolutions")
root.iconbitmap('images/logo.ico')
root.geometry("360x360")
app = Login(root)
  #call the method
app.create_widgets()

root.mainloop()
