#from tkinter import *
from Tkinter import *
import tkMessageBox as tm
#import pymysql.cursors
import MySQLdb
import ctypes
import sys
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class UpdateIDs(Frame):
    
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



        self.bframe = Frame(root, width=100, height=200, relief=GROOVE, borderwidth=2 )
        self.bframe.pack(padx=5, pady=5)

        self.updatelbl = Label(self.bframe, text="Update Here", width="20")
        self.updatelbl.grid(row=0, column=0, pady=5 )

        self.updatebutton = Button(self.bframe, text="UPDATE", fg="black", command = self.update_verify)
        self.updatebutton.grid(row=1, column=3, pady=5)



    def update_verify(self):
        #print("Clicked")
        
        #connection = pymysql.connect(host='192.168.1.100',
                                    #user='root',
                                    #passwd='root',
                                    #db='nims_store',
                                    #charset='utf8mb4',
                                    #cursorclass=pymysql.cursors.DictCursor)
        connection = MySQLdb.connect(host="localhost", user="root", passwd = "root", db="nims_store")
        cursor = connection.cursor ()

        mysql=  """
                UPDATE nims_attendance SET emp_id=2014 WHERE emp_id=2012 and t_id=54;
                UPDATE nims_attendance SET emp_id=2013 WHERE emp_id=2011 and t_id=54;
                UPDATE nims_attendance SET emp_id=2012 WHERE emp_id=2010 and t_id=54;
                UPDATE nims_attendance SET emp_id=2011 WHERE emp_id=2009 and t_id=54;
                UPDATE nims_attendance SET emp_id=2010 WHERE emp_id=2008 and t_id=54;
                UPDATE nims_attendance SET emp_id=2009 WHERE emp_id=2007 and t_id=54;
                UPDATE nims_attendance SET emp_id=2008 WHERE emp_id=2006 and t_id=54;
                UPDATE nims_attendance SET emp_id=2007 WHERE emp_id=2005 and t_id=54;
                UPDATE nims_attendance SET emp_id=2006 WHERE emp_id=2004 and t_id=54;
                UPDATE nims_attendance SET emp_id=2005 WHERE emp_id=2003 and t_id=54;
                UPDATE nims_attendance SET emp_id=2004 WHERE emp_id=2002 and t_id=54;
                UPDATE nims_attendance SET emp_id=2003 WHERE emp_id=2001 and t_id=54
                """

        cursor.execute(mysql)
        connection.commit()
        connection.close()         
        tm.showerror("Data Updated", "Data Updated Please Exit")
        



root = Tk()
root.title("Shah iSolutions")
root.iconbitmap('logo.ico')
root.geometry("360x360")
update = UpdateIDs(root)
  #call the method
update.create_widgets()

root.mainloop()
