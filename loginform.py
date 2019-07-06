# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginform.ui'
#
# Created: Thu May 28 13:21:44 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import MySQLdb


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class popupWindow(object):
    def __init__(self,Dialog):
        top=self.top=Toplevel(Dialog)
        self.l=Label(top,text="Hello World")
        self.l.pack()
        self.e=Entry(top)
        self.e.pack()
        self.b=Button(top,text='Ok',command=self.cleanup)
        self.b.pack()
    def cleanup(self):
        self.value=self.e.get()
        self.top.destroy()

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(450, 450)
	icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/FB_IMG_1431432647315_1.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(220, 190, 38, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 270, 171, 27))
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(146, 270, 68, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(146, 237, 52, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(150, 70, 174, 28))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(255, 83, 26);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200, 40, 82, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(220, 237, 171, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(47, 150, 371, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(220, 110, 51, 41))
        self.label_3.setStyleSheet(_fromUtf8("font: 75 oblique 11pt \"DejaVu Sans\";"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(170, 320, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 320, 98, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit, self.lineEdit_2)
        Dialog.setTabOrder(self.lineEdit_2, self.pushButton)
        Dialog.setTabOrder(self.pushButton, self.pushButton_2)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Shah iSolutions", None))
        self.label_6.setText(_translate("Dialog", "Login", None))
        self.label_5.setText(_translate("Dialog", "Passwprd:", None))
        self.label_4.setText(_translate("Dialog", "User ID:", None))
        self.label_2.setText(_translate("Dialog", "Shah iSolutions", None))
        self.label.setText(_translate("Dialog", "Welcome To", None))
        self.label_3.setText(_translate("Dialog", "AHIMS", None))
        self.pushButton.setText(_translate("Dialog", "Login", None))
        self.pushButton_2.setText(_translate("Dialog", "Close", None))
	QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), Dialog.close)   
	QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.login_verify)         
        QtCore.QMetaObject.connectSlotsByName(Dialog)

	
    def popup(self):
        self.w=popupWindow(self.Dialog)
        self.Dialog.wait_window(self.w.top)

    def login_verify(self):
	
	username = self.lineEdit.text()
	passwrd = self.lineEdit_2.text()	
	
	print username
	print passwrd 

	conn = MySQLdb.connect (host = "localhost",user = "root",passwd = "ShahiSolutionsL0ck3d",db = "ahims")
	cursor = conn.cursor ()
	cursor.execute ("SELECT * from login where userid = %s",(username))
	row = cursor.fetchone ()
	if row is not None:
		'''print "server version:", row[0], row[1]'''
		usrname = row[0]
		passw = row[1]
		print usrname
		print passw
		if passw == passwrd and usrname == username:
			print "Rows"
			
		elif passw <> passwrd or usrname <> username:
			print "Wrong Entry"
			self.popup
			

	else:
		print "No Rows" 
		return
      		dialog = QDialog()
        	dialog.ui = Ui_MyDialog()
        	dialog.ui.setupUi(dialog)
        	dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        	dialog.exec_()
	
		
	 
	cursor.close ()
	conn.close ()

    



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

