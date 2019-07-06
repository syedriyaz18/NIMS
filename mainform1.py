from Tkinter import *
import ctypes
import sys
import MySQLdb
import pyodbc
import tkMessageBox as tm


myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class Main(Frame):

    def _init_(self, master):
          self.master = master

    def create_main_widgets(self):
        self.topframe = Frame(root, width=100, height=100, relief=GROOVE, borderwidth=2 )
        self.topframe.pack(padx=5, pady=5)

        self.welcomelbl = Label(self.topframe, text="Welcome To", width="20")
        self.welcomelbl.grid(row=0, column=0, pady=5 )


class Login(Frame):
    
    def _init_(self, master):
          self.master = master


    def create_widgets(self):
        self.topframe = Frame(root, width=100, height=100, relief=GROOVE, borderwidth=2 )
        self.topframe.pack(padx=5, pady=5)

        self.welcomelbl = Label(self.topframe, text="Welcome To", width="20")
        self.welcomelbl.grid(row=0, column=0, pady=5 )

        self.cnamelbl = Label(self.topframe, text="Shah iSolutions", width="20", fg="RED", font="10")
        self.cnamelbl.grid(row=1, column=0, pady=5 )

        self.ahimslbl = Label(self.topframe, text="AHIMS", width="20")
        self.ahimslbl.grid(row=2, column=0, pady=5 )

        self.bottomframe = Frame(root, width=100, height=400, relief=GROOVE, borderwidth=2)
        self.bottomframe.pack(padx=5, pady=20)
       

        self.ipnolbl = Label(self.bottomframe, text="IPNO", width="20")
        self.ipnolbl.grid(row=0, column=0, pady=5 )
            
        self.ipnotxt = Entry (self.bottomframe, width="20")
        self.ipnotxt.grid(row=0, column=1, pady=5)

        self.getbutton = Button(self.bottomframe, text="Verify", fg="black", command = self.login_verify)
        self.getbutton.grid(row=1, column=3, pady=5)

        self.isdischargelbl = Label(self.bottomframe, text="IsDischarge", width="20")
        self.isdischargelbl.grid(row=2, column=0, pady=5)

            
        self.isdischargetxt = Entry (self.bottomframe, width="20", show="*")
        self.isdischargetxt.grid(row=2, column=1, pady=5)


        self.isbilledlbl = Label(self.bottomframe, text="IsBilled", width="20")
        self.isbilledlbl.grid(row=3, column=0, pady=5)

            
        self.isbilledtxt = Entry (self.bottomframe, width="20", show="*")
        self.isbilledtxt.grid(row=3, column=1, pady=5)


        self.bframe = Frame(root, width=100, height=200, relief=GROOVE, borderwidth=2 )
        self.bframe.pack(padx=5, pady=5)

        self.updatelbl = Label(self.bframe, text="Update Here", width="20")
        self.updatelbl.grid(row=0, column=0, pady=5 )

        self.updatebutton = Button(self.bframe, text="UPDATE", fg="black", command = self.update_verify)
        self.updatebutton.grid(row=1, column=3, pady=5)


    def login_verify(self):
        ipno = self.ipnotxt.get()
       
        print ipno
        

        
        cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=nimraser;DATABASE=mhims;UID=sa;PWD=torrent_123')
        cursor = cnxn.cursor()

        cursor.execute("SELECT isdischarge, billedflag FROM tblipregistration where ipno = %s"%(ipno))
        for row in cursor.fetchall():
            print row[0]
            print row[1]
            self.isdischargetxt.set(row[0])
            self.isbilledtxt.value = row[1]

              
            
        cursor.close()
        cnxn.close()
      

    def update_verify(self):
        print ipno
        cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=nimraser;DATABASE=mhims;UID=sa;PWD=torrent_123')
        cursor = cnxn.cursor()

        cursor.execute("update tblipregistration set isDischarge='False' and billedflag='False' where ipno=%s"%(ipno))
        tm.showinfo("Data Updated")
        cnxn.close()

root = Tk()
root.title("Shah iSolutions")
root.iconbitmap('images/logo.ico')
root.geometry("450x450")
login = Login(root)
  #call the method
login.create_widgets()

root.mainloop()
