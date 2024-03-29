from Tkinter import *
import ctypes
import sys
import pyodbc
import tkMessageBox as tm


myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


# Create a new database:
connection_str =    """
                    Driver={SQL Server Native Client 11.0};
                    Server=nimraser;
                    Database=MHIMS;
                    Trusted_Connection=yes;
                    """
db_connection = pyodbc.connect(connection_str)
db_connection.autocommit = True
db_cursor = db_connection.cursor()





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
            
        self.ipnotxt = Entry (self.bottomframe, width="15")
        self.ipnotxt.grid(row=0, column=1, pady=5)

        
        


        self.bframe = Frame(root, width=100, height=200, relief=GROOVE, borderwidth=2 )
        self.bframe.pack(padx=5, pady=5)

        self.updatelbl = Label(self.bframe, text="Update Here", width="20")
        self.updatelbl.grid(row=0, column=0, pady=5 )

        self.updatebutton = Button(self.bframe, text="UPDATE", fg="black", command = self.update_verify)
        self.updatebutton.grid(row=1, column=3, pady=5)


     

    def update_verify(self):
        ipno = self.ipnotxt.get()

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
            
        

root = Tk()
root.title("Shah iSolutions")
root.iconbitmap('images/logo.ico')
root.geometry("360x360")
login = Login(root)
  #call the method
login.create_widgets()

root.mainloop()
