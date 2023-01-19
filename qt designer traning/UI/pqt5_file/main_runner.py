from PyQt5 import QtCore, QtGui, QtWidgets 
import iconify  as ico
from PyQt5.QtWidgets import QApplication , QRadioButton , QWidget , QPushButton , QHBoxLayout , QFileDialog
# from iconify.qt import QtGui, QtWidgets
# from pyside2 import QtWidgets
import main
import sys
import os 

class MyQtApp(main.Ui_MainWindow,QtWidgets.QMainWindow ):
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
        self.load_data()
        

    def populate_tree_widget(self):
        self.tableWidget.setColumnWidth(0,100)
        self.tableWidget.setColumnWidth(1,150)
        self.tableWidget.setColumnWidth(2,500)
        self.load_data()

    def load_data(self):
        people = [{"no " : "1" , "name" : "resister" , "Description " : "used to resist the current "  ,} ,
        {"no " : "2","name" : "force" , "Description " : "NA "},
        {"no " : "3","name" : "voltage" , "Description " : "NA "},
        {"no " : "4","name" : "capactor" , "Description " : "NA "},
        {"no " : "5","name" : "inside" , "Description " : "NA "},
        {"no " : "6","name" : "netural" , "Description " : "NA "},
        {"no " : "7","name" : "postive" , "Description " : "NA "}]
                
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
        width = 1100
        self.setFixedHeight(height)
        self.setFixedWidth(width)
        self.frameGeometry().width()
    
    def save_dialog(self):
        file_filter = "Data File(*.xlsx *.csv *.dat);;Excel File(*.xlsx *.xls)"
        file = QFileDialog.getSaveFileName(
            parent=self, 
            caption="select a data file",
            directory= 'data file.dat',
            filter = file_filter,
            initialFilter="Excel File(*.xlsx *.xls)"
        ) 
        print(file)

    def Q_checkBox(self):
        print(self.QcheckBox.checkState())
        if self.QcheckBox.checkState == 0:
            self.labelA.setText("not selected")
        else:
            self.labelA.setText("selected")
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
    def check_Bo_changed(self):
        pass
    # def icon_setting(self):
    #     # icon = ico.Icon('feather:loader',color=QtGui.QColor('salmon'),anim =anim)
    #     # self.pushButton_3.setIcon(icon)
    #     # # self.pushButton(icon)
    #     # button = QpushButton 
    #     # anim.start()     
    #     pass
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    qt_app = MyQtApp()
    qt_app.show()
    anim = ico.anim.Spin()
    app.exec_()