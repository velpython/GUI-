from PyQt5 import QtCore, QtGui, QtWidgets , QtSerialPort  
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
import iconify  as ico
import csv
import os
import datetime as dt
import pandas as pd
from PyQt5.QtWidgets import qApp, QAction , QSplashScreen
from PyQt5.QtWidgets import QApplication , QRadioButton , QWidget , QPushButton , QHBoxLayout , QFileDialog , QCheckBox , QTableWidgetItem ,QTableWidget, QMainWindow , QTableView
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
import serial
from PyQt5.QtCore import Qt
import chardet
from PIL import ImageQt
import QT5_main
import sys
import os 

class MyQtApp(QT5_main.Ui_MainWindow,QtWidgets.QMainWindow , QTableWidget , QSplashScreen):
    def __init__(self):
        super(MyQtApp,self).__init__()
        self.setupUi(self)
        # self.import_datalog()
          
        # init the set windowsizze combo 
        self.setWindowTitle("MY GUI")
        self.resize(1500, 900)
        self.setMouseTracking(True)
        self.mouse_buttons = Qt.NoButton
        # assign's clicked functions 

        self.pushButton_savetab2.clicked.connect(self.save_sheet_2)
        self.pushButton_check.clicked.connect(self.combo_com)
        self.pushButton_clear.clicked.connect(self.combo_clear)   
        # passing file path        
        df = self.open_file(file_path =  r"D:\\Qt GUI\\GUI_Traning\\ui\pqt5_file\\QT5_main\\Bookdata.xls")
        self.import_datalog(df)
        self.add_checkbox(df, column=3)
        

    def open_file(self , file_path):
        try:
            df = pd.read_excel(file_path)
            return df

        except Exception as e:
            print("error founded in file opening")

    def import_datalog(self , df):   
        try:      
            rows = df.shape[0]
            columns = df.shape[1]
            self.Main_Board.setRowCount(rows)
            self.Main_Board.setColumnCount(columns)        
            # Set the table header
            header = df.columns.tolist()
            self.Main_Board.setHorizontalHeaderLabels(header)        
            # Insert data into the table
            for i in range(rows):
                for j in range(columns):
                    item = QTableWidgetItem(str(df.iloc[i, j]))
                    self.Main_Board.setItem(i, j, item)      
            return df     
        except Exception as e:
            print("Error :", e)

    def add_checkbox(self , df , column):

        column_data = df.iloc[:, column - 1]
        # Loop through all values in the column
        for i, val in enumerate(column_data):
            checkbox = QCheckBox()
        # Check if the value is equal to the target value
            if val == "__ Meas Voltage":
            # Add a checkbox to the table widget in the same row and column
                # self.Main_Board.setCellWidget(i, column - 1, None)
                self.Main_Board.setCellWidget(i, column - 1, checkbox)
            if val == "__ Force voltage":
                self.Main_Board.setCellWidget(i, column - 1, checkbox)
            if val == "__ Meas res":
                self.Main_Board.setCellWidget(i, column - 1, checkbox)
            if val == "__ Force current":
                self.Main_Board.setCellWidget(i, column - 1, checkbox)
            if val == "__ Meas current":
                self.Main_Board.setCellWidget(i, column - 1, checkbox)
            if val == "__ Meas cap":
                self.Main_Board.setCellWidget(i, column - 1, checkbox)
            if val == "__ Meas vth":
                self.Main_Board.setCellWidget(i, column - 1, checkbox)

                
    def combo_com(self):
        self.comboBox_Com.addItems([ port.portName() for port in QSerialPortInfo().availablePorts() ])

    def combo_clear(self):
        self.comboBox_Com.clear()
    
    def mousePressEvent(self, event):
        self.mouse_buttons = event.buttons()

    def mouseMoveEvent(self, event):
        if self.mouse_buttons == Qt.RightButton:
            self.resize(event.x(), event.y())
    
    def insert_checkBox(self , df):
      pass
    
    def save_sheet_2(self):
  
        path = QFileDialog.getSaveFileName(self, 'Save CSV', os.getenv('HOME'), 'CSV(*.csv)')
        if path[0] != '':
            self.progressBar.setValue(100)
            with open(path[0], 'w') as csvfile:
                writer = csv.writer(csvfile, dialect='excel', lineterminator='\n')
                columns = range(self.Main_Board.columnCount())
                header = [self.Main_Board.horizontalHeaderItem(column).text() for column in columns]
                writer.writerow(header)
                for row in range(self.Main_Board.rowCount()):
                        row_data = []
                        for column in range(self.Main_Board.columnCount()):
                            item = self.Main_Board.item(row, column)
                            print(item)
                            if item is not None:
                                row_data.append(item.text())
                            else:
                                row_data.append('')
                        writer.writerow(row_data)
    

   
if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    qt_app = MyQtApp()
    qt_app.show()
    anim = ico.anim.Spin()
    sys.exit(app.exec_())