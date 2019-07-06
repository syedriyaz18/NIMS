###################################################
# Tabbed interface script
# www.sunjay-varma.com
###################################################

__doc__ = info = '''
This script was written by Sunjay Varma - www.sunjay-varma.com

This script has two main classes:
Tab - Basic tab used by TabBar for main functionality
TabBar - The tab bar that is placed above tab bodies (Tabs)

It uses a pretty basic structure:
root
-->TabBar(root, init_name) (For switching tabs)
-->Tab    (Place holder for content)
	\t-->content (content of the tab; parent=Tab)
-->Tab    (Place holder for content)
	\t-->content (content of the tab; parent=Tab)
-->Tab    (Place holder for content)
	\t-->content (content of the tab; parent=Tab)
etc.
SREEDHARP@GMAIL.COM
'''

from Tkinter import *

BASE = RAISED
SELECTED = FLAT

# a base tab class
class Tab(Frame):
	def __init__(self, master, name):
		Frame.__init__(self, master)
		self.tab_name = name

# the bulk of the logic is in the actual tab bar
class TabBar(Frame):
        def __init__(self, master=None, init_name=None):
                Frame.__init__(self, master)
                self.tabs = {}
		self.buttons = {}
		self.current_tab = None
		self.init_name = init_name
	
	def show(self):
		self.pack(side=TOP, expand=YES, fill=X)
		self.switch_tab(self.init_name or self.tabs.keys()[-1])# switch the tab to the first tab
	
	def add(self, tab):
		tab.pack_forget()									# hide the tab on init
		
		self.tabs[tab.tab_name] = tab						# add it to the list of tabs
		b = Button(self, text=tab.tab_name, relief=BASE,	# basic button stuff
			command=(lambda name=tab.tab_name: self.switch_tab(name)))	# set the command to switch tabs
		b.pack(side=LEFT)												# pack the buttont to the left mose of self
		self.buttons[tab.tab_name] = b											# add it to the list of buttons
	
	def delete(self, tabname):
		
		if tabname == self.current_tab:
			self.current_tab = None
			self.tabs[tabname].pack_forget()
			del self.tabs[tabname]
			self.switch_tab(self.tabs.keys()[0])
		
		else: del self.tabs[tabname]
		
		self.buttons[tabname].pack_forget()
		del self.buttons[tabname] 
		
	
	def switch_tab(self, name):
		if self.current_tab:
			self.buttons[self.current_tab].config(relief=BASE)
			self.tabs[self.current_tab].pack_forget()			# hide the current tab
		self.tabs[name].pack(side=BOTTOM)							# add the new tab to the display
		self.current_tab = name									# set the current tab to itself
		
		self.buttons[name].config(relief=SELECTED)					# set it to the selected style
			




#Coding#############

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














if __name__ == '__main__':
	def write(x): print x
		
	root = Tk()
	
	root.title("Shah iSolutions")
        
        
	bar = TabBar(root, "Info")
	
	tab1 = Tab(root, "Wow...")				# notice how this one's master is the root instead of the bar
	Label(tab1, text="Sunjay Varma is an extra ordinary little boy.\n\n\n\n\nCheck out his website:\nwww.sunjay-varma.com", bg="white", fg="red").pack(side=TOP, expand=YES, fill=BOTH)
	Button(tab1, text="PRESS ME!", command=(lambda: write("YOU PRESSED ME!"))).pack(side=BOTTOM, fill=BOTH, expand=YES)
	Button(tab1, text="KILL THIS TAB", command=(lambda: bar.delete("Wow..."))).pack(side=BOTTOM, fill=BOTH, expand=YES)
	
	tab2 = Tab(root, "Hi there!")
	Label(tab2, text="How are you??", bg='black', fg='#3366ff').pack(side=TOP, fill=BOTH, expand=YES)
	txt = Text(tab2, width=50, height=20)
	txt.focus()
	txt.pack(side=LEFT, fill=X, expand=YES)
	Button(tab2, text="Get", command=(lambda: write(txt.get('1.0', END).strip()))).pack(side=BOTTOM, expand=YES, fill=BOTH)

	tab3 = Tab(root, "Info")
	Label(tab3, bg='white', text="This tab was given as an argument to the TabBar constructor.\n\nINFO:\n"+info).pack(side=LEFT, expand=YES, fill=BOTH)
	
	bar.add(tab1)                   # add the tabs to the tab bar
	bar.add(tab2)
	bar.add(tab3)

	#bar.config(bd=2, relief=RIDGE)			# add some border
	
	bar.show()
	
	root.mainloop()
