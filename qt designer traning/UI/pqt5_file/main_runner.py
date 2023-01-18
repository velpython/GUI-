from PyQt5 import QtCore, QtGui, QtWidgets
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
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()