# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\users\alexe\onedrive\documents\python3\pyqt5\calculator\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(121, 22, 531, 401))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Vivaldi")
        font.setPointSize(20)
        font.setItalic(True)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.mainLineEdit = QtWidgets.QLineEdit(self.widget)
        self.mainLineEdit.setObjectName("mainLineEdit")
        self.gridLayout.addWidget(self.mainLineEdit, 1, 0, 1, 4)
        self.b7 = QtWidgets.QPushButton(self.widget)
        self.b7.setObjectName("b7")
        self.gridLayout.addWidget(self.b7, 2, 0, 1, 1)
        self.b8 = QtWidgets.QPushButton(self.widget)
        self.b8.setObjectName("b8")
        self.gridLayout.addWidget(self.b8, 2, 1, 1, 1)
        self.b9 = QtWidgets.QPushButton(self.widget)
        self.b9.setObjectName("b9")
        self.gridLayout.addWidget(self.b9, 2, 2, 1, 1)
        self.bPlus = QtWidgets.QPushButton(self.widget)
        self.bPlus.setObjectName("bPlus")
        self.gridLayout.addWidget(self.bPlus, 2, 3, 1, 1)
        self.b4 = QtWidgets.QPushButton(self.widget)
        self.b4.setObjectName("b4")
        self.gridLayout.addWidget(self.b4, 3, 0, 1, 1)
        self.b5 = QtWidgets.QPushButton(self.widget)
        self.b5.setObjectName("b5")
        self.gridLayout.addWidget(self.b5, 3, 1, 1, 1)
        self.b6 = QtWidgets.QPushButton(self.widget)
        self.b6.setObjectName("b6")
        self.gridLayout.addWidget(self.b6, 3, 2, 1, 1)
        self.bMinus = QtWidgets.QPushButton(self.widget)
        self.bMinus.setObjectName("bMinus")
        self.gridLayout.addWidget(self.bMinus, 3, 3, 1, 1)
        self.b1 = QtWidgets.QPushButton(self.widget)
        self.b1.setObjectName("b1")
        self.gridLayout.addWidget(self.b1, 4, 0, 1, 1)
        self.b2 = QtWidgets.QPushButton(self.widget)
        self.b2.setObjectName("b2")
        self.gridLayout.addWidget(self.b2, 4, 1, 1, 1)
        self.b3 = QtWidgets.QPushButton(self.widget)
        self.b3.setObjectName("b3")
        self.gridLayout.addWidget(self.b3, 4, 2, 1, 1)
        self.bTimes = QtWidgets.QPushButton(self.widget)
        self.bTimes.setObjectName("bTimes")
        self.gridLayout.addWidget(self.bTimes, 4, 3, 1, 1)
        self.clearButton = QtWidgets.QPushButton(self.widget)
        self.clearButton.setObjectName("clearButton")
        self.gridLayout.addWidget(self.clearButton, 5, 0, 1, 1)
        self.resultButton = QtWidgets.QPushButton(self.widget)
        self.resultButton.setObjectName("resultButton")
        self.gridLayout.addWidget(self.resultButton, 5, 1, 1, 1)
        self.b0 = QtWidgets.QPushButton(self.widget)
        self.b0.setObjectName("b0")
        self.gridLayout.addWidget(self.b0, 5, 2, 1, 1)
        self.bDivide = QtWidgets.QPushButton(self.widget)
        self.bDivide.setObjectName("bDivide")
        self.gridLayout.addWidget(self.bDivide, 5, 3, 1, 1)
        self.exitButton = QtWidgets.QPushButton(self.widget)
        self.exitButton.setObjectName("exitButton")
        self.gridLayout.addWidget(self.exitButton, 6, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Simple PyQt5 Calculator"))
        self.b7.setText(_translate("MainWindow", "7"))
        self.b8.setText(_translate("MainWindow", "8"))
        self.b9.setText(_translate("MainWindow", "9"))
        self.bPlus.setText(_translate("MainWindow", "+"))
        self.b4.setText(_translate("MainWindow", "4"))
        self.b5.setText(_translate("MainWindow", "5"))
        self.b6.setText(_translate("MainWindow", "6"))
        self.bMinus.setText(_translate("MainWindow", "-"))
        self.b1.setText(_translate("MainWindow", "1"))
        self.b2.setText(_translate("MainWindow", "2"))
        self.b3.setText(_translate("MainWindow", "3"))
        self.bTimes.setText(_translate("MainWindow", "*"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.resultButton.setText(_translate("MainWindow", "Result"))
        self.b0.setText(_translate("MainWindow", "0"))
        self.bDivide.setText(_translate("MainWindow", "/"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))
