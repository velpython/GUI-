from PyQt5 import QtCore, QtGui, QtWidgets
# from pyside2 import QtWidgets
import main
import sys

class MyQtApp(main.Ui_MainWindow,QtWidgets.QMainWindow):
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
        self.load_data()

    def load_data(self):
        people = [{"no " : "1" , "name" : "resister" , "Description " : "used to resist the current " } , {"no " : "2","name" : "force" , "Description " : "force the current "} ]
        row = 0
        self.tableWidget.setRowCount(len(people))
        for person in people:
            self.tableWidget.setItem(row, 0 , QtWidgets.QTableWidgetItem(person["no "]))
            self.tableWidget.setItem(row, 1 , QtWidgets.QTableWidgetItem(person["name"]))
            self.tableWidget.setItem(row, 2 , QtWidgets.QTableWidgetItem(person["Description "]))
            row = row+1
            
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()