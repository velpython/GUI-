
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView
import qtexample_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        MainWindow.resize(626, 392)
        
        # create main window 
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        # self.centralwidget.setGeometry(QtCore.QRect(0, 0, 1500, 800))
        #create tab 
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1400, 800))
        #create a tab_1 for setting
        self.setting_tab = QtWidgets.QWidget()
        self.tabWidget.addTab(self.setting_tab, "")
        self.lineEdit = QtWidgets.QLineEdit(self.setting_tab)
        self.lineEdit.setGeometry(QtCore.QRect(30, 250, 600, 60))
        # create pushbutton's
        self.pushButton_savetab1 = QtWidgets.QPushButton(self.setting_tab)
        self.pushButton_savetab1.setGeometry(QtCore.QRect(700, 250, 200, 50))
        self.pushButton_clear = QtWidgets.QPushButton(self.setting_tab)
        self.pushButton_clear.setGeometry(QtCore.QRect(850, 50, 200, 50))
        self.pushButton_refresh = QtWidgets.QPushButton(self.setting_tab)
        self.pushButton_refresh.setGeometry(QtCore.QRect(570, 50, 200, 50))
        self.pushButton_check = QtWidgets.QPushButton(self.setting_tab)
        self.pushButton_check.setGeometry(QtCore.QRect(300, 50, 200, 50))
        #create combobox for serial communication port 
        self.comboBox_Com = QtWidgets.QComboBox(self.setting_tab)
        self.comboBox_Com.setGeometry(QtCore.QRect(50, 50, 200, 50))

        #created label for anora logo 
        # label =- anoralogo

        self.anora_logo = QtWidgets.QLabel(self.centralwidget)
        self.anora_logo.setGeometry(QtCore.QRect(0, 800, 150, 50))
        self.anora_logo.setStyleSheet("image:url(:/qtc/Screenshot 2023-01-11 153546.png)")
        self.anora_logo.setText("")
        # created texas_logo 
        self.texas_logo = QtWidgets.QLabel(self.centralwidget)
        self.texas_logo.setGeometry(QtCore.QRect(1300, 800, 150, 40))
        self.texas_logo.setStyleSheet("image:url(:/qtc/texas instruments .png)")
        self.texas_logo.setText("")
         
        # created the tab and added the table widget
        self.Main_Board = QtWidgets.QTableWidget()
        self.tabWidget.addTab(self.Main_Board, "Main_Board")
        # created pushbutton's with respective tab
        self.pushButton_Refresh = QtWidgets.QPushButton(self.Main_Board)
        self.pushButton_Refresh.setGeometry(QtCore.QRect(600, 700, 180, 50))
        self.pushButton_result = QtWidgets.QPushButton(self.Main_Board)
        self.pushButton_result.setGeometry(QtCore.QRect(800, 700, 180, 50))
        self.pushButton_savetab2 = QtWidgets.QPushButton(self.Main_Board)
        self.pushButton_savetab2.setGeometry(QtCore.QRect(1000, 700, 180, 50))
        # created the progressBar for saving code
        self.progressBar = QtWidgets.QProgressBar(self.Main_Board)
        self.progressBar.setGeometry(QtCore.QRect(10, 700, 200, 50))
        self.progressBar.setProperty("value", 24)
        # setting and rising up the mainWindow
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 713, 18))
        MainWindow.setMenuBar(self.menubar)

        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.menuMenu.addAction(self.actionQuit)
        self.menuMenu.addAction(self.actionSave)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
          
    def retranslateUi(self, MainWindow):
        # setting up the name for all components
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_savetab1.setText(_translate("MainWindow", "save"))
        self.pushButton_clear.setText(_translate("MainWindow", "clear"))
        self.pushButton_refresh.setText(_translate("MainWindow", "refresh"))
        self.pushButton_check.setText(_translate("MainWindow", "check"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.setting_tab), _translate("MainWindow", "setting"))
        self.pushButton_Refresh.setText(_translate("MainWindow", "Refresh"))
        self.pushButton_result.setText(_translate("MainWindow", "check result"))
        self.pushButton_savetab2.setText(_translate("MainWindow", "save"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionSave.setText(_translate("MainWindow", "Save"))

