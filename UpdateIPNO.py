from Tkinter import *
import ctypes
import sys
import pyodbc
import tkMessageBox as tm



def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Something is Better than Nothing")
   button.pack()

   

# Create a new database:
connection_str1 =    """
                    Driver={SQL Server Native Client 11.0};
                    Server=nimraser;
                    Database=MHIMS;
                    Trusted_Connection=yes;
                    """

connection_str = ('DRIVER={SQL Server};SERVER=nimraser;DATABASE=MHIMS;UID=sa;PWD=torrent_123')
db_connection = pyodbc.connect(connection_str)
db_connection.autocommit = True
db_cursor = db_connection.cursor()







class Login(Frame):
    
    def _init_(self, master):
          self.master = master

    def create_main_widgets(self):

        self.topframe = Frame(root, width=100, height=100, relief=GROOVE, borderwidth=2 )
        self.topframe.pack(padx=100, pady=100)

        self.welcomelbl = Label(self.topframe, text="Welcome To", width="20")
        self.welcomelbl.grid(row=0, column=0, pady=5 )

        self.cnamelbl = Label(self.topframe, text="Shah iSolutions", width="20", fg="RED", font="10")
        self.cnamelbl.grid(row=1, column=0, pady=5 )

        self.ahimslbl = Label(self.topframe, text="AHIMS", width="20")
        self.ahimslbl.grid(row=2, column=0, pady=5 )


        
    def create_ipno_widgets(self):
        filewin = Toplevel(root)
        

        self.bottomframe = Frame(filewin, width=100, height=400, relief=GROOVE, borderwidth=2)
        self.bottomframe.pack(padx=5, pady=20)
       

        self.ipnolbl = Label(self.bottomframe, text="IPNO", width="20")
        self.ipnolbl.grid(row=0, column=0, pady=5 )
            
        self.ipnotxt = Entry (self.bottomframe, width="15")
        self.ipnotxt.grid(row=0, column=1, pady=5)

        
        


        self.bframe = Frame(filewin, width=100, height=200, relief=GROOVE, borderwidth=2 )
        self.bframe.pack(padx=5, pady=5)

        self.updatelbl = Label(self.bframe, text="Update Here", width="20")
        self.updatelbl.grid(row=0, column=0, pady=5 )

        self.updatebutton = Button(self.bframe, text="UPDATE", fg="black", command = self.update_verify)
        self.updatebutton.grid(row=1, column=3, pady=5)


     

    def create_guardian_widgets(self):

        filewin1 = Toplevel(root)

        self.bottomframe = Frame(filewin1, width=100, height=400, relief=GROOVE, borderwidth=2)
        self.bottomframe.pack(padx=5, pady=20)
       

        self.ipnolbl = Label(self.bottomframe, text="IPNO", width="20")
        self.ipnolbl.grid(row=0, column=0, pady=5 )
            
        self.ipnotxt = Entry (self.bottomframe, width="15")
        self.ipnotxt.grid(row=0, column=1, pady=5)

        self.guardianlbl = Label(self.bottomframe, text="Guardian Name", width="20")
        self.guardianlbl.grid(row=1, column=0, pady=5 )
            
        self.guardiantxt = Entry (self.bottomframe, width="15")
        self.guardiantxt.grid(row=1, column=1, pady=5)

        
        


        self.bframe = Frame(filewin1, width=100, height=200, relief=GROOVE, borderwidth=2 )
        self.bframe.pack(padx=5, pady=5)

        self.updatelbl = Label(self.bframe, text="Update Here", width="20")
        self.updatelbl.grid(row=0, column=0, pady=5 )

        self.updatebutton = Button(self.bframe, text="UPDATE", fg="black", command = self.update_verify2)
        self.updatebutton.grid(row=1, column=3, pady=5)





    def update_verify(self):
        ipno = self.ipnotxt.get()
        null = 'NULL'
        sql_command1 =   """
                        SELECT COUNT(ipno) AS person_count FROM tblipregistration WHERE IPNO = ?
                        """
        db_cursor.execute(sql_command1, ipno)
        row = db_cursor.fetchone()

        if row.person_count > 0:
        #print("---")
        #print("Count of selected table rows: %u" % row.person_count)
        #print("---")

        
            print ipno
        #cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=nimraser;DATABASE=MHIMS;UID=sa;PWD=torrent_123')
        #cursor = cnxn.cursor()

        #for row in cursor.execute("update tblipregistration set IsDischarge='False', Billedflag='False' where IPNO = %s"%ipno)
            sql_command =   """
                            UPDATE tblipregistration SET IsDischarge=?, Billedflag=? WHERE IPNO=?
                            """
            db_cursor.execute(sql_command, 'False', 'False', ipno)
            db_connection.commit()
            tm.showinfo("Data Updated ",ipno)
        #cnxn.close()
        else:
            ermessage = "IPNO Does Not Exists"
            tm.showinfo("No Data Found ",ermessage)



    def update_verify2(self):
        ipno = self.ipnotxt.get()
        fname = self.guardiantxt.get()
        null = 'NULL'
        sql_command1 =   """
                        SELECT COUNT(ipno) AS person_count, uhid FROM tblipregistration WHERE ipno = ? group by uhid
                        """
        db_cursor.execute(sql_command1, ipno)
        row = db_cursor.fetchone()

        if row is not None:
            person_count = row[0]
            uhid = row[1]
            print person_count
            print uhid
    


        if row.person_count > 0:
        #print("---")
        #print("Count of selected table rows: %u" % row.person_count)
        #print("---")

        
            print uhid
        #cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=nimraser;DATABASE=MHIMS;UID=sa;PWD=torrent_123')
        #cursor = cnxn.cursor()

        #for row in cursor.execute("update tblipregistration set IsDischarge='False', Billedflag='False' where IPNO = %s"%ipno)
            sql_command =   """
                            UPDATE tblpatinfo SET FNAME=? WHERE UHID=?
                            """
            db_cursor.execute(sql_command, fname, uhid)
            db_connection.commit()
            tm.showinfo("Data Updated ",fname)
        #cnxn.close()
        else:
            ermessage = "UHID Does Not Exists"
            tm.showinfo("No Data Found ",ermessage)
        self.ipnotxt.delete(0, 'end')
        self.guardiantxt.delete(0, 'end') 
            
        

root = Tk()
root.title("Shah iSolutions")
root.iconbitmap('logo.ico')
root.geometry("360x360")

login = Login(root)
  #call the method
login.create_main_widgets()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Update IPNO", command=login.create_ipno_widgets)
filemenu.add_command(label="Update GUARDIAN", command=login.create_guardian_widgets)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=login.quit)

menubar.add_cascade(label="Update", menu=filemenu)
"""
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
"""
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)





root.mainloop()
