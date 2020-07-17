#!/usr/bin/env python

# pyuic5 ./unic_ui.ui -o ./unic_ui.py
# qtDesigner

import sys
import re
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from email_extract_ui import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)

window = QMainWindow()

ui = Ui_MainWindow()
ui.setupUi(window)

def unique(list1): 
    # insert the list to the set 
    list_set = set(list1) 
    # convert the set to the list 
    unique_list = (list(list_set)) 
    return unique_list
      

def operatetext():
	text = ui.plainTextEdit.toPlainText()

	if (ui.checkBox_3.checkState()):
		text = text.lower()
	
	mails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
	
	# lines = text.splitlines()

	if (ui.checkBox_2.checkState()):
		mails = unique(mails)
	
	if (ui.checkBox.checkState()):
		mails.sort()

	ui.plainTextEdit_2.setPlainText("\n".join(mails))
	ui.plainTextEdit_2.repaint()

#clicks
ui.pushButton.clicked.connect(operatetext)


window.show()
sys.exit(app.exec_())
