from PyQt5 import QtCore, QtGui, QtWidgets , QtSerialPort  
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
# from PyQt5.QtGui import Qpixmap
import iconify  as ico
import csv
import os
import datetime as dt
import pandas as pd
from PyQt5.QtWidgets import qApp, QAction , QSplashScreen
from PyQt5.QtWidgets import QApplication , QRadioButton , QWidget , QPushButton , QHBoxLayout , QFileDialog , QLineEdit , QTableWidgetItem ,QTableWidget
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
import serial
# from iconify.qt import QtGui, QtWidgets
# from pyside2 import QtWidgets
import main
import sys
import os 

class MyQtApp(main.Ui_MainWindow,QtWidgets.QMainWindow , QTableWidget , QSplashScreen):
    def __init__(self):
        super(MyQtApp,self).__init__()
        self.setupUi(self)
        self.showMaximized()
        self.setWindowTitle("MY GUI")
        self.populate_tree_widget()
        self.pushButton_10.clicked.connect(self.save_dialog)
        self.QcheckBox.clicked.connect(self.Q_checkBox)
        self.QcheckBox_2.clicked.connect(self.Q_checkBox_2)
        self.QcheckBox_3.clicked.connect(self.Q_checkBox_3)
        self.QcheckBox_4.clicked.connect(self.Q_checkBox_4)
        self.QcheckBox_5.clicked.connect(self.Q_checkBox_5)
        self.QcheckBox_6.clicked.connect(self.Q_checkBox_6)
        self.QcheckBox_7.clicked.connect(self.Q_checkBox_7)
        self.pushButton_3.clicked.connect(self.clear_reset)
        self.pushButton_5.clicked.connect(self.save_sheet)
        self.pushButton_4.clicked.connect(self.pass_fail_check)
        self.pushButton_11.clicked.connect(self.Q_limit_check)
        self.pushButton_4.clicked.connect(self.show_result)
        self.pushButton_2.clicked.connect(self.combo_com)
        self.load_data()

    def populate_tree_widget(self):
        self.tableWidget.setColumnWidth(0,70)
        self.tableWidget.setColumnWidth(1,130)
        self.tableWidget.setColumnWidth(2,350)
        self.tableWidget.setColumnWidth(3,160)
        self.tableWidget.setColumnWidth(4,130)
        self.tableWidget.setColumnWidth(5,160)
        self.tableWidget.setColumnWidth(6,160)
        self.load_data()

    def load_data(self):
        people = [{"no " : "1" , "name" : "TEST NO" , "Description " : "NA "  ,} ,
        {"no " : "2","name" : "FORCE" , "Description " : "NA "},
        {"no " : "3","name" : "FORCE" , "Description " : "NA "},
        {"no " : "4","name" : "FORCE" , "Description " : "NA "},
        {"no " : "5","name" : "MEASURE" , "Description " : "NA "},
        {"no " : "6","name" : "MEASURE" , "Description " : "NA "},
        {"no " : "7","name" : "MEASURE" , "Description " : "NA "}]
                
        row = 0
        self.tableWidget.setRowCount(len(people))
        for person in people:
            self.tableWidget.setItem(row, 0 , QtWidgets.QTableWidgetItem(person["no "]))
            self.tableWidget.setItem(row, 1 , QtWidgets.QTableWidgetItem(person["name"]))
            self.tableWidget.setItem(row, 2 , QtWidgets.QTableWidgetItem(person["Description "]))
            row = row+1
            self.size_increase()
    def size_increase(self):
        self.setStyleSheet("QTabBar::tab_2 { height: 30px; width: 100px; background: 'yellow'}") 
        height = 600
        width = 1200
        self.setFixedHeight(height)
        self.setFixedWidth(width)
        self.frameGeometry().width()
    
    def save_dialog(self):
        pass
    
    def save_dialog_pushbutton(self):
        file_filter = "Data File(*.xlsx *.csv *.dat);;Excel File(*.xlsx *.xls)"
        file = QFileDialog.getSaveFileName(
            parent=self, 
            caption="select a data file",
            directory= "*.csv" ,
            filter = file_filter,
            initialFilter="*.csv ,Excel File(*.xlsx *.xls) "
        ) 
        print(file)
        return file

    def save_sheet(self):
  
        path = QFileDialog.getSaveFileName(self, 'Save CSV', os.getenv('HOME'), 'CSV(*.csv)')
        if path[0] != '':
            self.progressBar.setValue(100)
            with open(path[0], 'w') as csvfile:
                writer = csv.writer(csvfile, dialect='excel', lineterminator='\n')
                columns = range(self.tableWidget.columnCount())
                header = [self.tableWidget.horizontalHeaderItem(column).text() for column in columns]
                writer.writerow(header)
                for row in range(self.tableWidget.rowCount()):
                    row_data = []
                    for column in range(self.tableWidget.columnCount()):
                        item = self.tableWidget.item(row, column)
                        if item is not None:
                            row_data.append(item.text())
                        else:
                            row_data.append('')
                    writer.writerow(row_data)

    def Q_checkBox(self):
        self.QcheckBox.checkState()
        if self.QcheckBox.checkState == 0:
            self.labelA.setText("not selected")
            
        else:
            self.labelA.setText("selected")
            # self.progressBar.setValue(100)
    def Q_checkBox_2(self):
        if self.QcheckBox_2.checkState == 0:
            self.labelb.setText("not selected")
        else:
            self.labelb.setText("selected")

    def Q_checkBox_3(self):
        if self.QcheckBox_3.checkState == 0:
            self.labelc.setText("not selected")
        else:
            self.labelc.setText("selected")
    def Q_checkBox_4(self):
        if self.QcheckBox_4.checkState == 0:
            self.labeld.setText("not selected")
        else:
            self.labeld.setText("selected")

    def Q_checkBox_5(self):
        if self.QcheckBox_5.checkState == 0:
            self.labele.setText("not selected")
        else:
            self.labele.setText("selected")
    def Q_checkBox_6(self):
        if self.QcheckBox_6.checkState == 0:
            self.labelf.setText("not selected")
        else:
            self.labelf.setText("selected")
    def Q_checkBox_7(self):
        if self.QcheckBox_7.checkState == 0:
            self.labelg.setText("not selected")
        else:
            self.labelg.setText("selected")
    
    def Q_limit_check(self):
        self.label_21.setText("READY")
        
        
    def pass_fail_check(self):
        self.label_22.setText("PASS")
        self.label_23.setText("PASS")
        self.label_24.setText("FAIL")
        self.label_25.setText("PASS")
        self.label_26.setText("PASS")
        self.label_27.setText("FAIL")

    def show_result(self):
        self.value = self.Qspin_2.value()
        self.label_28.setText(str(self.value) +"V") 
        self.value = self.Qspin.value()
        self.label_29.setText(str(self.value) +"A") 
    def clear_reset(self , state):
       if state == 0:
                self.QcheckBox.setChecked(False)
                self.labelA.setText("not selected")
                self.label_21.setText("")
                self.label_22.setText("")
                self.label_23.setText("")
                self.label_24.setText("")
                self.label_25.setText("")
                self.label_26.setText("")
                self.label_27.setText("")
                self.QcheckBox_2.setChecked(False)
                self.labelb.setText("not selected")
                self.QcheckBox_3.setChecked(False)
                self.labelc.setText("not selected")
                self.QcheckBox_4.setChecked(False)
                self.labeld.setText("not selected")
                self.QcheckBox_5.setChecked(False)
                self.labele.setText("not selected")
                self.QcheckBox_6.setChecked(False)
                self.labelf.setText("not selected")
                self.QcheckBox_7.setChecked(False)
                self.labelg.setText("not selected")
       else:
            return None

    def combo_com(self):
        self.comboBox.addItems([ port.portName() for port in QSerialPortInfo().availablePorts() ])
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    qt_app = MyQtApp()
    qt_app.show()
    anim = ico.anim.Spin()
    sys.exit(app.exec_())