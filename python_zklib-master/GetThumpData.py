from Tkinter import *
import MySQLdb
import tkMessageBox as tm
import sys
sys.path.append("zklib")

import zklib
import time
import zkconst

import xlsxwriter

import tkMessageBox as tm






class Attendance(Frame):
    

    def _init_(self, master):
          self.master = master

    def create_widgets(self):
        self.topframe = Frame(root, width=100, height=100, relief=GROOVE, borderwidth=2 )
        self.topframe.pack(padx=5, pady=20)

        self.welcomelbl = Label(self.topframe, text="Welcome To", width="20")
        self.welcomelbl.grid(row=0, column=0, pady=5 )

        self.cnamelbl = Label(self.topframe, text="Shah iSolutions", width="20", fg="RED", font="10")
        self.cnamelbl.grid(row=1, column=0, pady=5 )

        self.ahimslbl = Label(self.topframe, text="Attendance System", width="20")
        self.ahimslbl.grid(row=2, column=0, pady=5 )

        self.bottomframe = Frame(root, width=100, height=100, relief=GROOVE, borderwidth=2)
        self.bottomframe.pack(padx=5, pady=60)

        

        self.blackbutton = Button(self.bottomframe, text="Clicl Here To Get Attendance Data", fg="black", command = self.attendance_verify)
        self.blackbutton.grid(row=2, column=3, pady=5)


    def attendance_verify(self):
        
        
        
        connection = MySQLdb.connect(host="localhost", user="root", passwd = "root", db="nims_store")
        cursor = connection.cursor ()
        #cursor.execute("select * from user_tbl where user_name= %s", (regdate1))
        #row = cursor.fetchone()

        zk1 = zklib.ZKLib("192.168.1.71", 4370)
        zk2 = zklib.ZKLib("192.168.1.72", 4370)

        ret1 = zk1.connect()
        ret2 = zk2.connect()
        print "Connected To Doctors Machine:", ret1
        print "Connected To General Machine:", ret1

        if ret1 == True and ret2 == True:
            print "Pesan Disable Device", zk1.disableDevice(), zk2.disableDevice()
    
            #print "Pesan Versi:", zk.version()
            #print "Pesan Versi OS:", zk.osversion()
            """
            print "Pesan Extend Format:", zk.extendFormat()
            print "Pesan Extend OP Log:", zk.extendOPLog()
            """
    
            #print "Pesan Platform:", zk.platform()
            #print "Pesan Platform Version:", zk.fmVersion()
            #print "Pesan Work Code:", zk.workCode()
            #print "Pesan Work Code:", zk.workCode()
            #print "Pesan SSR:", zk.ssr()
            #print "Pesan Pin Width:", zk.pinWidth()
            #print "Pesan Face Function On:", zk.faceFunctionOn()
            #print "Pesan Serial Number:", zk.serialNumber()
            #print "Pesan Device Name:", zk.deviceName()
    
            """
            data_user = zk.getUser()
            print "Pesan Get User:"
            if data_user:
                for uid in data_user:
            
                    if data_user[uid][2] == 14:
                        level = 'Admin'
                    else:
                        level = 'User'
                    #print "[UID %d]: ID: %s, Name: %s, Level: %s, Password: %s" % ( uid, data_user[uid][0], data_user[uid][1], level, data_user[uid][3]  )
        
            #print "Pesan Clear Admin:", zk.clearAdmin()
            #zk.setUser(uid=61, userid='41', name='Dony Wahyu Isp', password='123456', role=zkconst.LEVEL_ADMIN)
            """
            # Delete a row from a table.
            print "Deleting Previous Data" 
            sql_command =   """
                            DELETE  FROM nims_attendance 
                            """
            cursor.execute(sql_command)

            attendance1 = zk1.getAttendance()
            attendance2 = zk2.getAttendance()


            print "Pesan Get Attendance:"
            print "Retreiving Current Data"
    
            if ( attendance1 ):
                for lattendance1 in attendance1:
                    if lattendance1[1] == 15:
                        state1 = 'Check In'
                    elif lattendance1[1] == 0:
                       state1 = 'Check Out'

                    else:
                        state1 = 'Undefined'

                    
                     
                    # insert to table
                    cursor.execute("""INSERT INTO nims_attendance VALUES (%s,%s,%s,%s,%s,%s,%s)""",( lattendance1[0], lattendance1[2].date(), lattendance1[2].time(), 51, 0, 0, 0))
                        
                    #print "%s, %s, %s, 51, 0, 0, 0" % ( lattendance[0], lattendance[2].date(), lattendance[2].time()  )
                    #print "Pesan Clear Attendance:", zk.clearAttendance()

            if ( attendance2 ):
                for lattendance2 in attendance2:
                    if lattendance2[1] == 15:
                        state2 = 'Check In'
                    elif lattendance2[1] == 0:
                       state2 = 'Check Out'

                    else:
                        state2 = 'Undefined'

                    
                     
                    # insert to table
                    cursor.execute("""INSERT INTO nims_attendance VALUES (%s,%s,%s,%s,%s,%s,%s)""",( lattendance2[0], lattendance2[2].date(), lattendance2[2].time(), 54, 0, 0, 0))
                        
                    #print "%s, %s, %s, 51, 0, 0, 0" % ( lattendance[0], lattendance[2].date(), lattendance[2].time()  )
                    #print "Pesan Clear Attendance:", zk.clearAttendance()
            
            




            connection.commit()
            #print cursor.fetchall()
            connection.close()
    
            print "Pesan Get Time:", zk1.getTime()
    
            print "Pesan Enable Device", zk1.enableDevice()
            print "Pesan Enable Device", zk2.enableDevice()
    
            print "Pesan Disconnect Doctors Machine:", zk1.disconnect()
            print "Pesan Disconnect General Machine:", zk2.disconnect()



            ermessage = "Data Retrieve Completed"
            tm.showinfo("Data Completed ",ermessage)








root = Tk()
root.title("Shah iSolutions")
root.iconbitmap('images/logo.ico')
root.geometry("360x360")
app = Attendance(root)
  #call the method
app.create_widgets()

root.mainloop()
