from PyQt5 import QtCore, QtGui, QtWidgets
import iconify  as ico
# from iconify.qt import QtGui, QtWidgets
# from pyside2 import QtWidgets
import main
import sys

class MyQtApp(main.Ui_MainWindow,QtWidgets.QMainWindow ):
    def __init__(self):
        # app = QtWidgets.QApplication(sys.argv)
        # MainWindow = QtWidgets.QMainWindow()
        # self.ui = main.Ui_MainWindow()
        # self.ui.setupUi(MainWindow)
        # MainWindow.show()
        # sys.exit(app.exec_())
        super(MyQtApp,self).__init__()
        self.setupUi(self)
        self.showMaximized()
        self.setWindowTitle("MY GUI")
        self.populate_tree_widget()

    def populate_tree_widget(self):
        self.tableWidget.setColumnWidth(0,100)
        self.tableWidget.setColumnWidth(1,150)
        self.tableWidget.setColumnWidth(2,500)
        self.tableWidget_2.setColumnWidth(0,350)
        self.tableWidget_2.setColumnWidth(1,350)
        self.tableWidget_2.setColumnWidth(2,500)
        self.load_data()

    def load_data(self):
        people = [{"no " : "1" , "name" : "resister" , "Description " : "used to resist the current " } ,
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
        self.setStyleSheet("QTabBar::tab { height: 30px; width: 70px; background: 'yellow'}") 
        height = 600
        width = 1100
        self.setFixedHeight(height)
        self.setFixedWidth(width)
        self.frameGeometry().width()

    def icon_setting(self):
        # icon = ico.Icon('feather:loader',color=QtGui.QColor('salmon'),anim =anim)
        # self.pushButton_3.setIcon(icon)
        # # self.pushButton(icon)
        # button = QpushButton 
        # anim.start()     
        pass
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    qt_app = MyQtApp()
    qt_app.show()
    anim = ico.anim.Spin()
    app.exec_()